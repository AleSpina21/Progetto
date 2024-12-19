import numpy as np
from PIL import Image

def load_image_with_pillow(image_path):
    image = Image.open(image_path).convert('L')  # Apre l'immagine e la converte in scala di grigi
    image = image.resize((500, 500))  # Ridimensiona
    return np.array(image)  # Converte l'immagine in un array numpy (rappresentazione d'immagine tramite matrice di numeri)




