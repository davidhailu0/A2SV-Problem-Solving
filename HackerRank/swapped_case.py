def swap_case(s):
    swapped_str = ''
    
    for char in s:
        if char.upper() == char:
            swapped_str += char.lower()
        else:
            swapped_str += char.upper()
    return swapped_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)