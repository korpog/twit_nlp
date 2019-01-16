$(document).ready(function () {
    $('.sentiment').each(function () {
        var cell_value = parseFloat($(this).text());
        console.log(cell_value);
        if (cell_value > 0) {
            $(this).css({
                'background': 'limegreen'
            });
        } else if (cell_value < 0) {
            $(this).css({
                'background': 'tomato'
            });
        } else {
            $(this).css({
                'background': 'slategrey'
            });
        }
    });
});