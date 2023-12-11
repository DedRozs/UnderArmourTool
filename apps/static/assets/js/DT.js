
  // Truncate a string
  function strtrunc(str, max, add){
  add = add || '...';
  return (typeof str === 'string' && str.length > max ? str.substring(0, max) + add : str);
};
// [ Zero Configuration ] start
$('#simpletable').dataTable(
    {
        pageLength: 25,
        dom: 'Bfrtip',
        buttons: ['copy', 'csv', 'excel', 'print'],
        columnDefs: [
          {
            'targets': 2,
            'render': function(data, type, full, meta){
                if(type === 'display'){
                  data = strtrunc(data, 30);
                }
              
                return data;
            }
          }
        ]
    }
);
