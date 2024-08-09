// core/static/js/scripts.js

let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("mySlides");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(showSlides, 7000); // Change image every 7 seconds for smoother transition
}

let infoSlideIndex = 0;
showInfoSlides();

function showInfoSlides() {
    let infoSlides = document.getElementsByClassName("infoSlides");
    for (let i = 0; i < infoSlides.length; i++) {
        infoSlides[i].style.display = "none";
    }
    infoSlideIndex++;
    if (infoSlideIndex > infoSlides.length) {infoSlideIndex = 1}
    infoSlides[infoSlideIndex-1].style.display = "block";
    setTimeout(showInfoSlides, 7000); // Change image every 7 seconds for smoother transition
}

document.getElementById('userSignupButton').addEventListener('click', function() {
    document.getElementById('signupForm').style.display = 'block';
});

document.getElementById('loginButton').addEventListener('click', function() {
    // Add login functionality here
});

