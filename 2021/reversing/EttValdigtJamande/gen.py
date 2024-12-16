flagga = "cratectf{JLTScuYHpEZsMgYAV}"
i = 0
for _ in range(len(flagga)):
    i = (i+17)%len(flagga)
    print(flagga[i], end="")
print()

