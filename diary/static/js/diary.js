$(function() {

    // INITIALIZE DATEPICKER PLUGIN
    $('.datepicker').datepicker({
      clearBtn: true,
      format: "dd/mm/yyyy"
    });
  
  
    $('#reservationDate').on('change', function() {
      var pickedDate = $('input').val();
      $('#pickedDate').html(pickedDate);
      var year = (pickedDate.slice(-4));
      var month = (pickedDate.slice(3,5));
      var day = (pickedDate.slice(0,2));

      console.log(year);
      console.log(month);
      console.log(day);

      var url = "/show_date/YYYY/MM/DD".replace('YYYY',year).replace('MM',month).replace('DD',day);
      document.getElementById('Go').href = url;
      
      

    });
  });