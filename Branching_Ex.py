years = 100
population = [0, 10]

for i in range(years):
    population.append(population[-1] + population[-2])

print(population)
