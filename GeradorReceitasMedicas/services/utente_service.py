import random
from models.utente import Utente
from services.cifra_service import cifrar

LISTA_NOMES = ["João", "Maria", "Pedro", "Ana", "Carlos", "Sofia", "Luís", "Isabela", "Rafael", "Beatriz", "Francisco"]
LISTA_SOBRENOMES = ["Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues", "Almeida", "Gomes", "Martins", "Carvalho"]

def gerar_utentes(quantidade: int) -> list[Utente]:
    """Gera uma lista de objetos Utente com números e nomes aleatórios.

    Args:
        quantidade: Quantidade de utentes a gerar.

    Returns:
        Lista de objetos Utente.
    """
    lista_utentes = []
    for _ in range(quantidade):    
        numero = str(random.randint(100000, 999999))
        numero_cifrado = cifrar(numero, 3, 'criptografar')
        nome = f"{random.choice(LISTA_NOMES)} {random.choice(LISTA_SOBRENOMES)}"
        lista_utentes.append(Utente(numero_utente=numero_cifrado, nome=nome))
    return lista_utentes
