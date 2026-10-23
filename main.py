
print("--- Geometry Calculator ---")
print("1. Squre")
print("2. Rectangle")


opcao = input("Choose a figure (1, 2): ")

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
  

else:
    print("Opção inválida!")
