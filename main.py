from src.carregador import CarregadorImagem
from src.detector import DetectorCarro
from src.visualizador import Visualizador

def main():
    CAMINHO_XML = 'data/cars.xml'
    ARQUIVOS_IMAGEM = ['imagem1.jpg', 'imagem2.jpg', 'imagem3.jpg']

    try:
        carregador = CarregadorImagem()
        detector = DetectorCarro(CAMINHO_XML)
        visualizador = Visualizador()
        
        print(f"Iniciando processamento de {len(ARQUIVOS_IMAGEM)} imagens...\n")

        for i, nome_imagem in enumerate(ARQUIVOS_IMAGEM, 1):
            caminho_imagem = f'data/{nome_imagem}'
            print(f"--- [{i}/{len(ARQUIVOS_IMAGEM)}] Processando: {nome_imagem} ---")

            try:
                imagem_original = carregador.carregar_imagem(caminho_imagem)
                imagem_cinza = carregador.para_escala_cinza(imagem_original)

                resultados = detector.detectar(imagem_cinza)
                print(f">> {len(resultados)} carros detectados.")

                imagem_final = visualizador.desenhar_deteccoes(imagem_original, resultados)
                
                print("Pressione QUALQUER TECLA para ir para a próxima imagem...")
                visualizador.mostrar_resultados(imagem_final)

            except FileNotFoundError:
                print(f"ERRO: A imagem '{nome_imagem}' não foi encontrada.")
            except Exception as e:
                print(f"ERRO ao processar '{nome_imagem}': {e}")
            
            print("=" * 40)

    except Exception as e:
        print(f"Erro crítico: {e}")

if __name__ == "__main__":
    main()