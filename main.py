# Jackson Hauley, Gavin Pierce, Lizzy Saldana, Luke Murdock

password = ("MusicFestival1234")
password_attepmt = 3

loop_num=10

num_of_preformences=(15)

import random
import time

# Initializing Variables
artist_list = []
admin = False

# Artist name, insturment, genre, time
performances = [
    ["Zack Mills", "Guitar", "Country", "11:00am Jan 20th 2025"],
    ["Lena Brooks", "Piano", "Jazz", "2:00pm Jan 20th 2025"],
    ["Evan Matthews", "Drums", "Rock", "4:30pm Jan 20th 2025"],
    ["Sophia Reyes", "Violin", "Classical", "6:00pm Jan 20th 2025"],
    ["James Carter", "Saxophone", "Blues", "8:00pm Jan 20th 2025"],
    ["Tina Williams", "Vocals", "Pop", "10:00am Jan 21st 2025"],
    ["Oliver Grant", "Guitar", "Folk", "12:00pm Jan 21st 2025"],
    ["Chloe Anderson", "Cello", "Chamber Music", "3:00pm Jan 21st 2025"],
    ["Noah Fisher", "Trumpet", "Big Band", "5:30pm Jan 21st 2025"],
    ["Emily Stone", "Clarinet", "Contemporary", "7:30pm Jan 21st 2025"]
]

# Jacksons Variables
tickets = []
id = 0
female_ratio = 0
male_ratio = 0
tickets_bought = 0
total_money = 0
memberships_bought = []
durations_bought = []
age_list = []

# Defining Funcitons

def main(admin,id,performances): # Main function for running things
    if admin == True: 
        user = "Admin" # Changes name based on admin or not
    else: 
        user = "User"
    while True:
        cs()
        choice = int_input(f"""
███╗   ███╗██╗   ██╗███████╗██╗ ██████╗    ███████╗███████╗███████╗████████╗██╗██╗   ██╗ █████╗ ██╗     
████╗ ████║██║   ██║██╔════╝██║██╔════╝    ██╔════╝██╔════╝██╔════╝╚══██╔══╝██║██║   ██║██╔══██╗██║     
██╔████╔██║██║   ██║███████╗██║██║         █████╗  █████╗  ███████╗   ██║   ██║██║   ██║███████║██║     
██║╚██╔╝██║██║   ██║╚════██║██║██║         ██╔══╝  ██╔══╝  ╚════██║   ██║   ██║╚██╗ ██╔╝██╔══██║██║     
██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗    ██║     ███████╗███████║   ██║   ██║ ╚████╔╝ ██║  ██║███████╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝
                           \nWelcome {user}\n\n1. Information\n2. Tickets\n3. Schedule\n4. Artists\n5. Recommendation\n6. Venues\n7. Admin Login\n8. Exit\n\nChoose one (1-8): """)
        if choice == 1: # Information
            information()
        elif choice == 2: # Tickets
            ticket_main(admin,id,performances)
        elif choice == 3: # Schedule
            schedule_main(admin,performances)
        elif choice == 4: # Artist List
            artist_main(admin)
        elif choice == 5: # Recommendation
            recommendation()
        elif choice == 6: # Venues
            venue_main_checker(admin)
        elif choice == 7: # Switch to administrator
            admin_check(admin,id,performances)
        elif choice == 8: # Exit
            cs()
            print('Thanks for attending!')
            exit()

def information():
    cs()
    print("""
Welcome to our music festival!
          
We have daily performances ranging from 7:00am to 10:00pm

Our music shows have a variety of different genres, from pop to rock!
          
Music Festival Directors:
          
Jackson Hauley
Gavin Pierce
Luke Murdock
Nicole Saldana""")# Displays information about festival
    input("\nPress enter to continue")
    main(admin,id,performances)

def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError:
            print("Invalid Input! (only integers accepted)") # Invalid Input Text
            input("Press enter to try again")
            continue
        return output
    
def str_input(text): # Only takes in string
    while True:
        try: output = str(input(text))
        except ValueError:
            print("String Input! (only strings accepted)") # Invalid Input Text
            input("Press enter to try again")
            continue
        return output
    
