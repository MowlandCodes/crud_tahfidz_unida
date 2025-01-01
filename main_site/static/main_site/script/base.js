const sidebar = document.querySelector('.sidebar');
const logo = document.querySelector('.logo-unida');
const nav_link = document.querySelectorAll('.nav-link');

function toggle_sidebar(button) {
    const toggle_sidebar_icon = button.querySelector('i');
    sidebar.classList.toggle('close');
    toggle_sidebar_icon.classList.toggle('rotate');
    logo.classList.toggle('hidden');
    for (i = 0; i < nav_link.length; i++) {
        nav_link[i].classList.toggle('hidden');
    }
}
