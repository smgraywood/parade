"""Tests for core models."""

import hypothesis.strategies as st
from hypothesis import given

from parade.models import Step, free_float_calc, total_float_calc


@given(st.builds(Step))
def test_total_float_calc(step: Step):
    # assume(step.ls >= 0 and step.es >= 0)
    assert total_float_calc(step) <= step.ls


def test_known_total_float_calc():
    step = Step(
        name="Activity 6",
        duration=4,
        es=1,
        ls=2,
        ef=1,
        lf=5,
        children=[],
        parents=[],
    )
    assert total_float_calc(step) == 1


@given(st.builds(Step))
def test_free_float_calc(step: Step):
    if step.children:
        assert free_float_calc(step) == min(child.es for child in step.children)
    else:
        assert free_float_calc(step) == 0


@given(st.builds(Step))
def test_step_props(step: Step):
    assert step.free_float == free_float_calc(step)
    assert step.total_float == total_float_calc(step)
