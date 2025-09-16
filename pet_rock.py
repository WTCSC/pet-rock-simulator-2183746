print("Welcome to the Pet Rock Simulator!")
Name = input("What would you like to name your pet rock? ") 
rocky = 90
rockytwo = { 
    "age" : 10,
    "health" : 10,
    "hapiness" : 10
}
while rocky < 100:
    print(f"{Name} has the following stats:\n")
    print(f"Age: {rockytwo["age"]}/10")
    print(f"Health: {rockytwo["health"]}/10")
    print(f"Happiness: {rockytwo["hapiness"]}/10")
    rocky += 10
print("complete")
