import random

def gerar_matriz_combinacao() -> tuple[list, list]:
    """Cria uma matriz quadrada de interações entre medicamentos.

    Retorna uma tupla (medicamentos, matriz) em que as linhas e colunas da matriz
    correspondem à ordem dos medicamentos na lista retornada. O elemento na
    diagonal principal é sempre 0. Os valores fora da diagonal são um inteiro
    entre 0 e 5 representando o nível de interação.
    """
    try:
        with open('medicamentos.txt', 'r', encoding='utf-8') as arquivo:
            medicamentos = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    except FileNotFoundError:
        print("Erro: Arquivo medicamentos.txt não encontrado!")
        return [], []

    tamanho = len(medicamentos)
    matriz_combinacao = [[0]*tamanho for _ in range(tamanho)]

    for i in range(tamanho):
        for j in range(i+1, tamanho):
            valor = random.randint(0, 5)
            matriz_combinacao[i][j] = valor
            matriz_combinacao[j][i] = valor  # simetria

    return medicamentos, matriz_combinacao


def buscar_interacao(medicamentos: list, matriz: list, a: str, b: str) -> int | None:
    """Retorna a interação entre dois medicamentos pelo nome.

    Se um dos medicamentos não estiver na lista, retorna None.
    """
    try:
        i = medicamentos.index(a)
        j = medicamentos.index(b)
    except ValueError:
        return None
    return matriz[i][j]
