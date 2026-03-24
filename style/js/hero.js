const slides = [
  {
    title: "Nurturing<br>Young <span class='text-blue-600'>Minds</span>",
    desc: "Specialist behavioral and academic interventions to help your child thrive.",
    img1: "images/hero-1.jpg",
    img2: "images/hero-2.jpg",
  },
  {
    title: "Building  <br> Healthier <span class='text-blue-600'>Relationships</span>",
    desc: "Professional guidance to foster understanding, resolve conflict, and strengthen family bonds.",
    img1: "images/hero-3.jpg",
    img2: "images/hero-4.jpg",
  }, 
  {
    title: "Your  <br> Path to  <span class='text-blue-600'>Inner Balance</span>",
    desc: "Evidence-based psychotherapy and counseling for a more resilient you.",
    img1: "images/hero-4.jpg",
    img2: "images/hero-1.jpg",
  },
];

let index = 0;

const heroText = document.getElementById("hero-text");
const title = document.getElementById("hero-title");
const desc = document.getElementById("hero-desc");
const img1 = document.getElementById("img1");
const img2 = document.getElementById("img2");

function hideHero() {
  heroText.classList.add("opacity-0", "translate-y-10");
  img1.classList.add("opacity-0", "translate-y-14");
  img2.classList.add("opacity-0", "-translate-y-14");
}

function showHero() {
  heroText.classList.remove("opacity-0", "translate-y-10");
  img1.classList.remove("opacity-0", "translate-y-14");
  img2.classList.remove("opacity-0", "-translate-y-14");
}

function updateHero() {
  hideHero();

  setTimeout(() => {
    const s = slides[index];
    title.innerHTML = s.title;
    desc.innerHTML = s.desc;
    img1.querySelector("img").src = s.img1;
    img2.querySelector("img").src = s.img2;

    showHero();
  }, 600);
}

// init
updat
