import random
import copy


class Hat:

    def __init__(self, **kwargs):
        self.slov = kwargs
        self.contents = list()
        for i, (j,k) in enumerate(kwargs.items()):
            for l in range(k):
                self.contents.append(j)
    def draw(self, num):
        sc = self.contents
        if num > len(sc):
            return sc
        else:
            b = list()
            for i in range(num):
                a = random.randint(0, (len(sc)-1))
                b.append(sc[a])
                del sc[a]
            return b

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    a = hat.contents
    b = expected_balls #dict toho co chci vytáhnout
    c = num_balls_drawn #počet balonků, který se bude každý experiment tahat
    d = num_experiments #počet experimentů
    m = 0  # match

    a1 = list()  # vytažené míčky
    b1 = list() # list očekávané míčky, b převedeno do listu 
        
    for i in b: # převedené b do listu
        while True:
            b1.append(i)
            b[i] -= 1
            if b[i] == 0:
                break
    b1.sort()
    print("b1",b1)

    for x in range(d):
        a1=list() # vytažené míčky, pokaždé vynulovat!
        a2= copy.copy(a)
        for i in range(c):
            a11 = random.randint(0, len(a2)-1)  # náhodné číslo od 0 do počtu všech míčků
            a1.append(a2[a11])
            del a2[a11]
        a1.sort()
        #print(a1)
        f = 0
        g = copy.copy(a1)
        for y in b1:
            if y in g:
                g.remove(y)
                f += 1
            else:
                break
        if f == len(b1):
            m += 1
    p = m/d
    return p




    
h1 = Hat(yellow=3, blue=2, green=6)
print(h1.slov)  # {'yellow': 3, 'blue': 2, 'green': 6}
print(h1.slov["yellow"])  # 3
print(h1.contents)
print(h1.draw(3))
print(h1.draw(6))
print(h1.draw(12))
h1 = Hat(yellow=3, blue=2, green=6)
print(experiment(h1, {'yellow': 2, 'green': 4}, 12, 1000))
