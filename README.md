Ce projet contient un script Python simple qui génère des lettres de l'alphabet de manière aléatoire jusqu'à ce qu'il tombe sur une lettre spécifique (le "w").

📋 Description
Le script utilise les modules standards de Python pour effectuer une boucle de sélection aléatoire. Il illustre les concepts suivants :

L'utilisation de la bibliothèque random.

La manipulation des chaînes de caractères avec string.

L'utilisation d'une boucle while.

Le formatage de chaînes de caractères (f-strings).

🚀 Utilisation
Prérequis
Python 3.x installé sur votre machine.

Installation
Clonez ce dépôt :

Bash

git clone https://github.com/votre-utilisateur/nom-du-projet.git
Accédez au dossier :

Bash

cd nom-du-projet
Exécution
Lancez le script avec la commande suivante :

Bash

python nom_du_fichier.py
🔍 Explication du Code
Le fonctionnement du code est détaillé ci-dessous :

Python

import random
import string

# On récupère toutes les lettres (majuscules et minuscules)
lettres = string.ascii_letters
c = ""

# Tant que la lettre choisie n'est pas "w", on continue
while c != "w":
    c = random.choice(lettres) # Sélection aléatoire
    print(f"la lettre choisie est {c}")
string.ascii_letters : Contient abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.

random.choice() : Sélectionne un élément au hasard dans la liste des lettres.

Boucle while : Le script s'arrête immédiatement dès que la variable c prend la valeur "w".