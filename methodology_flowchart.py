import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(12, 16))
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)
ax.axis('off')

# Define colors
colors = {
    'header': '#1f4e79',
    'data': '#9dc3e6', 
    'preprocess': '#f4b183',
    'ml': '#a9d18e',
    'eval': '#ffd966',
    'xai': '#b4a7d6',
    'result': '#c5504b'
}

# Helper function to create boxes
def create_box(ax, x, y, width, height, text, color, text_size=10):
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.1",
                         facecolor=color, edgecolor='black', linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, 
            ha='center', va='center', fontsize=text_size, 
            weight='bold', wrap=True)

# Helper function to create arrows
def create_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))

# Title
create_box(ax, 1, 18, 8, 1.5, 'METODOLOGI PENELITIAN\nPerbandingan ML + XAI untuk Kanker Payudara', 
           colors['header'], 12)

# 1. Data Source
create_box(ax, 2, 16, 6, 1.2, 'SUMBER DATA\nWisconsin Breast Cancer Dataset\n569 samples × 30 features', 
           colors['data'])

# 2. Preprocessing
create_box(ax, 1, 13.5, 8, 2, 'PREPROCESSING\n\nData Exploration → Label Encoding → Feature Standardization\n(M→1, B→0)          (StandardScaler)', 
           colors['preprocess'])

# 3. Data Splitting
create_box(ax, 2, 11, 6, 1.2, 'DATA SPLITTING\nTrain-Test Split (80:20)\nStratified Sampling', 
           colors['data'])

# 4. Model Training
create_box(ax, 0.5, 8.5, 2.5, 1.8, 'Random Forest\nClassifier', colors['ml'])
create_box(ax, 3.75, 8.5, 2.5, 1.8, 'Support Vector\nMachine', colors['ml'])
create_box(ax, 7, 8.5, 2.5, 1.8, 'XGBoost\nClassifier', colors['ml'])

# 5. Model Evaluation
create_box(ax, 1, 6, 8, 1.5, 'MODEL EVALUATION\nPerformance Metrics | Cross Validation | Overfitting Detection', 
           colors['eval'])

# 6. Explainable AI
create_box(ax, 0.5, 3, 4, 2.5, 'SHAP\n\nGlobal Explanation\nTreeExplainer\nFeature Importance\nSummary Plot', 
           colors['xai'])
create_box(ax, 5.5, 3, 4, 2.5, 'LIME\n\nLocal Explanation\nTabularExplainer\nInstance-specific\nTop-10 Features', 
           colors['xai'])

# 7. Comparative Analysis
create_box(ax, 1, 0.5, 8, 1.5, 'COMPARATIVE ANALYSIS\nModel Performance | SHAP vs LIME | Clinical Interpretation', 
           colors['result'])

# Add arrows
create_arrow(ax, 5, 17.5, 5, 16.5)  # Title to Data
create_arrow(ax, 5, 15.5, 5, 14.8)  # Data to Preprocessing
create_arrow(ax, 5, 13, 5, 12.5)    # Preprocessing to Split
create_arrow(ax, 5, 10.5, 5, 10)    # Split to Models

# From split to each model
create_arrow(ax, 4, 10.5, 1.75, 10)   # To RF
create_arrow(ax, 5, 10.5, 5, 10)      # To SVM  
create_arrow(ax, 6, 10.5, 8.25, 10)   # To XGB

# From models to evaluation
create_arrow(ax, 1.75, 8.5, 3, 7.8)   # RF to eval
create_arrow(ax, 5, 8.5, 5, 7.8)      # SVM to eval
create_arrow(ax, 8.25, 8.5, 7, 7.8)   # XGB to eval

# From evaluation to XAI
create_arrow(ax, 3.5, 6, 2.5, 5.8)    # To SHAP
create_arrow(ax, 6.5, 6, 7.5, 5.8)    # To LIME

# From XAI to final
create_arrow(ax, 2.5, 3, 3.5, 2.3)    # SHAP to final
create_arrow(ax, 7.5, 3, 6.5, 2.3)    # LIME to final

plt.title('Flowchart Metodologi Penelitian', fontsize=16, weight='bold', pad=20)
plt.tight_layout()
plt.savefig('methodology_flowchart.png', dpi=300, bbox_inches='tight')
plt.show()