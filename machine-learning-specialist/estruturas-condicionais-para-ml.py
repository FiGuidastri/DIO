#%%
#Estrutura condicional simples
print('Estrutura condicional simples')

def soma(soma):
    if soma > 0:
        return 'Maior do que zero!'
    else:
        return 'Menor do que zero!'
    
display(soma(10+(-15)))
display(soma(-5+6))
display(soma(-135))

num1 = 3
num2 = 3

if num1 == num2:
    print('Os números são iguais')
else:
    print('Os números são diferentes')
# %%
# Estrutura condicional composta
print('Estrutura condicional composta')
# %%
# Estrutura condicional aninhada
print('Estrutura condicional aninhada')

def soma2(soma):
    if soma > 0:
        return 'Soma maior que zero'
    elif soma == 0:
        return 'Soma é igual a zero'
    else:
        return 'Soma menor do que zero'

display(soma2(-35))
display(soma2(0))
display(soma2(1564))

# %%
