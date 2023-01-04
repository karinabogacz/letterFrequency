alphabet = "abcdefghijklmnopqrstuvwxyz"

def open_f():
    f = open('words.txt','r')
    return f

def has_one(letter):
    f = open_f()
    counter = 0
    for word in f:
        if letter in word:
            counter += 1                
    return counter

def has_any():

    d = dict()

    for letter in alphabet:
        d[letter] = has_one(letter)
    
    return d

def sorted_all():
    
    d = has_any()
    alist = list(d.keys())

    sorted_list = []

    for index in range(len(alist)):
        sorted_list.append(d[alist[index]])

    sorted_list.sort(reverse=True)    

    new_d = dict()
    for value in sorted_list:
        for index in range(len(alist)):
            if value == d[alist[index]]:
                new_d[alist[index]] = value
    return new_d

result = sorted_all()
for item in result:
    print(item, result[item])

def percentage_any():

    alist = []
    words = list(open_f())
    sum_all = len(words)
    result = new_d

    for key in new_d:
        val = new_d[key]
        percentage = (val/sum_all)*100
        alist.append(percentage)
    return alist


