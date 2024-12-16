import z3
import random
import re

interMidateN = 0
inp = [z3.BitVec(f'i{i}', 1) for i in range(0,32)]

def add_round(solver, op1, op2):
    choice = random.randint(0,2)
    
    #print(solver.assertions())
    
    interN = z3.BitVec(f'N{interMidateN}', 1)
    if choice == 0:
        solver.add(interN == op1 ^ op2)
    if choice == 1:
        solver.add(interN == op1 & op2)
    if choice == 2:
        solver.add(interN == op1 | op2)

    return interN

def checkSolutions(solver, sol=None):
    solutions = 0
    fsol = ''
    while solver.check() == z3.sat:
        m = solver.model()
        if sol:
            fSol = ''.join([str(m.evaluate(sol_char)) for sol_char in sol])


        solver.add(z3.Or([f != solver.model()[f] for f in inp]))
        solutions += 1
        if sol:
            return fSol
    return solutions
def getSolution(solver):
    while solver.check() == z3.sat:
        m = solver.model()
        sol = ''.join([str(m.evaluate(inp_char)) for inp_char in inp])
        #     pass
        print(sol)
        solver.add(z3.Or([f != solver.model()[f] for f in inp]))
f1 = z3.BitVecVal('0', 1)

s = z3.Solver()

currentOperation = inp.copy()
currentOperationLen = len(currentOperation)
inters = inp.copy()
# number of rounds
for i in range(0,5):

    for j in range(0, int(currentOperationLen/2)):
        op1 = random.randint(0, len(currentOperation) - 1)
        op1Val = currentOperation[op1]
        currentOperation.remove(op1Val)

        op2 = random.randint(0, len(currentOperation) - 1)
        op2Val = currentOperation[op2]
        currentOperation.remove(op2Val)
        
        inter = add_round(s, op1Val, op2Val)

        interMidateN += 1
        inters.append(inter)
    
    currentOperation = inters.copy()
    currentOperationLen = len(inters)
    print(currentOperation)
    print("Round done", currentOperationLen)

target = bin(random.randint(0,2**32))[2:].zfill(32)
solution = [z3.BitVec(f's{i}', 1) for i in range(0,32)]

sCpy = z3.Solver()
for assertion in s.assertions():
    sCpy.add(assertion)

for index, bit in enumerate(target):
    print((-1 * index) - 1)
    sCpy.add(currentOperation[(-1 * index) - 1] == solution[index])
    #s.add(currentOperation[(-1 * index) - 1] == solution[index])

print("Final Assertions", sCpy.assertions())
print("Target is", target)

if sCpy.check() != z3.sat:
    print("Z3 says constraints are not satisfiable, exiting.")
    exit()
s.check()
print(sCpy.assertions())

solutionFound = False
print("Number of rules: ", len(s.assertions()))
while not solutionFound:
    exampleSolution = checkSolutions(sCpy, sol=solution)
    print("testing solution ", exampleSolution)
    sCpy2 = z3.Solver()
    for assertion in s.assertions():
        sCpy2.add(assertion)
    for index, bit in enumerate(exampleSolution):
        sCpy2.add(currentOperation[(-1 * index) - 1] == exampleSolution[index])

    nSolution = checkSolutions(sCpy2)

    print("String: ", exampleSolution, "Has", nSolution, "solutions")
    res = input("y/n")
    if res == 'y':
        solutionFound = True
        for index, bit in enumerate(exampleSolution):
            s.add(currentOperation[(-1 * index) - 1] == exampleSolution[index])

print("Generating C code...")
assertions = [str(a) for a in s.assertions()]

while True:
    targetSymbol = assertions[0].split(" == ")
    print("target symbol", targetSymbol)
    newAssertions = assertions[1:].copy()

    matchRe = re.compile(targetSymbol[0] + "(?![0-9])")
    for index, a in enumerate(assertions[1:]):
        newAssertions[index] = re.sub(matchRe, f"({targetSymbol[1]})", a)
    assertions = newAssertions
    
    for a in newAssertions:
        print(str(a))
    if len(assertions) == 32:
        print("Should exit now!")
        break
cStatement = '(' + ') && ('.join(assertions) + ')'

cStatementCpy = cStatement
for i in inp:
    targetSymbol = str(i)
    matchRe = re.compile(targetSymbol + "(?![0-9])")
    cStatement = re.sub(matchRe, f"input[{targetSymbol[1:]}]", cStatement)
        #exit()
getSolution(s)
print(cStatement)
