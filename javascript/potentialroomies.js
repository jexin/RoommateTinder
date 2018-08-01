$('#city_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked_city = "checked"; //string is true
  } else {
  	localStorage.checked_city = ""; //empty string is false
  }
})
$( document ).ready(function() {
	document.querySelector('#city_filter').checked = localStorage.checked_city;
});

$('#state_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked_state = "checked";
  } else {
  	localStorage.checked_state = "";
  }
})
$( document ).ready(function() {
	document.querySelector('#state_filter').checked = localStorage.checked_state;
});

$('#smoking_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked_smoking = "checked";
  } else {
  	localStorage.checked_smoking = "";
  }
})
$( document ).ready(function() {
	document.querySelector('#smoking_filter').checked = localStorage.checked_smoking;
});

$('#hobbies_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked_hobbies = "checked";
  } else {
  	localStorage.checked_hobbies = "";
  }
})
$( document ).ready(function() {
	document.querySelector('#hobbies_filter').checked = localStorage.checked_hobbies;
});
