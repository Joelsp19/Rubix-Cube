from random import seed
from random import randint

w=0
g=1
r=2
o=3
b=4
y=5

wface = None
yface = None
gface = None
bface = None
rface = None
oface = None

frontFaceC = w;
topFaceC = b;
leftFaceC = o;

scrambled = []
compCol = lambda col: 5-col

def reset():

    ##white face

    global wface
    wface = [[w for i in range (3)] for i in range(3)]

    ##yellow face

    global yface  
    yface = [[y for i in range (3)] for i in range(3)] 
    ##green face

    global gface
    gface = [[g for i in range (3)] for i in range(3)]
    ##blue face

    global  bface
    bface = [[b for i in range (3)] for i in range(3)]
    ##red face

    global rface 
    rface = [[r for i in range (3)] for i in range(3)]
    ##orange face

    global oface
    oface = [[o for i in range (3)] for i in range(3)]

def scramble(level):
    global scrambled
    
    if(level == "LOW"):
        start = 16
        end = 25
    elif (level == "MEDIUM"):
        start = 26
        end = 35
    elif (level == "HIGH"):
        start = 36
        end = 45
    ranNum1 = randint(start,end)
    ranNum2 = randint(1,4)
    ranNum3 = randint(1,6)
    ranNum4 = randint(0,1)
    ranNum5 = randint(0,1)
    
    det = lambda x: 1 if (x==0) else -1 
    detLOR = lambda x: "left" if(x==0) else "right"
    detUOD = lambda x: "down" if(x==0) else "up"

    for i in range(ranNum1):
        
        scrambled.append([ranNum1,ranNum2, ranNum3, ranNum4, ranNum5])
        
        if ranNum2 == 1:
            rotateCubeH(det(ranNum4))
            scrambled.append("rotate cube horizontally to the " + detLOR(ranNum4))
        elif ranNum2 == 2:
            rotateCubeS(det(ranNum4))
            scrambled.append("rotate cube sideways to the " + detLOR(ranNum4))
        elif ranNum2 == 3:
            rotateCubeV(det(ranNum4))
            scrambled.append("rotate cube vertically " + detUOD(ranNum4) + "-wards" )
        else:
            scrambled.append("no cube rotation" )
        if ranNum3==1:
            rotateB(det(ranNum5))
            scrambled.append("Back turn to the " + detLOR(ranNum5))
        elif ranNum3==2:
            rotateD(det(ranNum5))
            scrambled.append("Down turn to the " + detLOR(ranNum5))
        elif ranNum3==3:
            rotateF(det(ranNum5))
            scrambled.append("Front turn to the " + detLOR(ranNum5))
        elif ranNum3==4:
            rotateL(det(ranNum5))
            scrambled.append("Left turn " + detUOD(ranNum5) + "-wards")
        elif ranNum3==5:
            rotateR(det(ranNum5))
            scrambled.append("Right turn " + detUOD(ranNum5) + "-wards")
        elif ranNum3==6:
            rotateU(det(ranNum5))
            scrambled.append("Up turn to the " + detLOR(ranNum5))
            
        ranNum2 = randint(1,4)
        ranNum3 = randint(1,6)
        ranNum4 = randint(0,1)
        ranNum5 = randint(0,1)
        
def showScrambleInstructions():
    det = lambda x:  '\n' if ((x+1)%3==0) else ''
    det2 = lambda x,c: str(c) + '.' if((x+2)%3==0 or (x+1)%3==0) else ""
    
    print('\n' + "number of steps: " + str(scrambled[0][0] * 2) + '\n')
    count = 1
    for i in range(len(scrambled)):
        print(det2(i,count) + str(scrambled[i]) + det(i))
        if((i+2)%3==0 or (i+1)%3==0):
            count+=1
   

def faceFromColor(col):
    
    if col==w:
        return wface
    elif col==y:
        return yface
    elif col==g:
        return gface
    elif col==b:
        return bface
    elif col==r:
        return rface
    elif col==o:
        return oface
    
def printFace(face):
    
    for j in face:
        print(j)
        print()    

def rotateCubeH(dir):
    global frontFaceC
    global leftFaceC
   
    temp = frontFaceC
    if(dir>0):
        frontFaceC = compCol(leftFaceC)
        leftFaceC = temp
        
        changeArrL(faceFromColor(topFaceC))
        changeArrL(faceFromColor(compCol(topFaceC)))
    else:
        frontFaceC = leftFaceC
        leftFaceC = compCol(temp)
        
        changeArrR(faceFromColor(topFaceC))
        changeArrR(faceFromColor(compCol(topFaceC)))
           