def float_input(text): # Only takes in floats
    while True:
        try: output = float(input(text))
        except ValueError:
            print("Invalid Input! (only floats accepted)") # Invalid Input Text
            input("Press enter to try again")
            continue
        return output

def cs(): # Clear Screen
    print("\033c",end="")

def recommendation(): 
    cs()
    recommendation_search = input("What genre/artists do you like the best? (exact): ")
    for x in range(len(performances)):
        for i in performances[x]:
            if str(i) == recommendation_search:
                print(f"Name: {performances[x][0]}   Insturment: {performances[x][1]}   Genre: {performances[x][2]}   Time: {performances[x][3]}")
    input("Press enter to continue")


def ticket_main(admin,id,performances): # Ticket main function (runs all ticket information through here) (jacksons function)
    if admin == True:
        while True:
            cs()
            choice = int_input("TICKET MENU\n\n1. Search Tickets\n2. Ticket Information\n3. Ticket Report\n4. Generate Random People\n5. Exit\n\nChoose one (1-5): ")
            if choice == 1: # Search Tickets
                search_tickets()
            elif choice == 2: # Ticket Informatoin
                ticket_information()
            elif choice == 3: # exit
                ticket_report()
            elif choice == 4: # Random People Generator
                id = gen_rand_ticket(age_list,total_money,tickets_bought,male_ratio,female_ratio,id)
            elif choice == 5: # Random People Generator
                main(admin,id,performances)
            else:
                input('Invalid Input!\nPress enter to continue')
    else:
        while True:
            cs()
            choice = int_input("TICKET MENU\n\n1. Buy Ticket\n2. Ticket Information\n3. Exit\n\nChoose one (1-3): ")
            if choice == 1: # Buy Ticket
                id = buy_ticket(total_money,tickets_bought,male_ratio,female_ratio,id)
            elif choice == 2: # Ticket Information
                ticket_information()
            elif choice == 3: # Exit
                main(admin,id,performances)

def gen_rand_ticket(age_list,total_money,tickets_bought,male_ratio,female_ratio,id): # Random Ticket Generator
    cs()
    amount = int_input("How many tickets do you want to generate?: ")
    print()
    for x in range(amount):
        firstname = random.choice(["Jackson","Gavin","Nicole","Luke","Lizzy","Hauley","Saldana","Murdock","Pierce","Lincoln","Haggard","Eli","Cooper","Owen","Bowerbank","Powerbank","LaRose","Alec","George","Busby","RealHumanFirstName001"])
        lastname = random.choice(["Jackson","Gavin","Nicole","Luke","Lizzy","Hauley","Saldana","Murdock","Pierce","Lincoln","Haggard","Eli","Cooper","Owen","Bowerbank","Powerbank","LaRose","Alec","George","Busby","RealHumanLastName002"])
        age = random.choice(list(range(1,120)))
        age_list.append(age)
        membership = random.choice(["NPC","VIP","MVP"])
        duration = random.choice(["1 Day","3 Day","1 Week","1 Month","Season Pass"])
        cost = getcost(membership,duration)
        total_money += cost
        tickets_bought += 1
        id += 1
        creditcard = random.randint(1000000000000000,9999999999999999) # Random Credit Card
        cvv = random.randint(100,999)
        ticket_time = time.ctime()
        gender = random.choice(["Male","Female"])
        if gender == "Male": # Changing ratio
            male_ratio += 1
        else:
            female_ratio += 1
        ticketlist = [firstname,lastname,age,membership,duration,cost,id,creditcard,cvv,ticket_time,gender]
        tickets.append(ticketlist) # First, Last, Age, Member, Duration, Cost, ID, CC, CVV, TIME, gender
        print(f"Ticket Created! [ID: {id}]")
    input("\nFINISHED GENERATING\nPress enter to continue")
    return id

