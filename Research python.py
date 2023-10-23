
'''
+------------+------------------------+-----------------------+---------------------+------------------+---------------
|  Data Type |        Description     |     Example           |   Common Methods    |  Common Functions|
+------------+------------------------+-----------------------+---------------------+------------------+
|    List    | Ordered collection     | [1, 'apple', 3.14]    | append(), extend(), | len(), sorted(), |
|            | of mutable elements   |                       | insert(), remove()  | max(), min()     |
+------------+------------------------+-----------------------+---------------------+------------------+
| Dictionary | Unordered collection   | {'key': 'value',     | keys(), values(),   | len(), str()     |
|            | of key-value pairs    |  'name': 'John'}      | items(), get(),     |                  |
|            | with unique keys      |                       | pop()               |                  |
+------------+------------------------+-----------------------+---------------------+------------------+
|    Tuple   | Ordered collection     | (1, 'apple', 3.14)    | count(), index()    | len(), str()     |
|            | of immutable elements |                       |                     |                  |
+------------+------------------------+-----------------------+---------------------+------------------+
|     Set    | Unordered collection   | {1, 'apple', 3.14}    | add(), remove(),    | len(), max(),    |
|            | of unique elements     |                       | discard(),          | min()            |
|            |                        |                       | pop()               |                  |
+------------+------------------------+-----------------------+---------------------+------------------+
'''





#1.list[]
#Suitable for sequences
#Access-Index-based access

# +----------------------------------------------------------------------------------------+
# | Method                   | Description                                                |
# +----------------------------------------------------------------------------------------+
# | append(item)             | Adds an item to the end of the list.                      |
# | extend(iterable)         | Appends items from an iterable to the end of the list.    |
# | insert(index, item)      | Inserts an item at a specific index in the list.          |
# | remove(item)             | Removes the first occurrence of an item from the list     |
# | pop([index])             | Removes and returns an item at the specified index.       |
# | index(item)              | Returns the index of the first occurrence of an item.     |
# | count(item)              | Returns the number of occurrences of an item.             |
# | sort(key=None, ...)      | Sorts the list in place.                                  |
# | reverse()                | Reverses the elements of the list in place.               |
# | copy()                   | Returns a shallow copy of the list.                       |
# | clear()                  | Removes all items from the list.                          |
# | len(list)                | Returns the number of items in the list.                  |
# | min(list)                | Returns the smallest item in the list.                    |
# | max(list)                | Returns the largest item in the list.                     |
# | sum(list)                | Returns the sum of all items in the list.                 |
# | all(iterable)            | Returns True if all elements of the iterable are true.    |
# | any(iterable)            | Returns True if any element of the iterable is true.      |
# | join(separator, list)    | Joins list items as strings using the separator.          |
# | index(item, start, end)  | Returns the index of an item within a specified range.   |
# | count(item, start, end)  | Returns the count of occurrences within a specified range.|
# | reverse(list)            | Returns a reversed iterator over the list.               |
# | sort(key=None, ..., list)| Returns a sorted list without modifying the original.    |
# | pop()                    | Removes and returns the last item in the list.            |
# | remove(item, start, end)| Removes the first occurrence in a specified range.        |
# | clear(list)              | Removes all items from the list.                          |
# | copy(list)               | Returns a shallow copy of the list.                       |
# | list(iterable)           | Converts an iterable to a list.                          |
# | sorted(iterable, key=...,)| Returns a sorted list from the iterable.                 |
# | reversed(iterable)       | Returns a reversed iterator over the iterable.           |
# | enumerate(iterable, start)| Returns an enumerate object with pairs of index and value.|
# | map(func, iterable)      | Applies a function to all items in the iterable.          |
# | filter(func, iterable)   | Returns items from the iterable for which func is true.  |
# | zip(iterable1, iterable2, ...)| Returns an iterator of tuples, aggregating elements.   |
# | slice(start, stop, step) | Returns a slice object for slicing a sequence.           |
# | list.append(item)        | Adds an item to the end of the list (method syntax).      |
# | list.extend(iterable)    | Appends items from an iterable to the end of the list.    |
# | list.insert(index, item) | Inserts an item at a specific index in the list.          |
# | list.remove(item)        | Removes the first occurrence of an item from the list.    |
# | list.pop([index])        | Removes and returns an item at the specified index.      |
# | list.index(item)         | Returns the index of the first occurrence of an item.     |
# | list.count(item)         | Returns the number of occurrences of an item.             |
# | list.sort(key=None, ...)| Sorts the list in place.                                  |
# | list.reverse()           | Reverses the elements of the list in place.              |
# | list.copy()              | Returns a shallow copy of the list.                       |
# | list.clear()             | Removes all items from the list.                          |
# | list.__len__()           | Returns the number of items in the list.                  |
# | list.__getitem__(index)  | Returns the item at the specified index.                 |
# | list.__setitem__(index, value)| Sets the item at the specified index.                 |
# | list.__delitem__(index)  | Deletes the item at the specified index.                  |
# | list.__iter__()          | Returns an iterator object for the list.                  |
# | list.__contains__(item)  | Returns True if the item is in the list.                 |
# +----------------------------------------------------------------------------------------+









