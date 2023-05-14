// ---------------скролл sidebar---------------
const navbar = document.querySelector(".navbar_block");
const sidebar = document.querySelector(".sidebar_block");
const scrollThreshold = 20;
// --------------------------------------------

// -------------скролл sidebar --------------
window.addEventListener("scroll", () => {
  const currentScroll = window.scrollY;
  console.log(currentScroll)
  console.log(currentScroll)

  if (currentScroll > 20) {
    // sidebar.style.display = "block";
    sidebar.classList.add("show_hide");
  }
  if (currentScroll < 65) {
    sidebar.classList.remove("show_hide")
  }   // sidebar.style.display = "none";
  if (currentScroll > 3650) {
    sidebar.classList.remove("show_hide")
  }

});
// --------------------------------------------


const scrollTopBtn = document.querySelector(".scroll-top-btn");

window.addEventListener("scroll", () => {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollTopBtn.style.display = "block";
  } else {
    scrollTopBtn.style.display = "none";
  }
});

scrollTopBtn.addEventListener("click", () => {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
});

scrollTopBtn.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});
