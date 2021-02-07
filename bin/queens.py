"""queens
"""
from string import ascii_uppercase

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-2-7"

class queens:
	def __init__ (self, queens=8):
		"""Where it all begins
		"""
		self.setup(queens)
		self.add_queen()

	def setup(self, queens):
		"""Setup parameters
		"""
		self.queens = queens
		self.queens_pos = [None] * self.queens
		self.founded = 0

	def add_queen(self, line=0):
		"""Add a queen if possible
		"""
		if self.queens == line:
			self.print()
		else:
			for column in range(self.queens): # Try all possibile position into the same line
				if self.secure(column, line):
					self.queens_pos[line] = column
					self.add_queen(line + 1)

	def secure(self, column, line):
		"""Check if a cell is secure
		"""
		for i in range(line): # Check all old queens
			if self.queens_pos[i] == column or self.queens_pos[i] == column - (line - i) or self.queens_pos[i] == column + (line - i):
				return False
		return True

	def print(self):
		"""Costumized print
		"""
		self.founded += 1
		print(f"Combination #{self.founded}")

		# Intestation
		board = " " * (len(str(self.queens)) + 2)
		for i in range(self.queens):
			board += ascii_uppercase[i % len(ascii_uppercase)] + " "
		board += "\n"

		# Body
		board += " " * (len(str(self.queens)) + 1) + "--" * self.queens + "-\n"
		for i in range(self.queens):
			board += str(self.queens - i) + " " * (len(str(self.queens)) - len(str(self.queens - i)) + 1) + "| " * self.queens_pos[i] + "|x" +  "| " * (self.queens - self.queens_pos[i] - 1) + "|" + " " * (len(str(self.queens)) - len(str(self.queens - i)) + 1) + str(self.queens - i) + "\n"
			board += " " * (len(str(self.queens)) + 1) + "--" * self.queens + "-\n"
		
		# Footer
		board += " " * (len(str(self.queens)) + 2)
		for i in range(self.queens):
			board += ascii_uppercase[i % len(ascii_uppercase)] + " "
		board += "\n"

		# Print
		print(board)
		
if __name__ == "__main__":
	queens()
