class droneDeliverySystem:

    def __init__(self):
        self.movements=[[0,1],[1,0],[-1,0],[0,-1]]   #Initializing the directions of Drone

    def printMatrix(self,m): # Grid Matrix
        print("Matrix is :")
        r,c=len(m),len(m[0])
        for i in range(r):
            for j in range(c):
                print(m[i][j],end="\t")
            print("\n")

    def getMinTime(self,m,start_location,destination_location): 
        r,c=len(m),len(m[0])
        l=[[start_location[0],start_location[1],0, [start_location]]]
        visited=[[False for i in range (c) ] for j in range(r)] # Initializing the matrix visited with False to track the nodes
        visited[start_location[0]][start_location[1]]=True
        while l: 
            x,y,time,path=l.pop(0) 
            if [x,y]==destination_location:
                return time ,path
            for i , j in self.movements: 
                tx,ty= x+i , y+j
                if 0<=tx<=r-1 and 0<=ty<=c-1:
                    if not visited[tx][ty]:
                        if m[tx][ty]==2:  
                            l=[[tx,ty,time,path+[[tx,ty]]]] + l 
                        elif m[tx][ty]==1:
                            continue
                        else:
                            l.append([tx,ty,time+1,path+[[tx,ty]]])
                        visited[tx][ty]=True            
        return "Drone cannot be reached"


r=int(input("Enter The Number of Rows: "))
c=int(input("Enter The Number of Coloumns: "))
# 0 represents Buildings
# 1 represents obstacle
# 2 represents Shortcut
m=[[0 for i in range (c) ] for j in range(r)]
obstacles = int(input("Enter The Number of Obstacles: "))
for i in range(obstacles):
    a,b=input("Enter the Obstacle Coordinates: ").split()
    m[int(a)][int(b)]=1
shortcuts = int(input("Enter The Number of Shortcuts: "))    
for i in range(shortcuts):
    x,y=input("Enter the Shortcut Coordinates: ").split()
    m[int(x)][int(y)]=2
a,b=input("Enter the starting Location: ").split()    
start=[int(a),int(b)]
x,y=input("Enter the Destination Location: ").split()    
end=[int(x),int(y)]
ob=droneDeliverySystem()
minTime,path=ob.getMinTime(m,start,end)      
ob.printMatrix(m)                
print("Minimum Time = ",minTime )
print("Path : ", path)

                        


                

                    









