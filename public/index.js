// Get the navigation bar element
const navBar = document.getElementById('nav-bar');

// Get all the navigation links and dropdown menus
const navLinks = navBar.getElementsByClassName('nav-link');
const dropdownMenus = navBar.getElementsByClassName('dropdown-menu');

// Loop through all the navigation links
for (let i = 0; i < navLinks.length; i++) {
  const link = navLinks[i];

  // Add a click event listener to each navigation link
  link.addEventListener('click', function(e) {
    e.preventDefault();

    // Remove the "active" class from all navigation links
    for (let j = 0; j < navLinks.length; j++) {
      navLinks[j].classList.remove('active');
    }

    // Add the "active" class to the clicked navigation link
    link.classList.add('active');
  });

  // If the navigation link has a dropdown menu
  if (link.nextElementSibling && link.nextElementSibling.classList.contains('dropdown-menu')) {
    const dropdownMenu = link.nextElementSibling;

    // Hide the dropdown menu
    dropdownMenu.style.display = 'none';

    // Add a click event listener to the navigation link to toggle the dropdown menu
    link.addEventListener('click', function(e) {
      e.preventDefault();
      if (dropdownMenu.style.display === 'none') {
        dropdownMenu.style.display = 'block';
      } else {
        dropdownMenu.style.display = 'none';
      }
    });
  }
}


// Adjust the navigation bar on window resize
window.addEventListener('resize', function () {
  const width = window.innerWidth;
  if (width >= 768) {
    for (let i = 0; i < dropdownMenus.length; i++) {
      dropdownMenus[i].style.display = 'block';
    }
  } else {
    for (let i = 0; i < dropdownMenus.length; i++) {
      dropdownMenus[i].style.display = 'none';
    }
  }
});
