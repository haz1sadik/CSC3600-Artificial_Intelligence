import proplog

print("\nNegation\n+--------+--------+")
print("| %-6s | %-6s |" % ("p", "not(p)"))
print("+--------+--------+")
for p in [True, False]:
    print("| %-6s | %-6s |" % (p, proplog.negation(p)))
print("+--------+--------+")

print("\nConjunction\n+--------+--------+--------+")
print("| %-6s | %-6s | %-6s |" % ("p", "q", "p ∧ q"))
print("+--------+--------+--------+")
for p in [True, False]:
    for q in [True, False]:
        print("| %-6s | %-6s | %-6s |" % (p, q, proplog.conjunction(p, q)))
print("+--------+--------+--------+")

print("\nDisjunction\n+--------+--------+--------+")
print("| %-6s | %-6s | %-6s |" % ("p", "q", "p ∨ q"))
print("+--------+--------+--------+")
for p in [True, False]:
    for q in [True, False]:
        print("| %-6s | %-6s | %-6s |" % (p, q, proplog.disjunction(p, q)))
print("+--------+--------+--------+")

print("\nImplication\n+--------+--------+--------+")
print("| %-6s | %-6s | %-6s |" % ("p", "q", "p → q"))
print("+--------+--------+--------+")
for p in [True, False]:
    for q in [True, False]:
        print("| %-6s | %-6s | %-6s |" % (p, q, proplog.implication(p, q)))
print("+--------+--------+--------+")

print("\nBi-Implication\n+--------+--------+--------+")
print("| %-6s | %-6s | %-6s |" % ("p", "q", "p ↔ q"))
print("+--------+--------+--------+")
for p in [True, False]:
    for q in [True, False]:
        print("| %-6s | %-6s | %-6s |" % (p, q, proplog.bi_implication(p, q)))
print("+--------+--------+--------+")