def search_tickets(): # Search tickets 
    cs()
    print("Search All Tickets")
    search_keyword = input("Enter any keyword or ID to try and find a ticket (case sensitive): ") # First, Last, Age, Member, Duration, Cost, ID, CC, CVV, TIME,gender
    print()
    for x in range(len(tickets)):
        for i in tickets[x]:
            if str(i) == search_keyword:
                print(f"Name: {tickets[x][0]} {tickets[x][1]}   ID: {tickets[x][6]}")
    search_ID = int_input("\nWhich ticket do you want to open? (ID) (type 0 to exit): ")
    print()
    for x in range(len(tickets)):
        if tickets[x][6] == search_ID:
            if tickets[x][10] == "Male":
                print(f"""
    ██████████████████████████████████████████████████████
    █   WMWMW   █ Name: {tickets[x][0]} {tickets[x][1]}
    █  /     \\  █ Age: {tickets[x][2]} Gender: {tickets[x][10]}                 
    █  |O   O|  █ Membership Level: {tickets[x][3]}   
    █  |  L  |  █ Date Bought: {tickets[x][9]}  
    █   \ U /   █ Duration: {tickets[x][4]}         
    █    | |    █ ID: {tickets[x][6]}                     
    ██████████████████████████████████████████████████████""") # Printing out their ticket
            else:
                print(f"""
    ██████████████████████████████████████████████████████
    █   WMWMW   █ Name: {tickets[x][0]} {tickets[x][1]}
    █  W     W  █ Age: {tickets[x][2]} Gender: {tickets[x][10]}                 
    █ W|O   O|W █ Membership Level: {tickets[x][3]}   
    █ M|  L  |M █ Date Bought: {tickets[x][9]}  
    █   \ U /   █ Duration: {tickets[x][4]}         
    █    | |    █ ID: {tickets[x][6]}                     
    ██████████████████████████████████████████████████████""") # Printing out their ticket
            print(f"\nCost: ${tickets[x][5]}")
            print(f"Credit Card: {tickets[x][7]}")
            print(f"CVV: {tickets[x][8]}")
            input("Press enter to continue")
            break

def getcost(membership,duration):
    if membership == "NPC":
        cost = 19.99
    elif membership == "VIP":
        cost = 49.99
    elif membership == "MVP":
        cost = 99.99
    if duration == "1 Day": 
        cost += 0
    elif duration == "3 Days":
        cost += 40
    elif duration == "1 Week":
        cost += 80
    elif duration == "1 Month":
        cost += 120
    elif duration == "Season Pass":
        cost += 300
    return cost

def ticket_report(): # Ticket report 
    cs()
    total_ratio = male_ratio + female_ratio # Calculates percentage of female/male people who bought tickets
    if total_ratio != 0:
        male_percentage = (male_ratio / total_ratio) # Handling dividing by 0
        female_percentage = (female_ratio / total_ratio)
    if total_ratio == 0:
        male_percentage = 0
        female_percentage = 0
    print(f"""
TICKET REPORT (excludes generated tickets)
          
Total tickets bought: {tickets_bought}

Genders:
{male_percentage:.2%} Male
{female_percentage:.2%} Female

Total Money Earned: ${total_money}

Memberships Bought:
NPC: {memberships_bought.count("NPC")}
VIP: {memberships_bought.count("VIP")}
MVP: {memberships_bought.count("MVP")}

Durations Bought:
1 Day: {durations_bought.count("1 Day")}
3 Days: {durations_bought.count("3 Day")}
1 Week: {durations_bought.count("1 Week")}
1 Month: {durations_bought.count("1 Month")}
Season Pass: {durations_bought.count("Season Pass")}

          """)   # The report is being worked on
    if len(age_list) != 0:
        print(f"Average Age: {round(sum(age_list)/len(age_list),2)}")
    input('\nPress enter to continue')


