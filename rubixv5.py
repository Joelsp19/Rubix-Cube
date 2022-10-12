import curses
import pygame,sys
from pygame.locals import *
import math

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
        self.mov = []
        self.char = u"\u25A0"
        
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
    
    def getColorLetter(self,num):
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
   
    def getColor(self,color):
        if color == 0:
            return (255,255,255)
        elif color== 1:
            return (0,255,0)
        elif color == 2:
            return (255,0,0)
        elif color==3:
            return (0,255,255)
        elif color==4:
            return (255,165,0)
        elif color==5:
            return (255,255,0)
    

       
    def addCube(self):
        x=250 
        y=250
        
        for face in [2,3,0]:
            for i in range(3):
                for j in range(3):
                    if face==2: 
                        vl=int(50-((2-j)*10)) 
                        vh = int(60-(i*10))
                        l = int(x +(j*50))
                        h = int((i*70) + y + j*25)  
                        o=int(vl/2)
                        color = self.getColor(self.cube[face][i][j])
                        pygame.draw.polygon(screen,color,((l,h),(l+vl,h+o),(l+vl,h+o+vh),(l,h+vh)))
                    if face==3:
                        vl=int(50-((j)*10)) 
                        vh = int(60-((i)*10))
                        l = int(x+150+12 +(j*60))
                        h = int((i*70) + y+75 - j*30)  
                        o=int(vl/2)
                        color = self.getColor(self.cube[face][i][j])
                        pygame.draw.polygon(screen,color,((l,h),(l+vl,h-o),(l+vl,h-o+vh),(l,h+vh)))
                    if face==0:
                        vl=int(50-((2-j)*10))
                        vl2=int(50-((2-i)*10))
                        
                        l = int(x+133 +(j*50) - i*60)
                        h = int((i*30) + y-75+j*25)
                        o=int(vl/2 -2)
                        o2=int(vl2/2 -2)
                        xMov = int(math.sqrt(vl*vl - o*o)) 
                        xMov2= int(math.sqrt(vl2*vl2 - o2*o2))
                        color = self.getColor(self.cube[face][i][j])
                        pygame.draw.polygon(screen,color,((l,h),(l+xMov2,h-o2),(l+xMov2+xMov,h-o2+o),(l+xMov,h+o)))
                    
    def addCubeAllFaces(self):
        x=250 
        y=250
        
        for face in range(6):
            for i in range(3):
                for j in range(3):
                    if face==2: 
                        vl=int(50-((2-j)*10)) 
                        vh = int(60-(i*10))
                        l = int(x +(j*50))
                        h = int((i*70) + y + j*25)  
                        o=int(vl/2)
                        color = self.getColor(self.cube[face][i][j])
                        pygame.draw.polygon(screen,color,((l,h),(l+vl,h+o),(l+vl,h+o+vh),(l,h+vh)))
                    if face==3:
                        vl=int(50-((j)*10)) 
                        vh = int(60-((i)*10))
                        l = int(x+150+12 +(j*60))
                        h = int((i*70) + y+75 - j*30)  
                        o=int(vl/2)
                        color = self.getColor(self.cube[face][i][j])
                        pygame.draw.polygon(screen,color,((l,h),(l+vl,h-o),(l+vl,h-o+vh),(l,h+vh)))
                    if face==0:
                        vl=int(50-((2-j)*10))
                        vl2=int(50-((2-i)*10))
                        
                        l = int(x+133 +(j*50) - i*60)
                        h = int((i*30) + y-75+j*25)
                        o=int(vl/2 -2)
                        o2=int(vl2/2 -2)
                        xMov = int(math.sqrt(vl*vl - o*o)) 
                        xMov2= int(math.sqrt(vl2*vl2 - o2*o2))
                        color = self.getColor(self.cube[face][i][j])
                        pygame.draw.polygon(screen,color,((l,h),(l+xMov2,h-o2),(l+xMov2+xMov,h-o2+o),(l+xMov,h+o)))
        
                    if face==4: 
                        vl=int(50-((2-j)*10)) 
                        vh = int(60-(i*10))
                        l = int(x +(j*50) +330)
                        h = int((i*70) + y + j*25 -180)
                        o=int(vl/2)
                        color = self.getColor(self.cube[face][i][2-j])
                        pygame.draw.polygon(screen,color,((l,h),(l+vl,h+o),(l+vl,h+o+vh),(l,h+vh)))

                    if face==1:
                        vl=int(50-((j)*10)) 
                        vh = int(60-((i)*10))
                        l = int(x-170 +(j*60))
                        h = int((i*70) + y - (j*30) -100)  
                        o=int(vl/2)
                        color = self.getColor(self.cube[face][i][2-j])
                        pygame.draw.polygon(screen,color,((l,h),(l+vl,h-o),(l+vl,h-o+vh),(l,h+vh)))

                    if face==5:
                        vl=int(50-((2-j)*10))
                        vl2=int(50-((2-i)*10))
                        
                        l = int(x+133 +(j*50) - i*60)
                        h = int((i*30) + y+j*25 +300)
                        o=int(vl/2 -2)
                        o2=int(vl2/2 -2)
                        xMov = int(math.sqrt(vl*vl - o*o)) 
                        xMov2= int(math.sqrt(vl2*vl2 - o2*o2))
                        color = self.getColor(self.cube[face][2-i][j])
                        pygame.draw.polygon(screen,color,((l,h),(l+xMov2,h-o2),(l+xMov2+xMov,h-o2+o),(l+xMov,h+o)))
    
    def addCubeFlat(self):
        size =40
        offset=2
        x=int(400/(size+offset)-6)  
        y=int(400/(size+offset)-4) 
        
        for face in range(6):
            for i in range(3):
                for j in range(3):
                    if face==0: 
                        addX=3
                        addY=0
                    elif face==2:
                        addX=3
                        addY=1
                    elif face==5:
                        addX=3
                        addY=2
                    elif face==3:
                        addX=6
                        addY=1
                    elif face==4:
                        addX=9
                        addY=1
                    elif face==1:
                        addX=0
                        addY=1
                    color = self.getColor(self.cube[face][2-i][j])
                    pygame.draw.rect(screen,color,((x+j+addX)*(size+offset),(3*addY+y+i)*(size+offset),size,size))

                    
             
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
    
    def cubeRedo(self):
        if len(self.mov)>0:
            ch = self.mov[len(self.mov)-1]
            self.mov.pop()
            
            if ch== ord('w'):
                cube.movU(-1)
                
            elif ch== ord('e'):
                cube.movU(1)
                
            elif ch== ord('r'):
                cube.movD(-1)
                
            elif ch== ord('t'):
                cube.movD(1)
                
            elif ch== ord('a'):
                cube.movR(-1)
                
            elif ch== ord('s'):
                cube.movR(1)
                
            elif ch== ord('d'):
                cube.movL(-1)
                
            elif ch== ord('f'):
                cube.movL(1)
                
            elif ch== ord('z'):
                cube.movF(-1)
                
            elif ch== ord('x'):
                cube.movF(1)
                
            elif ch== ord('c'):
                cube.movB(-1)
                
            elif ch== ord('v'):
                cube.movB(1)
                
            elif ch == curses.KEY_UP:
                cube.rotateCube(V,-1)
                
            elif ch== curses.KEY_DOWN:
                cube.rotateCube(V,1)
                
            elif ch== curses.KEY_LEFT:
                cube.rotateCube(H,1)
                
            elif ch== curses.KEY_RIGHT:
                cube.rotateCube(H,-1)
        
   
    
