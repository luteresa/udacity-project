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
class Node():
    def __init__(self,id,state,action,cost,parent):
        self.id = id
        self.state = state
        self.action = action
        self.cost = cost
        self.parent = parent
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
        cost = path.end().cost #+distance(path.end().id,self.goal,M)
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
    def __init__(self,id,state,actions,cost,parent):
        self.id = id
        self.state = state
        self.actions = actions
        self.cost = cost
        self.parent = parent
def distance(id1,id2,M):
    dist = math.sqrt(math.pow(abs( M.intersections[id1][0]- M.intersections[id2][0]),2) + math.pow(abs( M.intersections[id1][1]- M.intersections[id2][1]),2))
    return dist
def Result(node,id,M):
    cost = node.cost + distance(node.id,id,M)
    return Node(id,1,M.roads[id],cost,node)
def path_2_answer(path):
    answer = []
    for node in path.list:
        answer.append(node.id)
    print(answer)
    return answer
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
    node = Node(start,1,M.roads[start],0,start)
    frontier = Frontier()
    frontier.set_goal(goal)
    path = Path()
    path.add(node)
    frontier.add(path,M)         
    
    explored = Explored()
    
    while True:
        if frontier.queue.len() < 1:
            return []
      
        path_choice = frontier.choice(M)#get from frontier
        s = path_choice.end()
        if s.id in explored.set:   #避免多余的搜索
            continue
            
        explored.set.add(s.id)    #add s to explored
        #print("explored.set:",explored.set)
        
        if s.id == goal:
            return path_2_answer(path_choice)
        
        for id in s.actions:
            node_new = Result(s,id,M)
            path_new = copy.deepcopy(path_choice)
            path_new.add(node_new)
    
            #if node_new.id not in frontier.set and node_new.id not in explored.set: #add[path+a > Result(s,a)]
            if node_new.id not in explored.set:
                frontier.add(path_new,M)    #to frontier