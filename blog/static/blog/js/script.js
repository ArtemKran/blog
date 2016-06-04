/**
 * Created by Artem Kraynev on 04.06.16.
 */

/*
 Фокус на форму при нажатии на ответить на комментарий и
 добавления в value input id родителя комментария
 */
$('#comments').find('.answer').each(function (i, elem) {
    var parentId = $(this).prev().val();
    $(elem).click(function () {
        $('#author').focus();
        console.log(parentId);
        $('form input[name=parent_id]').val(parentId)
    });
});
