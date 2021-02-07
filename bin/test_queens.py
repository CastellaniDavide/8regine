"""Test queens file
"""
import queens

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-2-7"

def test():
	"""Tests the 8regine function in the 8regine class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert queens.queens() != "", "test all failed"
	#assert otto_regine.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
