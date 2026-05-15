import random
from repository.data_repository import ler_medicamentos

def gerar_lista_medicamentos(quantidade: int) -> list[str]:
    """Seleciona aleatoriamente medicamentos.

    Args:
        quantidade: Número de medicamentos.

    Returns:
        Lista de medicamentos.
    """
    medicamentos = ler_medicamentos()
    if quantidade > len(medicamentos):
        quantidade = len(medicamentos)
    return random.sample(medicamentos, quantidade)

def gerar_matriz_interacao() -> tuple[list[str], list[list[int]]]:
    """Gera uma matriz de interações entre medicamentos.

    Returns:
        Tupla com (lista_medicamentos, matriz_interacoes).
    """
    medicamentos = ler_medicamentos()
    tamanho = len(medicamentos)
    matriz = [[0] * tamanho for _ in range(tamanho)]

    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            valor = random.randint(0, 5)
            matriz[i][j] = valor
            matriz[j][i] = valor
    return medicamentos, matriz

def buscar_interacao(medicamentos: list[str], matriz: list[list[int]], med_a: str, med_b: str) -> int | None:
    """Retorna o nível de interação entre dois medicamentos.

    Args:
        medicamentos: Lista de medicamentos.
        matriz: Matriz de interações.
        med_a: Nome do medicamento A.
        med_b: Nome do medicamento B.

    Returns:
        Nível de interação (0-5) ou None se não encontrado.
    """
    try:
        i = medicamentos.index(med_a)
        j = medicamentos.index(med_b)
        return matriz[i][j]
    except ValueError:
        return None
