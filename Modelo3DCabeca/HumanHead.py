import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Matriz 12x6 "Planar Head" (Anatomia Ultra-Refinada)
# Formato: [Profundidade (X), Largura (Y), Altura (Z)]

# Topo e Testa (Mais arredondada nas têmporas)
row0  = [[ 0.20, 0.00,  1.30], [ 0.15, 0.20,  1.28], [ 0.05, 0.40,  1.20], [-0.10, 0.55,  1.10], [-0.30, 0.65,  1.00], [-0.50, 0.65,  0.90]]
row1  = [[ 0.45, 0.00,  1.00], [ 0.40, 0.22,  0.98], [ 0.30, 0.45,  0.95], [ 0.05, 0.65,  0.88], [-0.25, 0.75,  0.80], [-0.50, 0.75,  0.75]]

# Linha da Sobrancelha (Glabela definida no centro, arco forte)
row2  = [[ 0.70, 0.00,  0.65], [ 0.65, 0.22,  0.63], [ 0.55, 0.45,  0.60], [ 0.20, 0.70,  0.58], [-0.25, 0.80,  0.55], [-0.50, 0.80,  0.55]] 

# Órbitas Oculares (Cantos internos mais fundos para realçar o nariz)
row3  = [[ 0.55, 0.00,  0.45], [ 0.40, 0.18,  0.45], [ 0.42, 0.42,  0.45], [ 0.15, 0.70,  0.45], [-0.20, 0.80,  0.45], [-0.50, 0.80,  0.45]] 

# Ponte Nasal e Maçãs do Rosto Superiores (Zigomático bem vincado)
row4  = [[ 0.78, 0.00,  0.25], [ 0.55, 0.18,  0.22], [ 0.62, 0.48,  0.20], [ 0.30, 0.75,  0.15], [-0.15, 0.82,  0.10], [-0.50, 0.82,  0.05]] 

# Ponta do Nariz e Bochechas Inferiores
row5  = [[ 0.92, 0.00, -0.05], [ 0.60, 0.22, -0.10], [ 0.58, 0.50, -0.15], [ 0.25, 0.75, -0.20], [-0.15, 0.82, -0.20], [-0.50, 0.82, -0.20]] 

# Lábio Superior (Começa a curva do cilindro dental)
row6  = [[ 0.75, 0.00, -0.25], [ 0.65, 0.18, -0.25], [ 0.52, 0.45, -0.30], [ 0.20, 0.70, -0.35], [-0.15, 0.78, -0.35], [-0.50, 0.78, -0.35]] 

# Linha da Boca (Recuada em relação aos lábios para criar sombra)
row7  = [[ 0.72, 0.00, -0.35], [ 0.60, 0.18, -0.35], [ 0.48, 0.42, -0.40], [ 0.18, 0.65, -0.45], [-0.15, 0.75, -0.45], [-0.50, 0.75, -0.45]] 

# Lábio Inferior (Projeta-se ligeiramente para fora)
row8  = [[ 0.76, 0.00, -0.45], [ 0.65, 0.18, -0.45], [ 0.48, 0.40, -0.50], [ 0.15, 0.60, -0.55], [-0.15, 0.70, -0.55], [-0.50, 0.70, -0.55]] 

# Queixo e Linha do Maxilar (Queixo quadrado, maxilar forte)
row9  = [[ 0.85, 0.00, -0.65], [ 0.75, 0.18, -0.62], [ 0.60, 0.40, -0.60], [ 0.12, 0.55, -0.60], [-0.15, 0.65, -0.60], [-0.50, 0.65, -0.60]] 

# Base do Maxilar / Papada
row10 = [[ 0.55, 0.00, -0.80], [ 0.48, 0.18, -0.80], [ 0.30, 0.38, -0.80], [ 0.05, 0.50, -0.80], [-0.20, 0.55, -0.80], [-0.50, 0.55, -0.80]] 

# Pescoço (Cilíndrico)
row11 = [[ 0.40, 0.00, -1.10], [ 0.35, 0.18, -1.10], [ 0.25, 0.35, -1.10], [ 0.00, 0.45, -1.10], [-0.25, 0.50, -1.10], [-0.50, 0.50, -1.10]] 

half_mesh_base = np.array([row0, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11])

