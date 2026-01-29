def split_and_join(line):
    splitted_line = line.split(" ")

    joined_string = "-".join(splitted_line)
    
    return joined_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)