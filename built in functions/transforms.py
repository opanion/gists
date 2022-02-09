def main():
    numbers = ( 1, 8, 4, 5, 13, 26, 381, 410, 58,47)
    chars= 'abcdEfghIjkMnop'
    grades = (81, 89, 78, 61, 72, 84, 68, 75)

    #use filter to remove even numbers
    odds = list(filter(filterfunc, numbers))
    print(odds)

    #use filter to remove uppercase characters
    lower = list(filter(filterfunc2, chars))
    print(lower)

    #use map to square numbers
    squared = list(map(squarefunc, numbers))
    print(squared)

    #use map to print letter grades
    grades = sorted(grades)
    letters = list(map(gradesfunc, grades))
    print(letters)

def filterfunc(x):
    if x % 2 == 0:
        return False
    return True

def filterfunc2(x):
    #for char in x:
    if x.isupper():
        return False
    return True

def squarefunc(x):
    return x**2

def gradesfunc(x):
    if x >= 90: return 'A'
    elif x >= 80 and x < 90: return'B'
    elif x >= 70 and x < 80: return 'C'
    elif x >= 50 and x < 70: return 'D'

    return 'F'

if __name__ == '__main__': main()