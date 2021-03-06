import pytest
from nth_smallest_element import nth_smallest_element

def test_1st_smallest_element():
	input_list = [4, 5, 8, 2, 0]
	assert nth_smallest_element(input_list, 1) == 0

def test_2nd_smallest_element():
	input_list = [4, 5, 8, 2, 0]
	assert nth_smallest_element(input_list, 2) == 2

def test_3rd_smallest_element():
	input_list = [4, 5, 8, 2, 0]
	assert nth_smallest_element(input_list, 3) == 4

def test_4th_smallest_element():
	input_list = [4, 5, 8, 2, 0]
	assert nth_smallest_element(input_list, 4) == 5

def test_5th_smallest_element():
	input_list = [4, 5, 8, 2, 0]
	assert nth_smallest_element(input_list, 5) == 8

def test_raise_exception_if_n_equals_0():
	input_list = [4, 5, 8, 2, 0]
	with pytest.raises(Exception):
		nth_smallest_element(input_list, 0)

def test_raise_exception_if_n_equals_negative_1():
	input_list = [4, 5, 8, 2, 0]
	with pytest.raises(Exception):
		nth_smallest_element(input_list, -1)
