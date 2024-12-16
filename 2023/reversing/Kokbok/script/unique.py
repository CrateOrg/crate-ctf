lines_seen = set()
for each_line in open('rena_recept.json', 'r'):
    if each_line not in lines_seen:
        lines_seen.add(each_line)

with open('unika_rena_recept.json', 'w') as output_file:
    output_file.write("[")
    for i, line in enumerate(lines_seen):
        if i > 0: output_file.write(",")
        output_file.write(line)
    output_file.write("]")
