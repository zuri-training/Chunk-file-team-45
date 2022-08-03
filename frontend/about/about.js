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

///// SLIDER /////

let slider = tns({
  container: ".my-slider",
  "slideBy": 1,
  "speed": 400,
  "nav": false,
  controlsContainer: "#controls",
  prevButton: ".previous",
  nextButton: ".next",
  responsive: {
    1600: {
      items: 4.8,
      gutter: 10
    },
    1024: {
      items: 4.8,
      gutter: 10
    },
    768:{
      items: 3.8,
      gutter: 10
    },
    480: {
      items: 2.3,
      gutter: 10
    },
    375: {
      items: 2.3,
      gutter: 10
    }

  }
})