## Side note: don't change the size of the terminal window, then it won't be centered
if __name__ == '__main__':
          
    cube = Cube()
    print("starting cube")
    cube.printCube()
  
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    
    cube.addCube()
    showFace=1
    press_redo=False
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
                

            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_w:
                    cube.movU(1)
                    
                elif event.key== pygame.K_e:
                    cube.movU(-1)
                    
                elif event.key== pygame.K_r:
                    cube.movD(1)
                    
                elif event.key== pygame.K_t:
                    cube.movD(-1)
                    
                elif event.key== pygame.K_a:
                    cube.movR(1)
                    
                elif event.key== pygame.K_s:
                    cube.movR(-1)
                    
                elif event.key== pygame.K_d:
                    cube.movL(1)
                    
                elif event.key== pygame.K_f:
                    cube.movL(-1)
                    
                elif event.key== pygame.K_z:
                    cube.movF(1)
                    
                elif event.key== pygame.K_x:
                    cube.movF(-1)
                    
                elif  event.key== pygame.K_c:
                    cube.movB(1)
                    
                elif  event.key== pygame.K_v:
                    cube.movB(-1)
                    
                elif event.key== pygame.K_UP:
                    cube.rotateCube(V,1)
                    
                elif event.key== pygame.K_DOWN:
                    cube.rotateCube(V,-1)
                    
                elif event.key== pygame.K_LEFT:
                    cube.rotateCube(H,-1)
                    
                elif event.key== pygame.K_RIGHT:
                    cube.rotateCube(H,1)
                elif event.key == pygame.K_p:
                    cube.cubeRedo()
                
                elif event.key== pygame.K_o:
                    press_redo= True
                
                elif event.key== pygame.K_l:
                    if showFace==1:
                       showFace=2     
                    elif showFace==2:
                        showFace=3
                    else:
                        showFace=1
      
                if event.key!= pygame.K_p and event.key!= pygame.K_l:
                    cube.mov.append(event.key)    
            
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_o:
                    press_redo = False
            
        if press_redo:
            cube.cubeRedo()
            pygame.time.delay(100)
        
        screen.fill((0,0,0))

        if showFace==1:
            cube.addCube()
        elif showFace==2:
            cube.addCubeAllFaces()

        else:
            cube.addCubeFlat()
      
        
        pygame.display.update()
        
    
    
   
    print("ending cube")
    cube.printCube()
    
    
     