from random import randint
from random import randrange

class Node():
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt

class Utils():
    def randomNumber(self, min=0, max=1000):
        '''
        Returns random integer of given range (MIN, MAX)
        '''
        return randint(min, max) 

    def randomArray(self, min=0, max=1000, length=10):
        '''
        Returns random array of given length and range (MIN, MAX)
        '''
        array = []
        for _ in range(length):
            array.append(self.randomNumber(min, max))

        return array

    def createRandomList(self, val_range=(0, 1000), length=10):
        '''
        Creates a Linked List of given length and range (MIN, MAX)
        '''
        first = None
        for _ in range(length):
            temp = Node(val=randrange(*val_range), nxt=first)
            first = temp
        return first


    def printList(self, list_head):
        '''
        Prints given Linked List
        '''
        if list_head == None:
            print(None)
            return
        print('[', end='')
        while list_head.nxt != None:
            print(list_head.val, end=', ')
            list_head = list_head.nxt
        print(list_head.val, end=']\n')


    def createArray(self, length, val_range=(int, int)):
        '''
        Creates an array of given length and range (MIN, MAX)
        '''
        return [randrange(*val_range) for _ in range(length)]