def extphrases(texte):
    w = []
    A= ""
    for caractere in texte:
        A = A + caractere
        if caractere in ".!?":  
            w.append(A.strip()) 
            A = ""
    return w

def compte(texte):
    n = extphrases(texte)
    return len(n)

def occphrases(texte):
    phrases = extphrases(texte) 
    totalmots = 0
    for phrase in phrases:       
        mots = phrase.split()
        totalmots = totalmots + len(mots)
    if len(phrases) == 0:
        return 0
    return totalmots / len(phrases)

def ponctuationu(text):
    ponctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~"
    stat = {}
    for caractere in text:
        if caractere in ponctuations:
            if caractere in stat:
                stat[caractere] = stat[caractere] + 1
            else:
                stat[caractere] = 1
    return stat

def statistiquemot(text):
    mot = text.split()
    types = {"courts":0, "moyens":0, "longs":0}
    for m in mot:  # éviter de réutiliser le nom 'mot'
        motpropre = m.strip(".,!?;:\"'()[]{}")
        longueur = len(motpropre)
        if longueur <= 3:
            types["courts"] = types["courts"] + 1
        elif longueur <= 6:
            types["moyens"] = types["moyens"] + 1
        else:
            types["longs"] = types["longs"] + 1
    return types


with open("fichier.txt", "r") as f:
    texte = f.read()

phrases = extphrases(texte)
print("Liste de phrases ", phrases)
print("Nombre de phrases ", compte(texte))
print("Longueur moyenne des phrases en mots :", occphrases(texte))
print("Ponctuation utilisee ", ponctuationu(texte))
print("Statistiques type mot ", statistiquemot(texte))
