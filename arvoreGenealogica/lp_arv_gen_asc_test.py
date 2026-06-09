from lp_arv_gen_asc import ArvGenAsc, construir_arvore_de_ficheiro
from lp_noo_arv_gen_asc import NooArvGenAsc

def main() -> None:
    """
    Função principal onde os testes para as funcionalidades da árvore
    genealógica são executados. Aqui é demonstrada a leitura de um ficheiro
    e a execução de todos os requisitos definidos.
    """
    print("Construindo a árvore genealógica a partir do ficheiro...")

    aga = construir_arvore_de_ficheiro("arvoreGenealogica/arvore_dados.txt")
    
    if aga is None:
        print("Erro ao construir a árvore.")
        return
        
    print(f"Pessoa na raiz da árvore: {aga.get_raiz().get_nome()}")
    print(f"Travessia em ordem: {aga.in_ord_trav()}")
    print("-" * 40)

    # Teste 1: Obter pais de pelo menos 3 pessoas
    pessoas_teste_pais = ["P1", "P2", "P5"]
    print("--- Operação: Obter os pais ---")
    for pessoa in pessoas_teste_pais:
        mae, pai = aga.obter_pais(pessoa)
        print(f"Pais de {pessoa}: Mãe = {mae}, Pai = {pai}")

    print("-" * 40)
    
    # Teste 2: Obter ascendentes de grau 1 a 4 de pelo menos 3 pessoas
    pessoas_teste_grau = ["P1", "P2", "P3"]
    print("--- Operação: Obter ascendentes por grau ---")
    for pessoa in pessoas_teste_grau:
        for grau in range(1, 4):
            ascendentes = aga.obter_ascendentes_grau(pessoa, grau)
            if ascendentes:
                print(f"Ascendentes de {pessoa} no grau {grau}: {', '.join(ascendentes)}")
            else:
                print(f"Ascendentes de {pessoa} no grau {grau}: Nenhum encontrado na árvore.")

    print("-" * 40)

    # Teste 3: Obter um ascendente de linha (materna ou paterna)
    print("--- Operação: Obter ascendente de linha (Materna/Paterna) ---")
    for pessoa in pessoas_teste_grau:
        for grau in range(1, 4):
            asc_mat = aga.obter_ascendente_linha(pessoa, grau, "materna")
            asc_pat = aga.obter_ascendente_linha(pessoa, grau, "paterna")
            print(f"{pessoa} (Grau {grau}) -> Linha Materna: {asc_mat} | Linha Paterna: {asc_pat}")

    return None

if __name__ == "__main__":
    main()

