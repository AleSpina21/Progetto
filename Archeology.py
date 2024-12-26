import numpy as np
from PIL import Image
import cv2
from skimage.feature import local_binary_pattern
import streamlit as st


def load_image_gray(image_path):
    image = Image.open(image_path).convert('L')  # Apre l'immagine e la converte in scala di grigi
    return np.array(image)  # Converte l'immagine in un array numpy (rappresentazione d'immagine tramite matrice di numeri)


# Carica l'immagine e converte in array numpy (ora è possibile lavorarci)
def load_image(image_path):
    image = Image.open(image_path)
    return np.array(image)

# 1. Edge Detection (Rilevamento dei Bordi) - Canny Edge Detector
# Converte in scala di gridio l'immagin (ottimo per lavorarci con Canny)
# Applico il metodo di Canny
##### ATTENZIONE sto usando 2 diverse tecniche per convertire l'immagine in spettro di grigio, perché se ne uso uno uguale per tutti mi dà errori strani. Siccome è un dettaglio piccolissimo e insignificante, ho deciso di ignorare il problema.
def edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) 
    edges = cv2.Canny(gray, 100, 200)  
    return edges

# 2. NDVI (Indice di Vegetazione) - Rilevamento di anomalie nei canali verdi
# La formula per l'indice è (scala_verde - scala_rosso) / (scala_verde + scala_rosso)
# Formalizza le scale e scrivo la formula
def compute_ndvi(image):
    red = image[:, :, 0].astype(float)  
    green = image[:, :, 1].astype(float) 
    ndvi = (green - red) / (green + red + 1e-10)  # Evitiamo la divisione per zero
    return ndvi

# 3. Texture Analysis (LBP - Local Binary Patterns)
# La texture è molto complessa, in parole semplici evidenzia anomalie nella texture dei pixel e a queste anomalie viene associato un numero di 8 cifre binarie, in base a questo viene associato un puntino in vicinanza o meno. Dunque anomalie vengono rilevate in base a vicinanza di punti.
# Si lavora su scala di grigi
def texture_analysis(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) 
    radius = 1  
    n_points = 8 * radius  # evidenzio il fatto che in un quadrato 3x3, i punti vicini al pixel centrale di raggio 1 sono 8.
    lbp = local_binary_pattern(gray, n_points, radius, method="uniform")  # Calcoliamo LBP, c'è la funzione direttamente 
    return lbp

# Funzione per visualizzare i risultati
def visualize_results(image, edges=None, ndvi=None, lbp=None):  # non so perché ma se non metto quel image l'immagine mi esce 2 volte, non riesco a trovare un motivo
    # Mostriamo solo le immagini risultanti
    if edges is not None:
        st.image(edges, caption="Edge Detection (Canny)", use_container_width=True, clamp=True)
    
    if ndvi is not None:
        st.image(ndvi, caption="NDVI", use_container_width=True, clamp=True, channels="RGB")
    
    if lbp is not None:
        st.image(lbp, caption="Texture Analysis (LBP)", use_container_width=True, clamp=True)


