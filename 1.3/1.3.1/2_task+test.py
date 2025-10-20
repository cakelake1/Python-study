def white_walkers(village):
    dig = 0
    wnum = 0
    has10 = False
    for char in village: 
        if char.isdigit():
            curret_digit = int(char)
            if curret_digit + dig == 10:
                if wnum != 3:
                    return False
                has10 = True
            dig = curret_digit
            wnum = 0
        elif char == "=":
            wnum +=1
    return has10

test_cases = [
    ("axxb6===4xaf5===eee5", True),
    ("5==ooooooo=5=5", False),
    ("abc=7==hdjs=3gg1=======5", True),
    ("aaS=8", False),
    ("9===1===9===1===9", True),
    ("", False),
    ("abc", False),
    ("1=2", False),
    ("5====5", False),
    ("5==5", False)
]
for village, expected in test_cases:
    result = white_walkers(village)
    print(f'"{village}" -> {result} (expected: {expected}) {"✓" if result == expected else "✗"}')