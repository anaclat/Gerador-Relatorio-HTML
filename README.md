# 📊 Gerador de Relatório HTML a partir de Arquivo CSV

Este projeto em Python tem como objetivo **ler um arquivo `.csv` com informações de produtos e gerar automaticamente um relatório em formato HTML**. A aplicação foi projetada com modularidade, permitindo fácil manutenção, leitura e expansão.


## 🚀 Funcionalidades

* Leitura de arquivos `.csv` com estrutura específica.
* Processamento de dados com separação por cabeçalho e produtos.
* Geração de um relatório HTML estilizado com base em template.
* Registro de logs de todo o processo de execução.


## 🗂 Estrutura do CSV

O arquivo de entrada deve seguir o seguinte formato:

```csv
H;Título do Relatório;2025-07-21
P;Notebook X;Marca Y;15.6";Preto;i5;8GB;256GB;3500.00;2023-09-01;http://imagem.com/x.png
P;Notebook Z;Marca W;14";Cinza;i7;16GB;512GB;5400.00;2024-02-15;http://imagem.com/z.png
```

* `H` define o cabeçalho (título e data).
* `P` define os produtos.


## 📄 Módulos principais

* **`principal.py`**: Arquivo principal que orquestra a leitura, processamento e escrita do relatório.
* **`arquivo_entrada_csv.py`**: Contém as classes `ArquivoEntrada`, `Cabecalho` e `Produto` responsáveis pelo parser do CSV.
* **`relatorio_html.py`**: Responsável por renderizar e escrever o relatório final em HTML.
* **`utils.py`**: Utilitários, como o parser de argumentos da linha de comando.


## 📌 Requisitos

* Python 3.7 ou superior
* Estrutura correta do arquivo CSV