#2. Dictionary{}-dict{}
#Mapping
'''
+---------------------+---------------------------------------------------------+
| Method              | Description                                             |
+---------------------+---------------------------------------------------------+
| dict()              | Creates a new dictionary.                               |
| len(dict)           | Returns the number of key-value pairs in the dictionary.|
| dict[key]           | Accesses the value associated with the given key.       |
| dict[key] = value   | Sets the value for the given key in the dictionary.     |
| del dict[key]       | Removes the key-value pair from the dictionary.         |
| key in dict         | Checks if a key is present in the dictionary.           |
| dict.keys()         | Returns a list of all the keys in the dictionary.       |
| dict.values()       | Returns a list of all the values in the dictionary.     |
| dict.items()        | Returns a list of key-value pairs as tuples.           |
| dict.get(key)       | Returns the value for the given key, or a default value if the key is not present. |
| dict.pop(key)       | Removes the key-value pair and returns the value.      |
| dict.popitem()      | Removes and returns the last key-value pair added.     |
| dict.clear()        | Removes all key-value pairs from the dictionary.        |
| dict.update(other)  | Updates the dictionary with key-value pairs from another dictionary or iterable. |
| dict.copy()         | Creates a shallow copy of the dictionary.               |
| dict.fromkeys(keys, value) | Creates a new dictionary with the given keys and a common value. |
+---------------------+---------------------------------------------------------+
'''

# tuple():
#Lightweight data storage
#Acess-Index-based access
'''
+-------------------+---------------------------------------------------------+
| Method            | Description                                             |
+-------------------+---------------------------------------------------------+
| tuple()           | Creates an empty tuple.                                 |
|                   |                                                         |
| tuple(iterable)   | Creates a tuple from the elements of an iterable.       |
|                   |                                                         |
| len(tuple)        | Returns the number of elements in the tuple.            |
|                   |                                                         |
| tuple[index]      | Accesses the element at the specified index.            |
|                   |                                                         |
| tuple.count(x)    | Returns the number of occurrences of element 'x'        |
|                   | in the tuple.                                           |
|                   |                                                         |
| tuple.index(x)    | Returns the index of the first occurrence of element 'x'|
|                   | in the tuple. Raises ValueError if 'x' is not found.    |
|                   |                                                         |
| tuple + tuple2    | Concatenates two tuples, creating a new tuple.          |
|                   |                                                         |
| tuple * n         | Creates a new tuple by repeating the original tuple 'n' |
|                   | times.                                                  |
                   |                                                          |
| any(tuple)        | Returns True if at least one element in the tuple is    |
|                   | True.no 0                                                   |                                                         |
| all(tuple)        | Returns True if all elements in the tuple are True.     |                   |                                                         |
| sorted(tuple)     | Returns a sorted list of the elements in the tuple.     |
+-------------------+---------------------------------------------------------+
'''

# set{}-set()
#Eliminate duplicates, set operations
#Acess-No direct access

'''
+--------------------------+-------------------------------------------------------+---------------+
| Method                   | Description                                           | Symbol        |
+--------------------------+-------------------------------------------------------+---------------+
| set.add(element)         | Adds an element to the set.                          |               |
| set.remove(element)      | Removes an element from the set; raises an error if  |               |
|                          | the element is not present.                          |               |
| set.discard(element)     | Removes an element from the set if it's present,     |               |
|                          | otherwise does nothing.                              |               |
| set.pop()                | Removes and returns an arbitrary element from the    |               |
|                          | set; raises an error if the set is empty.            |               |
| set.clear()              | Removes all elements from the set.                   |               |
| set.copy()               | Returns a shallow copy of the set.                   |               |
| set.union(other_set)     | Returns a new set containing all elements from both  | set1 | set2   |
|                          | sets.                                                |               |
| set.intersection(other)  | Returns a new set containing common elements of      | set1 & set2   |
|                          | both sets.                                           |               |
| set.difference(other)    | Returns a new set with elements from the first set   | set1 - set2   |
|                          | that are not in the second set.                      |               |
| set.symmetric_difference | Returns a new set with elements that are in either   | set1 ^ set2   |
|   (other)                | set, but not in both.                                |               |
| set.issubset(other)      | The issubset() method returns True if all items in   |               |
|                          |   the set exists in the specified set, otherwise it  |               |
|                          | returns False.                                       | set1 <= set2  |
| set.issuperset(other)    | The issuperset() method returns True if all items in | set1 <= set2  |
|                          | the specified set exists in the original set,        |               |
|                          | otherwise  it returns False.                         |               |
|                          |                                                      |               |                                
| set.isdisjoint(other)    | Checks if the set has no elements in common with     |               |
|                          | another set.Return True if no items common in both set               |                          |               |
+--------------------------+-------------------------------------------------------+---------------+
'''


