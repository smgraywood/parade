from dataclasses import dataclass
from typing import Optional

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
    children: list["Step"]
    parents: list["Step"]
    

def total_float_calc(step:Step)->int:
    return step.ls - step.es 
#sometimes calc by lf-ef instead

def free_float_calc(step:Step)->int:
    return min([child.es for child in step.children])

