# árvore (binária) genealógica ascendente
from lp_noo_arv_gen_asc import NooArvGenAsc

class ArvGenAsc:
    """
    Classe que representa uma árvore genealógica ascendente.
    """
    def __init__(self, noo: NooArvGenAsc):
        """
        Construtor da árvore genealógica ascendente.
        
        :param noo: O nó (NooArvGenAsc) que servirá de raiz à árvore.
        """
        self._raiz = noo

    def get_raiz(self) -> NooArvGenAsc:
        """
        Obtém a raiz da árvore.
        
        :return: O nó raiz da árvore.
        """
        return self._raiz

    def set_raiz(self, noo: NooArvGenAsc):
        """
        Modifica a raiz da árvore.
        
        :param noo: O novo nó raiz.
        """
        self._raiz = noo

    def in_ord_trav(self)-> list:
        """
        Travessia "em-ordem" dos nós da árvore.
        Percorre primeiro o pai, depois a pessoa atual, e por fim a mãe.
        
        :return: Lista dos nomes (nós) pela ordem que resultou da travessia.
        """
        def em_ordem(aga:NooArvGenAsc):
            if aga is None:
                return []
            else:
                em_ordem(aga.get_pai())
                visit.append(aga.get_nome())
                em_ordem(aga.get_mae())

        visit: list = []
        em_ordem(self._raiz)
        return visit

    def pesquisar_no(self, no: NooArvGenAsc, nome: str) -> NooArvGenAsc:
        """
        Pesquisa recursiva por um nó com o nome dado a partir de um nó específico.
        
        :param no: O nó de partida para a pesquisa.
        :param nome: O nome da pessoa a procurar.
        :return: O nó encontrado ou None caso não exista.
        """
        if no is None:
            return None
        if no.get_nome() == nome:
            return no
        
        res_mae = self.pesquisar_no(no.get_mae(), nome)
        if res_mae is not None:
            return res_mae
            
        return self.pesquisar_no(no.get_pai(), nome)

    def adicionar_pais(self, nome_pessoa: str, nome_mae: str, nome_pai: str) -> bool:
        """
        Adiciona mãe e pai a uma pessoa existente na árvore, desde que não os tenha ainda definidos.
        
        :param nome_pessoa: O nome da pessoa (nó alvo) que já existe na árvore.
        :param nome_mae: O nome a atribuir à mãe.
        :param nome_pai: O nome a atribuir ao pai.
        :return: True se a pessoa foi encontrada e atualizada, False caso contrário.
        """
        no_pessoa = self.pesquisar_no(self._raiz, nome_pessoa)
        if no_pessoa is not None:
            if nome_mae and no_pessoa.get_mae() is None:
                no_pessoa.set_mae(NooArvGenAsc(nome_mae))
            if nome_pai and no_pessoa.get_pai() is None:
                no_pessoa.set_pai(NooArvGenAsc(nome_pai))
            return True
        return False

    def obter_pais_rec(self, no: NooArvGenAsc, nome: str) -> tuple:
        """
        Pesquisa recursivamente os pais de uma dada pessoa.
        
        :param no: O nó de partida atual.
        :param nome: O nome da pessoa de quem procuramos os pais.
        :return: Um tuplo contendo (nome_mae, nome_pai). Se algum não existir, retorna None nessa posição.
        """
        if no is None:
            return None, None
        if no.get_nome() == nome:
            mae = no.get_mae().get_nome() if no.get_mae() else None
            pai = no.get_pai().get_nome() if no.get_pai() else None
            return mae, pai
        res_mae = self.obter_pais_rec(no.get_mae(), nome)
        if res_mae != (None, None):
            return res_mae
        return self.obter_pais_rec(no.get_pai(), nome)

    def obter_pais(self, nome: str) -> tuple:
        """
        Obtém os nomes dos pais (mãe e pai) de uma dada pessoa na árvore.
        
        :param nome: O nome da pessoa.
        :return: Tuplo (nome_mae, nome_pai).
        """
        return self.obter_pais_rec(self._raiz, nome)

    def obter_ascendentes_grau_rec(self, no: NooArvGenAsc, grau: int) -> list:
        """
        Obtém recursivamente todos os ascendentes de um determinado grau a partir de um nó.
        
        :param no: O nó de partida.
        :param grau: O grau pretendido (1=pais, 2=avós, etc).
        :return: Lista com os nomes de todos os ascendentes daquele grau.
        """
        if no is None:
            return []
        if grau == 0:
            return [no.get_nome()]
        ascendentes = []
        ascendentes.extend(self.obter_ascendentes_grau_rec(no.get_mae(), grau - 1))
        ascendentes.extend(self.obter_ascendentes_grau_rec(no.get_pai(), grau - 1))
        return ascendentes

    def obter_ascendentes_grau(self, nome: str, grau: int) -> list:
        """
        Obtém todos os ascendentes maternos e paternos de um certo grau para a pessoa dada.
        
        :param nome: O nome da pessoa base.
        :param grau: O grau pretendido (1=pais, 2=avós, etc).
        :return: Lista de nomes correspondente aos ascendentes no grau estipulado.
        """
        no = self.pesquisar_no(self._raiz, nome)
        if no:
            return self.obter_ascendentes_grau_rec(no, grau)
        return []

    def obter_ascendente_linha_rec(self, no: NooArvGenAsc, grau: int, linha: str) -> str:
        """
        Navega recursivamente por uma linha (materna ou paterna) para encontrar um ascendente singular.
        
        :param no: O nó base para pesquisar.
        :param grau: O grau do ascendente.
        :param linha: String que define qual linha seguir ("materna" ou "paterna").
        :return: O nome do ascendente procurado ou None.
        """
        if no is None:
            return None
        if grau == 0:
            return no.get_nome()
        if linha == "materna":
            return self.obter_ascendente_linha_rec(no.get_mae(), grau - 1, linha)
        elif linha == "paterna":
            return self.obter_ascendente_linha_rec(no.get_pai(), grau - 1, linha)
        return None

    def obter_ascendente_linha(self, nome: str, grau: int, linha: str) -> str:
        """
        Obtém um dos ascendentes para a pessoa selecionada, seguindo estritamente apenas a linha materna ou paterna.
        
        :param nome: O nome da pessoa da qual se quer procurar o ascendente.
        :param grau: Grau (ex: 1=Pai/Mãe, 2=Avô(ó), etc).
        :param linha: String "materna" ou "paterna".
        :return: O nome do ascendente em questão ou None se não existir.
        """
        no = self.pesquisar_no(self._raiz, nome)
        if no:
            return self.obter_ascendente_linha_rec(no, grau, linha)
        return None

