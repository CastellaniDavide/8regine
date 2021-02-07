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
			self.print() # All queens are placed
		else:
			for column in range(self.queens): # Try all possibile position into the same line
				if self.secure(column, line):
					self.queens_pos[line] = column
					self.add_queen(line + 1)

	def secure(self, column, line):
		"""Check if a cell is secure
		"""
		for i in range(line): # Check all old queens
			if self.queens_pos[i] == column or self.queens_pos[i] == column - (line - i) or self.queens_pos[i] == column + (line - i): # Check the column, and diagonals, we didn't search by line, because it's impossibile have two queens into the same line with this algorithm
				return False
		return True # If passed all tests it's possible place a new queen in that place

	def print(self):
		"""Costumized print
		"""
		self.founded += 1
		print(f"Combination #{self.founded}")

		# Intestation
		board = " " * (len(str(self.queens)) + 2) # Initials spaces
		for i in range(self.queens):
			board += ascii_uppercase[i % len(ascii_uppercase)] + " " # Board's letters
		board += "\n"

		# Body
		board += " " * (len(str(self.queens)) + 1) + "--" * self.queens + "-\n"
		for i in range(self.queens):
			board += str(self.queens - i) + " " * (len(str(self.queens)) - len(str(self.queens - i)) + 1) # Left number + some spaces
			board += "| " * self.queens_pos[i] + "|x" +  "| " * (self.queens - self.queens_pos[i] - 1) + "|" # Single line of the board
			board += " " * (len(str(self.queens)) - len(str(self.queens - i)) + 1) + str(self.queens - i) + "\n" # Right number + some spaces + new line
			board += " " * (len(str(self.queens)) + 1) + "--" * self.queens + "-\n" # Separator line
		
		# Footer
		board += " " * (len(str(self.queens)) + 2)# Initials spaces
		for i in range(self.queens):
			board += ascii_uppercase[i % len(ascii_uppercase)] + " " # Board's letters
		board += "\n"

		# Print
		print(board)
		
if __name__ == "__main__":
	queens()
