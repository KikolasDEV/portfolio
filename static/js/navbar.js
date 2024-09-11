// Este script asegura que el navbar permanezca visible al hacer scroll
window.onscroll = function() {
    var navbar = document.querySelector(".navbar");
    var sticky = navbar.offsetTop;
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("fixed-top");
    } else {
        navbar.classList.remove("fixed-top");
    }
};
