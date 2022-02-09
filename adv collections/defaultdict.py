import collections

def main():
    fruits = ['apple', 'banana', 'kiwi', 'apple', 'orange',
                'banana', 'apple', 'mango', 'orange']
                
    #create default dict with an initialized value for each key
    fruits_counter = collections.defaultdict(lambda: 0)
    for fruit in fruits:
        fruits_counter[fruit] += 1

    for key, value in fruits_counter.items():
        print(f'{key} : {value}')

if __name__ == '__main__': main()