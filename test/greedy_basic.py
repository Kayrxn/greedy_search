import pytest
from src.greedy import greedy_search, needed_states, stations

@pytest.mark.greedy
def test_greedy_basic():  #hay alguna estación cubriendo algún estado
    selected, covered = greedy_search(needed_states, stations)
    assert len(selected) > 0
    assert len(covered) > 0