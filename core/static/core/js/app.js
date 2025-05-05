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


const sections = document.querySelectorAll('.section');
const sectBtns = document.querySelectorAll('.controls');
const sectBtn = document.querySelectorAll('.control');
const allSections = document.querySelector('.main-content');

function PageTransitions(){

    // Active button class activation on click
    for(let i = 0; i < sectBtn.length; i++){
        sectBtn[i].addEventListener('click', function(){
            let currentBtn = document.querySelectorAll('.active-btn');
            currentBtn[0].className = currentBtn[0].className.replace('active-btn', '')
            this.className += ' active-btn'
        })
    }

    // Active section activation on click
    allSections.addEventListener('click', (e) => {
        const id = e.target.dataset.id;
        if (id){
            // Remove the selected button from other buttons
            sectBtns.forEach((btn) => {
                btn.classList.remove('active')
            })
            e.target.classList.add('active')

            // Hide other sections
            sections.forEach((section) => {
                section.classList.remove('active')
            })

            const element = document.getElementById(id);
            element.classList.add('active');
        }
    })
}

PageTransitions();