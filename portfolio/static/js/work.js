// HAMBURGER MENU

const menuToggle = document.getElementById("menuToggle");

const navMenu = document.getElementById("navMenu");

menuToggle.addEventListener("click", () => {

  navMenu.classList.toggle("active");

});

// FILTER FEATURE

const filterButtons = document.querySelectorAll(".filter-btn");

const cards = document.querySelectorAll(".work-card");

filterButtons.forEach(button => {

  button.addEventListener("click", () => {

    document
      .querySelector(".filter-btn.active")
      .classList.remove("active");

    button.classList.add("active");

    const filter = button.getAttribute("data-filter");

    cards.forEach(card => {

      if(
        filter === "all" ||
        card.classList.contains(filter)
      ){

        card.style.display = "block";

      }else{

        card.style.display = "none";

      }

    });

  });

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