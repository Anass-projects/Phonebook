import subprocess
import pickle
import os
import sys



# Set base directory for data storage
if os.name == 'nt':
    base_dir = os.getenv('LOCALAPPDATA')
else:
    base_dir = os.path.expanduser('~')

# Set and create app-specific directory
app_dir = os.path.join(base_dir, "PhonebookApp")
if not os.path.exists(app_dir):
    os.makedirs(app_dir)

# Define absolute database path
file_path = os.path.join(app_dir, "phonebook.pkl")


def control():
    while True:
        progress = input("To continue type continue (or c).\n"
                         "To return to the main menu type abandon (or a)\n"
                         "Inserted value: ").strip().lower()

        if progress in ("abandon", "a"):
            return False
            
        elif progress in ("continue", "c"):
            print(" ") 
            return True
            
        else:
            print(" ")
            print("***********************************************************")
            print("ERROR: The inserted value is not in the domain, try again.")
            print("***********************************************************")
            print(" ")
            input("Press enter to proceed... ")
            print(" ")
            continue

def len_control(container):
    if len(container) == 0:
        print(" ")
        print("The phonebook is empty, please add a contact first.")
        input("Press enter to return to the main menu... ")
        print(" ")
        return False

def strip_control(value):
       if value.strip() == "":
            print("*****************************************************************")
            print("ERROR: The inserted name is not defined (empty space), try again.")
            print("*****************************************************************")
            print(" ")
            input("Press enter to proceed... ")
            return True



