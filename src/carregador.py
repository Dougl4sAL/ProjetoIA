import cv2
import os

class CarregadorImagem:
    """Responsável por carregar e pré-processar as imagens."""
    
    def carregar_imagem(self, caminho):
        """Carrega uma imagem do disco."""
        if not os.path.exists(caminho):
            raise FileNotFoundError(f"Imagem não encontrada: {caminho}")
        
        imagem = cv2.imread(caminho)
        if imagem is None:
            raise ValueError("Falha ao ler o arquivo de imagem.")
        return imagem

    def para_escala_cinza(self, imagem):
        """Converte imagem para tons de cinza para o Haar Cascade."""
        return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)