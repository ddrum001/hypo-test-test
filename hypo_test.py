import pytest

from hypothesis import given, example
from hypothesis.strategies import integers

from biz_logic import *

class TestClass: 
	@given( x = integers() )
	@example ( x = 6 )
	def test_add_two(self, x):
		assert add_two(x) == x + 2
