print("Welcome to the Pet Rock Simulator!")
Name = input("What would you like to name your pet rock? ") 
rocky = 90
rockytwo = { 
    "anger" : 6,
    "health" : 7,
    "happiness" : 2,
    "hunger" : 8
}
while rocky < 100:
    print("Welcome to the Rock Orphanage!")
    print("We heard you wanted to adopt a new pet rock.")
    print(f"{Name} has the following stats:\n")
    print(f"Health: {rockytwo["health"]}/10")
    complete = input("Would you like to coninue the game? ")
    if complete == "yes" or complete == "continue the game" or complete == "continue":
       print(f"Awesome, {Name} is looking foward to meeting their new caretaker! ")
       two = input("Your first task to get to know your pet rock. Go ahead and ask the rock how it is feeling. ")
       if two =="How are you feeling?":
           print(f"Happiness: {rockytwo["happiness"]}/10")  
           print(f"Anger: {rockytwo["anger"]}/10")
           print(f"Hunger: {rockytwo["hunger"]}/10")
           three = input("What should you do?\n" 
           f"1. Take {Name} to get food\n"
           f"2. Meditate with {Name}\n"
           f"3. Play with {Name}")   
    else:
        rocky += 101
print("You have quit the game")
