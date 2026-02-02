import cv2

class Visualizer:
    """Responsável por desenhar os resultados na imagem."""

    def draw_detections(self, image, detections):
        """Desenha retângulos ao redor dos carros detectados."""
        output_img = image.copy()
        for (x, y, w, h) in detections:
            # Desenha retângulo azul (255, 0, 0) com espessura 2
            cv2.rectangle(output_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return output_img

    def show_results(self, image, window_name="Deteccao de Carros"):
        """Mostra a imagem em uma janela."""
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()