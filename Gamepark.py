import pickle
animals_parkone = "park_One.pickle"
animals_parktwo = "park_Two.pickle"

try:
    with open(animals_parkone, "rb") as f:
        animalsinparkone = pickle.load(f)
        print("Loaded dictionary from file:", animalsinparkone)
except FileNotFoundError:
    animalsinparkone = {}
    print("Created new empty dictionary")

try:
    with open(animals_parktwo, "rb") as f:
        animalsinparktwo = pickle.load(f)
        print("Loaded dictionary from file:", animalsinparktwo)
except FileNotFoundError:
    animalsinparktwo = {}
    print("Created new empty dictionary")


while True:
    park_choice = input("Input data: Would you like to add an observation about Park 1 or Park 2 ? [1] or [2]\n a. Veiw the animals in park one [a]\n b. View the animals in park two [b]\n c. View the common animals between park one and two [c]\n d. View animals only seen in park one [d]\n e. View animalsonly seen in park two [e]\n f. Total number of animals in both parks [f]\n\nEnter your choice: " )
    if park_choice == "1":
        animalname = input("Please enter the animal name: ")
        numobserved = int(input("Please enter the number of this animal you observed: "))
        animalsinparkone[animalname] = numobserved
        print("Added",numobserved, animalname,"to the database")
        another = input("Do you want to enter another key-value pair? (y/n) ")
        if another.lower() != "y":
            break
        else:
            continue
    
    elif park_choice == "2":
        animalname = input("Please enter the animal name: ")
        numobserved = int(input("Please enter the number of this animal you observed: "))
        animalsinparktwo[animalname] = numobserved
        print("Added",numobserved, animalname,"to the database")
        another = input("Do you want to enter another key-value pair? (y/n) ")
        if another.lower() != "y":
            break
        else:
            continue
        
    elif park_choice.lower() == "a":
        total_sum_dict1 = 0
        for value in animalsinparkone.values():
            total_sum_dict1 += value
        print("The animals in park two are", animalsinparkone,f"and they add up to {total_sum_dict1} animals")
        
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
    
    elif park_choice.lower() == "b":
        total_sum_dict2 = 0
        for value in animalsinparktwo.values():
            total_sum_dict2 += value
        print("The animals in park two are", animalsinparktwo,f"and they add up to {total_sum_dict2} animals")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
    
    elif park_choice.lower() == "c":
        common_animals = set(animalsinparkone.keys()).intersection(animalsinparktwo.keys())
        print(f"The common animals between park one and two are {common_animals}")
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
        
    elif park_choice.lower() == "d":
        unique_animalsone = set(animalsinparkone.keys()) - set(animalsinparktwo.keys())
        unique_animalsone_list = list(unique_animalsone)
        unique_animalsone_separated = ','.join(unique_animalsone_list)
        print(f"The animals that are only seen in park one are {unique_animalsone_separated}")
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
        
    elif park_choice.lower() == "e":
        unique_animalstwo = set(animalsinparktwo.keys()) - set(animalsinparkone.keys())
        unique_animalstwo_list = list(unique_animalstwo)
        unique_animalstwo_separated = ','.join(unique_animalstwo_list)
        print(f"The animals that are only seen in park two are {unique_animalstwo_separated}")
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
    
    elif park_choice.lower() == "f":
        keys_dict1 = set(animalsinparkone.keys())
        keys_dict2 = set(animalsinparktwo.keys())
        unique_key_set = keys_dict1.union(keys_dict2)
        unique_keys_list = list(unique_key_set)
        unique_keys_separated = ', '.join(unique_keys_list)
        total_sum_dict1 = 0
        for value in animalsinparkone.values():
            total_sum_dict1 += value
            
        total_sum_dict2 = 0
        for value in animalsinparktwo.values():
            total_sum_dict2 += value
        
        Total_animals = total_sum_dict1 + total_sum_dict2
        print(f"The animals found in both park one and two are {unique_keys_separated}. Park one and Park two have a combined {Total_animals} animals")
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break

    
    
with open(animals_parkone, "wb") as f:
    pickle.dump(animalsinparkone, f)
    print("Saved dictionary to file:", animalsinparkone)


with open(animals_parktwo, "wb") as f:
    pickle.dump(animalsinparktwo, f)
    print("Saved dictionary to file:", animalsinparktwo)



    
        
            