def buy_ticket(total_money,tickets_bought,male_ratio,female_ratio,id): # Buy a ticket (Jacksons Function)
    ticket = []
    cs()
    print("Buying Ticket\n") # Visual
    firstname = input("What is your first name?: ") # Name Input
    if firstname == "":
        print("Thats not a name, so your new name is 'Blank'")
        firstname = "Blank"
    lastname = input("What is your last name?: ")
    age = int_input("How old are you?: ") # Age Selection
    if 120 < age or age < 0:
        randage = random.randint(1,random.randint(10,random.randint(11,18)))
        print(f"\nBro there is no way your that age, I bet your {randage}") # Dissing on people who are joking around
        age = randage
    while True:
        gender_choice = input("Male or Female? (m/f): ") # chooses gender
        if gender_choice.lower()  == "m":
            gender = "Male"
            break
        elif gender_choice.lower() == "f":
            gender = "Female"
            break
        else:
            print("Invalid Input (m/f)")
            input("Press enter to continue")
    while True:
        membership_choice = int_input("\nWhat membership level do you want to buy?\n1. NPC ($19.99)\n2. VIP ($49.99)\n3. MVP ($99.99)\n\nType number here (1-3): ") # Membership Level Selection
        if membership_choice == 1:
            membership = 'NPC' # NPC membership setting
            break
        elif membership_choice == 2:
            membership = 'VIP' # VIP membership setting
            break
        elif membership_choice == 3:
            membership = 'MVP' # MVP membership setting
            break
        else:
            print("Invalid Input (1-3)")
            input("Press enter to continue")
    while True:
        duration_choice = int_input("\nHow long do you want this ticket to work?\n1. 1 day (+$0.00)\n2. 3 days (+$40.00)\n3. 1 week (+$80.00)\n4. 1 month (+$120.00)\n5. Season pass (+$300.00)\n\nType number here (1-5): ") # Duration Selection
        if duration_choice == 1: # These are for how long your ticket works
            duration = "1 Day" # 1 day duration
            break
        elif duration_choice == 2:
            duration = "3 Days" # 3 days duration
            break
        elif duration_choice == 3:
            duration = "1 Week" # 1 week duration
            break
        elif duration_choice == 4:
            duration = "1 Month"  # 1 month duration
            break
        elif duration_choice == 5:
            duration = "Season Pass" # season pass
            break
        else:
            print("Invalid Input (1-5)") # Error Handling
            input("Press enter to continue")

    print(f"\nMembership {membership} selected") # Visual
    print(f"This ticket will last {duration}!")
    print(f"Cost: ${getcost(membership,duration)}")
    cost = getcost(membership,duration)
    quick_choice1 = input("\nType yes to confirm, anything else will cancel: ") # Confirming Information
    if quick_choice1.lower() == "yes":
        cs()
        print(f"Buying {membership} ticket") # Buying Ticket
        creditcard = int_input("Enter credit card number, with no spaces (1234123412341234): ") # Getting money
        cvv = int_input("Enter CVV number, with no spaces (123): ")
        quick_choice2 = input("\nType yes to confirm, anything else will cancel: ") # Confirming Information
        if quick_choice2 == "yes":
            print("\nTicket Bought!\n")
            total_money += cost # All these variables are updating stuff for the report
            tickets_bought += 1
            memberships_bought.append(membership)
            if gender == "Male":
                male_ratio += 1
            else:
                female_ratio += 1
            age_list.append(age)
            durations_bought.append(duration)
            id += 1
            print(f"Ticket ID: {id}")
            ticket_time = time.ctime()
            if gender == "Male":
                print(f"""
    ██████████████████████████████████████████████████████
    █   WMWMW   █ Name: {firstname} {lastname}
    █  /     \\  █ Age: {age} Gender: {gender}             
    █  |O   O|  █ Membership Level: {membership}   
    █  |  L  |  █ Date Bought: {ticket_time}  
    █   \ W /   █ Duration: {duration}         
    █    | |    █ ID: {id}                     
    ██████████████████████████████████████████████████████""") # Printing out their ticket
            else:
                print(f"""
    ██████████████████████████████████████████████████████
    █   WMWMW   █ Name: {firstname} {lastname}
    █  W     W  █ Age: {age} Gender: {gender}                 
    █ W|O   O|W █ Membership Level: {membership}  
    █ M|  L  |M █ Date Bought: {ticket_time}  
    █   \ U /   █ Duration: {duration}         
    █    | |    █ ID: {id}                     
    ██████████████████████████████████████████████████████""") # Printing out their ticket
            input("\nPress enter to continue")
            ticketlist = [firstname,lastname,age,membership,duration,cost,id,creditcard,cvv,ticket_time,gender]
            tickets.append(ticketlist) # First, Last, Age, Member, Duration, Cost, ID, CC, CVV, TIME, gender
        else:
            print("Ticket Canceled!")
            input("Press enter to continue")
    else:
        print("Ticket Canceled!")
        input("Press enter to continue")
    return id
    
    
