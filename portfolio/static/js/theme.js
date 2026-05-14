const savedTheme = localStorage.getItem("portfolioTheme");
const prefersLight = window.matchMedia("(prefers-color-scheme: light)").matches;
const initialTheme = savedTheme || (prefersLight ? "light" : "dark");

document.body.classList.toggle("light-theme", initialTheme === "light");

const themeToggle = document.getElementById("themeToggle");

document.querySelectorAll(".work-card > img").forEach((image) => {
  image.parentElement.style.setProperty("--card-image-bg", `url("${image.currentSrc || image.src}")`);
});

if (themeToggle) {
  const updateThemeButton = () => {
    const isLight = document.body.classList.contains("light-theme");
    themeToggle.setAttribute("aria-pressed", String(isLight));
    themeToggle.setAttribute("aria-label", isLight ? "Switch to dark theme" : "Switch to light theme");
    themeToggle.querySelector(".theme-label").textContent = isLight ? "Dark" : "Light";
    themeToggle.querySelector("i").className = isLight ? "fa-solid fa-moon" : "fa-solid fa-sun";
  };

  updateThemeButton();

  themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("light-theme");
    localStorage.setItem(
      "portfolioTheme",
      document.body.classList.contains("light-theme") ? "light" : "dark"
    );
    updateThemeButton();
  });
}
