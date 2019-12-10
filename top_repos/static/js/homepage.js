$(document).ready(function () {

    $('.homeicon').hover(function () {
        $('.homeicon').not($(this)).css('opacity', '.1');
        var linkID = $(this).attr('id');
        var labelID = linkID.replace('link', 'label');
        $('#' + labelID).css('opacity', '1');
    }, function () {
        $('.homeicon').not($(this)).css('opacity', '1');
        var linkID = $(this).attr('id');
        var labelID = linkID.replace('link', 'label');
        $('#' + labelID).css('opacity', '0');
    });

});