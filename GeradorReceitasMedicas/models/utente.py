from dataclasses import dataclass, field

@dataclass
class Utente:
    """Representa um utente do sistema.

    Attributes:
        numero_utente: Número de utente (cifrado).
        nome: Nome completo do utente.
        medicamentos: Lista de medicamentos atribuídos (opcional).
    """
    numero_utente: str
    nome: str
    medicamentos: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Converte a instância do Utente para um dicionário.

        Returns:
            Dicionário com os atributos do utente.
        """
        return {
            "numero_utente": self.numero_utente,
            "nome": self.nome,
            "medicamentos": self.medicamentos
        }
