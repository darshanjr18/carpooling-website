// routes.js

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 19.041200906199247, lng: 72.85027501007903 }, // Example: New York City
        zoom: 12
    });

    // Example: Adding markers for the routes
    var markers = [
        { position: { lat: 19.057893211773823, lng: 72.84105558568427}, title: "bandra" },
        { position: { lat: 19.019675936335098, lng: 72.84377568510308 }, title: "dadar" },
        { position: { lat: 19.069700198834774, lng: 72.99968295136141 }, title: "vashi" }
    ];

    markers.forEach(function(marker) {
        new google.maps.Marker({
            position: marker.position,
            map: map,
            title: marker.title
        });
    });
}

window.onload = initMap;

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
