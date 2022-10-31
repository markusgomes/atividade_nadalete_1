    
    # quantos anos pop_a >= pop_b

pop_a = 15000 # crescimento 10%/a
pop_b = 45000 # crescimento 5%/a
anos = 0

while pop_a < pop_b:
    pop_a += int(pop_a * 0.10)
    pop_b += int(pop_b * 0.05)
    anos += 1
print(f'\nPopulação do país A igualará ou ultrapassará do país B em: {anos} ano(s).')


    # quantos anos pop_a + 23% > pop_c

pop_a = 15000 # crescimento 10%/a
pop_c = 65000 # crescimento 2,5%/a
anos = 0

while (pop_c+(pop_a*0.23)) > pop_a:
    pop_a += int (pop_a * 0.10)
    pop_c += int (pop_c * 0.025)
    anos += 1
print(f'\nPopulação do país A ultrapassará em 23% do país C em: {anos} ano(s).')