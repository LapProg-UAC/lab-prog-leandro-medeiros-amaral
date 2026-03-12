import random
from cifraDeCesar import cifra_de_cesar  

listaDeNomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Sofia", "Luís", "Isabela", "Rafael", "Beatriz","Francisco"]
listaDeSobrenomes = ["Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues", "Almeida", "Gomes", "Martins", "Carvalho"]

def gerar_numero_utente(numero_de_utentes: int) -> list:
    """Gera uma lista de utentes com números e nomes aleatórios.

    A função utiliza listas de nomes e sobrenomes pré-definidas e cria
    `numero_de_utentes` dicionários, cada um contendo as chaves
    `"numero_utente"` (um inteiro entre 100000 e 999999) e `"nome"`
    (um nome completo aleatório).

    Parâmetros
    ----------
    numeroDeUtentes : int
        Quantidade de utentes a gerar.

    Retorno
    -------
    list
        Lista de dicionários, cada um representando um utente. Caso o valor
        de entrada seja zero ou negativo, retorna lista vazia sem erro.
    """
    lista_numeros = []
    for _ in range(numero_de_utentes):    
        numero_utente = random.randint(100000, 999999) 
        numero_utente_str = str(numero_utente)
        numero_utente_encrypted = cifra_de_cesar(numero_utente_str, 3, 'criptografar')  # Encrypt the string
        nome = random.choice(listaDeNomes) + " " + random.choice(listaDeSobrenomes)
        lista_numeros.append({"numero_utente": numero_utente_encrypted, "nome": nome})
    return lista_numeros