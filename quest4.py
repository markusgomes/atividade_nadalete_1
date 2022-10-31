dig = None
dig_m = 0
cont = 0
seq = 0
seq_u = 0


for n in range(1, 21):
    entrada = int (input (f"\nInforme a entrada Nº{n}:"))

    if entrada == dig:
        cont += 1
        if (cont + 1) >= seq and dig_m < dig:
            seq = cont + 1
            dig_m = dig
            

    else:
        dig = entrada
        cont = 0

    
print (dig_m, seq, (cont+1))







    


