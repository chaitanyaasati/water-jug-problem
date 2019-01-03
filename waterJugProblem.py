# -*- coding: utf-8 -*-
import networkx as nx
import queue as q
import matplotlib.pyplot as plt

def generateTree(jug1,jug2):
    
    class rules:
        
        def __init__(self,j1,j2):
            self.j1=j1
            self.j2=j2
            
        def emptyj1(self,state):
            state=list(state)
            state[0]=0
            return tuple(state)
        
        def fillj1(self,state):
            state=list(state)
            state[0]=self.j1
            return tuple(state)
        
        def emptyj2(self,state):
            state=list(state)
            state[1]=0
            return tuple(state)
                    
        def fillj2(self,state):
            state=list(state)
            state[1]=self.j2
            return tuple(state)
        
        def transj1toj2(self,state):
            state=list(state)
            state[0],state[1]=max(0,state[1]+state[0]-self.j2),min(self.j2,state[1]+state[0])
            return tuple(state)    
                
        def transj2toj1(self,state):
            state=list(state)
            state[0],state[1]=min(self.j1,state[1]+state[0]),max(0,state[1]+state[0]-self.j1)
            return tuple(state)
            
        def applyAll(self,state):
            l=[]
            l.append(self.emptyj1(state))
            l.append(self.fillj1(state))
            l.append(self.emptyj2(state))
            l.append(self.fillj2(state))
            l.append(self.transj1toj2(state))
            l.append(self.transj2toj1(state))
            return l
                
    rule=rules(jug1,jug2)            
    node=(0,0)
    G=nx.Graph()
    G.add_node(node)
    Q=q.Queue(50)
    while(True):
        l=rule.applyAll(node)
        for i in l:
            if not G.has_node(i):
                G.add_node(i,time=i)
                G.add_edge(node,i)
                Q.put(i)
        if(Q.empty()):
            break
        node=Q.get()              
    return G  
    
def generatePath(G,goal):
    j=0
    flag=0
    l=list(nx.bfs_edges(G,(0,0)))
    for i in l:
       if(i[1]==goal):
          k=i[0]
          h=[]
          h.append(i)
          while(k!=(0,0)):
              if(l[j][1]==k):
                  k=l[j][0]
                  h.append(l[j])
              j=j-1
          flag=1    
          break    
       j=+1   
    if(flag!=0):
        h.reverse()
        print(h)
    else:
        print("No Solution")

jug1=int(input("Enter JUG1 SIZE\n"))
jug2=int(input("Enter JUG2 SIZE\n"))
goal=[]
goal.append(int(input("Enter JUG1 TARGET\n")))
goal.append(int(input("Enter JUG2 TARGET\n")))
G=generateTree(jug1,jug2)
generatePath(G,tuple(goal))   


            
            
    
    
        
        
        
        
        
        
        