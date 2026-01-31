document.addEventListener('DOMContentLoaded', () => {
    const mobileBtn = document.getElementById('mobile-btn');
    const menuIcon = document.getElementById('menu-icon');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-link');
    let isMenuOpen = false;

    if (mobileBtn && mobileMenu) {
        mobileBtn.addEventListener('click', () => {
            isMenuOpen = !isMenuOpen;

            if (isMenuOpen) {
                // 1. Reveal Menu Container
                mobileMenu.classList.remove('invisible', 'opacity-0');
                
                // 2. Animate Icon to "X" (Rotate)
                menuIcon.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>`;
                menuIcon.classList.add('rotate-90', 'text-blue-600'); // Add color to active icon

                // 3. Staggered Link Entrance
                mobileLinks.forEach((link, index) => {
                    setTimeout(() => {
                        link.classList.remove('translate-y-8', 'opacity-0');
                    }, 100 + (index * 100)); // 100ms delay per link
                });

            } else {
                // 1. Hide Menu Container
                mobileMenu.classList.add('invisible', 'opacity-0');
                
                // 2. Revert Icon to Hamburger
                menuIcon.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>`;
                menuIcon.classList.remove('rotate-90', 'text-blue-600');

                // 3. Reset Links for next time
                mobileLinks.forEach((link) => {
                    link.classList.add('translate-y-8', 'opacity-0');
                });
            }
        });
    }
});