def ticket_information(): # Prints out ticket information (anyone change this if you want and its a good idea no stupid stuff)
    cs()
    print(f"""
TICKET INFORMATION

Membership Levels:
    NPC ($19.99)
The most basic pass, provides you with all concerts/artist shows in public seating
    VIP ($49.99)
The 2nd best pass, gives you a special fast lane in all lines and VIP seating zone, plus you get to meet an artist
    MVP ($99.99)
THE BEST pass you can buy, gives extremely fast lines and 50% off everything in the convention, meet all artists/performers and free merch + candy + 1 meal/day
          
Duration Levels:
    1 Day: 1 day in the convention from 7:00am to 10:00pm
    3 Day: 3 days in the convention from 7:00am to 10:00pm (2 overnights)
    1 Week: 7 days in the convention from 7:00am to 10:00pm (6 overnights)
    1 Month: 30 days in the convention from 7:00am to 10:00pm (29 overnights)
    Season Pass: Full season access to the convention any time, 1 free meal a day (stackable with MVP)

Your information is kept in a secure online server with {random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(1,10000000000),10000000000),10000000000),10000000000),10000000000),10000000000),10000000000),10000000000),10000000000)} firewalls protecting it RIGHT NOW
          """)   
    input('Press enter to continue')


        




# Luke's Functions
def artist_main(admin): # Brings the user to the admin main or the non-admin main
    if admin == False:
        artist_nonadmin_main()
    elif admin == True:
        artist_admin_main()

def artist_nonadmin_main():
    while True:
        cs()
        choice = int_input("\nArtist List\n\n1. Display\n2. Search\n3. Exit\n\nChoose one (1-3): ")
        if choice == 1:
            artist_display()
        elif choice == 2:
            search_artist()
        elif choice == 3:
            main(admin,id,performances)
        else:
            print("Not in Range\nPress enter to continue")
            input()

def artist_admin_main(): # Lets the user choose how they want to manipulate the artist list.
    while True:
        cs()
        choice = int_input("\nArtist List Management\n\n1. Display\n2. Search\n3. Add\n4. Remove\n5. Edit\n6. Exit\n\nChoose one (1-6): ")
        if choice == 1:
            artist_display()
        elif choice == 2:
            search_artist()
        elif choice == 3:
            add_artist()
        elif choice == 4:
            remove_artist()
        elif choice == 5:
            edit_artist()
        elif choice == 6:
            main(admin,id,performances)
        else:
            print("Not in Range\nPress enter to continue")
            input()

def artist_display(): # Displays the artist list
    print("Displaying Artists:\n")
    if artist_list == []:
        print("Nothing In List\n")
    for artist in artist_list:
        print(f"Artist:\n Name- {artist[0]}\n Genre- {artist[1]}\n Time- {artist[2]}\n")
    input("Press enter to continue\n")

def search_artist(): # It shows results of the word used to search through the artist list.
    artist_results = []
    print("Searching For An Artist")
    artist_search = str_input("Search for the artist through their name, genre, or time:\n").upper()
    for artist in artist_list:
        for fact in artist:
            if artist_search in str(fact).upper():
                artist_results.append(artist)
                break
            
    print(f"Results: {'None Found' if artist_results == [] else ''}\n")
    for artist in artist_results:
        print(f"Artist:\n Name- {artist[0]}\n Genre- {artist[1]}\n Time- {artist[2]}\n")
    input("Press enter to continue\n")

