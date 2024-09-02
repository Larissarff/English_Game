import time

def medieval_scene():
    print("\n*** Medieval Scene: The Lost Knight's Enigma ***")
    time.sleep(1)
    print("You arrive at the village of Castlerock. The villagers tell you about Sir Aldric.")
    time.sleep(2)

    # Primeira pergunta
    print("Villager: 'Our knight, Sir Aldric, ___ a brave warrior. (is/was/be)'")
    answer = input("Your answer: ").strip().lower()

    if answer == "was":
        print("Correct! He was the strongest and kindest knight we had.")
        time.sleep(1)
        find_knight()
    else:
        print("Incorrect. Try again.")
        medieval_scene()

def find_knight():
    print("\nYou find Sir Aldric’s statue in the forest, trapped in his cursed armor.")
    time.sleep(2)
    print("Sir Aldric: 'I ___ cursed because I failed to protect the king. (am/was/is)'")
    answer = input("Your answer: ").strip().lower()

    if answer == "was":
        print("Correct! 'I was cursed by the sorceress Morgana.'")
        time.sleep(1)
        solve_mystery()
    else:
        print("Incorrect. Try again.")
        find_knight()

def solve_mystery():
    print("\nSir Aldric needs your help to recall important moments before his curse.")
    time.sleep(2)
    
    # Pergunta 1
    print("Sir Aldric: 'I ___ at the battlefield when the curse struck me. (am/was/were)'")
    answer = input("Your answer: ").strip().lower()
    
    if answer == "was":
        print("Correct!")
        time.sleep(1)
    else:
        print("Incorrect. Try again.")
        solve_mystery()
        return

    # Pergunta 2
    print("Sir Aldric: 'My men ___ brave, but they couldn’t fight the magic. (was/were/be)'")
    answer = input("Your answer: ").strip().lower()
    
    if answer == "were":
        print("Correct!")
        time.sleep(1)
        final_challenge()
    else:
        print("Incorrect. Try again.")
        solve_mystery()

def final_challenge():
    print("\nTo break the curse, choose the correct sentence:")
    time.sleep(2)
    print("Sir Aldric ___ the bravest knight of all. (was/is/be)")
    answer = input("Your answer: ").strip().lower()

    if answer == "was":
        print("The curse is broken! Sir Aldric’s spirit is freed.")
        print("Congratulations, you have successfully helped the knight.")
    else:
        print("Incorrect. Try again.")
        final_challenge()

# Inicia o cenário medieval
medieval_scene()
