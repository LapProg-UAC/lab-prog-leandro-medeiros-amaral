def f(n: int) -> int:
    """
    Calcula a sequência de Jacobsthal até o n-ésimo termo.

    Args:
        n (int): O índice final da sequência (n >= 0).

    Returns:
        list[int]: Lista contendo [f(0), f(1), ..., f(n)].

    Raises:
        ValueError: Se n < 0.
    """
    if n < 0:
        raise ValueError("O índice 'n' deve ser maior ou igual a 0.")
    
    # Função recursiva auxiliar para calcular cada termo
    def termo(k: int) -> int:
        if k == 0: return 0
        if k == 1: return 1
        return 2 * termo(k - 2) + termo(k - 1)
    
    return [termo(i) for i in range(n + 1)]

def main():
    """
    Função principal que gerencia a interação com o usuário,
    capturando entradas e exibindo os resultados calculados.
    """
    while True:
        entrada = input("Digite um número inteiro (ou 'sair' para terminar): ")
        
        if entrada.lower() == 'sair':
            break
            
        try:
            n = int(entrada)
            resultado = f(n)
            print(f"f({n}) = {resultado}")
        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()