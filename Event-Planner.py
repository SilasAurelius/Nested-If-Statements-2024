# Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Venue Selection: Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

# Task 3: Catering Choices: Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

equipment = "audio system" if venue == "large hall" else "projector"
print(equipment)
choice = input("Would you like a vegetarian meal? (Yes/No): ").lower()
catering = "vegetarian" if choice == "yes" else "Gourmet Meals Caterers"
print(catering)