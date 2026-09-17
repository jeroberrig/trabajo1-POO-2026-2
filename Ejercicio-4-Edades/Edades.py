class Edades:
    @staticmethod
    def calcular_edalber(edjuan):
        return edjuan * 2 / 3

    @staticmethod
    def calcular_edana(edjuan):
        return edjuan * 4 / 3

    @staticmethod
    def calcular_edmama(edjuan, edana, edalber):
        return edjuan + edana + edalber

if __name__ == "__main__":
    edjuan = float(input("Ingrese la edad de Juan: "))

    edalber = Edades.calcular_edalber(edjuan)
    edana = Edades.calcular_edana(edjuan)
    edmama = Edades.calcular_edmama(edjuan, edana, edalber)

    print(f"La edad de Juan es: {edjuan}")
    print(f"La edad de Alberto es: {edalber}")
    print(f"La edad de Ana es: {edana}")
    print(f"La edad de la mamá es: {edmama}")