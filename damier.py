
class Damier:

    def longueur(self,n=-1):
        while n <= 4 or n >= 31:
              n = int(input("Nombre de case en X :"))
              if n > 30:
                print("Valeur trop grande , mettez une valeur entre 5 et 30")
              if n < 5:
                print("Valeur trop petite , mettez une valeur entre 5 et 30")
        return n

    def largeur (self,p=-1):
        while p <= 4 or p >= 31:
              p = int(input("Nombre de case en Y :"))
              if p > 30:
                print("Valeur trop grande , mettez une valeur entre 5 et 30")
              if p < 5:
                print("Valeur trop petite , mettez une valeur entre 5 et 30")
        return p

    def nom(self,x=-1):
        x = input("Entrer le nom de la simulation : ")
        return x