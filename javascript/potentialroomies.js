$('#city_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked = "checked"; //string is true
  } else {
  	localStorage.checked = ""; //empty string is false
  }
})
$( document ).ready(function() {
	document.querySelector('#city_filter').checked = localStorage.checked;
});

$('#state_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked = "checked";
  } else {
  	localStorage.checked = "";
  }
})
$( document ).ready(function() {
	document.querySelector('#state_filter').checked = localStorage.checked;
});

$('#smoking_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked = "checked";
  } else {
  	localStorage.checked = "";
  }
})
$( document ).ready(function() {
	document.querySelector('#smoking_filter').checked = localStorage.checked;
});

$('#hobbies_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked = "checked";
  } else {
  	localStorage.checked = "";
  }
})
$( document ).ready(function() {
	document.querySelector('#hobbies_filter').checked = localStorage.checked;
});
