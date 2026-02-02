from src.loader import ImageLoader
from src.detector import CarDetector
from src.visualizer import Visualizer

def main():
    XML_PATH = 'data/cars.xml'
    
    # Lista de imagens para processar
    IMAGE_FILES = ['test_image1.jpg', 'test_image2.jpg', 'test_image3.jpg']

    try:
        loader = ImageLoader()
        detector = CarDetector(XML_PATH)
        vis = Visualizer()
        
        print(f"Iniciando processamento de {len(IMAGE_FILES)} imagens...\n")

        # 2. Loop para processar cada imagem da lista
        for i, image_name in enumerate(IMAGE_FILES, 1):
            image_path = f'data/{image_name}'
            print(f"--- [{i}/{len(IMAGE_FILES)}] Processando: {image_name} ---")

            try:
                # Carregar e Processar
                original_img = loader.load_image(image_path)
                gray_img = loader.to_grayscale(original_img)

                # Detectar
                results = detector.detect(gray_img)
                print(f">> {len(results)} carros detectados.")

                # Visualizar
                final_img = vis.draw_detections(original_img, results)
                
                print("Visualize a janela e pressione QUALQUER TECLA para ir para a próxima imagem...")
                vis.show_results(final_img) # O código pausa aqui até você apertar uma tecla

            except FileNotFoundError:
                print(f"ERRO: A imagem '{image_name}' não foi encontrada na pasta data/.")
            except Exception as e:
                print(f"ERRO ao processar '{image_name}': {e}")
            
            print("=" * 40)

    except Exception as e:
        print(f"Erro crítico na inicialização do sistema: {e}")

if __name__ == "__main__":
    main()