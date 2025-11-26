import pytest
from src.greedy import greedy_search, needed_states, stations

@pytest.mark.greedy
def test_greedy_full_coverage():  #todas las estaciones están cubiertas
    selected, covered = greedy_search(needed_states, stations)
    assert covered == needed_states