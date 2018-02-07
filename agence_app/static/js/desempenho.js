
$(document).ready(function() {

  $('select').material_select();

  $('#relatorio, #bar, #pizza').on('click', function() {
    var action_button = this.id;
    var url_ajax = '';
    $("#bloque").empty();
    if($('.datepicker_ini').val()==''){
      alert("Seleccione una fecha de inicio.");
      return false;
    }
    if($('.datepicker_fin').val()==''){
      alert("Seleccione una fecha de finalizacion.");
      return false;
    }
    if($('#consultores').val()==null){
      alert("Seleccione al menos un consultor.");
      return false;
    }
    if(action_button=='relatorio'){
      url_ajax = '/desempenho/detail_receitas/';
    }
    else if(action_button=='bar'){
      url_ajax = '/desempenho/detail_bar/';
    }
    else if(action_button=='pizza'){
      url_ajax = '/desempenho/detail_pizza/';
    }
    else{
      alert("Hubo un error obteniendo la URL para su consulta.");
      return false;
    }
    cons = $('#consultores').val();
    fecha_ini = $('.datepicker_ini').val();
    fecha_fin = $('.datepicker_fin').val();
    $.ajax({
        url: url_ajax,
        data: {
          'consultores': cons,
          'fecha_ini': fecha_ini,
          'fecha_fin': fecha_fin
        },
        method: "GET",
        dataType: "html"
    }).done(function(data){
      $("#bloque").empty();
      $("#bloque").html(data);
    }).error(function(data){
      alert('error');
    })
  });

  var max = $("#max_year").val().split("-");
  var max_date = new Date(max[2], max[1] - 1, max[0]);
  var min = $("#min_year").val().split("-");
  var min_date = new Date(min[2], min[1] - 1, min[0]);

  $('.datepicker_ini, .datepicker_fin').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 10, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    format: 'dd-mm-yyyy',
    min: min_date,
    max: max_date,
    closeOnSelect: true // Close upon selecting a date,
  });

})
