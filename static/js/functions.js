function message_error(obj){
    var html = ''
    if(typeof(obj) === 'object'){
        html ='<ul style="text-align: left;">';
        $.each(obj, function(key, value){
            html +="<li>"+key+":"+value+"</li>";
        });
        html +="<ul>";
    }else{
        html = '<p>'+obj+'';
    }
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}