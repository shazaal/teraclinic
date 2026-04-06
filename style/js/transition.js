document.addEventListener("DOMContentLoaded", () => {
    const wrapper = document.querySelector('.page-transition-wrapper');

    // 1. ANIMATE IN
    setTimeout(() => {
        if(wrapper) wrapper.classList.add('loaded');
    }, 50);

    // 2. HANDLE EXIT
    const links = document.querySelectorAll('a');

    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            
            // Filter out empty links, anchors, and new tabs
            if (href && !href.startsWith('#') && link.target !== '_blank') {
                e.preventDefault();
                
                // Fade out the wrapper
                if(wrapper) wrapper.classList.remove('loaded');

                setTimeout(() => {
                    window.location.href = href;
                }, 400); 
            }
        });
    });
});

// 3. BACK BUTTON FIX 

window.addEventListener('pageshow', (event) => {
    if (event.persisted) {
        const wrapper = document.querySelector('.page-transition-wrapper');
        if(wrapper) wrapper.classList.add('loaded');
    }
});