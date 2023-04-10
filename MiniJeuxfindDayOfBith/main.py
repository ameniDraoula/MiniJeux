import tkinter
import tkinter.messagebox
import calendar
import tkinter as tk

def FindDayOfBirth():
    # Récupération des valeurs saisies par l'utilisateur
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())

    # Vérification que les valeurs saisies sont valides pour une date
    if  year < 1  or month < 1 or month > 12 or day < 1 or day > 31:
        tkinter.messagebox.showerror('Erreur de saisie', 'Veuillez saisir une date valide')
        return

    # Calcul du jour de la semaine correspondant à la date de naissance
    day_of_week = calendar.weekday(year, month, day)

    # Affichage du résultat
    days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
   
    tkinter.messagebox.showinfo('Résultat', f'Le jour de votre naissance était un {days[day_of_week]}')
    
        
window = tkinter.Tk()    # pour afficher l'interface on appel l'objet Tk de tkinter
window.title('Mini Jeux Find Day Of Birth')

# on utilise le gestionnaire d'emplacement .pack() pour afficher notre element de l'interface en block verticale
tkinter.Label(text=' Donner la date de naissance exact').pack()    

# création des entrées pour les variables year, month, et day
tkinter.Label(text=' Donner l année').pack() 
year_entry = tkinter.Entry()
year_entry.pack()

tkinter.Label(text=' Donner le mois').pack()
month_entry = tkinter.Entry()
month_entry.pack()

tkinter.Label(text=' Donner le jour').pack()
day_entry = tkinter.Entry()
day_entry.pack()

tkinter.Button(text='FindDayOfBirth', command=FindDayOfBirth).pack()
window.geometry("500x200")
window.mainloop()