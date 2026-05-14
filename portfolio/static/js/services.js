// HAMBURGER MENU

const menuToggle = document.getElementById("menuToggle");

const navMenu = document.getElementById("navMenu");

menuToggle.addEventListener("click", () => {

  navMenu.classList.toggle("active");

});

// POPUP

const popup = document.getElementById("popup");

const getTouchBtn = document.getElementById("getTouchBtn");

const workTogetherBtn = document.getElementById("workTogetherBtn");

const heroBtn = document.getElementById("heroBtn");

const closePopup = document.getElementById("closePopup");

getTouchBtn.addEventListener("click", () => {

  popup.style.display = "flex";

});

workTogetherBtn.addEventListener("click", () => {

  popup.style.display = "flex";

});

heroBtn.addEventListener("click", () => {

  popup.style.display = "flex";

});

closePopup.addEventListener("click", () => {

  popup.style.display = "none";

});

window.addEventListener("click", (e) => {

  if(e.target === popup){

    popup.style.display = "none";

  }

});

// SUCCESS POPUP AUTO HIDE

const successPopup = document.querySelector(".success-popup");

if(successPopup){

  setTimeout(() => {

    successPopup.style.display = "none";

  }, 3000);

}