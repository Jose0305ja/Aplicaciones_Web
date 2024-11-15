//Seleccionar todas las imagenes del slider
let slides = document.querySelectorAll('.slide');
let currentSlide = 0;

//funcion para cambiar de imagen
function changeSlide() {
    //Oculta la imagen actual
    slides[currentSlide].classList.remove('active');

    //Cambia al siguiente slide
    currentSlide = (currentSlide + 1) % slides.length;

    //Muestra la siguiente imagen
    slides[currentSlide].classList.add('active');
}

//Inicia el slider cambiando cada 3 segundos
setInterval(changeSlide, 3000);