def ucs11(n):
	if n %11 == 0 : return f'{n} is a multiple of 11.'
	else : return '{n} is not a multiple of 11.'
while True:
	try:
		n = int(input())
		if n == 0 : break
		print(ucs11(n))
	except EOFError:
		break