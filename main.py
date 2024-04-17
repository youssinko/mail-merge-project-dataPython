#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as first:
    first_name = first.read()
    search_text = "[name]"
    second_search = "Angela"

with open("./Input/Names/invited_names.txt") as looping:
    names = looping.readlines()
    print(names)
    for x in names:
        new_name= x.replace('\n', '')
        new = first_name.replace(search_text, new_name)
        new_signature = new.replace(second_search, "Rania")
        print(new)
        with open(f"./Output/ReadyToSend/{new_name}", 'w') as data:
            data.write(new_signature)

