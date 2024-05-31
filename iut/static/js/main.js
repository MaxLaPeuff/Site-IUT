



$(document).ready(function() {
  $(".d-flex").click(function() {
    $(this).find(".icon").toggleClass("fa-angle-up fa-angle-down");
    $(this).find(".content").slideToggle();
  });

  $(".icon").click(function() {
    $(this).toggleClass("fa-angle-up fa-angle-down");
    $(this).parent().find(".content").slideToggle();
  });
});

  