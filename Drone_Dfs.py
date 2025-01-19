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

    def getMinTimeDFS(self, m, start_location, destination_location):
        r, c = len(m), len(m[0])
        visited = [[False for i in range(c)] for j in range(r)]
        min_time = float('inf')
        best_path = []
        def dfs(x, y, time, path):
            nonlocal min_time, best_path
            # If destination is reached
            if [x, y] == destination_location:
                if time < min_time:
                    min_time = time
                    best_path = path[:] 
                return
            visited[x][y] = True
            for i, j in self.movements:
                tx, ty = x + i, y + j
                if 0 <= tx < r and 0 <= ty < c:
                    if visited[tx][ty]==False:
                        if m[tx][ty] == 2:  
                            dfs(tx, ty, time, path + [[tx, ty]])   
                        elif m[tx][ty] == 1:  
                            continue
                        else:  
                            dfs(tx, ty, time + 1, path + [[tx, ty]])
            visited[x][y] = False  # BrackTracking
        dfs(start_location[0], start_location[1], 0, [start_location])
        if min_time != float('inf'):
            return (min_time, best_path)
        else:
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
minTime,path=ob.getMinTimeDFS(m,start,end)      
ob.printMatrix(m)                
print("Minimum Time = ",minTime )
print("Path : ", path)

                        


                

                    









