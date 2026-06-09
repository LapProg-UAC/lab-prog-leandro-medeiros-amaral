import csv
from pathlib import Path
import plotly.graph_objects as go
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN

# --- 1. Gráfico Plotly: Pinguins de Palmer  ---
def criar_plotly_pinguins():
    csv_path = Path(__file__).parent / "pinguins_palmer.csv"
    dados_por_especie = {}
    try:
        with csv_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    esp = row["especie"]
                    m, b = float(row["massa"]), float(row["barbatana"])
                    if esp not in dados_por_especie:
                        dados_por_especie[esp] = {"massa": [], "barbatana": []}
                    dados_por_especie[esp]["massa"].append(m)
                    dados_por_especie[esp]["barbatana"].append(b)
                except: continue
    except: return "<p style='color:red;'>Erro: pinguins_palmer.csv não encontrado.</p>"

    fig = go.Figure()
    cores = {'Adelie': 'orange', 'Chinstrap': 'purple', 'Gentoo': 'teal'}
    for esp, dados in dados_por_especie.items():
        fig.add_trace(go.Scatter(
            x=dados["massa"], y=dados["barbatana"], mode='markers', name=esp,
            marker=dict(color=cores.get(esp, 'gray'), size=10, opacity=0.7, line=dict(width=1, color='White'))
        ))
    fig.update_layout(template='plotly_white', height=450, xaxis_title="Massa (g)", yaxis_title="Barbatana (mm)", margin=dict(t=20))
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

# --- 2. Gráfico Bokeh: Evolução do CO2 ---
def criar_bokeh_co2():
    csv_path = Path(__file__).parent / "co2_maunaloa.csv"
    anos, ppm = [], []
    try:
        with csv_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    anos.append(int(row["ano"]))
                    ppm.append(float(row["ppm"]))
                except: continue
    except: return "", "<p style='color:red;'>Erro: co2_maunaloa.csv não encontrado.</p>"

    p = figure(title="Concentração de CO₂ na atmosfera (Mauna Loa)", x_axis_label='Ano', y_axis_label='PPM',
               sizing_mode="stretch_width", height=400, tools="pan,wheel_zoom,box_zoom,reset,save")
    p.varea(x=anos, y1=min(ppm)-5, y2=ppm, fill_alpha=0.3, fill_color="skyblue")
    p.line(anos, ppm, legend_label="CO₂ (ppm)", line_width=3, color="navy")
    p.circle(anos, ppm, size=8, fill_color="white", line_color="navy")
    p.legend.location = "top_left"
    
    return components(p)

# --- 3. Gráfico Plotly: Correlação Mutante (Barbatana vs CO2) ---
def criar_plotly_mutacao():
    csv_path = Path(__file__).parent / "co2_maunaloa.csv"
    dados = {"co2": [], "barbatana": [], "ano": []}
    try:
        with csv_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    ano = int(row["ano"])
                    if ano >= 2010:
                        # Regra: 180mm em 2010 + 14mm por ano
                        b_tamanho = 180 + (14 * (ano - 2010))
                        dados["ano"].append(ano)
                        dados["co2"].append(float(row["ppm"]))
                        dados["barbatana"].append(b_tamanho)
                except: continue
    except: return "<p>Erro nos dados para o gráfico de mutação.</p>"

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dados["co2"], y=dados["barbatana"], mode='lines+markers',
        line=dict(color='crimson', width=3), marker=dict(size=10, color='black'),
        text=[f"Ano: {a}" for a in dados["ano"]],
        hovertemplate="<b>%{text}</b><br>CO2: %{x} ppm<br>Barbatana: %{y} mm<extra></extra>"
    ))
    fig.update_layout(template='plotly_white', height=500, xaxis_title="Concentração de CO2 (PPM)", 
                      yaxis_title="Comprimento da Barbatana Mutante (mm)", margin=dict(t=20))
    return fig.to_html(full_html=False, include_plotlyjs=False)

# --- FUNÇÃO DASHBOARD ---
def gerar_dashboard_completo():
    print("A processar gráficos...")
    plot1 = criar_plotly_pinguins()
    b_script, b_div = criar_bokeh_co2()
    plot3 = criar_plotly_mutacao()
    
    bokeh_res = CDN.render()

    html_template = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Eco-Análise Pinguins 2026</title>
        {CDN.render()}
        <style>
            :root {{
                --bg: #f8fafc;
                --card-bg: #ffffff;
                --text-main: #1e293b;
                --text-muted: #64748b;
                --accent: #3b82f6;
                --danger: #ef4444;
            }}
            
            body {{ 
                font-family: 'Inter', -apple-system, sans-serif; 
                background-color: var(--bg); 
                color: var(--text-main);
                margin: 0; padding: 0;
                line-height: 1.5;
            }}

            header {{
                background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
                color: white;
                padding: 40px 20px;
                text-align: center;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}

            .container {{ 
                max-width: 1100px; 
                margin: -40px auto 40px; 
                padding: 0 20px;
            }}

            .card {{ 
                background: var(--card-bg); 
                border-radius: 16px; 
                padding: 24px; 
                box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
                margin-bottom: 30px;
                transition: transform 0.2s;
            }}

            .card:hover {{ transform: translateY(-4px); }}

            h1 {{ margin: 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.025em; }}
            h2 {{ 
                font-size: 1.25rem; font-weight: 700; margin-top: 0; 
                display: flex; align-items: center; gap: 10px;
            }}
            
            h2::before {{
                content: ''; width: 4px; height: 24px; 
                background: var(--accent); border-radius: 2px;
            }}

            .badge {{
                display: inline-block;
                padding: 4px 12px;
                background: #e0f2fe;
                color: #0369a1;
                border-radius: 9999px;
                font-size: 0.75rem;
                font-weight: 600;
                margin-bottom: 15px;
            }}

            .info-text {{ color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px; }}
            .error {{ color: var(--danger); font-weight: bold; padding: 20px; text-align: center; }}
            
            footer {{ text-align: center; padding: 40px; color: var(--text-muted); font-size: 0.8rem; }}
        </style>
    </head>
    <body>
        <header>
            <h1>Observatório Biométrico & Climático</h1>
            <p>Análise de Correlação: Crescimento de Nadadeiras vs. Emissões de CO₂</p>
        </header>

        <div class="container">
            <div class="card">
                <span class="badge">DADOS BIOMÉTRICOS</span>
                <h2>Distribuição por Espécie (plotly)</h2>
                <p class="info-text">Comparação entre massa corporal e comprimento da barbatana nos dados de Palmer Penguins.</p>
                {plot1}
            </div>

            <div class="card">
                <span class="badge">ATMOSFERA</span>
                <h2>Evolução do CO₂ (bokeh)</h2>
                {b_div}
            </div>

            <div class="card" style="border-top: 4px solid var(--danger);">
                <span class="badge" style="background:#fee2e2; color:#991b1b;">SIMULAÇÃO MUTANTE</span>
                <h2>Relação: Barbatana vs. Nível de CO₂ (plotly)</h2>
                <p class="info-text">Projeção de crescimento biológico (14mm/ano) cruzado com o nível de CO₂ registado desde 2010.</p>
                {plot3}
            </div>
        </div>

        <footer>
            Leandro Medeiros Amaral - 2026 
        </footer>

        {b_script}
    </body>
    </html>
    """
    
    with open("dashboard_final.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("Sucesso! Abre o ficheiro 'dashboard_final.html' no teu navegador.")

if __name__ == "__main__":
    gerar_dashboard_completo()