
  const lenis = new Lenis({
    duration: 1.1,          // scroll speed (lower = faster)
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true,      // 👈 mouse wheel
    smoothTouch: false      // keep mobile native (recommended)
  });

  function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
  }

  requestAnimationFrame(raf);
