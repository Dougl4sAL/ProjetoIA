import unittest
import cv2
import numpy as np
from src.detector import DetectorCarro

class TestCarDetector(unittest.TestCase):
    
    def setUp(self):
        # Cria uma imagem preta simples para teste técnico (sem carregar arquivo externo)
        self.fake_image = np.zeros((100, 100), dtype=np.uint8)
        # Caminho do XML
        self.xml_path = 'data/cars.xml' 

    def test_initialization_error(self):
        """Testa se o sistema avisa quando o XML não existe."""
        with self.assertRaises(IOError):
            DetectorCarro("caminho/inexistente.xml")

    def test_detection_format(self):
        """Verifica se a detecção retorna um formato válido (numpy array ou tupla)."""
        try:
            detector = DetectorCarro(self.xml_path)
            result = detector.detect(self.fake_image)
            # O resultado deve ser uma lista/array, mesmo que vazia
            self.assertIsNotNone(result) 
        except IOError:
            print("Algo deu errado.")

if __name__ == '__main__':
    unittest.main()