def add_artist(): # Lets the user add an artist and their information to the list.
    print("Adding An Artist")
    artist_name = str_input("What is the artist's name?: ")
    artist_genre = str_input("What is the artist's genre?: ")
    artist_time = int_input("What is the artist's time duration in minutes?: ")
    artist_list.append([artist_name, artist_genre, artist_time])
    input("Press enter to continue")

def remove_artist(): # Removes the inputted artist from the list
    removed = 0
    print("Removing An Artist")
    artist_name = str_input("What is the artist's name?: ")

    for artist in artist_list.copy(): 
        if artist_name.title() == artist[0].title():
            artist_list.remove(artist)
            removed = 1
    if removed == 0:
        print("Not in List\nPress enter to continue")
        input()

def edit_artist(): # Edits the specified information to the inputted information from a specific artist
    edited = 0
    print("Editing An Artist")
    artist_name = str_input("What is the artist's name?: ")
    while True:
        change_type = int_input("\nWhat do you want changed?\n1. Name\n2. Genre\n3. Time\n\nPick one (1-3): ") -1
        if change_type < 0 or change_type > 2:
            print("Not in Range (1-3)")
            continue
        break
    while True:
        new_text = str_input("What do you want it changed to?: ")
        if change_type == 2:
            try:
                new_text = int(new_text)
            except:
                input("Invalid Input! (only integers accepted)\nPress Enter to Continue")

                continue
        input("Press enter to continue")
        break

    for artist_num, artist in enumerate(artist_list):
        if artist_name.title() == artist[0].title():
            artist_list[artist_num][change_type] = new_text
            edited = 1
    if edited == 0:
        print("Not In List\nPress enter to continue")
        input()



# Gavins code

def schedule_main(admin,performances): # schedule main function 
    if admin == True:
        while True:
            cs()
            choice = int_input("SCHEDULE MENU\n\n1.add to schedule\n2. remove item from schedule\n3. exit\n\nPick one (1-3): ")

            if choice == 1: # adds schedule info
                schedule_add(performances)
            elif choice == 2: # removes from schedule
                schedule_remove(performances)
            elif choice == 3: # exit
                main(admin,id,performances)
            else:
                input('Invalid Input!\nPress enter to continue')
    else:
        while True:
            cs()
            choice = int_input("SCHEDULE MENU\n\n1. See schedule\n2. Exit\n\nChoose one (1-2): ")
            if choice == 1: # See Schedule
                print_schedule()
            elif choice == 2: # Exit
                main(admin,id,performances)


# the schedule

# adds people to schedule
def schedule_add(performances):
    artist_name_add=input("what is the artist's name?: ")
    artist_intrument_add=input("what is their intrument?: ")
    artist_genre_add=input("what is their genre?: ")
    artist_time_add=input("what time are they playing?: ")
    new_artist_list=[artist_name_add,artist_intrument_add,artist_genre_add,artist_time_add]
    performances.append(new_artist_list)
    input("Press enter to continue")

def print_schedule():
    print("Schedule with name and time:\n")
    for x in performances:
        print(f"Name: {performances[x][0]} Time: {performances[x][3]}")
    input("\nPress enter to continue")

# removes from schedule
def schedule_remove(performances):
            artist_remove=input("what is the artist's name that you would like to remove? (exact): ")
            performances.remove(artist_remove)
            performances-=1
            print(artist_list)

# changes schedule
def schedule_change():
            artist_change=("what is the artist that you would like to change?")



#this is nicoles function

venue_names = set()  
venue_stages = {}
venue_equipment = {}

def display_venues(): #displays the venues
    cs()
    if venue_names:
        print("_______Venues available:_______")
        for venue in venue_names:
            print(f"- {venue}\n")
    else:
        print("____________________")
        print("No venues available.")

def add_venue(): #Adds venues+stages
    cs()
    venue = input("What is the name of the venue you would like to add?: ").lower()
    venue_names.add(venue)
    print(f"{venue} added!")
    print("")
    stage = input(f"Enter the name of the stage for {venue}!: ").lower()
    venue_stages[venue] = stage
    venue_equipment[venue] = [] 
    print(f"{stage} was added to the {venue}.")

