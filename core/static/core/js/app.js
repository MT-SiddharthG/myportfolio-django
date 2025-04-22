document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('.side-nav a');

    // This will trigger when a section is active, and we apply the "falling" animation
    function applyTransition(sectionId) {
        const section = document.getElementById(sectionId);
        section.classList.add('falling-transition'); // Add CSS class for transition
    }

    // Event listener for the nav links to apply the transition
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetSection = this.getAttribute('href').split('#')[1];

            // Apply the transition to the target section
            applyTransition(targetSection);

            // Smooth scroll to the section
            document.getElementById(targetSection).scrollIntoView({
                behavior: 'smooth'
            });

            // Optional: Update the active nav link
            navLinks.forEach(link => link.classList.remove('active-btn'));
            this.classList.add('active-btn');
        });
    });
});