from random import randint
from random import randrange

class Node():
    def __init__(self):
        self.val = None
        self.next = None

class Utils(Node):
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

    def createRandomList(self, length, val_range=(int, int)):
        '''
        Creates a Linked List of given length and range (MIN, MAX)
        '''
        first = None
        for _ in range(length):
            temp = Node()
            temp.val = randrange(*val_range)
            temp.next = first
            first = temp
        return first


    def printList(self, list_head):
        '''
        Prints given Linked List
        '''
        print('[', end='')
        while list_head.next != None:
            print(list_head.val, end=', ')
            list_head = list_head.next
        print(list_head.val, end=']\n')


    def createArray(self, length, val_range=(int, int)):
        '''
        Creates an array of given length and range (MIN, MAX)
        '''
        return [randrange(*val_range) for _ in range(length)]