def negation(p):
    return not p

def conjunction(p, q):
    return p and q

def disjunction(p, q):
    return p or q

def implication(p, q):
    return negation(p) or q

def bi_implication(p, q):
    return (implication(p, q)) and (implication(q, p))