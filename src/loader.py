import cv2
import os

class ImageLoader:
    """Responsável por carregar e pré-processar as imagens."""
    
    def load_image(self, path):
        """Carrega uma imagem do disco."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Imagem não encontrada: {path}")
        
        image = cv2.imread(path)
        if image is None:
            raise ValueError("Falha ao ler o arquivo de imagem.")
        return image

    def to_grayscale(self, image):
        """Converte imagem para tons de cinza (necessário para Haar Cascade)."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)