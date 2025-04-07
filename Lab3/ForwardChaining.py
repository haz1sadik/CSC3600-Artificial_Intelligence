# Define the rules
rules = [
    # Rule 1
    {'antecedents': ['item is A', 'item is B'], 'consequent': 'recommend item X'},

    # Rule 2
    {'antecedents': ['item is A', 'item is C'], 'consequent': 'recommend item Y'},

    # Rule 3
    {'antecedents': ['item is B', 'item is D'], 'consequent': 'recommend item Z'},

    # Add more rules as needed
]

# Define the initial facts
facts = {
    'item is A': True,
    'item is B': True,
    'item is C': False,
    'item is D': True,

}

# Apply the rules to the facts
recommendations = []
for rule in rules:
    if all(facts.get(ant, False) for ant in rule['antecedents']):
        recommendations.append(rule['consequent'])


    # Print the recommendations
if recommendations:
    print("We recommend the following: ")
    for item in recommendations:
        print("- " + item)
else:
    print("We could not find any suitable recommendation based on your preferences.")
