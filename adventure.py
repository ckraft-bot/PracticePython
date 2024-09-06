# prompt user for name
name = input("What's your name ").lower() 
# greet user
print(f"Welcome {name} to this adventure!")  

# first prompt
answer = input(  
    "You are in an airport as a standby passenger, there are a couple of destinations you can reroute to from this airport. The options are: Tokyo or Nairobi. Which destination would you like to go to? ")  
  
# standardizing inputs by lower casing all responses  
answer = answer.lower()

# scenario 1
if answer == "tokyo":  
    answer = input(  
        "You go sightseeing at a temple, will you walk around it or run to the top (walk/run)? ")  
    if answer == "walk":  
        print("As you walk around you met other tourists and went out to dinner with them after.")  
    elif answer == "run":  
        print("You tripped while running now you're unable move and the trip will be cut short.")  
    else:  
        print('not a valid option. You lose.')  
# scenario 2
elif answer == "nairobi":  
    answer = input(  
        "You come to a safari at the Nairobi National Park. Do you want join a group tour or go alone (tour/alone)? ")  

    if answer == "tour":  
        print("You meet some new friends and wildlife photographers.")  
    elif answer == "alone":  
        answer = input(  
            "You get lost but you see a group of tourists from the distance. Do you talk to them (yes/no)? ")  

        if answer == "yes":  
            print("You talk to the strangers and they give you a ride back. You WIN!")  
        elif answer == "no":  
            print("You ignore the strangers and you lose because you're ignorant.")  
        else:  
            print('not a valid option. You lose.')  
    else:  
        print('not a valid option. You lose.')  

else:  
    print('not a valid option. You lose.')  
# exit greeting
print(f"Thank you for playing {name}!")    
