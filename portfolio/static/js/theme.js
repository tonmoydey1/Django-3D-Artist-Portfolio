const savedTheme = localStorage.getItem("portfolioTheme");
const prefersLight = window.matchMedia("(prefers-color-scheme: light)").matches;
const initialTheme = savedTheme || (prefersLight ? "light" : "dark");

document.body.classList.toggle("light-theme", initialTheme === "light");

const themeToggle = document.getElementById("themeToggle");
const queryParams = new URLSearchParams(window.location.search);

if (queryParams.get("sent") === "1") {
  const container = document.querySelector(".message-container") || document.createElement("div");
  container.classList.add("message-container");

  if (!container.parentElement) {
    document.body.prepend(container);
  }

  const popup = document.createElement("div");
  popup.className = "success-popup";
  popup.textContent = "Message Sent Successfully!";
  container.appendChild(popup);

  window.history.replaceState({}, document.title, window.location.pathname + window.location.hash);
}

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
