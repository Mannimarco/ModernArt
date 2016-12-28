/**
 * Created by mannimarco on 29/11/2016.
 */
$(document).ready(function () {

    function updateRating() {

        var ids = [];

        $('.rating-value').each(function () {
            ids.push($(this).data('post-id'));
            // $(this).load($)
        });

        $.getJSON('/posts_rating', {ids: ids.join(',')}, function (data) {
            for (var i in data) {
                $('.rating-value[data-post-id=' + i + ']').html(data[i]);
            }
        })
    }


    $('.vote-up').click(function () {
        var url = $(this).data('url-vote-up');
        $.post(url, function () {
            updateRating();
        })

    });

    $('.vote-down').click(function () {
        var url = $(this).data('url-vote-down');
        $.post(url, function () {
            updateRating();
        })

    });


    function updateCommentList() {
        $.ajax({
            url: $('.comments-list').data('url'),          //defined in html
            success: function (data) {
                $('.post-comments').html(data);
            }
        });
    }


    window.setInterval(updateCommentList, 1000);
    window.setInterval(updateRating, 1000);


    $('#post-edit-link').click(function () {
        $('.bgdialog').show();
        $('.dialog').load($(this).attr("href"));
        return false;
    });


    $(document).on('submit', '.ajax-form', function () {
        var form = $(this);
        $.post(form.attr('action'), form.serialize(), function (data) {
            if (data == 'OK') {
                location.reload();
            }
            form.html(data);
        });
        return false;
    });
    $(document).on('click', '.bgdialog', function () {
        $('.bgdialog').hide();
    });
    $(document).on('click', '.dialog', function (e) {
        e.stopPropagation();
    });

});