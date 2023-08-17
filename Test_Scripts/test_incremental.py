import pytest
from classes.incremental import Incrimental


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------
@pytest.fixture
def incre():
  return Incrimental()

def test_accumulator_init(incre):
  assert incre.count == 0

def test_accumulator_add_one(incre):
  incre.increment()
  assert incre.count == 1

def test_accumulator_add_three(incre):
  incre.increment(3)
  assert incre.count == 3

def test_accumulator_add_twice(incre):
  incre.increment()
  incre.increment()
  assert incre.count == 2

def test_accumulator_add_five_then_one(incre):
  incre.increment(5)
  with pytest.raises(ValueError, match=r"count can not be more than 5") as e:
    incre.increment()

def test_accumulator_add_six(incre):
  incre.increment(6)
  assert incre.count == 5

def test_accumulator_cannot_set_count_directly(incre):
  incre = Incrimental()
  with pytest.raises(AttributeError, match=r"can't set attribute 'count'") as e:
    incre.count = 10