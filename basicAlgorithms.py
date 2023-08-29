#Sort

# Selection sort is a simple and efficient sorting algorithm that
# works by repeatedly selecting the smallest (or largest) element
# from the unsorted portion of the list and moving it to the sorted 
# portion of the list. 

# https://www.geeksforgeeks.org/selection-sort/

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# Check
# print(selectionSort([5, 3, 6, 2, 10])) 

# -----



#Recursion 

# The process in which a function calls itself directly or indirectly 
# is called recursion and the corresponding function is called a recursive 
# function.

# https://www.geeksforgeeks.org/introduction-to-recursion-data-structure-and-algorithm-tutorials/

def countdown(i):
    print(i)
    if i <= 0: #Это база
        return
    else:
        countdown(i - 1) #Рекурсивный случай
   
# Check        
# countdown(5)

# -----



#Stack

# Datastructure

# https://www.geeksforgeeks.org/stack-data-structure/

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()
    
def greet2(name):
    print("how are you, " + name + "?")
    
def bye():
    print("ok, bye!")

# Check
# greet("Ann")

# -----



#Quicksort

# QuickSort is a sorting algorithm based on the Divide and Conquer
# algorithm that picks an element as a pivot and partitions the given
# array around the picked pivot by placing the pivot in its correct 
# position in the sorted array.

# https://www.geeksforgeeks.org/quick-sort/

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0] # Рекурсивный случай/выбор опорного элемента
        less = [i for i in arr[1:] if i <= pivot] # Подмассив элементов меньше опорного
        greater = [i for i in arr[1:] if i > pivot] # Подмассив элементов больше опорного
        
        return quickSort(less) + [pivot] + quickSort(greater)

# Check
# print(quickSort([10, 5, 2, 3]))
    
# -----
  
  
    
# Hash

# Hashing is a technique or process of mapping keys, and values
# into the hash table by using a hash function. It is done for 
# faster access to elements. The efficiency of mapping depends 
# on the efficiency of the hash function used.

# https://www.geeksforgeeks.org/hashing-data-structure/

voted = {}
def checkVoter(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = True
        print('let them vote')
        
# Check
# checkVoter('Tom')
# checkVoter('Mike')
# checkVoter('Mike')    
    
# -----



#Wide search (Breadth First Search or BFS for a Graph)

# The Breadth First Search (BFS) algorithm is used to search a graph 
# data structure for a node that meets a set of criteria. It starts at 
# the root of the graph and visits all nodes at the current depth level 
# before moving on to the nodes at the next depth level.

# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

from collections import deque

graph = {}
graph["you"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Fred", "Anji", "Peggy"]
graph["Alice"] = ["Andy", "Peggy", "Anji"]
graph["Claire"] = ["Tom", "Tim", "Bob"]
graph["Fred"] = []
graph["Anji"] = []
graph["Peggy"] = []
graph["Andy"] = []
graph["Tom"] = []
graph["Tim"] = []

def person_is_seller(name):
    if name == "Fred":
        return True
    else:
        return False
    
def search(name): 
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

# Check
# search("you")

# -----



#Binary Search

# Binary Search is defined as a searching algorithm used in a sorted 
# array by repeatedly dividing the search interval in half. The idea 
# of binary search is to use the information that the array is sorted 
# and reduce the time complexity to O(log N).

# https://www.geeksforgeeks.org/binary-search/

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid, count
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        count += 1
    return None, count
     
# Check

# my_List = [1, 3, 5, 7, 9, 10, 17, 18, 20, 21, 22, 45, 55, 56, 57, 59, 61, 64, 65, 70]

# print (binary_search(my_List, 7)) # 3
# print (binary_search(my_List, 45)) # 11

# -----



#Deykstra Algorytm

# В отличии от поиска в ширину ищет не путь с меньшим числом узлом
# А путь с меньшим суммарным весом
# Работает только с направленными ациклическими графами DAG (Directed Acyclic Graph)
# Ошибается с графами в которых есть отрицательные веса
# А Беллмана-Форда - работает с отрицательными весами

# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['fin'] = 5
graph['b']['a'] = 3
graph['fin'] = {}

infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = "start"
parents['b'] = "start"
parents['fin'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
# Check
# print(costs['fin']) #6 получилось

# -----

#Greedy Algorithms

# Greedy is an algorithmic paradigm that builds up a solution piece
# by piece, always choosing the next piece that offers the most obvious
# and immediate benefit. So the problems where choosing locally optimal 
# also leads to global solution are the best fit for Greedy.

# https://www.geeksforgeeks.org/greedy-algorithms/

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# Структура данных - множество (каждый элемент может встречаться не более одного раза)
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['id', 'wa', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered

# Check
# print(final_stations) 

# -----

# NEXT >>>>>
# ------------Dynamic prog

# Обязательно построение таблицы
# С более малыми подмножествами

# ------------------- K - соседи
# Стандартный алгоритм использует замер по расстоянию (ф. Пифагора)
# Использование метрики косинусов в данном алгоритме лучше для случаев, когда есть оценки (например фильмов)


#! Далее

# Базы данных
# Б - деревья 
# красно-черные деревья
# кучи
# скошенные (splay) деревья

# Поисковые системы
# инвертированные индексы

# Преобразование Фурье

# вероятностные алгоритмы
# Фильтры блума
# HyperLogLog

# Алгоритмы хеширования SHA

# Шифрования односторонние - двусторонние

# Оптимизация - Линейное программирование

