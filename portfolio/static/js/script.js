// static/js/script.js

// MOBILE MENU

const menuToggle = document.getElementById("menuToggle");
const navMenu = document.getElementById("navMenu");

menuToggle.addEventListener("click", () => {
  navMenu.classList.toggle("active");
});

// POPUP

const popup = document.getElementById("popup");

const getTouchBtn = document.getElementById("getTouchBtn");
const workTogetherBtn = document.getElementById("workTogetherBtn");

const closePopup = document.getElementById("closePopup");

getTouchBtn.addEventListener("click", () => {
  popup.style.display = "flex";
});

workTogetherBtn.addEventListener("click", () => {
  popup.style.display = "flex";
});

closePopup.addEventListener("click", () => {
  popup.style.display = "none";
});

window.addEventListener("click", (e) => {
  if (e.target === popup) {
    popup.style.display = "none";
  }
});

// VIEW WORK BUTTON

const viewWorkBtn = document.getElementById("viewWorkBtn");

viewWorkBtn.addEventListener("click", () => {
  document
    .getElementById("work")
    .scrollIntoView({ behavior: "smooth" });
});

// ABOUT BUTTON

const aboutBtn = document.getElementById("aboutBtn");

aboutBtn.addEventListener("click", () => {
  document
    .getElementById("about")
    .scrollIntoView({ behavior: "smooth" });
});


// SUCCESS MESSAGE AUTO HIDE

const successPopup = document.querySelector(".success-popup");

if(successPopup){

  setTimeout(() => {

    successPopup.style.display = "none";

  }, 3000);

}