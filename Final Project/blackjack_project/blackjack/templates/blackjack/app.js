
$(".dropdown-menu li a").click(function(){
  $(".btn:first-child").html($(this).text()+' <span class="caret"></span>');
});

var policyChoice = $("#policy").text();
alert(policyChoice);

$('#policy').on('hidden.bs.dropdown', function () {
  $('#chosen-policy').text(policyChoice);
});
