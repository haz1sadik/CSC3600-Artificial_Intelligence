from logic import *

S = Symbol("storm") # storm today
D = Symbol("darkseid") # Superman fought darkseid today
L = Symbol("lex") # Superman fought Lex today

overall_proposition = And(Implication(Not(S) , D),
                          Or(D, L),
                          Not(And(D, L)),
                          L)

print(overall_proposition.formula())

print("\nIs is storm today?")
print(model_check(overall_proposition, S)) # check if there is a storm

print("\nDoes superman fights darkseid today?")
print(model_check(overall_proposition, D)) # check if superman fights darkseid today

print("\nDoes superman NOT fights Lex today?")
print(model_check(overall_proposition, Not(L))) # check if superman NOT fights Lex today

print("\nDoes is it storming or superman fights darkseid today?")
print(model_check(overall_proposition, Or(S, D)))