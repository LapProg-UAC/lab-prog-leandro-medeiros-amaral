# nó de árvore (binária) genealógica ascendente

class NooArvGenAsc:
    """
    Classe que representa um nó de uma árvore genealógica ascendente.
    Cada nó contém o nome da pessoa e referências para a sua mãe e o seu pai.
    """
    
    def __init__(self, val:str):
        """
        Construtor do nó da árvore genealógica.
        
        :param val: O nome da pessoa a ser armazenada neste nó.
        """
        self._nome: str = val
        self._mae = None
        self._pai = None

    def get_nome(self) -> str:
        """
        Obtém o nome da pessoa.
        
        :return: Uma string com o nome.
        """
        return self._nome

    def set_nome(self, nome: str):
        """
        Modifica o nome da pessoa.
        
        :param nome: Novo nome a atribuir.
        """
        self._nome = nome

    def get_mae(self):
        """
        Obtém o nó correspondente à mãe (subárvore esquerda).
        
        :return: Um objeto NooArvGenAsc representando a mãe ou None.
        """
        return self._mae

    def set_mae(self, mae):
        """
        Define o nó correspondente à mãe da pessoa.
        
        :param mae: O nó (NooArvGenAsc) da mãe.
        """
        self._mae = mae

    def get_pai(self):
        """
        Obtém o nó correspondente ao pai (subárvore direita).
        
        :return: Um objeto NooArvGenAsc representando o pai ou None.
        """
        return self._pai

    def set_pai(self, pai):
        """
        Define o nó correspondente ao pai da pessoa.
        
        :param pai: O nó (NooArvGenAsc) do pai.
        """
        self._pai = pai
