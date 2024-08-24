import base64
print("Converter string to base 64 and binary")
select = input("Enter number to select mode 1.Base64 2.Binary:")
if select == '1':
	text = input("Enter text to convert in base64:")
	b = base64.b64encode(bytes(text, 'utf-8'))
	print("In base64:", b.decode('utf-8') )
elif select == '2':
	text = input("Enter text to convert in binary")
	binary = ''.join(format(ord(i), '08b') for i in text)
	print("In binary:", binary)
