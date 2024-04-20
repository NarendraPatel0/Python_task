# 1. Write a program for Ascending and Descending order without using the inbuilt method.?

def ascending_order(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers
def descending_order(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers
num=0
print("Original list:", num)
print("Ascending order:", ascending_order(num.copy()))
print("Descending order:", descending_order(num.copy()))







# 2 ]  Find the largest number in a given List without using the inbuilt method?
[20,25,10,45,22,50,40]
l=[20,25,10,45,22,50,40]
min=l[0]
for i in range(len(l)):
    if min > l[i]:
        min = l[i]
print(min)







# 3. Write a program for single inheritance in python

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name, "makes", dog.sound())
print(cat.name, "makes", cat.sound())




# 4 ] Write a program for overloading and overriding

class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

if __name__ == "__main__":
    generic_animal = Animal()
    my_dog = Dog()
    generic_animal.make_sound()
    my_dog.make_sound()  



# Write a program for multiprocessing thread.


import multiprocessing
import time

def worker(num):
    print(f"Worker {num} started")
    time.sleep(2)
    print(f"Worker {num} finished")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    print("All workers have finished")



# Write a program to add two matrices.

X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Y = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
print("Resultant Matrix:")
for row in result:
    print(row)
