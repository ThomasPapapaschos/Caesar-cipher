plaintext = input("Please type your message: \n").upper()
shift = int(input("Please type the desired shift value (1-25): \n"))
while shift not in range(1,26):
	shift = int(input("Error, shift value must be (1-25).Try again: \n"))
ciphertext= ""

for character in plaintext:
	if character == " ":
		ciphertext += " "
	elif ord(character) + shift > ord("Z"):
		ciphertext += chr(ord(character) + shift - 26)
	else:
		ciphertext += chr(ord(character) + shift)


print(ciphertext)
