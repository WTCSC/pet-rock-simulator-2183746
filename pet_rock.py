print("Welcome to the Pet Rock Simulator!")

Name = input("What would you like to name your pet rock? ") 
rocky = 90
rockytwo = { 
    "anger" : 6,
    "health" : 7,
    "happiness" : 2,
    "hunger" : 8,
    "anger(munchies)": 4,
    "health(munchies)": 7,
    "happiness(munchies)": 4,
    "hunger(munchies)": 10,
    "happiness(zen)": 6,
    "anger(zen)": 2,
    "hunger(zen)": 9,
    "health(zen)": 9,
}
playmate = {
    "anger" : 2,
    "hunger" : 10,
    "happiness" : 8,
    "health" : 9
}
food = {
    "anger" : 1,
    "hunger" : 10,
    "happiness" : 5,
    "health" : 8 
}
def num_input():
      while True:
            three = int(input("Your answer: "))
            if three not in (1,2,3,4):
                print("Thats not an option")
                continue
            else:
                  return three
            
while rocky < 100:
    print("Welcome to the Rock Orphanage!")
    print("We heard you wanted to adopt a new pet rock.")
    print(f"{Name} has the following stats:\n")
    print(f"Health: {rockytwo["health"]}/10")
    complete = input("Would you like to coninue the game? ")
    if complete == "yes" or complete == "continue the game" or complete == "continue":
        print(f"Awesome, {Name} is looking foward to meeting their new caretaker! ")
        print(f"Here are the rest of {Name}'s stats")
        print(f"Happiness: {rockytwo["happiness"]}/10")  
        print(f"Anger: {rockytwo["anger"]}/10")
        print(f"Hunger: {rockytwo["hunger"]}/10")
        print("What would you like to do?")
        print(f"1. Take {Name} to get food")
        print(f"2. Meditate with {Name}")
        print(f"3. Play with {Name}")
        three = num_input()
        if three == 1:
            print(f"{Name} is excited to go get food!.\n"
                     f"Happiness: {rockytwo["happiness(munchies)"]}/10.\n"
                     f"Anger: {rockytwo["anger(munchies)"]}/10.\n"
                     f"Hunger: {rockytwo["hunger(munchies)"]}/10.\n"
                     f"Health: {rockytwo["health(munchies)"]}/10.")
            print(f"Where would you like to take {Name}?\n"
                  "1. Mcdonalds\n"
                  "2. Chipotle\n"
                  "3. Your kitchen")
            four = num_input()
            if four == 1:
                    rocky += 101
                    print("Did you read your pet rock care pamphlet?!\n" 
                    f"{Name} has died because he to much proccessed unhealthy food:(")
                    print("Game over")
            elif four == 2:
                    print(f"Anger: {food["anger"]}/10\n"
                          f"Hunger: {food["hunger"]}/10\n"
                          f"Happiness: {food["happiness"]}/10\n"
                          f"Health: {food["health"]}/10")
                    print(f"{Name} is glad that you have decided to eat healthy\n"
                          f"What do you order for {Name}?\n"
                          "1. Burrito\n"
                          "2. Burrito Bowl\n"
                          "3. Tacos")
                    five = num_input()
                    if five == 1:
                          rocky +=101
                          print(f"{Name} died from becoming too fat")
                          print("Game over")
                    if five == 2: 
                          rocky +=101
                          print(f"Oops! {Name} filled his bowl up to much and collapsed from exahustion")
                          print("Game over")   
                    if  five == 3:
                          rocky +=101
                          print(f"{Name} became unhappy with his tacos and decided to go psycho on the chef. You disowned him.")
                          print("Game over")

            elif four == 3:
                    print(f"{Name}: OMG YAY your saving money and still feeding me!!!\n"
                          "Do you cook with what you have at home (1) or buy more groceries and risk going broke (2)?")
                    six = input("Your answer: ")
                    if six == "2":
                        rocky += 101
                        print(f"You went broke trying to feed {Name} and had to sell him:(")
                    elif six == "1":
                        rocky += 101
                        print(f"Unfortunantly {Name} got way too hungry on the way home and died of starvation!")

            rocky += 101
        elif three == 2:
                print(f"After participating in the program, {Name} feels very zen.\n"
                  f"Happiness: {rockytwo[ "happiness(zen)"]}/10.\n"
                  f"Anger: {rockytwo["anger(zen)"]}/10.\n"
                  f"Hunger: {rockytwo["hunger(zen)"]}/10.\n"
                  f"Health: {rockytwo["health(zen)"]}/10.")
                rocky += 101
        elif three == 3: 
                print(f"{Name} is so excited to play with you!\n"
                  f"Happiness: {playmate[ "happiness"]}/10.\n"
                  f"Anger: {playmate["anger"]}/10.\n"
                  f"Hunger: {playmate["hunger"]}/10.\n"
                  f"Health: {playmate["health"]}/10.")
                rocky += 101
else:
    rocky += 101
    print("You have quit the game")
print("End of game")
