string = input()
freq = {}
for char in string:
    if char == char.lower():
        freq["lower"] = freq.get("lower", 0) + 1
    else:
        freq["upper"] = freq.get("upper", 0) + 1
if freq.get("lower", 0) >= freq.get("upper", 0):
    print(string.lower())
else:
    print(string.upper())