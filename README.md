# Extrator de BibTeX a partir de DOIs

Este script em Python lê um arquivo de texto contendo linhas com DOIs no
formato `https://doi.org/...`, extrai esses DOIs automaticamente e
consulta a API da **Crossref** para obter as referências correspondentes
em formato **BibTeX**.\
Todas as entradas BibTeX recuperadas são então salvas em um arquivo
`.bib`.

## Funcionalidade

O programa:

1.  Lê um arquivo de texto linha por linha (padrão: `referencias2.txt`);
2.  Identifica automaticamente DOIs contidos em cada linha;
3.  Consulta a API Crossref para obter o BibTeX de cada DOI;
4.  Coleta todas as entradas e salva em `referencias2.bib`;
5.  Exibe mensagens informativas, incluindo DOIs não encontrados ou
    erros de requisição.

## Estrutura do Arquivo de Entrada

O arquivo **referencias2.txt** deve conter DOIs no formato:

    Alguma referência com DOI https://doi.org/10.1016/j.tree.2019.02.001
    Outra linha https://doi.org/10.1093/sysbio/syaa001

## Requisitos

-   Python 3.x
-   Biblioteca `requests`

### Instalação:

``` bash
pip install requests
```

## Como usar

1.  Coloque o arquivo `referencias2.txt` na mesma pasta do script.
2.  Execute:

``` bash
python nome_do_script.py
```

3.  Ao final, será gerado o arquivo:

```{=html}
<!-- -->
```
    referencias2.bib

## Explicação das Funções

### `extrair_dois(linha)`

Localiza um DOI na forma `https://doi.org/...` dentro de uma linha
usando regex.

### `get_bibtex_from_crossref(doi)`

Consulta a Crossref usando o DOI e retorna a entrada BibTeX associada.

### `main()`

-   Lê o arquivo de entrada\
-   Extrai DOIs\
-   Obtém BibTeX\
-   Salva tudo no arquivo final `.bib`

## Mensagens de Erro

-   `DOI não encontrado na linha: ...`
-   `Não foi possível buscar o DOI ...`

## Licença

Este código pode ser utilizado e modificado livremente para fins
acadêmicos e pessoais.
# Buscar_referencias