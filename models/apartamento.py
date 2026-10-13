from dataclasses import dataclass, field, asdict

@dataclass(frozen=True)
class Apartamento:
    url: str
    preco: float
    quartos: int
    wc: int
    m2: int
    novo: bool = False
    morada: str 
    extras: dict[str, str] = field(default_factory=dict, compare=False)
    
    def __post_init__(self):
        if not self.url.strip():
            raise ValueError("Url can´t be empty!")
        if self.preco <= 0:
            raise ValueError("Preço tem de ser positivo.")
        if self.quartos < 0 or self.wc < 0:
            raise  ValueError("Os quartos e WC têm de ser números positivos.")
        
    def to_dict(self) -> dict:
        return asdict(self)