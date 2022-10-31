
    #Maior sequência consecutiva de Nº constantes

dig = None
dig_m = 0
cont = 0
seq = 0
    
for n in range(1, 21):
    entrada = int (input (f"\nInforme a entrada Nº{n}:"))

    if entrada == dig:
        cont += 1
        if (cont + 1) >= seq:
            seq = cont + 1
            dig_m = dig
    else:
        dig = entrada
        cont = 0

print(f'\nA maior sequência consecutiva de números constantes: {seq} vezes. Sendo o Nº: {dig_m}.')







    


