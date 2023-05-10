// ---------------скролл sidebar---------------
const navbar = document.querySelector(".navbar_block");
const sidebar = document.querySelector(".sidebar_block");
const scrollThreshold = 20;
// --------------------------------------------

// -------------скролл sidebar --------------
window.addEventListener("scroll", () => {
  const currentScroll = window.scrollY;
  console.log(currentScroll)

  if (currentScroll > 20) {
    // sidebar.style.display = "block";
    sidebar.classList.add("show_hide");
  }
  if (currentScroll < 65) {
    sidebar.classList.remove("show_hide")
  }   // sidebar.style.display = "none";

});
// --------------------------------------------

