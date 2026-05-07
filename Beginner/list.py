
'''1. You have a list of superheroes representing the Justice
League. justice_league = ["Superman", "Batman", "Wonder
Woman", "Flash", "Aquaman", "Green Lantern"]'''

#1. Calculate the number of members in the Justice League.
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("the number of members in the Justice League:",len(justice_league))

#2. Batman recruited Batgirl and Nightwing as new members. Add them to your list.

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After addition new list",justice_league)

#3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list. 

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Current list:", justice_league)

'''4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" 
and move them in between Aquaman and Flash.'''

justice_league.remove("Superman")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index+1, "Superman")
print("Current list:", justice_league)

'''5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following
new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".'''

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

#6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.

justice_league.sort()
print("Sorted justice_league:",justice_league)
print("New leader:",justice_league[0])


