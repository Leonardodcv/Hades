$(function (){
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                "action" : "searchdata"
            }, // parametros
            dataSrc: ""
        },
        columns: [
            { "data": "name"},
            { "data": "desc"},
            { "data": "desc"},
        ],
        columnDefs: [
            {
                targets: [2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return data;
                }
            },
        ],
        initComplete: function(settings, json) {
        
          }
        });
});