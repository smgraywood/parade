from dataclasses import dataclass

@dataclass
class Step: 
    name: str
    duration: int
    total_float: int
    free_float: int
    es: int
    ls: int
    ef: int
    lf: int
