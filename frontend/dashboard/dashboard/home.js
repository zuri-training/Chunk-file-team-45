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


const sizeRadio = document.getElementById("split");
const sizeInput = document.querySelector(".two");
const chunk = document.querySelector(".one");
sizeInput.disabled = true



function disableInput() {
  if (sizeRadio.checked) {
    chunk.disabled = true;
    sizeInput.disabled = false;
  } else {
    sizeInput.disabled = true;
    chunk.disabled = false;
  }
}
