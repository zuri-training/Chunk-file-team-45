//toggle
const menuBtn = document.querySelector(".menu__btn");
const menuRespond = document.querySelector(".responsive");
let menuClosed = true;

menuBtn.addEventListener("click", () => {
  if (menuClosed) {
    menuBtn.classList.add("open");
    menuRespond.classList.add("responsiveBlock");
    menuClosed = false;
  } else {
    menuBtn.classList.remove("open");
    menuClosed = true;
    menuRespond.classList.remove("responsiveBlock");
  }
});

///VALIDATION////

const form = document.getElementById("form");
const userName = document.getElementById("username");
const password = document.getElementById("password");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  checkInput();
});

function checkInput() {
  const userNameValue = userName.value.trim();
  const passwordValue = password.value.trim();

  ///VALIDATE USERNAME//

  if (userNameValue === "") {
    setErrorFor(userName, "Username cannot be blank");
  } else if (!validateUserName(userNameValue)) {
    setErrorFor(userName, "only letters,numbers and underscore allowed");
  } else {
    setSuccessFor(userName);
  }

  if (passwordValue === "") {
    setErrorFor(password, "Password cannot be blank");
  } else if (passwordValue.length < 8 ) {
    setErrorFor(password, "Password can not be less than 8 characters");
  } else {
    setSuccessFor(password);
  }
}

function setErrorFor(input, message) {
  const formControl = input.parentElement;
  const small = formControl.querySelector("small");

  small.innerText = message;

  //Display the error class
  formControl.className = "form-control errors";
}

function setSuccessFor(input) {
  const formControl = input.parentElement;
  formControl.className = "form-control success";
}

//USERNAME VALIDATOR
function validateUserName(userName) {
  const regex = /^[a-zA-Z0-9_]+$/;
  return regex.test(userName);
}
