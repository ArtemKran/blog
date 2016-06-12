/**
 * Created by Artem Kraynev on 12.06.16.
 */

/*
Конечно немного не доделано, но клиент то здесь не главное
 */
$(document).ready(function(){
    $("#comments").on("click", ".reply", function(event){
        event.preventDefault();
        var form = $("#post-comment").clone(true);
        form.find('.parent').val($(this).parent().parent().attr('id'));
        $(this).parent().append(form);
    });
});