from oscar.apps.catalogue.utils import *

class MyImporter(Importer):
    def __init__(self, logger, field):
        self.logger = logger
        self._field = field
        ProductImage.objects.all().delete()

    def _process_image(self, dirname, filename, lookup_value):
        file_path = os.path.join(dirname, filename)
        trial_image = Image.open(file_path)
        trial_image.verify()

        kwargs = {self._field: lookup_value}
        item = Product._default_manager.get(**kwargs)

        new_data = open(file_path, 'rb').read()
        if len(os.path.splitext(filename)[0].split('_')) > 1:
            display_order = os.path.splitext(filename)[0].split('_')[1]
        else:
            display_order = 0
        # for existing in item.images.all():
        #     if display_order == existing.display_order:
        #         print('deleting',filename,display_order)
        #         existing.delete()
        #     else:
        #         try:
        #             if new_data == existing.original.read():
        #                 raise IdenticalImageError()
        #         except IOError:
        #             # File probably doesn't exist
        #             existing.delete()

        new_file = File(open(file_path, 'rb'))
        im = ProductImage(product=item, display_order=display_order)
        im.original.save(filename, new_file, save=False)
        im.save()
        self.logger.debug('Image added to "%s"' % item)


    def _get_lookup_value_from_filename(self, filename):
        return os.path.splitext(filename)[0].split('_')[0]
