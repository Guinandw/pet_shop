$('.product-list-item').click(function() {
    let value = $(this).attr('data-filter');
    if(value === 'todo') {
      $('.filter').show(0);
    } else {
      $('.filter').not('.' + value).hide(0);
      $('.filter').filter('.' + value).show(0);
    }
  });

  $('.producto-activo').click(function() {
    $('.producto-activo').removeClass('active');
    $(this).addClass('active')
  });