def construir_arvore_de_ficheiro(nome_ficheiro: str) -> ArvGenAsc:
    """
    Constrói a árvore genealógica ascendente a partir de um ficheiro de texto.
    O ficheiro deve ter as linhas no formato "Pessoa,Mae,Pai".
    Os nós da árvore não podem ter grau 1, e a construção é feita recursivamente.
    
    :param nome_ficheiro: O caminho/nome do ficheiro a ler.
    :return: A árvore ArvGenAsc construída, ou None em caso de ficheiro vazio.
    """
    with open(nome_ficheiro, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        
    dados = {}
    for linha in linhas:
        partes = linha.strip().split(',')
        if len(partes) >= 3:
            nome = partes[0].strip()
            mae = partes[1].strip()
            pai = partes[2].strip()
            dados[nome] = (mae, pai)
            
    if not linhas:
        return None
        
    raiz_nome = linhas[0].split(',')[0].strip()
    arvore = ArvGenAsc(NooArvGenAsc(raiz_nome))
    
    def construir_recursivo(arv: ArvGenAsc, nome_atual: str):
        if nome_atual in dados:
            mae, pai = dados[nome_atual]
            if mae and pai:
                arv.adicionar_pais(nome_atual, mae, pai)
                construir_recursivo(arv, mae)
                construir_recursivo(arv, pai)

    construir_recursivo(arvore, raiz_nome)
    return arvore


