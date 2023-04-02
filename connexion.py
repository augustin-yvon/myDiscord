import tkinter as tk
import mysql.connector
from password import verif_mdp

class Connexion:
    def __init__(self):
        pass

    def connexion(self, root, entry_mail, entry_mdp):
        mail = entry_mail.get()
        mdp = entry_mdp.get()
        test = 0
        for i in mail, mdp:
            if len(i) != 0:
                test += 1
        if test == 2:
            # Connexion à la base données
            db = mysql.connector.connect(user='root', password='Troll1394@@@@', host='localhost', database='discord')
            cursor = db.cursor()

            cursor.execute("select mdp from utilisateur where mail = '{}'".format(mail))
            
            # Récupération du résultat
            resultat = cursor.fetchone()[0]
            
            # Validation des changements
            db.commit()

            # Fermeture de la connexion
            cursor.close()
            db.close()
            if resultat and resultat == mdp:
                
                # Ferme la fenêtre
                root.destroy()

                # Création de la fenêtre principale
                main_page = tk.Tk()
                main_page.title("Chat")

                # Création de la page principale
                principal_frame = tk.Frame(main_page, bg="#36393F")
                principal_frame.pack(fill="both", expand=True)

                # Ajout des widgets à la page principale
                top_bar_frame = tk.Frame(principal_frame, bg="#2F3136", height=50)
                top_bar_frame.pack(side="top", fill="x")
                tk.Button(top_bar_frame, text="Vocale", bg="#2F3136", fg="white", font=("Arial", 12), bd=0, padx=20).pack(side="left", padx=20, pady=10)
                tk.Button(top_bar_frame, text="Changer de channel", bg="#2F3136", fg="white", font=("Arial", 12), bd=0, padx=20).pack(side="left", padx=20, pady=10)

                # Ajout du widget à la page principale
                tk.Button(top_bar_frame, text="Déconnexion", command = lambda:self.deconnexion(main_page), bg="#2F3136", fg="white", font=("Arial", 12), bd=0, padx=20).pack(side="right", padx=20, pady=10)

                messages_frame = tk.Frame(principal_frame, bg="#2C2F33")
                messages_frame.pack(fill="both", expand=True, padx=20, pady=20)
                scrollbar = tk.Scrollbar(messages_frame)
                scrollbar.pack(side="right", fill="y")
                messages_list = tk.Listbox(messages_frame, yscrollcommand=scrollbar.set, bg="#2C2F33", fg="white", font=("Arial", 12), bd=0, highlightthickness=0)
                messages_list.pack(side="left", fill="both", expand=True)
                scrollbar.config(command=messages_list.yview)

                send_button = tk.Button(principal_frame, text="Envoyer", bg="#7289DA", fg="white", font=("Arial", 12), bd=0, padx=20)
                send_button.pack(side="bottom", padx=20, pady=20)
                entry_message = tk.Entry(principal_frame, bg="#40444B", fg="white", font=("Arial", 12), bd=0)
                entry_message.pack(side="bottom", fill="x", padx=20, pady=0)

                main_page.mainloop()

            else:
                print("Adresse mail ou mot de passe incorrect")
        else:
            print("Un champ est vide")


    def deconnexion(self, main_page):
        # Ferme la fenêtre
        main_page.destroy()

        # Création de la fenêtre principale
        root = tk.Tk()
        root.title("Chat")

        # Création de la page de connexion
        connexion_frame = tk.Frame(root, bg="#2C2F33")
        connexion_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Ajout des widgets à la page de connexion
        tk.Label(connexion_frame, text="Adresse e-mail :", bg="#2C2F33", fg="#FFFFFF").grid(row=0, column=0, pady=10)
        tk.Label(connexion_frame, text="Mot de passe :", bg="#2C2F33", fg="#FFFFFF").grid(row=1, column=0, pady=10)

        entry_email = tk.Entry(connexion_frame, bg="#999")
        entry_email.grid(row=0, column=1, pady=10)

        entry_mdp = tk.Entry(connexion_frame, show="*", bg="#999")
        entry_mdp.grid(row=1, column=1, pady=10)

        tk.Button(connexion_frame, text="Connexion", command = lambda:self .connexion(root,entry_email, entry_mdp), bg="#7289DA", fg="#FFFFFF", activebackground="#677BC4", activeforeground="#FFFFFF", bd=0, pady=5).grid(row=2, column=0, columnspan=2, pady=20)
        tk.Button(connexion_frame, text="S'inscrire", command = lambda:self.inscription(root), bg="#7289DA", fg="#FFFFFF", activebackground="#677BC4", activeforeground="#FFFFFF", bd=0, pady=5).grid(row=3, column=0, columnspan=2)

        root.mainloop()


    def inscription(self, root):
        # Ferme la fenêtre
        root.destroy()

        # Création de la fenêtre principale
        sign_in = tk.Tk()
        sign_in.title("Chat")
        sign_in.geometry("233x248")

        # Création de la page principale
        principal_frame = tk.Frame(sign_in, bg="#2C2F33")
        principal_frame.pack(fill="both", expand=True)

        # Création de la page d'inscription
        inscription_frame = tk.Frame(principal_frame, bg="#2C2F33", bd=10)
        inscription_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Ajout des widgets à la page d'inscription
        tk.Label(inscription_frame, text="Inscription", font=("Helvetica", 20), bg="#2C2F33", fg='white').grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(inscription_frame, text="Nom :", bg="#2C2F33", fg='white').grid(row=1, column=0, pady=5)
        nom_entry = tk.Entry(inscription_frame, bg = '#999')
        nom_entry.grid(row=1, column=1, pady=5)

        tk.Label(inscription_frame, text="Prénom :", bg="#2C2F33", fg='white').grid(row=2, column=0, pady=5)
        prenom_entry = tk.Entry(inscription_frame, bg = '#999')
        prenom_entry.grid(row=2, column=1, pady=5)

        tk.Label(inscription_frame, text="Adresse e-mail :", bg="#2C2F33", fg='white').grid(row=3, column=0, pady=5)
        mail_entry = tk.Entry(inscription_frame, bg = '#999')
        mail_entry.grid(row=3, column=1, pady=5)

        tk.Label(inscription_frame, text="Mot de passe :", bg="#2C2F33", fg='white').grid(row=4, column=0, pady=5)
        mdp_entry = tk.Entry(inscription_frame, show="*", bg = '#999')
        mdp_entry.grid(row=4, column=1, pady=5)
        
        def s_incrire(sign_in):
            """Cette fonction enregistre les information utilisateur dans la base de données"""
            test = 0
            for i in [nom_entry.get(), prenom_entry.get(), mail_entry.get(), mdp_entry.get()]:
                if len(i) != 0:
                    test += 1
            if test == 4:
                mdp_verifié = verif_mdp(mdp_entry.get())
                if mdp_verifié == None:
                    if '@' in mail_entry.get():
                        # Connexion à la base données
                        db = mysql.connector.connect(user='root', password='Troll1394@@@@', host='localhost', database='discord')
                        cursor = db.cursor()
                        cursor.execute("insert into utilisateur (nom, prenom, mail, mdp) VALUES ('{}', '{}', '{}', '{}')".format(nom_entry.get(),prenom_entry.get(),mail_entry.get(),mdp_entry.get()))
                        
                        # Validation des changements
                        db.commit()
                        # Fermeture de la connexion
                        cursor.close()
                        db.close()
                    
                        sign_in.destroy()

                        # Création de la fenêtre principale
                        root = tk.Tk()
                        root.title("Chat")

                        # Création de la page de connexion
                        connexion_frame = tk.Frame(root, bg="#2C2F33")
                        connexion_frame.pack(fill="both", expand=True, padx=5, pady=5)

                        # Ajout des widgets à la page de connexion
                        tk.Label(connexion_frame, text="Adresse e-mail :", bg="#2C2F33", fg="#FFFFFF").grid(row=0, column=0, pady=10)
                        tk.Label(connexion_frame, text="Mot de passe :", bg="#2C2F33", fg="#FFFFFF").grid(row=1, column=0, pady=10)

                        entry_email = tk.Entry(connexion_frame, bg="#999")
                        entry_email.grid(row=0, column=1, pady=10)

                        entry_mdp = tk.Entry(connexion_frame, show="*", bg="#999")
                        entry_mdp.grid(row=1, column=1, pady=10)

                        tk.Button(connexion_frame, text="Connexion", command = lambda:self.connexion(root, entry_email, entry_mdp), bg="#7289DA", fg="#FFFFFF", activebackground="#677BC4", activeforeground="#FFFFFF", bd=0, pady=5).grid(row=2, column=0, columnspan=2, pady=20)
                        tk.Button(connexion_frame, text="S'inscrire", command = lambda:self.inscription(root), bg="#7289DA", fg="#FFFFFF", activebackground="#677BC4", activeforeground="#FFFFFF", bd=0, pady=5).grid(row=3, column=0, columnspan=2)

                        root.mainloop()
                    else:
                        print("Votre adresse n'est pas valide")
                else:
                    print(verif_mdp(mdp_entry.get()))
            else:
                print("Un champs est vide")

        tk.Button(inscription_frame, text="S'inscrire", bg="#7289DA", fg="white", font=("Arial", 12), bd=0, padx=20, command = lambda:s_incrire(sign_in)).grid(row=5, column=0, columnspan=2, pady=10)

        # Masquer la page principale
        principal_frame.tkraise()

        # Lancement de la fenêtre principale
        sign_in.mainloop()
