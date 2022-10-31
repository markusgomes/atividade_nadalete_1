
salario_fixo = float(input("\nInforme o valor do salário fixo:"))
vendas_efetuadas = float(input("\nInforme valor de vendas efetuadas:"))
soma_valor = salario_fixo + vendas_efetuadas
valor_base = 1500.0

if soma_valor > valor_base:
    vl1 = soma_valor - valor_base
    vl1 += vl1 * 0.07
    vl2 = (valor_base + (valor_base*0.05)) + vl1
    print(f'\nSalário final: R${vl2:.2f}')

else:
    soma_valor += soma_valor * 0.05
    print(f'\nSalário final: R${soma_valor:.2f}')

