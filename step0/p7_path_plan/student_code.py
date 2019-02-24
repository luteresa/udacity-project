import heapq
import math
import copy
    
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
        self.openSet = {}
    def set_goal(self,goal):
        self.goal = goal
        
    def add(self,node):
        cost = node.g_cost + node.h_cost
        self.queue.push(node,cost)
        #self.set.add({path.end().id:path.end()})
        self.openSet[node.id] = node
        #print("g_cost:{},h_cost:{}".format(node.g_cost,node.h_cost))
        #print("add new path,cost=",cost)
        #print_path(path)
        
    def choice(self):
        node = self.queue.pop()
        del self.openSet[node.id]
        
        return node
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

def heuristic_cost_estimate(start,goal,M):
    dist = math.sqrt(math.pow(abs( M.intersections[start][0]- M.intersections[goal][0]),2) + math.pow(abs( M.intersections[start][1]- M.intersections[goal][1]),2))
    return dist
def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.append(current)
    print("return path:",total_path)
    return total_path[::-1]  
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
    frontier.add(node)    
    
    cameFrom={}

    gScore={}
    gScore[start] = 0
    fScore={}
    fScore[start] = heuristic_cost_estimate(start,goal,M)
    
    explored = set()
    
    while frontier.queue.len() > 0:
        cur_node = frontier.choice()#get from frontier
        
        if cur_node.id == goal:
            return reconstruct_path(cameFrom,cur_node.id)
        
        if cur_node.id in explored:   #避免多余的搜索
            continue
            
        explored.add(cur_node.id)    #add s to explored
        
        #print("explored.set:",explored.set) 
        
        for neighbor_id in cur_node.actions:
            if neighbor_id in explored:
                continue
        
            tentative_gScore = gScore[cur_node.id] + distance(cur_node.id,neighbor_id,M)
            
            #if node_new.id not in frontier.set and node_new.id not in explored.set: #add[path+a > Result(s,a)]
            if neighbor_id not in frontier.openSet:
                node_new = Result(cur_node,neighbor_id,goal,M)
                frontier.add(node_new)    #to frontier
            elif tentative_gScore >= gScore[neighbor_id]:
                continue
            
            cameFrom[neighbor_id]=cur_node.id
            gScore[neighbor_id] = tentative_gScore
            fScore[neighbor_id] = gScore[neighbor_id] + heuristic_cost_estimate(neighbor_id,goal,M)
    return False
