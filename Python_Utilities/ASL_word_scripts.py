f_old = open("C:\\Users\\craig\\Documents\\Listening-Effort\\Max\\Audio_Only\\BKBQwordsreduced.txt", "r")
f_new = open("C:\\Users\\craig\\Documents\\Listening-Effort\\Max\\Audio_Only\\BKBQwords_new.txt", "w+")

for cnt, line in enumerate(f_old):
    line_cells = ['']*5
    word = ''
    num = 0
    for char in line:
        if (char is ' ' or char is '\n') and yes:
            line_cells[num] = word
            word = ''
            num = num + 1
            yes = False
        elif char is not ' ':
            word += char
            yes = True
    print(line_cells)

    if len(line_cells[0]) is 1:
        first = "0" + line_cells[0]
    else:
        first = line_cells[0]
    if len(line_cells[1]) is 1:
        second = "0" + line_cells[1]
    else:
        second = line_cells[1]

    number = first + 's' + second

    f_new.write(str(cnt + 1) + " bkbgl" + number + ".wav " + line_cells[2] + " " + line_cells[3] + " " + line_cells[4] + ";\r")
