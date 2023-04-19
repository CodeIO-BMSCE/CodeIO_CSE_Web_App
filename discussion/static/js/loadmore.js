function myFunction(){

        var u_id = document.getElementsByName('to_user_id')[0].value;
        var page = document.getElementById('page_number');
        var page_number = parseInt(page.value);

        $.ajax({
            url: '/direct_message/loadmore/',
            data: {
                'page': page_number,
                'u_id': u_id,
                'csrfmiddlewaretoken': window.CSRF_TOKEN
            },
            cache: false,
            type: 'post',
            success: function(data){
                if(data.empty == true){
                    $("#loadmorebtn").hide();
                } else {
                    $.each(data,function(i,v){
                        var ol_collection_html = '<li style="border-bottom: 0px;" class="collection-item avatar"><img src="/media/'+ v.sender__profile__pfp + ' "width=50 height=50" "class="circle responsive-img"><span class="title"><b>'+ v.sender__first_name + ' ' + v.sender__last_name + '</b></span><p>'+ v.body +'</p><p class="right-align">' + v.date + '</p></li>';
                        $('#oldirects').append(ol_collection_html);
                    });
                }
            page_number = page_number + 1;
            $("#page_number").attr('value', page_number);

            }
        });
        return false;
 // end of document ready
}(jQuery)
; // end of jQuery name space


