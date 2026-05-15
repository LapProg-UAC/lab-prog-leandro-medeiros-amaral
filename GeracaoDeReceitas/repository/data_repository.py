import json
import csv
from models.utente import Utente

ARQUIVO_MEDICAMENTOS = 'data/medicamentos.txt'

def ler_medicamentos() -> list[str]:
    """Lê a lista de medicamentos a partir do ficheiro de dados.

    Returns:
        Lista de nomes de medicamentos.
    """
    try:
        with open(ARQUIVO_MEDICAMENTOS, 'r', encoding='utf-8') as arquivo:
            return [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: Ficheiro {ARQUIVO_MEDICAMENTOS} não encontrado!")
        return []

def exportar_utentes(lista_utentes: list[Utente]):
    """Exporta a lista de utentes para ficheiros JSON e CSV.

    Args:
        lista_utentes: Lista de objetos Utente a exportar.
    """
    if not lista_utentes:
        return

    dados = [u.to_dict() for u in lista_utentes]

    try:
        with open('utentes.json', 'w', encoding='utf-8') as jf:
            json.dump(dados, jf, ensure_ascii=False, indent=2)
        
        keys = dados[0].keys()
        with open('utentes.csv', 'w', newline='', encoding='utf-8') as cf:
            writer = csv.DictWriter(cf, fieldnames=keys)
            writer.writeheader()
            writer.writerows(dados)
        print("Ficheiros utentes.json e utentes.csv criados com sucesso.")
    except Exception as e:
        print(f"Erro ao exportar dados: {e}")
