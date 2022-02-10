def main():
    even = [2, 4, 6, 8, 10, 12]
    odd = [1, 3, 5, 7, 9, 11]

    #mapping and filtering
    print(list(map(lambda e: e**2, filter(lambda e: e > 4 and e <16 ,even))))
    print(list(filter(lambda o: o>4, odd)))

    #derive a new list from a given list
    new_even = [ e**2  for e in even]
    print(new_even)

    #use predicate condition
    new_even_p = [ e**2  for e in even if e > 4 and e < 16]
    print(new_even_p)
if __name__ == '__main__': main() 