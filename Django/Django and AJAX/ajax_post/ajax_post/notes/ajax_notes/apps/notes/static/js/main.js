$(document).ready(function(e){
    console.log("Get all notes")
    $.ajax({
        url: '/all_note',
        method: 'get',
        success: function(res){
            $('#all_notes').html(res)
            }
        })
    
    $('#create_ajax_form').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            method: 'post',
            data: $(this).serialize(),
            success: function(res) {
                $('#all_notes').html(res);
                $('textarea[id=form_content]').val('');
                $('input[id=adding_new_note]').val('');
            },
            error: function(){
                alert('Error sending data');
            }
        })
    })

    $('#form_description').submit(function(e){
        e.preventDefaultI();
        $.ajax({
            url: $(this).attr('action'),
            method: 'post',
            data: $(this).serialize(),
            success: function(res){
                $('#all_notes').html(res);
            },
            error: function(){
                alert('Error sending data');
            }
        })
    })

    $('#form_delete').submit(function(e){
        e.preventDefault();
        console.log("deleted")
        $.ajax({
            url: $(this).attr('action'),
            method: 'post',
            data: $(this).serialize(),
            success: function(res){
                $(this).remove();
                $('#all_notes').html(res)
            },
            error: function(){
                alert('Error sending data');
            }
        })
    })
})