def remove_venue(): #Removes venues
    cs()
    display_venues()
    print("__________________")
    venue = input("Which venue would you like to remove?: ").lower()
    if venue in venue_names:
        venue_names.remove(venue)
        del venue_stages[venue]  
        del venue_equipment[venue]  
        print(f"{venue} and it's information has been removed.")
    else:
        print(f"{venue} was not found.")

def display_stages(): #Displays venues and all their stages
    cs()
    if venue_stages:
        print("Stages and their venues:")
        print("____________________")
        for venue, stage in venue_stages.items():
            print(f"Venue: {venue} | Stage: {stage}")
    else:
        print("There are no stages yet.")

def add_equipment(): #Adds equipment to the venues
    cs()
    venue = input("Enter the venue where you want to add equipment: ").lower()
    if venue in venue_names:
        equipment = input("Enter the equipment name to add: ").lower()
        venue_equipment[venue].append(equipment)
        print(f"{equipment} added to venue {venue} successfully! ")
    else:
        print(f"{venue} was not found.")

def remove_equipment(): #removes equipment
    cs()
    venue = input("What Venue would you like to remove from?: ").lower()
    if venue in venue_names:
        equipment = input("Enter the equipment name to remove: ").lower()
        if equipment in venue_equipment[venue]:
            venue_equipment[venue].remove(equipment)
            print(f"Equipment {equipment} removed from {venue} successfully!")
        else:
            print(f"{equipment} was not found at {venue}.")
    else:
        print(f"{venue} was not found.")

def display_equipment(): #Displays ALL the equipment on a given stage for a given venue
    cs()
    if venue_equipment:
        print("Equipment in each venues stage:")
        for venue, equipment in venue_equipment.items():
            stage = venue_stages[venue] 
            if equipment:
                print("______________________________________________")
                print(f"Venue: {venue} | Stage: {stage} | Equipment:")
                for item in equipment:
                    print(f"   - {item}")
            else:
                print("________________________________________________")
                print(f"Venue: {venue} | Stage: {stage} | No equipment")
    else:
        print("No equipment available.")

def venue_main_checker(admin): # Brings the user to the admin main or the non-admin main
    if admin == False:
        venue_nonadmin_main()
    elif admin == True:
        venue_main()

def venue_nonadmin_main():
    while True:
        cs()
        choice = int_input("\n1. display venues and their associated information\n 2. Exit\n")
        if choice == 1:
           display_equipment()
        elif choice == 2:
           search_artist()
        elif choice == 3:
            main(admin,id,performances)

        else:
            print("Not in Range\nClick Enter to Continue")
            input()

def venue_main(): #main user interface for venues
    while True:
        cs()
        choice = input("""
What would you like to do?: 
1. Add Venue
2. Remove Venue
3. Add Equipment
4. Remove Equipment
5. Display Venues
6. Display Stages
7. Display Equipment
8. Exit
""")
        if choice == '1':
            add_venue()
        elif choice == '2':
            remove_venue()
        elif choice == '3':
            add_equipment()
        elif choice == '4':
            remove_equipment()
        elif choice == '5':
            display_venues()
        elif choice == '6':
            display_stages()
        elif choice == '7':
            display_equipment()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Try again.")


def admin_check(admin,id,performances): # Checks if your admin or not (login interface)
    while True:
        cs()
        choice = int_input("Music Festival Login\n\n1. User login\n2. Admin login\n\nWhich one are you logging into? (1-2): ")
        if choice == 1: # User Login
            admin = False
            main(admin,id,performances)
        elif choice == 2: # Admin Login
            cs()
            print("Admin Login Terminal")
            admin_password = "Admin123" # Admin password
            password_try = input("\nEnter password: ")
            if password_try == admin_password: # If correct
                print("\nPassword Verified!")
                admin = True
                input("\nWelcome Admin!\nPress enter to continue")
                main(admin,id,performances)
            else: # If incorrect
                input("Invalid Password!\nPress enter to continue")
        else:
            input("Invalid Input! (1-2)\nPress enter to continue")

# Running the Code
admin_check(admin,id,performances) # Checks if they are admin or not, then runs main
