#to automate the test cases
from src.session_example import is_valid_answers_count

def test_zero_answers_is_valid():
  assert is_valid_answers_count(0) == True # or without == True

def test_negative_answers_is_invalid():
  assert is_valid_answers_count(-1) == False # or without == False

def test_positive_answers_is_valid():
  assert is_valid_answers_count(6) == True # or without == True