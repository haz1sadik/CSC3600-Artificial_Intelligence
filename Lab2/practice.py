from logic import *

S = Symbol("storm") # storm today
D = Symbol("darkseid") # Superman fought darkseid today
L = Symbol("lex") # Superman fought Lex today

"""
i.      If there is no storm, Superman fought Darkseid today.  
ii.     Superman fought Darkseid or Lex Luthor today, but not both of 
        them. 
iii.    Superman fought Lex Luthor today. 
"""

sentenceImplication = Implication(S, D)
print(sentenceImplication.formula())

sentenceAND = And(S, D)
print(sentenceAND.formula())

sentenceOR = Or(S, D)
print(sentenceOR.formula())

kb = Implication(Not(S), D)
print(kb.formula())

