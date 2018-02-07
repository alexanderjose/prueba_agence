$('#bar').on('click', function() {
  $("#bloque").empty();
  // console.log($('#consultores').val());
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
  cons = $('#consultores').val();
  fecha_ini = $('.datepicker_ini').val();
  fecha_fin = $('.datepicker_fin').val();
  $.ajax({
      url: "/desempenho/detail_bar/",
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
