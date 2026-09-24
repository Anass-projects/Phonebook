import subprocess
import pickle
import os
import sys


#Check if we run .exe file or normal script
if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

#Creation the path for the pickle database
file_path = os.path.join(current_dir, "phonebook.pkl")


def control():
    while True:
        progress = input("To continue type continue (or c).\n"
                        "To return to the main menu type abandon (or a)\n"
                        "Inserted value: ").strip().lower()

        if progress in ("abandon", "a"):
            return False
            
        elif progress in ("continue", "c"): 
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


    

def phonebook():
    '''
    PHONEBOOK MENU PROGRAM
    RETURNS PHONEBOOK
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
        digit = input("------------------- MAIN MENU -------------------\n"
                      "To add a contact in your phonebook dial 1.\n"
                      "To change a contact in your phonebook dial 2.\n" 
                      "To search contacts dial 3.\n"
                      "To save the changes and leave the menu dial 4.\n" 
                      "Inserted value: ")
        print(" ")
        

        #Operateable values control
        if digit == "1" or digit == "2" or digit == "3":

            #Number add
            if digit == "1":
                while True:
                    subprocess.run('cls', shell=True)
                    if control() == False:
                        break
                    print(" ")
            
                    n_name_0 = input("Insert the contacts name: ").lower()
                    
                    if n_name_0.strip() == "":
                        print(" ")
                        print("*****************************************************************")
                        print("ERROR: The inserted name is not defined (empty space), try again.")
                        print("*****************************************************************")
                        print(" ")
                        input("Press enter to proceed... ")
                        continue

                    surname_0 = input("Insert the contacts surname: ").lower()
                    name = (n_name_0, surname_0)

                    if name in phonebook:
                        print(" ")
                        print("This name already exists, try again.")
                        input("Press a key to proceed... ")
                        print(" ")
                        continue
                    else:
                        number = input("Insert the persons number: ")
                        phonebook[name] = number
                        print(" ")
                        print("Contact was added successfully.")
                        input("Press enter to return to the main menu... ")
                        print(" ")
                        break

            #Contact change
            if digit == "2":
                while True:
                    subprocess.run('cls', shell=True)

                    if len(phonebook) == 0:
                        print(" ")
                        print("The phonebook is empty, please add a contact first.")
                        input("Press enter to return to the main menu... ")
                        print(" ")
                        break

                    if control() == False:
                        break
                    print(" ")
                    
                    n_name_1 = input("Insert the contacts name: ").lower()
                    
                    if n_name_1.strip() == "":
                        print(" ")
                        print("*****************************************************************")
                        print("ERROR: The inserted name is not defined (empty space), try again.")
                        print("*****************************************************************")
                        print(" ")
                        input("Press enter to proceed... ")
                        print(" ")
                        continue

                    surname_1= input("Insert the contacts surname: ").lower()
                    name = (n_name_1, surname_1)
                    print(" ")
                    if name in phonebook:
                        local_digit_0 = input("To change the name insert 1.\n"
                                            "To change the number insert 2.\n"
                                            "To change the name and number insert 3.\n"
                                            "Inserted value: ")
                        print(" ")
                        if local_digit_0 == "1":
                            n_name_2 = input("Type in the new name: ").lower()

                            if n_name_2.strip() == "":
                                print(" ")
                                print("*****************************************************************")
                                print("ERROR: The inserted name is not defined (empty space), try again.")
                                print("*****************************************************************")
                                print(" ")
                                input("Press enter to proceed... ")
                                continue

                            surname_2 = input("Type in the new surname: ").lower()
                            new_name = (n_name_2, surname_2)
                            phonebook[new_name] = phonebook[name]
                            phonebook.pop(name)
                            print(" ")
                            print("Contact was updated successfully.")
                            input("Press enter to return to the main menu... ")
                            print(" ")
                            break

                        elif local_digit_0 == "2":
                            new_number = input(f"Type in the new number for {n_name_1}: ")
                            phonebook[name] = new_number
                            print(" ")
                            print("Contact was updated successfully.")
                            input("Press enter to return to the main menu... ")
                            print("")
                            break

                        elif local_digit_0 == "3":
                            n_name_3 = input("Type in the new name: ").lower()
                            if n_name_3.strip() == "":
                                print(" ")
                                print("*****************************************************************")
                                print("ERROR: The inserted name is not defined (empty space), try again.")
                                print("*****************************************************************")
                                print(" ")
                                input("Press enter to proceed... ")
                                continue

                            surname_3 = input("Type in the new surname: ").lower()
                            new_name = (n_name_3, surname_3)
                            new_number = input(f"Type in the new number for {n_name_3}: ")
                            phonebook[new_name] = new_number
                            phonebook.pop(name)
                            print(" ")
                            print("Contact was updated successfully.")
                            input("Press enter to return to the main menu... ")
                            print(" ")
                            break
                        else:
                            print(" ")
                            print(" ")
                            print("***********************************************************")
                            print("ERROR: The inserted value is not in the domain, try again.")
                            print("***********************************************************")
                            print(" ")
                            input("Press enter to proceed... ")
                            continue
                    else:
                        print(" ")
                        print("The given name does not exist, try again.")
                        input("Press enter to proceed... ")
                        print(" ")
                        continue
                        

            #Contact Search
            if digit == "3":
                subprocess.run('cls', shell=True)

                while True:
                    if len(phonebook) == 0:
                        print(" ")
                        print("The phonebook is empty, please add a contact first.")
                        input("Press enter to return to the main menu... ")
                        print(" ")
                        break

                    if control() == False:
                        break
                    print(" ")
                    subprocess.run('cls', shell=True)
                    
                    local_digit_1 = input("To search a contacts number insert 1.\n"
                                            "To search the corresponding contacts to a certain number insert 2.\n"
                                            "To display all contacts at once insert 3.\n"
                                            "Inserted value: ")
                    print(" ")
                    if local_digit_1 == "1":
                        n_name_4 = input("Insert the contacts name: ").lower()
                        if n_name_4.strip() == "":
                            print(" ")
                            print("*****************************************************************")
                            print("ERROR: The inserted name is not defined (empty space), try again.")
                            print("*****************************************************************")
                            print(" ")
                            input("Press enter to proceed... ")
                            continue
                        surname_4 = input("Insert the contacts surname: ").lower()
                        name = (n_name_4, surname_4)
                        if name in phonebook:
                            print(" ")
                            print(f"The contacts number is === {phonebook[name]} ===.")
                            print(" ")
                            input("Press enter to return to the main menu... ")
                            print(" ")
                            break
                        else:
                            print(" ")
                            print("The given name does not exist, try again.")
                            print(" ")
                            input("Press enter to proceed... ")
                            print(" ")
                            continue
                    elif local_digit_1 == "2":
                        number = input("Insert the contacts number: ")
                        local_names = []
                        for name in phonebook:
                            if phonebook[name] == number:
                                local_names.append(name)
                                print(f"--- A corresponding contact is {name[0]} {name[1]} ---")

                        if len(local_names) == 0:
                            print(" ")
                            print("The given number does not exist, try again.")
                            print(" ")
                            input("Press enter to proceed... ")
                            print(" ")
                            continue
                        else:
                            print(" ")
                            input("Press enter to return to the main menu... ")
                            
                            break

                    elif local_digit_1 == "3":
                        counter = 0
                        for name in phonebook:
                            counter += 1
                            print(f"### {counter}. name: {name[0]} {name[1]}, number: {phonebook[name]} ###")
                            print(" ")
                        input("Press enter to return to the main menu... ")
                        print(" ")
                        break

                    else:
                        print(" ")
                        print(" ")
                        print("***********************************************************")
                        print("ERROR: The inserted value is not in the domain, try again.")
                        print("***********************************************************")
                        print(" ")
                        input("Press enter to proceed... ")
                        continue

                                                    
        #saving and leaving the function
        elif digit == "4":
            with open(file_path, "wb") as file:
                pickle.dump(phonebook, file)

            print(" ")
            print("Phonebook synced succesfully...")

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
            input("Press enter to proceed... ")
            continue

if __name__ == "__main__":
    phonebook()