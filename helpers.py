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

