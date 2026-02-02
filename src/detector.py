import cv2

class CarDetector:
    """Encapsula a lógica de detecção de veículos usando Haar Cascades."""
    
    def __init__(self, cascade_path):
        self.cascade_path = cascade_path
        self.classifier = self._load_classifier()

    def _load_classifier(self):
        """Carrega o classificador XML (Modelo pré-treinado)."""
        classifier = cv2.CascadeClassifier(self.cascade_path)
        if classifier.empty():
            raise IOError(f"Não foi possível carregar o classificador XML em: {self.cascade_path}")
        return classifier

    def detect(self, gray_image, scale_factor=1.1, min_neighbors=3):
        """
        Realiza a detecção.
        :param gray_image: Imagem em escala de cinza.
        :return: Lista de retângulos [(x, y, w, h), ...] onde carros foram vistos.
        """
        # detectMultiScale é o método que 'varre' a imagem buscando padrões
        cars = self.classifier.detectMultiScale(
            gray_image,
            scaleFactor=scale_factor,
            minNeighbors=min_neighbors
        )
        return cars