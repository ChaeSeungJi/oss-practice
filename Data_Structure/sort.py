import time
import random


def make_rand_list():
    a = []
    for i in range(0,300):
        a.append(random.randint(0,100))
    return a

def selection_sort(a,n):
    if(n>2):
        k = max(a)
        
    

a = make_rand_list()

start = time.time()
a = selection_sort(a)
end = time.time()
print(a.count)
print(f"{end - start:.5f} sec")