#string
#1.rpartition
# The str.rpartition() method searches for the last occurrence
# of a specified string, and splits the string into a tuple containing three elements.
# ("I could eat bananas all day,"," bananas",are my favorite fruit")
#create partion from last occurrence of the word "bananas", and return a tuple with three elements:

#2 split()-The split() method splits a string into a list.split each word
#welcome to the jungle - ["welcome","to","the","jungle"]

#3 startswith()-The startswith() method returns True if the string starts with
 # the specified value, otherwise False.  string.startswith(value, start, end)

#4 strip() -Remove spaces at the beginning and at the end of the string

#5.swapcase()-Make the lower case letters upper case and the upper case letters lower case:

#title()- The title() method returns a string where the first
# character in every word is upper case. Like a header, or a title.



#1.all()
# mylist = [0, 1, 1]#he all() function returns True if all items in an iterable are true
# x = all(mylist) #it return false if 0 is in list
               # in dictionary it can check keys only if 0 are in keys then output is false

#2.bin()  #The bin() function returns the binary version of a specified integer
# a=bin(10) # The result will always have the prefix 0b
# print(a)

#3.callable()
# def a():
#     b=5              #The callable() function returns True if the specified object is callable,
# print(callable(a))   #otherwise it returns False. it use only in def function


#5.divmod()
# a=divmod(11,3) #The divmod() function returns a tuple containing the quotient  and the remainder
# print(a)      # when argument1 (dividend) is divided by argument2 (divisor).(quotient-3,Remainder-2)

#6.enumerate
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate objec


#7.filter() function:-function that tests if each element of a sequence is true or not.
# sets, lists, tuples, or containers of any iterators.
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def is_multiple_of_3(num):
# 	return num % 3 == 0
# # number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Use filter and a lambda function to
# # filter the list of numbers and only
# # keep the ones that are multiples of 3
# result = list(filter(lambda x: is_multiple_of_3(x), num))

# Print the result
# print(result)

# a list contains both even and odd numbers. find Odd and even
# seq = [0, 1, 2, 3, 5, 8, 13]
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result))

# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))

#8.format()
# x = format(50, '%')#The format() function formats a specified value into a specified format.
# print(x)          #ex-'+' Use a plus sign to indicate if the result is positive or negative
                  #'b' - Binary format,'n' - Number format etc....
                  #%s store string and %d store integer value
                  #f("{:.2f}") print 2point decimal value




# 9.globals() or locals
# x = globals()#Get the filename of the current program:
# print(x["__file__"])
# x = locals()Get the filename of the current program:
# print(x["__file__"])

#10. iter()
#1.
# x = iter(["apple", "banana", "cherry"])
# print(next(x))# function- returns an iterator object.Required. An iterable object
# print(next(x))#The next() function returns the next item in an iterator.
# print(next(x))
#2.
# mylist = iter(["apple", "banana", "cherry"])
# x = next(mylist)
# print(x)

#11. map()         # function executes a specified function for each item in an iterable.
#1.
# def myfunc(a,b): # The item is sent to the function as a parameter
#     return a+b   #map(function, iterables)
# x = map(myfunc,('apple', 'banana', 'cherry'),("1","2","3"))
# print(list(x))   # convert the map into a list, for readability:
#
# #2.
# def myfunc(a):
#   return len(a) # it shows len of each element
# x = map(myfunc, ('apple', 'banana', 'cherry'))
# print(list(x))


#12.pow()
# a= pow(4, 3)#4 to the power of 3 (same as 4 * 4 * 4):
# print(a)#The pow() function returns the value of x to the power of y (xy).
# #If a third parameter is present, it returns x to the power of y, modulus z.
# b = pow(4, 3, 6)#4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):
# print(b)

#13.print()
# print("Hello", "how are you?", sep="---")#Hello---how are you? separator
            #end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)

#14.reversed() -Reverse the sequence of a list, and print each item
# alph = ["a", "b", "c", "d"]
# ralph = reversed(alph)
# for x in ralph:
#   print(x,end=",")

#reverse list
# alph = ["a", "b", "c", "d"]
# reversed_alph = [alph[i] for i in range(len(alph) -1, -1, -1)]
# print(reversed_alph)


