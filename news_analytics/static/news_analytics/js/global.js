
$(document).ready(function() {

   $('#submitButton').on('click', searchKeyword);
   function searchKeyword(event){
    event.preventDefault();
    var keyword = $("#search_keyword").val();
    alert(keyword);
    $.ajax({
                 url: '/get_news/',
                 type: 'POST',
                 dataType :"json",
                 data : {
                    val: keyword,
                    csrfmiddlewaretoken: '{{csrf_token}}'
                  },
                 success :  function(data){
                     // Your Code here
                     alert("success");
                 }
             });

    }

});