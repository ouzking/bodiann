import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")
with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()
    

class Gestion_Contact:
    
    def __init__(self):
        print("votre compte de budget est de:")

        
    def le_revenu(self):
        self.somme_revenu=float(input("donnez la somme obtenu de votre revenu:"))
        print(self.somme_revenu)
        return self.somme_revenu
    
    def la_depense(self): 
        somme_dépensé=float(input("donnez la somme dépensé de votre dépense:"))
        print(somme_dépensé) 
        if self.somme_revenu>somme_dépensé:
             self.somme_revenu=self.somme_revenu-somme_dépensé
             return self.somme_revenu
        else:
             print("votre solde est insuffissant")
             
    def affichageinfo(self):
        print("l'ecart qui existe entre les deux est:",self.somme_revenu)
        
compte=Gestion_Contact()
compte.le_revenu()
compte.la_depense()
compte.affichageinfo()