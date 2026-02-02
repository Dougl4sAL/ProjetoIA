from src.loader import ImageLoader
from src.detector import CarDetector
from src.visualizer import Visualizer

def main():
    # Caminhos (ajuste conforme seu computador)
    XML_PATH = 'data/cars.xml'
    IMAGE_PATH = 'data/test_image.jpg'

    try:
        # 1. Instanciar objetos
        loader = ImageLoader()
        detector = CarDetector(XML_PATH)
        vis = Visualizer()

        # 2. Carregar e Processar
        print("Carregando imagem...")
        original_img = loader.load_image(IMAGE_PATH)
        gray_img = loader.to_grayscale(original_img)

        # 3. Detectar (Inteligência)
        print("Detectando carros...")
        results = detector.detect(gray_img)
        print(f"{len(results)} carros detectados.")

        # 4. Visualizar
        final_img = vis.draw_detections(original_img, results)
        vis.show_results(final_img)

    except Exception as e:
        print(f"Erro crítico: {e}")

if __name__ == "__main__":
    main()