mangled = "pfAueMTrE{VYcgSaZJ}HtYctsLcHvIKoOHWOuFceqOeidBIUhdDOKLTxbgpZMvDxADWfuVjZFtCDv"

for testlen in range(1, 40):
    i = 0
    solution = ["a"]*testlen
    j = 0
    for char in mangled:
        i = (i+17)%testlen
        j += 1
        solution[i] = char
        if j == testlen:
            break

    sol = "".join(solution)
    if sol.startswith("cratectf"):
        print(sol)

