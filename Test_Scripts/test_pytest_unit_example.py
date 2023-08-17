"""
Let’s test various situations for an application designed in this way.
Can we add passengers seamlessly?
Is the passenger we add included in the passenger list?
It is necessary that we cannot add new passengers when the aircraft capacity is full, is there any measure against this situation?
Can we calculate the total revenue correctly?
"""

import pytest
from unittest.mock import Mock
from classes.pytest_unit_example import TravellerDb, Plane

@pytest.fixture
def appTest():
    plane = Plane(5, 10)
    plane.add_trveller("Sachin")
    plane.add_trveller("Virat")
    plane.add_trveller("Dhoni")
    d = TravellerDb()
    yield plane, d
    d.close()

def test_adding_a_trveller(appTest):
    appTest[0].add_trveller("Kapil")
    assert appTest[0].number_of_traveller() == 4

def test_plane_contains_booked_traveller(appTest):
    appTest[0].add_trveller("Rohit")
    assert "Rohit" in appTest[0].get_traveller_list()

def test_booking_not_allowed_after_max(appTest):
    for _ in range(2):
        appTest[0].add_trveller("Sourabh")

    with pytest.raises(OverflowError):
        appTest[0].add_trveller("Sourabh")


def test_total_wo_mock(appTest):
    total = appTest[0].calculate_total(appTest[1])
    assert total == 21.7

def test_total_mocking_constant(appTest):
    d = appTest[1]
    d.get_traveller_membership = Mock(return_value=1)
    total = appTest[0].calculate_total(d)
    assert total == 30

def test_total_mocking_w_se(appTest):
    """with side effect"""
    def mock_members(name: str) -> int:
        if name == "Sachin":
            return 2
        elif name == "Virat":
            return 1.5
        return 1

    d = appTest[1]
    d.get_traveller_membership = Mock(side_effect=mock_members)
    total = appTest[0].calculate_total(d)
    assert total == 21.7
