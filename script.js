// Navbar Scroll Effect
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Mobile Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Close mobile menu when a link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

// Handling Appointment Form Submit to WhatsApp & Storing Data
const turnoForm = document.getElementById('turnoForm');

turnoForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const telefono = document.getElementById('telefono').value;
    const email = document.getElementById('email').value;
    const fecha = new Date().toLocaleString();

    const newLead = {
        Fecha: fecha,
        Nombre: nombre,
        Telefono: telefono,
        Email: email
    };

    // Leads are now sent directly to Google Sheets for privacy and central management.

    // --- GOOGLE SHEETS INTEGRATION ---
    // Reemplaza esta URL con la que obtengas al desplegar tu Google Apps Script
    const scriptURL = 'https://script.google.com/macros/s/AKfycbwqzE40xR8Kgclv6JyiGtiBhJ9t9DMtO7EJQ6g6a2j6ZTKPNZXr71u_KiFl13tUsswRKQ/exec';

    fetch(scriptURL, {
        method: 'POST',
        mode: 'no-cors', // Importante para evitar problemas de CORS con Google Scripts
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newLead)
    })
        .then(() => console.log('Datos enviados a Google Sheets'))
        .catch(error => console.error('Error al enviar a Google Sheets:', error));

    const whatsappNumber = "5491125640517";

    const message = `¡Hola Club Brakko! 👋%0A%0AQuiero solicitar un turno. Mis datos son:%0A*Nombre:* ${nombre}%0A*Teléfono:* ${telefono}%0A*Email:* ${email}%0A%0A¿Podrían indicarme opciones de fechas y horarios disponibles?`;

    const whatsappURL = `https://wa.me/${whatsappNumber}?text=${message}`;

    window.open(whatsappURL, '_blank');

    // Optional: Reset form
    turnoForm.reset();
});

// Logic for Excel export removed for privacy. 
// Leads are now saved directly in a private Google Sheet.

// Services Tabs
const menuTabs = document.querySelectorAll('.menu-tab');
const menuCategories = document.querySelectorAll('.menu-category');

menuTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove active class from all tabs
        menuTabs.forEach(t => t.classList.remove('active'));
        // Add active class to clicked tab
        tab.classList.add('active');

        // Hide all categories
        menuCategories.forEach(cat => {
            cat.classList.remove('active');
        });

        // Show target category
        const target = tab.getAttribute('data-target');
        document.getElementById(target).classList.add('active');
    });
});
