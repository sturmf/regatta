import pytest
from regatta import main

def test_main():
  # This test does not make sense, it's just to check the coeverage framework
  assert(main.main()==None)