def rotateCubeV(dir):
    global frontFaceC
    global topFaceC
   
    temp = frontFaceC
    if(dir<0):
        frontFaceC = topFaceC
        topFaceC = compCol(temp)
        
        changeArrL(faceFromColor(leftFaceC))
        changeArrL(faceFromColor(compCol(leftFaceC)))
        
        for i in range (2):
            changeArrL(faceFromColor(topFaceC))
            changeArrL(faceFromColor(compCol(topFaceC)))
            
        
    else:
        frontFaceC = compCol(topFaceC)
        topFaceC = temp
        
        changeArrR(faceFromColor(leftFaceC))
        changeArrR(faceFromColor(compCol(leftFaceC)))
        
        for i in range (2):
           changeArrL(faceFromColor(frontFaceC))
           changeArrL(faceFromColor(compCol(frontFaceC)))
            
def rotateCubeS(dir):
    global leftFaceC
    global topFaceC
   
    temp = leftFaceC
    if(dir<0):
        leftFaceC = topFaceC
        topFaceC = compCol(temp)
        
        changeArrR(faceFromColor(frontFaceC))
        changeArrR(faceFromColor(compCol(frontFaceC)))
        
        changeArrR(faceFromColor(topFaceC))
        changeArrR(faceFromColor(compCol(topFaceC)))
    else:
        leftFaceC = compCol(topFaceC)
        topFaceC = temp
        
        changeArrL(faceFromColor(frontFaceC))
        changeArrL(faceFromColor(compCol(frontFaceC)))
        
        changeArrL(faceFromColor(topFaceC))
        changeArrL(faceFromColor(compCol(topFaceC)))

def changeArrL(face):
    
    temp = [[0 for i in range (3)] for i in range(3)]
    
    for r in range(len(face)):
        for c in range(len(face[0])):
            temp[r][c] = face[2-c][r]
         
    for r in range(len(face)):
        for c in range(len(face[0])):
            face[r][c] = temp[r][c]
       
def changeArrR(face):
    
    temp = [[0 for i in range (3)] for i in range(3)]
    
    for r in range(len(face)):
        for c in range(len(face[0])):
            temp[r][c] = face[c][2-c]
         
    for r in range(len(face)):
        for c in range(len(face[0])):
            face[r][c] = temp[r][c]
         
def rotateU(dir):
    ##w-->orange-->yellow--> red  --> white
    ##0--> 3-->5 --> 2 -->0
    
    global frontFaceC
    global leftFaceC
    
    temp = (faceFromColor(frontFaceC))[0]
    if dir<0:
        faceFromColor(frontFaceC)[0] = faceFromColor(compCol(leftFaceC))[0]
        faceFromColor(compCol(leftFaceC))[0] = faceFromColor(compCol(frontFaceC))[0]
        faceFromColor(compCol(frontFaceC))[0] = faceFromColor((leftFaceC))[0]
        faceFromColor((leftFaceC))[0] = temp
    else:
        faceFromColor(frontFaceC)[0] = faceFromColor(leftFaceC)[0]
        faceFromColor(leftFaceC)[0] = faceFromColor(compCol(frontFaceC))[0]
        faceFromColor(compCol(frontFaceC))[0] = faceFromColor(compCol(leftFaceC))[0]
        faceFromColor(compCol(leftFaceC))[0] = temp

def rotateD(dir):
    ##w-->orange-->yellow--> red  --> white
    ##0--> 3-->5 --> 2 -->0
    
    global frontFaceC
    global leftFaceC
    
    temp = (faceFromColor(frontFaceC))[2]
    if dir<0:
        faceFromColor(frontFaceC)[2] = faceFromColor(compCol(leftFaceC))[2]
        faceFromColor(compCol(leftFaceC))[2] = faceFromColor(compCol(frontFaceC))[2]
        faceFromColor(compCol(frontFaceC))[2] = faceFromColor((leftFaceC))[2]
        faceFromColor((leftFaceC))[2] = temp
    else:
        faceFromColor(frontFaceC)[2] = faceFromColor(leftFaceC)[2]
        faceFromColor(leftFaceC)[2] = faceFromColor(compCol(frontFaceC))[2]
        faceFromColor(compCol(frontFaceC))[2] = faceFromColor(compCol(leftFaceC))[2]
        faceFromColor(compCol(leftFaceC))[2] = temp
    
def rotateR(dir):
    rotateCubeS(-1)
    
    if dir<0:
        rotateU(1)
    else:
        rotateU(-1)
        
    rotateCubeS(1)

def rotateL(dir):
    rotateCubeS(1)
    
    if dir<0:
        rotateU(-1)
    else:
        rotateU(1)
        
    rotateCubeS(-1)

def rotateF(dir):
    rotateCubeV(1)
    if dir<0:
        rotateU(-1)
    else:
        rotateU(1)
    rotateCubeV(-1)
    
def rotateB(dir):
    rotateCubeV(-1)
    if dir<0:
        rotateU(-1)
    else:
        rotateU(1)
    rotateCubeV(1)


reset()


##scramble("LOW")
##showScrambleInstructions()

##need to test each functionality
##add more random numbers to make scramble more scrambled

printFace(faceFromColor(frontFaceC))
printFace(faceFromColor(topFaceC))
printFace(faceFromColor(leftFaceC))

