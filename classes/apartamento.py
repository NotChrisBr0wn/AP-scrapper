from dataclasses import dataclass

@dataclass
class Apartamento:
    url: str
    preco: float
    quartos: int
    wc: int
    m2: int
    novo: bool
    morada: str