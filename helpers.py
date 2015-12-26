import string

"""
Reads a .txt file and returns a list of all the lines in the text
"""
def read_file(filename):
	f = open(filename, "r").read()
	splitted_file = f.split("\n")[:]
	return splitted_file


"""
Decodes a message by shifting each letter a specified number of
times with respect to the alphabet. The a is considered to go
after the z. Example: shifts e -> g, z -> b if the specified
number is 2. Non-letters are left the same.
"""
def decode_msg(msg, shift):
	decoded_msg = ""
	for l in msg:
		if l in string.ascii_lowercase:
			print (string.ascii_lowercase.find(l)+shift)%len(string.ascii_lowercase)
			decoded_msg += string.ascii_lowercase[(string.ascii_lowercase.find(l)+shift)%len(string.ascii_lowercase)]
		elif l in string.ascii_uppercase:
			decoded_msg += string.ascii_uppercase[(string.ascii_uppercase.find(l)+shift)%len(string.ascii_uppercase)]
		else:
			decoded_msg += l
	return decoded_msg


"""
Decodes a message by shifting each letter the number of times
of its index plus a specified shift with respect to the alphabet.
If no shift is specified, defaults to 0. The a is considered to
go after the z. Non-letters are left the same.
Example: shifts aaa -> abc if the shift is 0, or aad -> cdg if the
shift is 2.
"""
def decode_msg_inc(msg, shift=0):
	decoded_msg = ""
	for i in xrange(len(msg)):
		if msg[i] in string.ascii_lowercase:
			decoded_msg += string.ascii_lowercase[(string.ascii_lowercase.find(msg[i])+i+shift)%len(string.ascii_lowercase)]
		elif msg[i] in string.ascii_uppercase:
			decoded_msg += string.ascii_uppercase[(string.ascii_uppercase.find(msg[i])+i+shift)%len(string.ascii_uppercase)]
		else:
			decoded_msg += msg[i]
	return decoded_msg


"""
Returns a dictionary with the number of times each character appears
in a string. Has an optional field that is an already existing dictionary
with a character count
"""
def character_count(strng,char_count={}):
	for letter in strng:
		if letter in char_count:
			char_count[letter] += 1
		else:
			char_count[letter] = 1
	return char_count


"""
Returns a dictionary with the number of times each character appears
in a file. 
"""
def character_count_file(file_dir):
	char_count = {}
	text = read_file(file_dir)
	for line in text:
		character_count(line, char_count)
	return char_count


"""
Finds the characters that appear only once in a file, and returns a
list with them, in the order that they appear.
"""
def find_chars_one_appearance(file_dir):
	chars_one_appearance = []
	all_chars = set()
	text = read_file(file_dir)
	for line in text:
		for char in line:
			if char not in all_chars:
				all_chars.add(char)
				chars_one_appearance.append(char)
			elif char in chars_one_appearance:
				chars_one_appearance.remove(char)
	return chars_one_appearance


"""
Determines if a pair of coordinates (row,col) is valid within a board
of given width and height (i.e. the coordinates would fall inside the board),
represented as a list of rows, each with the characters it contains
"""
def are_valid_coords(width, height, row, col):
	return (row >= 0 and row < height and col >= 0 and col < width)


"""
Given the coordinates of a cell in a rectangular board and the dimensions of
the board, returns the indices of its neighbors, which are the eight cells
right above, below, right, left or diagonal to it.
"""
def neighbor_cells_indices(width, height, row, col):
	neighbors = set()
	for j in xrange(row-1,row+2):
		for i in xrange(col-1,row+2):
			if are_valid_coords(width,height,j,i):
				neighbors.add((j,i))
	return neighbors


"""
Given a rectangular board represented as a list of the characters in each row,
returns a dictionary whose (key,value) pairs are the coordinates of each cell
and the set of characters that are neighbors to the cell.
"""
def find_char_neighbors(board):
	char_neighbors = {}
	height = len(board)
	width = len(board[0])
	for row in xrange(height):
		for col in xrange(width):
			char_neighbors[(row,col)] = []
			for neighbor_inds in neighbor_cells_indices(width,height,row,col):
				char_neighbors[(row,col)].append(board[row][col])
			for char in char_neighbors:
				if char_neighbors[(row,col)].count(char) == 3:
					print char
	return char_neighbors


def find_char_neighbors_file(file_dir):
	board = read_file(file_dir)
	return find_char_neighbors(board)

find_char_neighbors_file('python_challenge3.txt')
