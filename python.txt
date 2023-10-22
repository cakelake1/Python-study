def is_subline_in_line(line, subline):
    if len(line) == len(subline) == 0:
        return True
    if len(subline) == 0:
        return True

    curr_in_subline = 0
    
    for curr_in_line in range(len(line)):
        if line[curr_in_line] != subline[curr_in_subline]:
            continue

        if len(line) - curr_in_line < len(subline):
            return False

        for index_in_subline in range(len(subline)):
            if subline[index_in_subline] != line[curr_in_line]:
                break
            if index_in_subline == len(subline) - 1:
                return True
            curr_in_line +=1

    return False
    
print(is_subline_in_line("erwerwerwer werwer werwerr", "werwerr"))