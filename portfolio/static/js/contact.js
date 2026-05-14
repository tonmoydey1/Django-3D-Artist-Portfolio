// HAMBURGER MENU

const menuToggle = document.getElementById("menuToggle");

const navMenu = document.getElementById("navMenu");

menuToggle.addEventListener("click", () => {

  navMenu.classList.toggle("active");

});



// FAQ

const faqQuestions = document.querySelectorAll(".faq-question");

faqQuestions.forEach(question => {

  question.addEventListener("click", () => {

    const answer =
      question.nextElementSibling;

    if(answer.style.display === "block"){

      answer.style.display = "none";

    }else{

      answer.style.display = "block";

    }

  });

});

// SUCCESS POPUP AUTO HIDE

const successPopup = document.querySelector(".success-popup");

if(successPopup){

  setTimeout(() => {

    successPopup.style.display = "none";

  }, 3000);

}