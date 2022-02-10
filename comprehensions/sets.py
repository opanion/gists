
def main():
    temp = [4, 10, 25, 20, 50, 67, 90, 10]
    templist = [t*(9/5) + 32 for t in temp]
    tempset ={ t*(9/5) + 32 for t in temp}

    print(templist)
    print(tempset)

    s_string = 'Today I don\'t feel like doing anything'

    chars = {char.upper() for char in s_string if  not char.isspace()}
    print(chars)

if __name__ == '__main__': main() 