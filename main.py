import random
coin_flip = input("Heads or Tails? 🪙: ")
coin_flip_lower = coin_flip.lower()
heads_or_tails = random.randint(0, 1)
if coin_flip_lower == "Heads" or "Tails":
    if heads_or_tails < 1:
        print("It's tails!")
    elif heads_or_tails == 1:
        print("it's Heads!")



