document.addEventListener("DOMContentLoaded", function() {
    var currentPath = window.location.pathname;
    let texts = document.querySelectorAll(".nav-text");
    let bg = document.querySelector(".nav-bg");
    let icons = document.querySelectorAll(".nav-icon");
    let head = document.querySelector(".head");

    if (currentPath.includes("home") || currentPath.includes("contact")) {
        texts.forEach(text => {
            text.classList.remove('text-[#494949]');
        });

        bg.classList.remove('bg-white')
        bg.classList.remove('shadow-md')

        head.classList.remove('pt-[73px]')

    }
    else {
        texts.forEach(text => {
            text.classList.remove('text-white');
        });

        bg.classList.remove('bg-transparent')

        icons.forEach(icon => {
            icon.classList.remove('brightness-200');
            
        });
    }
  });
  