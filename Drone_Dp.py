class droneDeliverySystem:

    def __init__(self):
        self.movements=[[0,1],[1,0],[-1,0],[0,-1]]

    def printMatrix(self,m):
        print("Matrix is :")
        r,c=len(m),len(m[0])
        for i in range(r):
            for j in range(c):
                print(m[i][j],end="\t")
            print("\n")

    def getMinTimeDP(self, m, start_location, destination_location):
        r, c = len(m), len(m[0])
        dpMatrix = [[float('inf') for _ in range(c)] for _ in range(r)]
        dpMatrix[start_location[0]][start_location[1]] = 0  
        l=[[start_location[0],start_location[1],0, [start_location]]]
        while l:
            x, y, time, path = l.pop(0)
            if [x, y] == destination_location:
                return time, path
            for i, j in self.movements:  
                tx, ty = x + i, y + j
                if 0 <= tx < r and 0 <= ty < c:
                    if m[tx][ty] == 1:
                        continue
                    # Calculate new time
                    if m[tx][ty] == 2:
                        new_time = time
                    else :
                        new_time=time + 1
                    # Update DP and add to queue if shorter path found
                    if new_time < dpMatrix[tx][ty]:
                        dpMatrix[tx][ty] = new_time
                        if m[tx][ty] == 2:
                            l=[[tx,ty,new_time,path+[[tx,ty]]]] + l
                        else:
                            l.append([tx, ty, new_time, path + [[tx, ty]]])
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
minTime,path=ob.getMinTimeDP(m,start,end)      
ob.printMatrix(m)                
print("Minimum Time = ",minTime )
print("Path : ", path)

                        


                

                    









