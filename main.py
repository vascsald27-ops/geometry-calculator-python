print("--- Geometry Calculator ---")
print("1. Squre")
print("2. Rectangle")
print("3. Trapezoid")


opcao = input("Choose a figure (1, 2 or 3): ")

if opcao == "1":
    lado = float(input("How much is each side? "))
    area = lado * lado
    perimetro = lado * 4
    print(f"Area: {area} | Perimeter: {perimetro}")

elif opcao == "2":
    comprimento = float(input("What is the length? "))
    largura = float(input("What is the width? "))
    area = comprimento * largura
    perimetro = 2 * (comprimento + largura)
    print(f"Area: {area} | Perimeter: {perimetro}")
  
elif opcao == "3":
    base_menor = float(input("What is the minor base? "))
    base_maior = float(input("What is the largest base? "))
    lado_1 = float(input("What is the lenght of side 1? " ))
    lado_2 = float(input("What is the lenght of side 2? " ))
    altura = float(input("What is the height? "))
    area = (1 / 2) * (base_menor +  base_maior) * altura
    perimetro = base_menor + base_maior + lado_1 + lado_2
    print(f"Area: {area} | Perimeter: {perimetro}")
else:
    print("Opção inválida!")