def get_expression_mesh(expression):
    mesh = np.copy(half_mesh_base)
    
    if expression == "Fear (Medo)":
        mesh[2, 0:3, 2] += 0.06
        mesh[2, 0:2, 1] -= 0.03
        mesh[3, 1:3, 2] -= 0.02
        mesh[7, 0:3, 2] -= 0.05
        mesh[8, 0:3, 2] -= 0.08
        mesh[6:9, 2:4, 1] += 0.04
        mesh[6:9, 1:4, 0] -= 0.03 
        
    elif expression == "Disgust (Nojo)":
        mesh[4, 0:2, 2] += 0.04
        mesh[5, 0:2, 2] += 0.05
        mesh[6, 0:3, 2] += 0.05
        mesh[6, 0:3, 0] += 0.03
        mesh[2, 0:3, 2] -= 0.04
        
    elif expression == "Anger (Raiva)":
        mesh[2, 0:3, 2] -= 0.06
        mesh[2, 0:3, 0] += 0.04
        mesh[2, 0:2, 1] -= 0.03
        mesh[6, 0:3, 2] -= 0.02
        mesh[8, 0:3, 2] += 0.03
        mesh[5, 1, 1] += 0.03
        
    elif expression == "Sadness (Tristeza)":
        mesh[2, 0:2, 2] += 0.05
        mesh[2, 2:4, 2] -= 0.03
        mesh[6, 2:4, 2] -= 0.05
        mesh[7, 2:4, 2] -= 0.05
        mesh[8, 2:4, 2] -= 0.05
        
    elif expression == "Happiness (Alegria)":
        mesh[6, 2:4, 2] += 0.06
        mesh[7, 2:4, 2] += 0.07
        mesh[8, 2:4, 2] += 0.06
        mesh[6:9, 2:4, 0] -= 0.04
        mesh[6:9, 2:4, 1] += 0.04
        mesh[4, 1:4, 2] += 0.03
        mesh[4, 1:4, 0] += 0.03
        mesh[3, 2:4, 2] += 0.02
        
    elif expression == "Surprise (Surpresa)":
        mesh[2, 0:4, 2] += 0.08
        mesh[3, 1:3, 0] -= 0.03
        mesh[7, 0:3, 2] -= 0.06
        mesh[8, 0:4, 2] -= 0.12
        mesh[9, 0:4, 2] -= 0.12
        mesh[10, 0:4, 2] -= 0.10

    # Retorna a malha base *sem* subdivisão
    return mesh

def build_lowpoly_geometry(mesh):
    """Gera vértices e faces a partir da grade da malha, espelhando-a."""
    rows, cols, dims = mesh.shape
    
    full_vertices = []
    
    # Criar grade de vértices completa (espelhada)
    for i in range(rows):
        # Lado esquerdo (espelhado)
        for j in range(cols - 1, 0, -1):
            full_vertices.append([mesh[i, j, 0], -mesh[i, j, 1], mesh[i, j, 2]])
        # Centro e Lado Direito
        for j in range(cols):
            full_vertices.append([mesh[i, j, 0], mesh[i, j, 1], mesh[i, j, 2]])
    
    full_vertices = np.array(full_vertices)
    num_cols_full = cols + (cols - 1)
    
    # Gerar faces quadriláteras
    full_faces = []
    for i in range(rows - 1):
        for j in range(num_cols_full - 1):
            v0 = i * num_cols_full + j
            v1 = i * num_cols_full + (j + 1)
            v2 = (i + 1) * num_cols_full + (j + 1)
            v3 = (i + 1) * num_cols_full + j
            
            # Coordenadas dos 4 vértices da face
            face_coords = full_vertices[[v0, v1, v2, v3]]
            full_faces.append(face_coords)
            
    return full_faces

# --- Setup da Figura ---
fig = plt.figure(figsize=(14, 8))
fig.subplots_adjust(left=0.25)
fig.patch.set_facecolor('#2b2b2b') # Fundo escuro

# Subplots para duas visualizações lado a lado (como na referência)
ax_front = fig.add_subplot(121, projection='3d')
ax_profile = fig.add_subplot(122, projection='3d')

# Estética de ambos os subplots
for ax in [ax_front, ax_profile]:
    ax.set_facecolor('#2b2b2b')
    ax.tick_params(colors='white')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.set_axis_off()

# Definir ângulos de câmera fixos para as duas visualizações
ax_front.view_init(elev=10, azim=-40) # Visualização 3/4
ax_profile.view_init(elev=0, azim=-90)  # Visualização de perfil puro

face_collection_front = None
face_collection_profile = None

def update_plot(label):
    global face_collection_front, face_collection_profile
    
    # Obter a malha para a expressão (sem subdivisão)
    mesh = get_expression_mesh(label)
    # Gerar a geometria das faces
    faces = build_lowpoly_geometry(mesh)
    
    # Limpar as coleções anteriores
    if face_collection_front: face_collection_front.remove()
    if face_collection_profile: face_collection_profile.remove()
    
    # Criar novas coleções de faces 3D (aqui define o estilo "low poly")
    # facecolors='lightgrey', edgecolors='black' (wireframe)
    face_collection_front = Poly3DCollection(faces, facecolors='lightgrey', edgecolors='black', linewidths=0.5, antialiased=False)
    face_collection_profile = Poly3DCollection(faces, facecolors='lightgrey', edgecolors='black', linewidths=0.5, antialiased=False)
    
    # Adicionar as coleções aos subplots
    ax_front.add_collection3d(face_collection_front)
    ax_profile.add_collection3d(face_collection_profile)
    
    # Definir limites e proporção para garantir uma escala consistente
    for ax in [ax_front, ax_profile]:
        ax.set_box_aspect([1, 1, 1.2])
        ax.set_xlim(-1, 1.5)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-1.2, 1.5)
    
    fig.canvas.draw_idle()

# Menu Interativo (Radio Buttons)
rax = plt.axes([0.05, 0.35, 0.18, 0.35], facecolor='#444444')
options = ('Neutral', 'Fear (Medo)', 'Disgust (Nojo)', 'Anger (Raiva)', 
           'Sadness (Tristeza)', 'Happiness (Alegria)', 'Surprise (Surpresa)')
radio = RadioButtons(rax, options, activecolor='cyan')

# Mudar cor do texto do menu
for label in radio.labels:
    label.set_color('white')

radio.on_clicked(update_plot)

# Plotar o inicial
update_plot('Neutral')

plt.show()