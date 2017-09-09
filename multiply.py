print_me = [str(x) for x in range(1,13)] #<---- THIS IS THE COLUMN NUMBER
#print_me is simply numbers 1-12 AS A STRING
print("x\t" + "\t".join(print_me))
#"x\t" SHOULD CORRESPOND TO THE ROW NUMBER
#EVERYTHING IN PRINT_ME SHOULD CORRESPOND TO THE ROW NUMBER* THE COLUMN NUMBER
#EACH NUMBER is the ROW NUMBER times the COLUMN NUMBER

a = 1

for y in range(1,13):
    this_row = []
    for a in range (1,13):
        this_row.append(a * y)
        a += 1

    print_row = [str(z) for z in this_row] #THIS CHANGES EACH ELEMENT INTO A STRING SO THAT IT CAN BE PRINTED
    print (str(y) + "\t" + "\t".join(print_row))
