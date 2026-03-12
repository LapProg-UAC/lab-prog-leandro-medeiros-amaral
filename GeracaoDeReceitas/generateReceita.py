#generar numero de medicamentos da receita conforme a tabela de medicamentos e substancias
import random

def gerar_lista_medicamentos(numero_de_medicamentos: int) -> list:
    """Gera uma lista aleatória de medicamentos a partir de um arquivo.

    O arquivo **medicamentos.txt** deve conter um medicamento por linha. A
    função seleciona aleatoriamente `numero_de_medicamentos` distintos desse
    conjunto e retorna-os como lista.

    Parâmetros
    ----------
    numero_de_medicamentos : int
        Quantidade de medicamentos a incluir na lista. Se o valor for maior do
        que o número de entradas disponíveis no arquivo, todos os medicamentos
        serão retornados (com aviso impresso).

    Retorno
    -------
    list
        Lista de strings, cada uma representando o nome de um medicamento.
        Retorna lista vazia em caso de erro ao abrir o arquivo.
    """
    try:
        with open('medicamentos.txt', 'r', encoding='utf-8') as arquivo:
            medicamentos = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    except FileNotFoundError:
        print("Erro: Arquivo medicamentos.txt não encontrado!")
        return []
    
    if numero_de_medicamentos > len(medicamentos):
        print(f"Aviso: Número de medicamentos solicitado ({numero_de_medicamentos}) é maior que os disponíveis ({len(medicamentos)}).")
        numero_de_medicamentos = len(medicamentos)
    
    lista_medicamentos = random.sample(medicamentos, numero_de_medicamentos)
    return lista_medicamentos