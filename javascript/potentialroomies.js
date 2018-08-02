$('#college_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked_college = "checked"; //string is true
  } else {
  	localStorage.checked_college = ""; //empty string is false
  }
})
$( document ).ready(function() {
  if(localStorage.checked_college != undefined) {
    document.querySelector('#college_filter').checked = localStorage.checked_college;
  }
});

$('#year_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked_year = "checked";
  } else {
  	localStorage.checked_year = "";
  }
})
$( document ).ready(function() {
  if(localStorage.checked_year != undefined) {
    document.querySelector('#year_filter').checked = localStorage.checked_year;
	}
});

$('#gender_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked_gender = "checked";
  } else {
  	localStorage.checked_gender = "";
  }
})
$( document ).ready(function() {
  if(localStorage.checked_gender != undefined) {
    document.querySelector('#gender_filter').checked = localStorage.checked_gender;
	}
});

$('#city_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked_city = "checked";
  } else {
  	localStorage.checked_city = "";
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

$('#sleeping_filter').click(function(e){
	if (e.target.checked) {
  	localStorage.checked_sleeping = "checked";
  } else {
  	localStorage.checked_sleeping = "";
  }
})
$( document ).ready(function() {
	document.querySelector('#sleeping_filter').checked = localStorage.checked_sleeping;
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
