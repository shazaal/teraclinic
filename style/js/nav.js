document.addEventListener("DOMContentLoaded", () => {
  const mobileBtn = document.getElementById("mobile-btn");
  const mobileMenu = document.getElementById("mobile-menu");
  const mobileClose = document.getElementById("mobile-close");

  // Safety check
  if (!mobileBtn || !mobileMenu) return;

  mobileBtn.addEventListener("click", () => {
    mobileMenu.classList.remove("invisible", "opacity-0");
  });

  if (mobileClose) {
    mobileClose.addEventListener("click", () => {
      mobileMenu.classList.add("invisible", "opacity-0");
    });
  }

  document.querySelectorAll("#mobile-menu a").forEach(link => {
    link.addEventListener("click", () => {
      mobileMenu.classList.add("invisible", "opacity-0");
    });
  });
});
