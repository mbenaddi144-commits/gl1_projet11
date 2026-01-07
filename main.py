import random
import string

letters= string.ascii_letters

c=""
while c!="w":
    c=random.choice(letters)
    print(f"la lettre choisie est {c}")