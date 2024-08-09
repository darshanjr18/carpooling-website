document.addEventListener('DOMContentLoaded', function () {
    var splide = new Splide('#image-carousel', {
        type       : 'loop',           // Allows continuous looping
        heightRatio: 0.5,              // Adjust the height ratio if needed
        autoplay   : true,            // Enables automatic sliding
        interval   : 3000,            // Slide change interval (in milliseconds)
        perPage    : 1,               // Number of slides per page
        focus      : 'center',        // Focuses the center slide
        gap        : '1rem',          // Gap between slides
        pagination: false,           // Optional: hide pagination
        arrows: false,               // Optional: hide arrows
        speed: 1000,                 // Slide transition speed (in milliseconds)
    }).mount();
});


// Add to home.js

document.addEventListener('DOMContentLoaded', function () {
    const findRidesButton = document.querySelector('.btn');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');

    // Function to animate button click
    function animateClick(button) {
        button.classList.add('clicked');
        setTimeout(() => {
            button.classList.remove('clicked');
        }, 300);
    }

    // Event listeners for buttons
    findRidesButton.addEventListener('click', function() {
        animateClick(findRidesButton);
        // Implement redirection or form submission here
        // For example, window.location.href = 'URL';
    });

    prevButton.addEventListener('click', function() {
        animateClick(prevButton);
        // Implement previous slide functionality here
    });

    nextButton.addEventListener('click', function() {
        animateClick(nextButton);
        // Implement next slide functionality here
    });
});



// Trigger animations when the footer comes into view
document.addEventListener('DOMContentLoaded', function() {
    const footerSections = document.querySelectorAll('.footer-section');
    
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    footerSections.forEach(section => {
        observer.observe(section);
    });
});






