def shutdown(choice):
    if choice.lower() == "yes":
        print("Shutting down the system...")
    elif choice.lower() == "no":
        print("Shutdown canceled.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.") 


choice = input("You want to shutdown the system? (yes/no):")
shutdown(choice)
