import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import io
import base64

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN

# 1. Gerar Dados
t = np.linspace(0, 10, 400)
y1 = np.sin(t)
y2 = np.cos(t)
df = pd.DataFrame({'0': y1, '1': y2})
df['t'] = t
corr_matrix = df[['0', '1']].corr()

# --- A. SEABORN (Converter para Imagem Base64) ---
plt.figure(figsize=(5, 4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".3f")
plt.title("Seaborn Heatmap")
plt.tight_layout()

buf = io.BytesIO()
plt.savefig(buf, format='png')
plt.close()
sns_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

# --- B. PLOTLY (Converter para Div HTML) ---
fig_plotly = px.line(df, x='t', y=['0', '1'], title="Plotly Interativo",
                     color_discrete_map={'0': 'blue', '1': 'red'})
plotly_div = fig_plotly.to_html(full_html=False, include_plotlyjs='cdn')

# --- C. BOKEH (Obter Componentes JS/Div) ---
p_bokeh = figure(title="Bokeh Interativo", x_axis_label='t', y_axis_label='Amplitude', 
                 width=800, height=400)
p_bokeh.line(t, y1, legend_label="0 (sin)", color="blue", line_width=2)
p_bokeh.line(t, y2, legend_label="1 (cos)", color="red", line_width=2)
script_bokeh, div_bokeh = components(p_bokeh)

# --- D. GERAR HTML FINAL ---
html_template = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Relatório de Sinais e Correlação</title>
    {CDN.render_js()}
    <style>
        body {{ font-family: sans-serif; margin: 40px; background-color: #f4f4f9; }}
        .container {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; }}
        .plot-section {{ margin-bottom: 50px; border-bottom: 1px solid #eee; padding-bottom: 20px; }}
        img {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Análise de Sinais: Seno e Cosseno</h1>
        
        <div class="plot-section">
            <h2>1. Matriz de Correlação (Seaborn)</h2>
            <p>Correlação calculada: 0.052 (Intervalo [0, 10])</p>
            <img src="data:image/png;base64,{sns_base64}" />
        </div>

        <div class="plot-section">
            <h2>2. Visualização com Plotly</h2>
            {plotly_div}
        </div>

        <div class="plot-section">
            <h2>3. Visualização com Bokeh</h2>
            {script_bokeh}
            {div_bokeh}
        </div>
    </div>
</body>
</html>
"""

# Guardar o ficheiro
with open("relatorio_final.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Sucesso! O ficheiro 'relatorio_final.html' foi gerado com todos os gráficos.")