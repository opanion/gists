from collections import Counter

def main():
    class1 = ['John', 'James', 'Emmanuel', 'Harriet', 'Jake',
            'Ismael', 'James', 'Isaac', 'Rita']
    class2 = ['Billy', 'Joana', 'Riley', 'Aaron', 'Stephanie', 'Emmanuel']

    counter1 = Counter(class1)
    counter2 = Counter(class2)

    #number of students in class 1 called James
    print(counter1['James'])

    print(sum(counter1.values()), 'students in class 1')

    counter1.update(class2)
    
    print(sum(counter1.values()), 'students in both classes')
    #top 3 occurring names
    print(counter1.most_common(3))
    
    #remove class 2 students for the counter
    counter1.subtract(class2)
    print(counter1.most_common(3))

    #appearing in both counters
    print(counter1 & counter2)

if __name__ == '__main__': main()