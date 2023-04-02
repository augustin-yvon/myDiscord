import tkinter as tk
from connexion import Connexion
from PIL import Image, ImageTk

# Création de la fenêtre principale
root = tk.Tk()
root.title("Discord")
root.config(bg="#2C2F33")

# Charger l'image PNG
icon_image = Image.open('logo_discord.png')
# Convertir l'image en un format approprié pour l'icône
icon = ImageTk.PhotoImage(icon_image)
# Ajouter l'icône à la fenêtre
root.iconphoto(True, icon)

# Création de la page de connexion
connexion_frame = tk.Frame(root, bg="#2C2F33")
connexion_frame.pack(fill="both", expand=True, padx=5, pady=5)

# Ajout des widgets à la page de connexion
tk.Label(connexion_frame, text="Adresse e-mail :", bg="#2C2F33", fg="#FFFFFF").grid(row=0, column=0, pady=10)

entry_email = tk.Entry(connexion_frame, bg="#999")
value_email = entry_email.get()
entry_email.grid(row=0, column=1, pady=10)

tk.Label(connexion_frame, text="Mot de passe :", bg="#2C2F33", fg="#FFFFFF").grid(row=1, column=0, pady=10)

entry_mdp = tk.Entry(connexion_frame, show="*", bg="#999")
value_mdp = entry_mdp.get()
entry_mdp.grid(row=1, column=1, pady=10)

cnx = Connexion()

tk.Button(connexion_frame, text="Connexion", command = lambda:connexion(root, entry_email, entry_mdp, cnx), bg="#7289DA", fg="#FFFFFF", activebackground="#677BC4", activeforeground="#FFFFFF", bd=0, pady=5).grid(row=2, column=0, columnspan=2, pady=20)
tk.Button(connexion_frame, text="S'inscrire", command = lambda:inscription(root), bg="#7289DA", fg="#FFFFFF", activebackground="#677BC4", activeforeground="#FFFFFF", bd=0, pady=5).grid(row=3, column=0, columnspan=2)

# Création des fonctions
def connexion(root, entry_email, entry_mdp, cnx):
    cnx.connexion(root, entry_email, entry_mdp)

def inscription(root):
    cnx.inscription(root)

# Lancement de la fenêtre principale
root.mainloop()