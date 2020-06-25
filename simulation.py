import time
class Simulation:

    def nbr_génération(self, nbr_generation=-1):
        while nbr_generation <= 0 or nbr_generation >= 11:
            nbr_generation = int(input("Nombre de génération:"))
            if nbr_generation > 10:
                print("Valeur trop grande , mettez une valeur entre 0 et 10")
            if nbr_generation < 0:
                print("Valeur trop petite , mettez une valeur entre 0 et 10")
        return nbr_generation




