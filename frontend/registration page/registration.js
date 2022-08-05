//toggle
const menuBtn = document.querySelector(".menu__btn");
const menuRespond = document.querySelector(".responsive");
let menuClosed = true;

menuBtn.addEventListener("click", () => {
  if(menuClosed) {
    menuBtn.classList.add("open");
    menuRespond.classList.add("responsiveBlock");
    menuClosed = false;
  } else {
    menuBtn.classList.remove("open");
    menuClosed = true;   
    menuRespond.classList.remove("responsiveBlock");
  }
})

// form Validation

const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password1 = document.getElementById('password1');

form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});

const setError = (element,message) =>{
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}
const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};
const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password1Value = password1.value.trim();

    if(usernameValue === '') {
        setError(username, 'Username is required');
    } else {
        setSuccess(username);
    }

    if(emailValue === '') {
        setError(email, 'Email is required');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Provide a valid email address');
    } else {
        setSuccess(email);
    }
    
    if(passwordValue === '') {
        setError(password, 'Password is required');
    } else if (passwordValue.length < 8 ) {
        setError(password, 'Password must be at least 8 character.')
    } else {
        setSuccess(password);
    }
    
    
    if(password1Value === '') {
        setError(password1, 'Please confirm your password');
    } else if (password1Value.length!== passwordValue.length) {
        setError(password1, "Passwords doesn't match");
    } else {
        setSuccess(password1);
    }

    

};
