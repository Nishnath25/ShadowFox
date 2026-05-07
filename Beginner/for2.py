#2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.

total_jacks=100
completed=0
set_size=10

for i in range(1,(total_jacks//set_size)+1):
    completed+=10
    remaining=total_jacks-completed

    print(f"You have completed {completed} jumping jacks so far.")

    if completed == total_jacks:
        print("Congratulations! You completed the workout")
        break
    print("Remaning jacks:",remaining)

    tired = input('Are you tired? (yes/y or no/n): ').strip().lower()

    if tired in ("yes", "y"):
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()

        if skip in ("yes", "y"):
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            print(f" jumping jacks remaining {remaining}")
    else:
         print(f" jumping jacks remaining {remaining}")

       
