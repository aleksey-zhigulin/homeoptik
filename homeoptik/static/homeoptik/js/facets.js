window.onload = function() {
    $('li.facet div.collapse').each(function() {
        var div = $(this);
        $('input.facet_checkbox', this).each(
            function () {
                if ($(this).prop('checked')) {
                    div.collapse('show');
                    return;
                }
            }
        );
    })
}
