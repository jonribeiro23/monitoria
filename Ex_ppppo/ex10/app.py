alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
frase = str(input('Digite uma frase: '))
cont = 0

for letra in alfabeto:
    if letra in frase:
        cont+=1

print(cont)
if cont==26:
    print('É pangrama')
else:
    print('Não é pangrama')
