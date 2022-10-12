import curses

w=0
g=1
r=2
b=3
o=4
y=5

t=0
l=1
f=2
r=3
b=4
bo=5

H=0
V=1
S=2


class Face:
    def __init__(self, color):
        self.c = color
        self.arr = [[color for i in range (3)] for i in range(3)]
    


class Cube:
    def __init__(self):
        self.cube = [Face(color).arr for color in range (6)]
        
    def printFace(self,face):
        for j in self.cube[face]:
            print(j)      
    
    def printCube(self):
        print()
        for i in range(3):
            print ("         ", end = " ")
            print(self.cube[t][i]) 
        for i in range(3):
            for j in range(1,5):
                print(self.cube[j][i], end = " ")
            print()     
        for i in range(3):
            print ("         ", end = " ")
            print(self.cube[bo][i])
    
    def getColor(self,num):
        if num==0:
            return "W"
        elif num==1:
            return "G"
        elif num==2:
            return "R"
        elif num==3:
            return "B"
        elif num==4:
            return "O"
        elif num==5:
            return "Y"
    
    def addStrCube(self,centerX):
        string = ''
        for i in range(3):
            arr = self.cube[t][i]
            string +=  ''.join([" " for i in range(centerX)]) + "   " + ''.join([self.getColor(val) for val in arr]) + "\n" 
        for i in range(3):
            string +=''.join([" " for i in range(centerX)]) 
            for j in range(1,5):
                arr = self.cube[j][i]
                string += ''.join([self.getColor(val) for val in arr])
            string+= "\n"    
        for i in range(3):
            arr = self.cube[bo][i]
            string +=  ''.join([" " for i in range(centerX)]) + "   " + ''.join([self.getColor(val) for val in arr]) + "\n" 
        return string
        
    def addCube(self,o):
        o.addstr(curses.LINES // 2, 0, self.addStrCube(curses.COLS // 2 - 6),curses.color_pair(1))
    

    def rotateFace(self,face,direction):
        tempArr = [[0 for i in range(3)] for i in range(3)]
        
        for i in range(3):
            for j in range(3):
                tempArr[i][j] = self.cube[face][i][j]
                
        if direction==-1:
            for i in range(3):
                for j in range(3):
                    self.cube[face][i][j] = tempArr[j][2-i]
                    
        else:
            for i in range(3):
                for j in range(3):
                    self.cube[face][i][j] = tempArr[2-j][i]
                    
    def rotateCube(self, orientation, direction):
        if orientation == H:
            if direction == -1:
                temp = self.cube[l]
                for i in range(1,4):
                    self.cube[i] = self.cube[i+1]
                self.cube[b] = temp
                self.rotateFace(t,1)
                self.rotateFace(bo,-1)
                
            else:
                temp = self.cube[b]
                for i in reversed(range(1,5)):
                    self.cube[i] = self.cube[i-1]
                self.cube[l] = temp
                self.rotateFace(t,-1)
                self.rotateFace(bo,1)
                
        elif orientation == V:
            if direction == -1:
                temp = self.cube[b]
                self.cube[b] = self.cube[bo]
                self.rotateFace(b,-1)
                self.rotateFace(b,-1)
                self.cube[bo] = self.cube[f]
                self.cube[f] = self.cube[t]
                self.cube[t]= temp
                self.rotateFace(t,-1)
                self.rotateFace(t,-1)
                
            
                self.rotateFace(l,1)
                self.rotateFace(r,-1)
                
            else:
                temp = self.cube[b]
                self.cube[b] = self.cube[t]
                self.rotateFace(b,-1)
                self.rotateFace(b,-1)
                self.cube[t] = self.cube[f]
                self.cube[f] = self.cube[bo]
                self.cube[bo]= temp
                self.rotateFace(bo,-1)
                self.rotateFace(bo,-1)
                
            
                self.rotateFace(l,-1)
                self.rotateFace(r,1)
                
        else:
            
            if direction==-1:
                temp = self.cube[t]
                self.cube[t] = self.cube[r]
                self.cube[r] = self.cube[bo]
                self.cube[bo] = self.cube[l]
                self.cube[l] = temp
                
                
            else:
                temp = self.cube[t]
                self.cube[t] = self.cube[l]
                self.cube[l] = self.cube[bo]
                self.cube[bo] = self.cube[r]
                self.cube[r] = temp
                
            for i in range(6):
                if i==4:
                    self.rotateFace(b,-direction)
                else:
                    self.rotateFace(i,direction)
                

    def rotateChunk(self,direction):
        
        if direction==-1:
            tempArr = self.cube[l][0]
            for i in range(1,4):
                self.cube[i][0] = self.cube[i+1][0]
            self.cube[b][0] = tempArr
            self.rotateFace(t,1)
            
        else:
            tempArr = self.cube[b][0]
            for i in reversed(range(1,5)):
                self.cube[i][0] = self.cube[i-1][0]
            self.cube[l][0] = tempArr
            self.rotateFace(t,-1)
            
    def movU(self,d):
        self.rotateChunk(d)
    def movD(self,d):
        self.rotateCube(S,1)
        self.rotateCube(S,1)
        self.rotateChunk(-d)
        self.rotateCube(S,1)
        self.rotateCube(S,1)
    
    def movR(self,d):
        self.rotateCube(S,-1)
        self.rotateChunk(-d)
        self.rotateCube(S,1)
    def movL(self,d):
        self.rotateCube(S,1)
        self.rotateChunk(d)
        self.rotateCube(S,-1)
    
    def movF(self,d):
        self.rotateCube(V,1)
        self.rotateChunk(-d)
        self.rotateCube(V,-1)
    def movB(self,d):
        self.rotateCube(V,-1)
        self.rotateChunk(d)
        self.rotateCube(V,1)
    
    
    
if __name__ == '__main__':
          
    cube = Cube()
    cube.printCube()
  
    
    stdscr = curses.initscr()   
    curses.noecho()             
    curses.cbreak()             
                                    
    stdscr.keypad(1)            
    curses.start_color()
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)
    stdscr.bkgd(' ', curses.color_pair(1))
    
    cube.addCube(stdscr)
    while True:
        
        stdscr.addstr(10, curses.LINES//2 + len("RUBIX CUBE SIMULATOR")//2,"RUBIX CUBE SIMULATOR", curses.color_pair(1))
        ch = stdscr.getch()
        
        if ch == ord('q'):
            break
        elif ch== ord('w'):
            cube.movU(1)
            cube.addCube(stdscr)
        elif ch== ord('e'):
            cube.movU(-1)
            cube.addCube(stdscr)
        elif ch== ord('r'):
            cube.movD(1)
            cube.addCube(stdscr)
        elif ch== ord('t'):
            cube.movD(-1)
            cube.addCube(stdscr)
        elif ch== ord('a'):
            cube.movR(1)
            cube.addCube(stdscr)
        elif ch== ord('s'):
            cube.movR(-1)
            cube.addCube(stdscr)
        elif ch== ord('d'):
            cube.movL(1)
            cube.addCube(stdscr)
        elif ch== ord('f'):
            cube.movL(-1)
            cube.addCube(stdscr)
        elif ch== ord('z'):
            cube.movF(1)
            cube.addCube(stdscr)
        elif ch== ord('x'):
            cube.movF(-1)
            cube.addCube(stdscr)
        elif ch== ord('c'):
            cube.movB(1)
            cube.addCube(stdscr)
        elif ch== ord('v'):
            cube.movB(-1)
            cube.addCube(stdscr)
        elif ch == curses.KEY_UP:
            cube.rotateCube(V,1)
            cube.addCube(stdscr)
        elif ch== curses.KEY_DOWN:
            cube.rotateCube(V,-1)
            cube.addCube(stdscr)
        elif ch== curses.KEY_LEFT:
            cube.rotateCube(H,-1)
            cube.addCube(stdscr)
        elif ch== curses.KEY_RIGHT:
            cube.rotateCube(H,1)
            cube.addCube(stdscr)
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    
    
    cube.printCube()
     