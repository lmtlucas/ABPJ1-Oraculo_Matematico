print(f'***BEM-VINDO AO PLANEJADOR DE META FINANCEIRA*** \n - Primeiro você digitará os valores da sua meta financeira e da quantidade de meses para atingi-lá.\n - Em seguida será solicitado a digitar sua renda e as suas despesas mensais. \n - Para finalizar digite 0.')

meta = float(input('Digite a sua meta: '))
meses = int(input('Digite quantos meses para atingir a meta: '))
renda = float(input('Digite sua renda mensal: '))
despesas = []
despesas.append(float(input('Digite a valor de uma despesa mensal fixa (ou 0 para finalizar): ')))

while despesas[-1] != 0:
    despesas.append(float(input('Digite a valor de uma despesa mensal fixa (ou 0 para finalizar): ')))

total_despesas = sum(despesas)
economia = renda - total_despesas
acumulados = economia * meses

if acumulados >= meta:
    print(f'Você atingiu sua meta!!!\nEm cada mês você economizou R${economia:.2f}, somando essas economias ao longo dos {meses} meses, você acumulo o total de: R${acumulados:.2f}\n - Total de despesas mensais: R${total_despesas}\n - Total economizado por mês: R${economia} ')
else:  
    print(f'Você não atingiu a meta\nEm cada mês você economizou R${economia:.2f}, somando essas economias  ao longo dos {meses} meses, você acumulo o total de: R${acumulados:.2f}\n - Total de despesas mensais: R${total_despesas}\n - Total economizado por mês: R${economia} ')

