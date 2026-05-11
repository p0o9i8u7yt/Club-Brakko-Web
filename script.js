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

turnoForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value.trim();
    const telefono = document.getElementById('telefono').value.trim();
    const email = document.getElementById('email').value.trim();
    const fecha = new Date().toLocaleString('es-AR');

    const newLead = {
        Fecha: fecha,
        Nombre: nombre,
        Telefono: telefono,
        Email: email
    };

    // --- GOOGLE SHEETS INTEGRATION ---
    // URL del Google Apps Script desplegado como Web App
    // IMPORTANTE: Reemplazar esta URL si se vuelve a desplegar el script
    const scriptURL = 'https://script.google.com/macros/s/AKfycby0a6CBfdvbVFXunq565t08CxYXKMU88Jeqf_WsHAnxNtVUv9ADC1m8C3CQXkouy2CKqw/exec';

    const submitBtn = turnoForm.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn ? submitBtn.textContent : '';

    try {
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Enviando...';
        }

        const formData = new URLSearchParams();
        formData.append('Fecha', fecha);
        formData.append('Nombre', nombre);
        formData.append('Telefono', telefono);
        formData.append('Email', email);

        await fetch(scriptURL, {
            method: 'POST',
            mode: 'no-cors', 
            body: formData
        });

        console.log('✅ Intento de envío a Google Sheets completado');


    } catch (error) {
        // Si falla la conexión, igual abrimos WhatsApp (el lead principal ya está)
        console.error('❌ Error al guardar lead:', error);
    } finally {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = originalBtnText;
        }
    }

    // Abrir WhatsApp independientemente del resultado
    const whatsappNumber = "5491125640517";
    const message = `¡Hola Club Brakko! 👋%0A%0AQuiero solicitar un turno. Mis datos son:%0A*Nombre:* ${nombre}%0A*Teléfono:* ${telefono}%0A*Email:* ${email}%0A%0A¿Podrían indicarme opciones de fechas y horarios disponibles?`;
    const whatsappURL = `https://wa.me/${whatsappNumber}?text=${message}`;

    window.open(whatsappURL, '_blank');

    // Reset form
    turnoForm.reset();
});

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
