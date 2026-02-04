print(f'***BEM-VINDO AO PLANEJADOR DE META FINANCEIRA*** \n - Primeiro você digitará os valores da sua meta financeira e da quantidade de meses para atingi-lá.\n - Em seguida será solicitado a digitar sua renda e as despesas mensais. \n - Para finalizar digite 0.')

meta = float(input('Digite a sua meta: '))
meses = int(input('Digite quantos meses para atingir a meta: '))
renda = float(input('Digite sua renda mensal: '))
despesas = []
despesas.append(float(input('Digite a valor de uma despesa mensal fixa (ou 0 para finalizar): ')))

while despesas[-1] != 0:
    despesas.append(float(input('Digite a valor de uma despesa mensal fixa (ou 0 para finalizar): ')))

total_despesas = sum(despesas)
sobras = renda - total_despesas
acumulados = sobras * meses

if acumulados >= meta:
    print(f'Você atingiu sua meta!!!\nEm cada mês sua sobra foi de R${sobras:.2f}, somando as sobras ao longo dos {meses} meses, você acumulo o total de: R${acumulados:.2f}')
else:  
    print(f'Você não atingiu a meta\nEm cada mês sua sobra foi de R${sobras:.2f}, somando as sobras ao longo dos {meses} meses, você acumulo o total de: R${acumulados:.2f}')

