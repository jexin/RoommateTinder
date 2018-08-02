// Get the modal
let modal = document.getElementById('myModal');

// Get the button that opens the modal
let btn = document.querySelector("button");

if (btn.innerHTML == "Edit Profile") {
  // Get the <span> element that closes the modal
  let span = document.getElementsByClassName("close")[0];

  // When the user clicks on the button, open the modal
  btn.onclick = function() {
      modal.style.display = "block";
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
      modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }
  let upload = document.getElementById("uploadBtn");

  upload.addEventListener("click", e => {
    if( document.getElementById("imgUpload").files.length == 0 ){
        alert("no files selected");
        e.preventDefault();
    }
  });

  let genders = document.querySelector("#gender");
  let gender = document.querySelector(".gender");
  genders.value = gender.innerHTML;

  let years = document.querySelector("#year");
  let year = document.querySelector(".year");
  years.value = year.innerHTML;

  let states = document.querySelector("#state");
  let state = document.querySelector(".state");
  states.value = state.innerHTML;

  let smokes = document.querySelector("#smoke");
  let smoke = document.querySelector(".smoke");
  smokes.value = smoke.innerHTML;

  let hobbyes = document.querySelector("#hobbies");
  let hobbies = document.querySelector(".hobbies");
  hobbyes.value = hobbies.innerHTML;
}
else {
  let clicked = document.querySelector(".clicked");

  let form = document.querySelector("#likeBtn");
  btn.addEventListener('click', e => {
    clicked.innerHTML = "liked";
    btn.disabled = true;
    btn.style.backgroundColor = "#ccc";
    form.submit();
  });

  if (clicked.innerHTML == "liked") {
    btn.disabled = true;
    btn.style.backgroundColor = "#ccc";
  }
}
