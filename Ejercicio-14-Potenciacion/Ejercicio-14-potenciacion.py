if __name__ == "__main__":
    numero = float(input("Numero: "))

    cuadrado = Potenciacion.calcular_cuadrado(numero)
    cubo = Potenciacion.calcular_cubo(numero)

    print(f"El cuadrado de {round(numero)} es: {round(cuadrado)}")
    print(f"El cubo de {round(numero)} es: {round(cubo)}")