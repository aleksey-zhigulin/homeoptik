from oscar.apps.partner.importers import *

class HomeOptikImporter(object):

    def __init__(self, logger):
        self.logger = logger

    @atomic
    def handle(self, product_class_name, filepath):
        print (product_class_name)
        product_class = ProductClass.objects.get(
            name=product_class_name)

        attribute_codes = []
        with UnicodeCSVReader(filepath) as reader:
            for row in reader:
                if row[1] == 'UPC':
                    attribute_codes = row[9:]
                    continue
                self.create_product(product_class, attribute_codes, row)

    def create_product(self, product_class, attribute_codes, row):  # noqa
        (ptype, upc, title, description,
         category, partner, sku, price, stock) = row[0:9]

        # Create product
        is_child = ptype.lower() == 'variant'
        is_parent = ptype.lower() == 'group'

        if upc:
            try:
                product = Product.objects.get(upc=upc)
            except Product.DoesNotExist:
                product = Product(upc=upc)
        else:
            product = Product()

        if is_child:
            product.structure = Product.CHILD
            # Assign parent for children
            product.parent = self.parent
        elif is_parent:
            product.structure = Product.PARENT
        else:
            product.structure = Product.STANDALONE

        if not product.is_child:
            product.title = title
            product.description = description
            product.product_class = product_class

        # Attributes
        if not product.is_parent:
            for code, value in zip(attribute_codes, row[9:]):
                # Need to check if the attribute requires an Option instance
                attr = product_class.attributes.get(
                    code=code)
                if attr.is_option:
                    value = attr.option_group.options.get(option=value)
                if attr.type == 'date':
                    value = datetime.strptime(value, "%d/%m/%Y").date()
                setattr(product.attr, code, value)

        product.save()

        # Save a reference to last parent product
        if is_parent:
            self.parent = product

        # Category information
        if category:
            leaf = create_from_breadcrumbs(category)
            ProductCategory.objects.get_or_create(
                product=product, category=leaf)

        # Stock record
        if partner:
            partner, __ = Partner.objects.get_or_create(name=partner)
            try:
                record = StockRecord.objects.get(product=product)
            except StockRecord.DoesNotExist:
                record = StockRecord(product=product)
            record.partner = partner
            record.partner_sku = sku
            record.price_excl_tax = D(price)
            if stock != 'NULL':
                record.num_in_stock = stock
            record.save()
