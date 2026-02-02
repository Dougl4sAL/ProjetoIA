import cv2

class Visualizador:
    """Responsável por desenhar os resultados na imagem."""

    def desenhar_deteccoes(self, imagem, deteccoes):
        """Desenha retângulos ao redor dos carros detectados."""
        imagem_saida = imagem.copy()
        for (x, y, l, a) in deteccoes:
            # Desenha retângulo azul (255, 0, 0) com espessura 2
            cv2.rectangle(imagem_saida, (x, y), (x + l, y + a), (255, 0, 0), 2)
        return imagem_saida

    def mostrar_resultados(self, imagem, nome_janela="Detecção de Carros"):
        """Mostra a imagem em uma janela."""
        cv2.imshow(nome_janela, imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()