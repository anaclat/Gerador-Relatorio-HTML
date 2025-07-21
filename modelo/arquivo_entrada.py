from modelo.cabecalho import Cabecalho
from modelo.produto import Produto

class ArquivoEntrada:

    def __init__(self):
        self.cabecalho = None
        self.produtos = []


    @staticmethod
    def ler_arquivo_entrada():
        try:
            with open('/workspaces/gerador-relatorio-produtos/relatorio-html-produtos/arquivo-entrada-produtos.csv', 'r') as arquivo_entrada:
                linhas = arquivo_entrada.readlines()
                return linhas
        except FileNotFoundError:
            print("Erro: O arquivo 'arquivo-entrada-produtos.csv' não foi encontrado.")
            return []
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return []
        finally:
            arquivo_entrada.close()
    
    def preencher_objeto_arquivo_entrada(Self,linhas):
        linhas_do_arquivo = Self.ler_arquivo_entrada()
        if not linhas_do_arquivo:
            return None
        arquivo_entrada = ArquivoEntrada()
        
        for linha in linhas:
            linhas_separadas = linha.strip().split(';')

            if linhas_separadas[0] == 'H':
                cabecalho = Cabecalho()
                cabecalho.preencher_cabecalho(linhas_separadas)
                cabecalho.titulo = linhas_separadas[1]
                arquivo_entrada.cabecalho.data = linhas_separadas[2]
                Self.cabecalho = cabecalho

            elif linhas_separadas[0] == 'P':
                produto = Produto()
                produto.preencher_produto(linhas_separadas)
                Self.produtos.append(produto)

        return produto