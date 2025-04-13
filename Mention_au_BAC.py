moyenne = float(input("Entrez votre moyenne au BAC : "))

if moyenne >= 12 and moyenne < 14 :
    print("Assez bien")
elif moyenne >= 14 and moyenne < 16 :
    print("Bien")
elif moyenne >= 16 and moyenne < 18 :
    print("Très bien")
elif moyenne >= 18 and moyenne < 20 :
    print("Les félicitations du jury")
elif moyenne > 20 :
    print("Ce n'est pas possible")
elif moyenne < 0 :
    print("you are very very very dumb...")
else :
    print("Pas de mention")