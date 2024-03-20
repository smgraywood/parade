"""establish class model and calculate free float and total float"""

import functools
from dataclasses import dataclass
from typing import Annotated

from annotated_types import Ge

PositiveInt = Annotated[int, Ge(0)]


@dataclass(frozen=True)
class Step:
    """describe one task in a series"""

    name: str
    duration: PositiveInt
    es: PositiveInt
    ls: PositiveInt
    ef: PositiveInt
    lf: PositiveInt
    children: list["Step"]
    parents: list["Step"]

    @functools.cached_property
    def total_float(self) -> PositiveInt:
        """Amount of time task can be delayed w/o affecting completion date of project.

        Returns:
            PositiveInt: Time in project units
        """
        return total_float_calc(self)

    @functools.cached_property
    def free_float(self) -> PositiveInt:
        """Amount of time activity can be delayed w/o delaying start of successor.

        Returns:
            PositiveInt: Time in project units.
        """
        return free_float_calc(self)


def total_float_calc(step: Step) -> int:
    if step.ls < 0 or step.es < 0:
        raise ValueError("please only use positive numbers")
    return step.ls - step.es
    # sometimes calc by lf-ef instead


def free_float_calc(step: Step) -> int:
    if step.children:
        return min(child.es for child in step.children)
    return 0
