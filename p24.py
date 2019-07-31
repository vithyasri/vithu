V=input()
try:
    i = float(V)
except (ValueError, TypeError):
    print('\nno')
else:
	print('\nyes')
