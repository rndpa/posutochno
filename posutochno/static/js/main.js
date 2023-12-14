function burger() {
  let btn = document.getElementById("burgerBtn");
  let menuBtn = document.querySelector(".menu-btn");
  let headerBurger = document.querySelector(".header-burger");

  btn.addEventListener("click", function () {
    menuBtn.classList.toggle("active");
    headerBurger.classList.toggle("hidden");
  });
}

function slider() {
  const swiper = new Swiper(".swiper", {
    autoplay: {
      delay: 1500,
    },
    speed: 1800,
    pagination: {
      el: ".swiper-pagination",
    },
  });
}

slider();
burger();
