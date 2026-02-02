import cv2

class DetectorCarro:
    """Encapsula a lógica de detecção de veículos usando Haar Cascades."""
    
    def __init__(self, caminho_cascata):
        self.caminho_cascata = caminho_cascata
        self.classificador = self._carregar_classificador()

    def _carregar_classificador(self):
        """Carrega o classificador XML (Modelo pré-treinado)."""
        classificador = cv2.CascadeClassifier(self.caminho_cascata)
        if classificador.empty():
            raise IOError(f"Não foi possível carregar o classificador XML em: {self.caminho_cascata}")
        return classificador

    def detectar(self, imagem_cinza, fator_escala=1.1, min_vizinhos=3):
        """Realiza a detecção e retorna a lista de retângulos."""
        carros = self.classificador.detectMultiScale(
            imagem_cinza,
            scaleFactor=fator_escala,
            minNeighbors=min_vizinhos
        )
        return carros