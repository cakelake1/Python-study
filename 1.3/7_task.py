def WordSearch(width, s, subs):
    words = s.split()
    text_lines = []
    result = []
    current_text_line = ""

    for word in words: # Если слово длинное
        if len(word) > width:
            if current_text_line: 
                text_lines.append(current_text_line)
                current_text_line = ""
            start = 0
            while start < len(word):
                part_word = word[start:start + width]
                text_lines.append(part_word)
                start = start + width
        else: # во всех остальных случаях
            if current_text_line == "":
                current_text_line = word
            else:
                if len(current_text_line) + 1 + len(word) <= width:
                    current_text_line = current_text_line + " " + word
                else:
                    text_lines.append(current_text_line)
                    current_text_line = word
                    
    if current_text_line != "":
        text_lines.append(current_text_line)
    for line in text_lines:
        wd = line.split()
        correct = 0
        for w in wd:
            if w == subs:
                correct = 1
                break
        result.append(correct)

    return result