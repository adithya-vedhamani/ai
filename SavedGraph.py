
from Node import Node

def G1():
    graph = {'A' : Node('A',(360 , 466)), 'B' : Node('B', (509, 463), 7), 'C' : Node('C', (500, 331), 6),\
        'D' : Node('D', (487, 186), 7), 'E' : Node('E', (650, 170)),'F' : Node('F', (686, 467)),\
            'G' : Node('G', (789, 309)) }
    graph['A'].children = {'B' : 3, 'C' : 5}
    graph['B'].children = {'A' : 3, 'C' : 4, 'F' : 3}
    graph['C'].children = {'A' : 5, 'B' : 4, 'D' : 4}
    graph['D'].children = {'C' : 4, 'E' : 6}
    graph['E'].children = {'D' : 1}
    graph['F'].children = {'B' : 3, 'G' : 5}
    graph['G'].children = {'F' : 5} 

    return graph, 7

def G2():
    graph = {'A' : Node('A',(322 , 471), 5), 'B' : Node('B', (625, 335), 2), 'C' : Node('C', (468, 336), 4),\
        'D' : Node('D', (508, 250), 5), 'E' : Node('E', (479, 474), 3),'F' : Node('F', (316, 332), 5),\
            'G' : Node('G', (647, 472), 0), 'H' : Node('H', (461, 137), 5)}      
    graph['A'].children = {'E' : 3, 'F' : 3}
    graph['B'].children = {'C' : 3, 'D' : 3, 'H' : 2}
    graph['C'].children = {'B' : 3, 'D' : 4, 'F' : 3, 'H' : 3}
    graph['D'].children = {'B' : 3, 'C' : 4, 'H' : 3}
    graph['E'].children = {'A' : 3, 'F' : 3, 'G' : 3}
    graph['F'].children = {'A' : 3, 'C' : 3, 'E' : 3, 'H' : 4}
    graph['G'].children = {'E' : 3} 
    graph['H'].children = {'B' : 2, 'C' : 3, 'D' : 3, 'F' : 4}                                                   

    return graph, 8
