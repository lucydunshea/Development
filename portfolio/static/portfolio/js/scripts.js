document.addEventListener('DOMContentLoaded', function() {
  const hamburgerMenu = document.querySelector('.hamburger-menu');
  const popupMenu = document.querySelector('.popup-menu');
  hamburgerMenu.addEventListener('click', function() {
      if (hamburgerMenu.classList.contains('open')) {
          hamburgerMenu.classList.remove('open');
          popupMenu.classList.remove('open');
      } else {
          hamburgerMenu.classList.add('open');
          popupMenu.classList.add('open');
      }
  });
  });

  document.addEventListener('DOMContentLoaded', function() {
    const projectsSection = document.querySelector('.projects-section');
    let isMouseDown = false;
    let startX;
    let scrollLeft;

    projectsSection.addEventListener('mousedown', (e) => {
        isMouseDown = true;
        startX = e.pageX - projectsSection.offsetLeft;
        scrollLeft = projectsSection.scrollLeft;
    });

    projectsSection.addEventListener('mouseleave', () => {
        isMouseDown = false;
    });

    projectsSection.addEventListener('mouseup', () => {
        isMouseDown = false;
    });

    projectsSection.addEventListener('mousemove', (e) => {
        if (!isMouseDown) return;
        e.preventDefault();
        const x = e.pageX - projectsSection.offsetLeft;
        const walk = (x - startX) * 2; // Adjust scroll speed
        projectsSection.scrollLeft = scrollLeft - walk;
    });
});

lastScrollTop;
navbar = document.getElementById('navbar');
window.addEventListener('scroll',function(){
  var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  if(scrollTop > lastScrollTop){
    navbar.style.top='-80px';
  }
  else{
    navbar.style.top='0';
  }
  lastScrollTop = scrollTop;
});

