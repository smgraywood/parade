#happy, sad, bad, mad

#happy
#happy would be if we can calc the total and free float correctly using the given info

#sad
#can't calc free and total float, or get an error

#bad
#can calc a random thing or give random things to calc that is not correct

#mad

import hypothesis.strategies as st
from hypothesis import given
from parade.models import Step, total_float_calc

@given(st.builds(Step))
def test_total_float_calc(step:Step):
    assert total_float_calc(step) <= step.ls 