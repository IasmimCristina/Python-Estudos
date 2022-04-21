#Dólares. Um dólar são três reais.
t = '_'*10
print('{}{}{}{}'.format(t, t, t, t))
nome = str(input('Digite o seu nome: '))
r = float(input('{}, digite quanto dinheiro você possui em reais: '.format(nome)))
d = r // 3.37
print('')
print('{}{}{}{}'.format(t, t, t, t))
print('_____Saldo bancário de {}_____'.format(nome))
print('{}{}{}{}'.format(t, t, t, t))
print('Quantos dólares podem ser comprados: {}.'.format(d))
print('Dinheiro em reais: {:.2f}. '.format(r))
