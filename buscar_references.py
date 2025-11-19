import re
import requests

def extrair_dois(linha):
    """
    Extrai o DOI de uma linha no formato 'https://doi.org/...'
    """
    match = re.search(r'https://doi.org/([^\s]+)', linha)
    if match:
        return match.group(1).strip()
    return None

def get_bibtex_from_crossref(doi):
    url = f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex"
    headers = {"Accept": "application/x-bibtex"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Não foi possível buscar o DOI {doi}: {response.status_code}")
        return None

def main():
    input_file = "referencias2.txt"
    output_file = "referencias2.bib"
    all_bibtex_entries = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Extrai DOI da linha
            doi = extrair_dois(line)
            if doi:
                bibtex = get_bibtex_from_crossref(doi)
                if bibtex:
                    all_bibtex_entries.append(bibtex)
            else:
                print(f"DOI não encontrado na linha: {line.strip()[:50]}") # Mostra o início da linha

    # Salva todas as entradas num arquivo .bib
    if all_bibtex_entries:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(all_bibtex_entries))
        print(f"{len(all_bibtex_entries)} referências salvas em {output_file}")
    else:
        print("Nenhuma referência processada.")

if __name__ == "__main__":
    main()