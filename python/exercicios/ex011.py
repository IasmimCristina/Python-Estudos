#Parede. Cada litro pinta 2m2.
f = '_' * 5

print('{}{}{}'.format(f, f, f))
print('{}{}{}'.format(f, f, f))
print('_____Área______')
print('{}{}{}'.format(f, f, f))
print('{}{}{}'.format(f, f, f))

l = float(input('Digite a largura: '))
al = float(input('Digite a altura: '))
ar = l * al
lit = ar / 2

print('{}{}{}'.format(f, f, f))
print('Área: {:.2f}m².'.format(ar))
print('Litros necessários para pintar: {:.0f}.'.format(lit))

print('{}{}{}'.format(f, f, f))
print('{}{}{}'.format(f, f, f))

