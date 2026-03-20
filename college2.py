electives = {
    "marketing": 0,
    "data science" : 0,
    "finance" : 0,
    "design" : 0,
    "history" : 0
}

print("Elective recommender")

money = input("Do you wnat to make money?: yes/no: ").lower()
creativity = input("Are you creative?: yes/no: ").lower()
tech = input("Do you like tech?: yes/no: ").lower()
analysis = input("Do you like numbers and statistics?: yes/no: ").lower()
history= input("Do you like theory and history?: yes/no: ").lower()

if money == "yes":
    electives["marketing"] += 2
    electives["finance"] += 2

if creativity == "yes":
    electives["design"] += 3
    electives["marketing"] += 1

if tech == "yes":
    electives["data science"] += 2

if analysis == "yes":
    electives["finance"] += 2
    electives["data science"] += 2

if history == "yes":
    electives["history"] += 3

sorted_electives = sorted(electives.items(), key = lambda x: x[1], reverse= True)
print("\n3 best Recommended electives are: ")
for subject, score in sorted_electives[:3]:
    print(f"{subject} - Score: {score}")
