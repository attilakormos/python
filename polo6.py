def create_final_gym_svg():
    filename = "gym_final_design.svg"
    
    # --- SZÍNPALETTA (VS Code Dark Theme) ---
    bg_color = "#1E1E1E"       # Sötétszürke háttér
    
    # Kód színek
    keyword = "#C586C0"        # def, while, if (Lila)
    func_def = "#DCDCAA"       # függvény definiálás (Sárgás)
    func_call = "#DCDCAA"      # függvény hívás (Sárgás)
    variable = "#9CDCFE"       # változók (Kék)
    white = "#D4D4D4"          # Általános szöveg
    
    # Terminal / Debug színek
    term_green = "#E0E091"    # Mátrix zöld
    
    # --- SVG TARTALOM ---
    # Megjegyzés: Megnöveltem kicsit a magasságot, hogy kiférjen a több sor
    svg_content = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="2200" height="2600" viewBox="0 0 550 650" xmlns="http://www.w3.org/2000/svg">
    
    
    
    <text x="30" y="50" font-family="Consolas, monospace" font-size="18" fill="#6A9955" opacity="0.7">edzes_ma.py</text>
    <line x1="30" y1="60" x2="520" y2="60" stroke="#6A9955" stroke-width="1" opacity="0.3" />

    <g font-family="Consolas, 'Courier New', monospace" font-size="24" xml:space="preserve">
        
        <text x="40" y="100">
            <tspan fill="{keyword}" font-weight="bold">def</tspan> <tspan fill="{func_def}">edzes_program</tspan><tspan fill="{white}">():</tspan>
        </text>
        
        <text x="80" y="140">
            <tspan fill="{keyword}" font-weight="bold">while</tspan> <tspan fill="{variable}">True</tspan><tspan fill="{white}">:</tspan>
        </text>

        <text x="120" y="180">
            <tspan fill="{func_call}">elliptikus</tspan><tspan fill="{white}">()</tspan>
        </text>

        <text x="120" y="220">
            <tspan fill="{func_call}">guggolas</tspan><tspan fill="{white}">()</tspan>
        </text>

        <text x="120" y="260">
            <tspan fill="{func_call}">combfeszito</tspan><tspan fill="{white}">()</tspan>
        </text>

        <text x="120" y="300">
            <tspan fill="{func_call}">felsotest</tspan><tspan fill="{white}">()</tspan>
        </text>

        <text x="120" y="340">
            <tspan fill="{keyword}" font-weight="bold">if</tspan> <tspan fill="{variable}">fajdalom</tspan><tspan fill="{white}">:</tspan>
        </text>

        <text x="160" y="380">
            <tspan fill="{func_call}">edz_kemenyebben</tspan><tspan fill="{white}">()</tspan>
        </text>
    </g>

    <line x1="50" y1="440" x2="500" y2="440" stroke="{white}" stroke-width="2" stroke-dasharray="10,5" opacity="0.5" />

    <g font-family="Consolas, 'Courier New', monospace">
        
        <text x="275" y="480" font-size="20" fill="{white}" text-anchor="middle" letter-spacing="2">
            > SZKRIPT FUTTATÁSA...
        </text>
        
        <text x="275" y="530" font-size="32" font-weight="bold" fill="{term_green}" text-anchor="middle">
            EDZETTSÉGI ÁLLAPOT
        </text>

        <rect x="75" y="550" width="400" height="40" 
              fill="none" stroke="{term_green}" stroke-width="3" />
              
        <rect x="80" y="555" width="310" height="30" 
              fill="{term_green}" stroke="none" />
              
        <text x="430" y="575" font-size="20" fill="{term_green}" text-anchor="middle">78%</text>

    </g>

</svg>'''

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"Kész! A végleges fájl elmentve: {filename}")
    except Exception as e:
        print(f"Hiba: {e}")

if __name__ == "__main__":
    create_final_gym_svg()