#15. zip()
# The zip() function returns a zip object, which is an iterator of tuples where
# the first item in each passed iterator is paired together, and then the second
# item in each passed iterator are paired together etc.
#If one tuple contains more items, these items are ignored:


# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
# x = zip(a,b)
# print(list(x))# dict() tuple() set()


#16.maketrans() #replace function is better than this keyword
#The maketrans() method returns a mapping table
#that can be used with the translate() method to replace specified characters.
# txt = "Hi Sam!"
# x = "mSa"     #  x replaced by y string
# y = "eJo"     # J is placed at same index of S similarly e&m ,and o&a
# mytable = str.maketrans(x, y) # 3rd place charecter (z) remove from the string which is store in
# print(txt.translate(mytable)) # 3rd place  variable z="i" it removes print H only

#replace function is better than this keyword
# txt = "Hi Sam "
# a=txt.replace("sam","joe")
# print(a)

#17. rfind()  #The rfind() method finds the last occurrence of the specified value. find() finding 1st occurance
# txt = "Mi casa, su casa."  # use with rfind(12) and find(3) #W3 school
# x = txt.rfind("casa")  #rfind() same as rindex()
# print(x)

# txt = "Hello, welcome to my world." # rfind(value,start,end)
# x = txt.rfind("e",5,10) #5is starting value and 10 is ending
# print(x)                #it finding "e" from 5 to 10


# #17.removes duplicate from list
# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

# #18.reverse string
# txt = "Hello World"[::-1]
# print(txt)


#19.Class
#calling a class method from another class method

# class ABC:
#     def __init__(self,var):
#         self.var=var
#     def display(self):
#         print("value:-",self.var)
#     def add(self):
#         self.var+=2
#         self.display()
#
# obj = ABC(10)
# obj.add()       # call second method second method add 1st method value


# call the function defined global name space and
# calling class method from another class method
# def sq(x):
#     return  x*10
# class ABC:
#     def __init__(self,var):
#         self.var=var
#     def display(self):
#         print("value of  var is :- ",self.var)
#     def sqr(self):
#         self.var=sq(self.var)
#         self.display()
# obj=ABC(10)
# obj.display()
# obj.sqr()

# program to add variables to class at run time
# #modify variable and delet variable
#
# # class addrem:
# #     def __init__(self,var):
# #         self.var=var
# #     def display(self):
# #         print("value of var is ",self.var)
# # obj=addrem(10)
# # obj.display()
# #
# # #add new variable
# # obj.new_var=20
# # print("new variable value:- ",obj.new_var)
#
# #modification
# obj.new_var=30
# print("modify variable:-",obj.new_var)
# #delet variable
# del obj.new_var # deleted newly added variable
# #print(obj.new_var) # it shows attribute error




#20.1. dir,dict,help
# dir()- function is used to retrieve a list of valid attributes and
# methods available for a given object. when you pass an object as an argument
# to dir(), it will return a list of attributes and methods that can be accessed
# on that object.
# my_list = [1, 2, 3]   # This will print the list of attributes and methods for
# print(dir(my_list))   # the my_list object

#2.__dict__-this attribute returns a dictionary representation of an object's
#attribute
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.salary=100000
#
# p=person('rohit',25)
# print(p.__dict__)
#
#3.help()-this function use to get help documentation for an object,including a
# description of its atributes and methods
# print(help(classmethod))


#21 super()
# some time you want to use the parent class methods in the child class
#using  super keyword possible to access it


# class cricket:
#     def player(self, name, age):
#         self.name=name
#         self.age = age
#         print(self.name,self.age)
# class team(cricket): #inheritence method parent - child
#     def player1(self, name, age, team1):
#         super().player(name,age)
#         self.team1 = team1
#         print(self.name,self.age,self.team1)
#
# one= cricket()
# one.player("virat",36)
# two=team()
# two.player1("Rohit", 36,"india")
# print(one.name)



#22.static method
# Calling the static method without creating instance
#this method does not use self argument
#is defined using built in function @staticmethod
#syntax-print(classname.method(argument))
# class MathOperations:
#     @staticmethod
#     def add(x, y):
#         return x + y
#
# print( MathOperations.add(5, 3))  # Calling the static method without creating instance

#23.classmethod - class method as alternative converter when data in other format(string)
#data is in string format string='ajit,50000' use
# class person:
#     def __init__(self, name, salary):   # without class method it shows
#         self.name = name                #incorrect call argument
#         self.salary = salary            #parameter string unfilled
#
#     @classmethod                        #create variable as per separating
#     def fromstring(cls,string):         #the string 2separation requiring 2
#         name, salary = string.split(',')#variable
#         return cls (name,float(salary))
#
# person=person.fromstring('ajit,50000') # string format data in argument
# print("name- ",person.name,"\nsalary- ",person.salary)


