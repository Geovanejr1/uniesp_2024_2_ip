alturas = []
generos = []
total_masculino = 0
soma_alturas_masculino = 0
quantidade_feminino = 0


for i in range(15):
    altura = float(input(f"Pessoa {i+1} - Informe sua altura em metros: "))
    genero = input("Informe seu gênero (Masculino ou Feminino): ")
    
    
    alturas.append(altura)
    generos.append(genero)
    
    
    if genero == "Masculino":
        total_masculino += 1
        soma_alturas_masculino += altura
    elif genero == "Feminino":
        quantidade_feminino += 1


max_altura = max(alturas)
min_altura = min(alturas)
media_altura_masculino = soma_alturas_masculino / total_masculino if total_masculino > 0 else 0

print(f"Maior altura: {max_altura} metros")
print(f"Menor altura: {min_altura} metros")
print(f"Média de altura (Masculino): {media_altura_masculino:.2f} metros")
print(f"Número de mulheres: {quantidade_feminino}")