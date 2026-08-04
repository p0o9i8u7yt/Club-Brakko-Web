import json

data = [
    {"tab": "manos-pies", "title": "Manos y Pies", "categories": [
        {"name": "Manicuría", "items": [
            {"name": "Manicuría con Esmaltado Tradicional", "cash": "23.000", "list": "25.300", "time": "30'", "best": False},
            {"name": "Manicuría con Esmaltado Semipermanente", "cash": "24.000", "list": "26.400", "time": "60'", "best": False},
            {"name": "Kapping", "cash": "33.000", "list": "36.300", "time": "90'", "best": False},
            {"name": "Service Esculpidas (Gel, Polygel)", "cash": "35.000", "list": "38.500", "time": "90'", "best": False},
            {"name": "Full Set Esculpidas (Gel, Polygel)", "cash": "39.000", "list": "42.900", "time": "120'", "best": False},
            {"name": "Manicuría sin Esmaltado", "cash": "20.000", "list": "22.000", "time": "30'", "best": False},
            {"name": "Soft Gel", "cash": "35.000", "list": "38.500", "time": "90'", "best": False},
            {"name": "Spa de Manos", "cash": "17.000", "list": "18.700", "time": "30'", "best": True}
        ]},
        {"name": "Estética de Pies", "items": [
            {"name": "Belleza de Pies sin Esmaltado", "cash": "24.000", "list": "26.400", "time": "30'", "best": False},
            {"name": "Belleza de Pies con Esmaltado Tradicional", "cash": "28.000", "list": "30.800", "time": "60'", "best": False},
            {"name": "Belleza de Pies con Esmaltado Semipermanente", "cash": "28.000", "list": "30.800", "time": "60'", "best": False},
            {"name": "Spa de Pies", "cash": "20.000", "list": "22.000", "time": "40'", "best": True},
            {"name": "Pedicuría sin Esmaltado", "cash": "32.000", "list": "35.200", "time": "50'", "best": False},
            {"name": "Pedicuría con Esmaltado Semipermanente o Tradicional", "cash": "35.000", "list": "38.500", "time": "60'", "best": False},
            {"name": "Promo Spa Manos y Pies", "cash": "35.000", "list": "38.500", "time": "90'", "best": True}
        ]}
    ]},
    {"tab": "peluqueria", "title": "Peluquería", "categories": [
        {"name": "Peluquería", "items": [
            {"name": "Corte Dama", "cash": "30.000", "list": "33.000", "time": "60'", "best": False},
            {"name": "Corte Hombre", "cash": "24.000", "list": "26.400", "time": "40'", "best": False},
            {"name": "Corte Niño (Hasta 7 años)", "cash": "18.000", "list": "19.800", "time": "30'", "best": False},
            {"name": "Tintura (Desde)", "cash": "65.000", "list": "71.500", "time": "120'", "best": False},
            {"name": "Reflejos / Mechas / Balayage", "cash": "160.000", "list": "176.000", "time": "--", "best": False},
            {"name": "Alisado / Keratina (Desde)", "cash": "70.000", "list": "77.000", "time": "120'", "best": False},
            {"name": "Baño de Crema Karseell", "cash": "60.000", "list": "66.000", "time": "90'", "best": True},
            {"name": "Peinado para Fiestas", "cash": "70.000", "list": "77.000", "time": "--", "best": False},
            {"name": "Cauterización Células Madres", "cash": "65.000", "list": "71.500", "time": "90'", "best": True},
            {"name": "Reflejos Hombre Desde", "cash": "85.000", "list": "93.500", "time": "--", "best": False}
        ]}
    ]},
    {"tab": "pestanas-cejas", "title": "Pestañas y Cejas", "categories": [
        {"name": "Pestañas", "items": [
            {"name": "Lifting de Pestañas + Tinte y Botox", "cash": "38.000", "list": "41.800", "time": "60'", "best": False},
            {"name": "Pelo x Pelo Clásicas (Full)", "cash": "39.000", "list": "42.900", "time": "40'", "best": False},
            {"name": "Pelo x Pelo Clásicas (Service)", "cash": "37.000", "list": "40.700", "time": "90'", "best": False},
            {"name": "Efecto Rímel o Húmedo (Full)", "cash": "41.000", "list": "45.100", "time": "90'", "best": False},
            {"name": "Efecto Rímel o Húmedo (Service)", "cash": "39.000", "list": "42.900", "time": "90'", "best": False},
            {"name": "Tecnológicas 2D (Full)", "cash": "44.000", "list": "48.400", "time": "90'", "best": False},
            {"name": "Tecnológicas 2D (Service)", "cash": "42.000", "list": "46.200", "time": "90'", "best": False},
            {"name": "Tecnológicas 4D (Full)", "cash": "46.000", "list": "50.600", "time": "90'", "best": False},
            {"name": "Tecnológicas 4D (Service)", "cash": "44.000", "list": "48.400", "time": "90'", "best": False},
            {"name": "Consultar por Volumen // Tecnológicas 5 y 6D", "cash": "Consultar", "list": "", "time": "--", "best": False}
        ]},
        {"name": "Cejas y Promos", "items": [
            {"name": "Perfilado de Cejas", "cash": "16.000", "list": "17.600", "time": "30'", "best": False},
            {"name": "Perfilado de Cejas y Henna", "cash": "29.000", "list": "31.900", "time": "20'", "best": False},
            {"name": "Laminado de Cejas y Perfilado", "cash": "33.000", "list": "36.300", "time": "45'", "best": False},
            {"name": "Laminado de Cejas y Perfilado + Henna", "cash": "40.000", "list": "44.000", "time": "60'", "best": False},
            {"name": "Microblading", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Promo Ojos: Lifting Completo + Laminado + Perfilado", "cash": "60.000", "list": "66.000", "time": "60'", "best": False},
            {"name": "Promo Ojos: Lifting Completo + Perfilado", "cash": "49.000", "list": "53.900", "time": "60'", "best": False}
        ]}
    ]},
    {"tab": "cosmiatria", "title": "Cosmiatría", "categories": [
        {"name": "Tratamientos Faciales", "items": [
            {"name": "Higiene Premium", "cash": "50.000", "list": "55.000", "time": "90'", "best": True},
            {"name": "Peeling", "cash": "50.000", "list": "55.000", "time": "60'", "best": True},
            {"name": "Microneedling", "cash": "55.000", "list": "60.500", "time": "90'", "best": False},
            {"name": "Higiene Profunda de Espalda", "cash": "60.000", "list": "66.000", "time": "70'", "best": False},
            {"name": "Rejuvenecimiento en Manos", "cash": "25.000", "list": "27.500", "time": "20'", "best": True},
            {"name": "Higiene Premium con Dermaplaning", "cash": "60.000", "list": "66.000", "time": "90'", "best": False},
            {"name": "Dermaplaning con Nanoneedling", "cash": "70.000", "list": "77.000", "time": "90'", "best": False},
            {"name": "Radiofrecuencia Facial", "cash": "50.000", "list": "55.000", "time": "90'", "best": False},
            {"name": "Higiene con Terapia LED", "cash": "55.000", "list": "60.500", "time": "90'", "best": False},
            {"name": "Hidratación con Ultrasonido", "cash": "55.000", "list": "60.500", "time": "90'", "best": False},
            {"name": "Tratamiento con Acné", "cash": "50.000", "list": "55.000", "time": "90'", "best": False},
            {"name": "Colagenina y Fillerina (1 Sesión)", "cash": "70.000", "list": "77.000", "time": "90'", "best": False},
            {"name": "Colagenina y Fillerina (2 Sesiones)", "cash": "63.000", "list": "69.300", "time": "90'", "best": False},
            {"name": "Cauterización de Acrocordones con Plasma Pen", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Spa Facial", "cash": "50.000", "list": "55.000", "time": "90'", "best": False},
            {"name": "Vita C", "cash": "50.000", "list": "55.000", "time": "60'", "best": False},
            {"name": "Facial Holístico", "cash": "50.000", "list": "55.000", "time": "90'", "best": False},
            {"name": "Hydralips", "cash": "30.000", "list": "33.000", "time": "30'", "best": False},
            {"name": "Exoxomas", "cash": "60.000", "list": "66.000", "time": "60'", "best": False}
        ]}
    ]},
    {"tab": "masajes", "title": "Masajes", "categories": [
        {"name": "Masajes y Relax", "items": [
            {"name": "Descontracturante y Relajante", "cash": "40.000", "list": "44.000", "time": "60'", "best": False},
            {"name": "Drenaje Linfático", "cash": "40.000", "list": "44.000", "time": "60'", "best": False},
            {"name": "Masaje Premium (Descont. + Higiene Facial + Capilares)", "cash": "55.000", "list": "60.500", "time": "90'", "best": True},
            {"name": "Ayurveda", "cash": "55.000", "list": "60.500", "time": "90'", "best": True},
            {"name": "Strong", "cash": "55.000", "list": "60.500", "time": "60'", "best": False},
            {"name": "Maderoterapia / Masajes Reductores", "cash": "40.000", "list": "44.000", "time": "60'", "best": False},
            {"name": "Reflexología", "cash": "40.000", "list": "44.000", "time": "60'", "best": True},
            {"name": "Masaje con Reiki", "cash": "55.000", "list": "60.500", "time": "90'", "best": True},
            {"name": "Masaje Craneal y Piernas Cansadas", "cash": "40.000", "list": "44.000", "time": "45'", "best": False},
            {"name": "Piedras Calientes", "cash": "45.000", "list": "49.500", "time": "60'", "best": True}
        ]}
    ]},
    {"tab": "holistico", "title": "Holístico & Extras", "categories": [
        {"name": "Servicios Holísticos", "items": [
            {"name": "Reiki con Cristales y Péndulo", "cash": "38.000", "list": "41.800", "time": "90'", "best": True},
            {"name": "Registros Akáshicos", "cash": "45.000", "list": "49.500", "time": "90'", "best": False},
            {"name": "Péndulo Hebreo", "cash": "35.000", "list": "38.500", "time": "90'", "best": True},
            {"name": "Carta Natal", "cash": "70.000", "list": "77.000", "time": "60'", "best": True},
            {"name": "Revolución Solar", "cash": "80.000", "list": "88.000", "time": "60'", "best": False},
            {"name": "Astrología + Tarot + Oráculos", "cash": "60.000", "list": "66.000", "time": "60'", "best": True},
            {"name": "Carta Numerológica", "cash": "35.000", "list": "38.500", "time": "60'", "best": True},
            {"name": "Cosmetología Holística", "cash": "50.000", "list": "55.000", "time": "90'", "best": True}
        ]},
        {"name": "Servicios Adicionales", "items": [
            {"name": "Maquillaje Social, Quinceañeras / Novias / Madrinas", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Giftcards con Productos y Servicios", "cash": "Consultar", "list": "", "time": "--", "best": False}
        ]}
    ]},
    {"tab": "depilacion", "title": "Depilación Láser", "categories": [
        {"name": "Tratamiento realizado con equipo Alma Soprano Ice ORIGINAL", "items": [
            {"name": "Próxima Jornada: 25/08", "cash": "Consultar", "list": "", "time": "--", "best": True},
            {"name": "Combos y Precios (Esperando imagen)", "cash": "Consultar", "list": "", "time": "--", "best": False}
        ]}
    ]},
    {"tab": "aparatologia", "title": "Aparatología", "categories": [
        {"name": "Aparatología", "items": [
            {"name": "Crio-Fraxis", "cash": "Consultar", "list": "", "time": "30/07", "best": False},
            {"name": "HIFU 12D MAX", "cash": "Consultar", "list": "", "time": "25/08", "best": True},
            {"name": "Láser ND YAG", "cash": "Consultar", "list": "", "time": "12/08", "best": False},
            {"name": "Radiofrecuencia Fraccionada", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Criolipolisis", "cash": "Consultar", "list": "", "time": "27/08", "best": False},
            {"name": "Liposonix", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Body Up", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Vela Slim", "cash": "Consultar", "list": "", "time": "--", "best": False}
        ]}
    ]},
    {"tab": "nutricion", "title": "Nutrición", "categories": [
        {"name": "Nutrición con Profesional", "items": [
            {"name": "Nutrición Clínica", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Salud Digestiva", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Educación Alimentaria", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Planes de Alimentación Personalizados", "cash": "Consultar", "list": "", "time": "--", "best": False},
            {"name": "Acompañamiento Profesional y Personalizado", "cash": "Consultar", "list": "", "time": "--", "best": True}
        ]}
    ]},
    {"tab": "gift-cards", "title": "Gift Cards", "categories": [
        {"name": "Brakko Relax 🥉", "items": [
            {"name": "Masaje Relajante + Reiki", "cash": "55.000", "list": "Consultar", "time": "--", "best": False},
            {"name": "Masaje Piedras Calientes + Masajes Podales", "cash": "55.000", "list": "Consultar", "time": "--", "best": False},
            {"name": "Manicuría + Pedicuría + Perfilado de Cejas", "cash": "60.000", "list": "Consultar", "time": "--", "best": False}
        ]},
        {"name": "Brakko Premium 🥈", "items": [
            {"name": "Masaje Relajante + Reflexología", "cash": "80.000", "list": "Consultar", "time": "--", "best": False},
            {"name": "Masaje Strong + Pedicuría", "cash": "87.000", "list": "Consultar", "time": "--", "best": False}
        ]},
        {"name": "Brakko Experience 🥇", "items": [
            {"name": "Higiene Facial + Reflexología", "cash": "90.000", "list": "Consultar", "time": "--", "best": False},
            {"name": "Higiene Facial Profunda + Reflexología + Perfilado de Cejas", "cash": "106.000", "list": "Consultar", "time": "--", "best": False}
        ]}
    ]},
    {"tab": "actividades", "title": "Nuestras Actividades", "categories": [
        {"name": "Clases", "items": [
            {"name": "Yoga", "cash": "Consultar", "list": "", "time": "Mar y Jue 9hs, 17hs y 18.30hs", "best": False},
            {"name": "Esferodinamia", "cash": "Consultar", "list": "", "time": "Mié y Vie 18.30hs", "best": False},
            {"name": "Tai Chi", "cash": "Consultar", "list": "", "time": "Sáb 10hs", "best": False}
        ]}
    ]}
]

html = """
    <section class="services-section" id="servicios">
        <div class="container">
            <div class="section-title">
                <h2>Nuestros Servicios</h2>
                <div class="divider"></div>
                <p>Descubrí un espacio pensado para tu bienestar y belleza</p>
            </div>

            <div class="menu-container">
                <div class="menu-tabs">
"""

visible_tabs = [tab for tab in data if tab.get("show_tab", True)]
for i, tab in enumerate(visible_tabs):
    active = ' active' if i == 0 else ''
    html += f'                    <button class="menu-tab{active}" data-target="{tab["tab"]}">{tab["title"]}</button>\n'

html += """                </div>
                <div class="menu-content">
"""

for i, tab in enumerate(data):
    active = ' active' if i == 0 else ''
    html += f'                    <div class="menu-category{active}" id="{tab["tab"]}">\n'
    
    for cat in tab["categories"]:
        html += f"""                        <div class="category-header">
                            <h3>{cat["name"]}</h3>
                            <div class="line"></div>
                        </div>
                        <div class="service-grid">
"""
        for item in cat["items"]:
            best = ' best-seller' if item.get("best", False) else ''
            
            cash = f'${item["cash"]}' if item["cash"] != 'Consultar' else 'Consultar'
            list_val = f'${item["list"]}' if item.get("list", "Consultar") != 'Consultar' else 'Consultar'
            list_price = f'{list_val} <span>Lista</span>' if item.get("list", "") != '' else ''
            time_icon = f'<i class="far fa-clock"></i> {item["time"]}' if item.get("time", "--") != '--' else ''
            
            desc_html = f'<div class="service-desc">{item["desc"]}</div>' if item.get("desc") else ''
            
            html += f"""                            <div class="service-card{best}">
                                <div class="service-name">{item["name"]}</div>
                                {desc_html}
                                <div class="service-details-row">
                                    <div class="service-duration">{time_icon}</div>
                                    <div class="service-prices">
                                        <div class="price-cash">{cash} <span>{ "Efectivo" if cash != "Consultar" else ""}</span></div>
                                        {f'<div class="price-list">{list_price}</div>' if list_price else ''}
                                    </div>
                                </div>
                            </div>
"""
        html += "                        </div><br>\n"
    html += "                    </div>\n"

html += """                </div>
            </div>
        </div>
    </section>
"""

with open("services_html.txt", "w", encoding="utf-8") as f:
    f.write(html)
print("Done")
