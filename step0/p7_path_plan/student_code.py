import heapq
import math
import copy

class Path():
    def __init__(self):
        self.list = []
    def get(self):
        return self.list
    def add(self,node):
        self.list.append(node)
    def end(self):
        return self.list[-1]
def print_path(path):
    for node in path.list:
        print(node.id,end=',')
    print("")
    
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    def len(self):
        return len(self._queue)
class Frontier():
    def __init__(self):
        self.queue = PriorityQueue()
        self.set = set()
    def set_goal(self,goal):
        self.goal = goal
        
    def add(self,path,M):
        cost = path.end().g_cost + path.end().h_cost
        self.queue.push(path,cost)
        self.set.add(path)
        #print("add new path,cost=",cost)
        #print_path(path)
        
    def choice(self,M):
        path = self.queue.pop()
        self.set.remove(path)
        
        return path
    
class Explored():
    def __init__(self):
        self.set = set()
class Node():
    def __init__(self,id,state,actions,g_cost,h_cost,parent):
        self.id = id
        self.state = state
        self.actions = actions
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent
def distance(id1,id2,M):
    dist = math.sqrt(math.pow(abs( M.intersections[id1][0]- M.intersections[id2][0]),2) + math.pow(abs( M.intersections[id1][1]- M.intersections[id2][1]),2))
    return dist
def Result(node,id,goal,M):
    g_cost = node.g_cost + distance(node.id,id,M)
    h_cost = heuristic_cost_estimate(id,goal,M)
    return Node(id,1,M.roads[id],g_cost,h_cost,node)
def path_2_answer(path):
    answer = []
    for node in path.list:
        answer.append(node.id)
    print(answer)
    return answer
def heuristic_cost_estimate(start,goal,M):
    dist = math.sqrt(math.pow(abs( M.intersections[start][0]- M.intersections[goal][0]),2) + math.pow(abs( M.intersections[start][1]- M.intersections[goal][1]),2))
    return dist
    
def shortest_path(M,start,goal):
    '''
    for key,value in M.intersections.items():
        print(key,value)
    num = 0
    for item in M.roads:
        print(num,item)
        num += 1
    '''
    print("shortest path called")
    node = Node(start,1,M.roads[start],0,heuristic_cost_estimate(start,goal,M),start)
    frontier = Frontier()
    frontier.set_goal(goal)
    path = Path()
    path.add(node)
    frontier.add(path,M)         
    
    explored = Explored()
    
    while frontier.queue.len() > 0:
        path_choice = frontier.choice(M)#get from frontier
        s = path_choice.end()
        
        if s.id == goal:
            return path_2_answer(path_choice)
        
        if s.id in explored.set:   #避免多余的搜索
            continue
            
        explored.set.add(s.id)    #add s to explored
        #print("explored.set:",explored.set)
        
        
        for id in s.actions:
            if id in explored.set:
                continue
            node_new = Result(s,id,goal,M)
            path_new = copy.deepcopy(path_choice)
            path_new.add(node_new)
    
            #if node_new.id not in frontier.set and node_new.id not in explored.set: #add[path+a > Result(s,a)]
            if node_new.id not in explored.set:
                frontier.add(path_new,M)    #to frontier
     ret = []
     return ret