def phonebook():
    '''
    PHONEBOOK PROGRAM
    
    '''

    print("========================================")
    print("==== Welcome to your phonebook menu ====")
    print("========================================")
    print(" ")


    #The phonebook dictionary
    try: 
        with open(file_path, "rb") as file:
            phonebook = pickle.load(file)

    except FileNotFoundError:
        phonebook = dict()


    #Main while loop 
    while True:
        #clearing terminal
        subprocess.run('cls', shell=True)

        #Options menu
        digit = input("--------------- MAIN MENU ---------------\n"
                      "\n"
                      "To add a new contact dial 1.\n"
                      "To delete a contact dial 2.\n"
                      "To edit a contact dial 3.\n" 
                      "To search for a contact dial 4.\n"
                      "To save changes and exit dial 5.\n" 
                      "Inserted value: ").strip()
        print(" ")
        

        #Operable values control
        if digit in ("1", "2", "3", "4"):

            #Number add
            if digit == "1": 
                while True:
                    subprocess.run('cls', shell=True)
                    print("------------ ADD NEW CONTACT ------------\n")
                    print(" ")
                    if control() == False:
                        break
                    print(" ")
            
                    name = " ".join(input("Insert the contact's name: ").lower().split())
                    
                    if strip_control(name) == True:
                        continue
                    

                    surname = " ".join(input("Insert the contact's surname: ").lower().split())
                    name_key = (name, surname)

                    if name_key in phonebook:
                        print(" ")
                        print("This name already exists! You cannot overwrite an existing contact.")
                        input("Press enter to proceed...")
                        continue

                    else:
                        print(" ")
                        number = input(f"Insert the number for {name.title()} {surname.title()}: ").strip()
                        phonebook[name_key] = number
                        print(" ")
                        print("Contact was added successfully.")
                        input("Press enter to return to the main menu...")
                        break

            #Contact delete
            if digit == "2":
                while True:
                    subprocess.run('cls', shell=True)
                    
                    if len_control(phonebook) == False:
                        break

                    print("------------- DELETE CONTACT ------------\n")
                    print(" ")

                    if control() == False:
                        break

                    name = " ".join(input("Insert the contact's name: ").lower().split())
                    if strip_control(name) == True:
                        continue
                    surname = " ".join(input("Insert the contact's surname: ").lower().split())
                    name_key = (name, surname)
                    print(" ")

                    if name_key in phonebook:
                        print(f"ARE YOU SURE YOU WANT TO DELETE {name.title()} {surname.title()}?")
                        if control() == False:
                            break

                        phonebook.pop(name_key)
                        print(" ")
                        print(f"The contact: {name.title()} {surname.title()} was deleted successfully.")
                        input("Press enter to return to the main menu...")
                        break

                    else:
                        print("The given name does not exist, try again.")
                        input("Press enter to proceed...")
                        print(" ")
                        continue


            #Contact change
            if digit == "3":
                while True:
                    subprocess.run('cls', shell=True)

                    if len_control(phonebook) == False:
                        break

                    print("-------------- EDIT CONTACT -------------\n")
                    print(" ")

                    if control() == False:
                        break
                    
                    name = " ".join(input("Insert the contact's name: ").lower().split())
                    
                    if strip_control(name) == True:
                        continue

                    surname = " ".join(input("Insert the contact's surname: ").lower().split())
                    name_key = (name, surname)
                    print(" ")
                    if name_key in phonebook:
                        subprocess.run('cls', shell=True)
                        print("-------------- EDIT CONTACT -------------\n")
                        print(" ")

                        local_digit = input("To change the name insert 1.\n"
                                            "To change the number insert 2.\n"
                                            "To change the name and number insert 3.\n"
                                            "Inserted value: ").strip()

                        subprocess.run('cls', shell=True)
                        print("-------------- EDIT CONTACT -------------\n")
                        print(" ")
                        
                        if local_digit == "1":
                            new_name = " ".join(input("Type in the new name: ").lower().split())

                            if strip_control(new_name) == True:
                                continue

                            new_surname = " ".join(input("Type in the new surname: ").lower().split())
                            new_name_key = (new_name, new_surname)

                            #Checking for already existing contacts
                            if new_name_key in phonebook:
                                print(" ")
                                print("This name already exists! You cannot overwrite an existing contact.")
                                input("Press enter to proceed...")
                                print(" ")
                                continue
                            
                            phonebook[new_name_key] = phonebook[name_key]
                            phonebook.pop(name_key)
                            print(" ")
                            print("Contact was updated successfully.")
                            input("Press enter to return to the main menu...")
                            print(" ")
                            break

                        elif local_digit == "2":
                            new_number = input(f"Type in the new number for {name.title()} {surname.title()}: ").strip()
                            phonebook[name_key] = new_number
                            print(" ")
                            print("Contact was updated successfully.")
                            input("Press enter to return to the main menu...")
                            print("")
                            break

                        elif local_digit == "3":
                            new_name = " ".join(input("Type in the new name: ").lower().split())
                            if strip_control(new_name) == True:
                                continue

                            new_surname = " ".join(input("Type in the new surname: ").lower().split())
                            new_name_key = (new_name, new_surname)

                            #Checking for already existing contacts
                            if new_name_key in phonebook:
                                print(" ")
                                print("This name already exists! You cannot overwrite an existing contact.")
                                input("Press enter to proceed...")
                                print(" ")
                                continue

                            new_number = input(f"Type in the new number for {new_name.title()} {new_surname.title()}: ").strip()
                            phonebook[new_name_key] = new_number
                            phonebook.pop(name_key)
                            print(" ")
                            print("Contact was updated successfully.")
                            input("Press enter to return to the main menu...")
                            print(" ")
                            break
                        else:
                            print(" ")
                            print("***********************************************************")
                            print("ERROR: The inserted value is not in the domain, try again.")
                            print("***********************************************************")
                            print(" ")
                            input("Press enter to proceed...")
                            continue
                    else:
                        print(" ")
                        print("The given name does not exist, try again.")
                        input("Press enter to proceed...")
                        print(" ")
                        continue
                        

            #Contact Search
            if digit == "4":
                
                while True:
                    subprocess.run('cls', shell=True)

                    if len_control(phonebook) == False:
                        break

                    print("-------------- SEARCH MENU --------------\n")
                    print(" ")

                    if control() == False:
                        break
                    
                    local_digit = input("To search for a contact's number insert 1.\n"
                                        "To find the contact corresponding to a number insert 2.\n"
                                        "To display all contacts at once insert 3.\n"
                                        "Inserted value: ").strip()

                    subprocess.run('cls', shell=True)
                    print("-------------- SEARCH MENU --------------\n")
                    print(" ")
                    
                    if local_digit == "1":
                        name = " ".join(input("Insert the contact's name: ").lower().split())
                        if strip_control(name) == True:
                            continue

                        surname = " ".join(input("Insert the contact's surname: ").lower().split())
                        name_key = (name, surname)
                        if name_key in phonebook:
                            print(" ")
                            print(f"The number for {name.title()} {surname.title()} is === {phonebook[name_key]} ===.")
                            input("Press enter to return to the main menu...")
                            print(" ")
                            break
                        else:
                            print(" ")
                            print("The given name does not exist, try again.")
                            input("Press enter to proceed...")
                            print(" ")
                            continue

                    elif local_digit == "2":
                        number = input("Insert the contact's number: ").strip()
                        contact_found = False
                        for name_key in phonebook:
                            if phonebook[name_key] == number:
                                contact_found = True
                                print(f"--- A corresponding contact is {name_key[0].title()} {name_key[1].title()} ---")

                        if contact_found == False:
                            print(" ")
                            print("The given number does not exist, try again.")
                            input("Press enter to proceed...")
                            print(" ")
                            continue
                        else:
                            print(" ")
                            input("Press enter to return to the main menu...")
                            break

                    elif local_digit == "3":
                        counter = 0
                        for name_key in phonebook:
                            counter += 1
                            print(f"### {counter}. Name: {name_key[0].title()} {name_key[1].title()}, Number: {phonebook[name_key]} ###")
                            print(" ")
                        input("Press enter to return to the main menu...")
                        print(" ")
                        break

                    else:
                        print(" ")
                        print(" ")
                        print("***********************************************************")
                        print("ERROR: The inserted value is not in the domain, try again.")
                        print("***********************************************************")
                        print(" ")
                        input("Press enter to proceed...")
                        continue

                                                    
        #saving and leaving the function
        elif digit == "5":
            with open(file_path, "wb") as file:
                pickle.dump(phonebook, file)

            print(" ")
            print("Phonebook synced successfully...")

            print(" ")
            print("============================")
            print("===== Phonebook closed =====")
            print("============================")
            print(" ")
            input("Press enter to close the file...")
            break 

        #Confronting wrong value for digit     
        else:
            print(" ")
            print(" ")
            print("***********************************************************")
            print("ERROR: The inserted value is not in the domain, try again.")
            print("***********************************************************")
            print(" ")
            input("Press enter to proceed...")
            continue

if __name__ == "__main__":
    phonebook()