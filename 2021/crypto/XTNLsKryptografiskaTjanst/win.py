o = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS"
e = "avbuctdserfqgphoinjmklHIGJFKELDMCNBOAPzQyRxSw"

encrypted = "ckr_astneec_tnfa{mk_ankr_yaptttoegdr_aaflil}a"

solved = [0 for _ in range(len(encrypted))]

for i in range(len(o)):
    ch = o[i]
    original = i
    target = e.index(ch)
    solved[original] = encrypted[target]

print("".join(solved))
