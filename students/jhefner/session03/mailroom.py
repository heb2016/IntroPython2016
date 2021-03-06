#!/Users/jhefner/python_dev/uw_python/bin/python
import time

verbose = False



history = {
"Zapp Brannigan": [50, 73, 10],
"Philip J Fry": [5],
"Bender Bending Rodriguez": [500],
"Turanga Leela": [7, 20, 96],
"Hermes Conrad": [11, 14, 22],
"Amy Wong": [8, 27, 34],
}

def send_thank_you():
    if verbose: print("send_thank_you()")
    time.sleep(0.5)
    end = False
    while not end:
        print("--------------------------")
        print("--------------------------")
        print("--------------------------")
        print("Alright lets send that thank you note.")
        print("Type \"list\" if you need to be reminded of the donors.")
        print("Otherwise just type the persons full name.")
        thank_you_name = input("\n>>> ")
        if thank_you_name == "list":
            print("Here's the list of our donors:")
            for i in history: print("> ",i)

        if thank_you_name in history:
            if verbose: print("NAME IS IN LIST")
        else:
            history[thank_you_name]=[]

        donation_input = ''
        print("And what was their donation amount?")
        donation_input = input("\n>>> ")
        while not donation_input.isnumeric():
            print("And what was their donation amount? (e.g. 10)")
            donation_input = input("\n>>> ")
        donation_input = int(donation_input)
        history[thank_you_name]=[int(donation_input)]
        print("----------\n.Generating\n..your\n...thank you\n....email\n....now")
        time.sleep(0.5)
        print("\n\nDear "+thank_you_name+",\nIt is with great thanks that we send this note in reception of your donation. Please accept our gratitude and think of us again in the future.\nSincerely,\n\tUs\n\n")
        end=True



def create_a_report():
    if verbose: print("create_a_report()")
    donation_report = {}
    for key, value in history.items():
        value_total = 0
        for i in value:
            value_total+=i
        donation_report[key] = value_total
    # print(donation_report)
    # donation_report = list(donation_report.items())
    # print(donation_report)
    # donation_report = sorted(donation_report,key=lambda x:(-x[1],x[0]))
    # print(donation_report)
    # ^^^ this is all stuff i found online but i can't find anything that explains how I should be able to manually go over a dictionary or list of tuples.


    # print("--------------------------")
    # print("Here's your report:")
    # print("--------------------------")




def main():
    if verbose: print("main()")
    end = False
    while not end:
        main_menu_choice=0
        print("--------------------------")
        print("What would you like to do?")
        print("--------------------------\n")
        print("Enter the # for your selection")
        print("1. Send a Thank You\n2. Create a Report\n3. Exit")
        main_menu_choice = input("\n>>> ")
        if main_menu_choice == "1":
            send_thank_you()
        elif main_menu_choice == "2":
            create_a_report()
        elif main_menu_choice == "3":
            end=True
        else:
            print("\n\n\nPlease try your selection again.")
            time.sleep(1)


if __name__ == '__main__':
    main()