# halloween.py

# Oändlig loop för att användaren ska kunna testa flera karaktärer
while True:
    # Fråga användaren om deras favorit-Halloween-karaktär
    karaktar = input("Vilken är din favorit-Halloween-karaktär? (vampyr, zombie, spöke, varulv, eller skriv 'avsluta' för att avsluta): ").lower()

    # Kontrollera om användaren vill avsluta
    if karaktar == "avsluta":
        print("Tack för att du spelade! Ha en spöklik Halloween! 🎃")
        break

    # Ge ett svar baserat på användarens val
    if karaktar == "vampyr":
        print("Blod är livet! 🧛‍♂️")
    elif karaktar == "zombie":
        print("Hjärnor... hjärnor... 🧟")
    elif karaktar == "spöke":
        print("Buuuu! 👻")
    elif karaktar == "varulv":
        print("Awooo! 🐺")
    else:
        print("Det låter som en spännande karaktär!")
