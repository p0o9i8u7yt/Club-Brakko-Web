import re

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Read the generated services HTML
with open('services_html.txt', 'r', encoding='utf-8') as f:
    services_html = f.read()

# Replace the services section
html_pattern = re.compile(r'    <section class="services-section" id="servicios">.*?</section>', re.DOTALL)
new_html = html_pattern.sub(services_html, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Now for CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css_styles = """/* --- Services Menu --- */
.services-section {
    padding: 100px 0;
    background-color: #fff;
}

.menu-container {
    max-width: 1000px;
    margin: 0 auto;
    background: #fff;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    overflow: hidden;
}

.menu-tabs {
    display: flex;
    overflow-x: auto;
    background: var(--primary-color);
    padding: 15px 20px;
    gap: 10px;
    scrollbar-width: none;
}
.menu-tabs::-webkit-scrollbar {
    display: none;
}
.menu-tab {
    padding: 10px 20px;
    background: transparent;
    color: var(--text-light);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 30px;
    cursor: pointer;
    white-space: nowrap;
    transition: all var(--transition-speed);
    font-family: var(--font-body);
    font-size: 0.9rem;
    font-weight: 500;
}
.menu-tab.active, .menu-tab:hover {
    background: var(--accent-color);
    border-color: var(--accent-color);
    color: #fff;
}

.menu-content {
    padding: 40px;
}

.menu-category {
    display: none;
    animation: fadeIn 0.5s ease-in-out;
}

.menu-category.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.category-header {
    margin-bottom: 30px;
    display: flex;
    align-items: center;
    gap: 15px;
}
.category-header h3 {
    font-size: 1.8rem;
    color: var(--primary-color);
}
.category-header .line {
    flex-grow: 1;
    height: 1px;
    background: #eee;
}

.service-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.service-card {
    padding: 20px;
    border: 1px solid #eee;
    border-radius: 12px;
    background: #fafafa;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.service-card:hover {
    border-color: var(--accent-color);
    box-shadow: 0 10px 20px rgba(0,0,0,0.03);
    transform: translateY(-2px);
}

.service-card.best-seller::before {
    content: '★ Destacado';
    position: absolute;
    top: 15px;
    right: -30px;
    background: var(--accent-color);
    color: #fff;
    font-size: 0.7rem;
    padding: 4px 30px;
    transform: rotate(45deg);
    font-weight: bold;
    letter-spacing: 1px;
}

.service-name {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--primary-color);
    margin-bottom: 5px;
    padding-right: 20px;
}

.service-details-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 15px;
    padding-top: 15px;
    border-top: 1px dashed #ddd;
}

.service-duration {
    font-size: 0.9rem;
    color: #666;
    display: flex;
    align-items: center;
    gap: 5px;
}

.service-prices {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}

.price-cash {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--primary-color);
}
.price-cash span {
    font-size: 0.7rem;
    font-weight: 400;
    color: #888;
    text-transform: uppercase;
}
.price-list {
    font-size: 0.85rem;
    color: #888;
}
.price-list span {
    font-size: 0.7rem;
}"""

css_pattern = re.compile(r'/\* --- Services Section --- \*/.*?/\* --- Appointment Form --- \*/', re.DOTALL)
new_css = css_pattern.sub(new_css_styles + "\n\n/* --- Appointment Form --- */", css)

# Also need to remove the old responsive styles for .service-category
resp_pattern = re.compile(r'\.service-category, \.service-category\.reverse \{[^}]+\}\s*\.service-image img \{[^}]+\}')
new_css = resp_pattern.sub('.service-grid { grid-template-columns: 1fr; }\n    .menu-content { padding: 20px; }', new_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(new_css)
print("Files updated")
