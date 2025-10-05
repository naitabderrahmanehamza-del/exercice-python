# exo 20 : list

adressesip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

# 1):
print("question 1 est", adressesip[0])

# 2):
print("question2 est", adressesip[-1])

# 3):
print("question 3 est", adressesip[2])

# 4):
adressesip.append("172.31.0.1")
print("question4 est", adressesip)

# 5),
adressesip.remove("200.100.50.1")
print("question 5  est", adressesip)

# 6):
print("question 6  est", len(adressesip))

# 7):
print("question ;7 est", "192.168.0.1" in adressesip)

# 8):
print("question 8; est : classe A (car commence par 10)")

# 9):
adressesip.sort()
print("question 9  est", adressesip)

# 10):
toutes_C = True
for ip in adressesip:
    if not ip.startswith("192.168."):
        toutes_C = False
print("question 10 est", toutes_C)

# 11):
publiques = 0
for ip in adressesip:
    if not (ip.startswith("10.") or ip.startswith("172.") or ip.startswith("192.168.") or ip.startswith("169.254.")):
        publiques += 1
print("question 11 est", publiques)
