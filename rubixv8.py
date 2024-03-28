from random import randint
import pygame
from pygame.locals import *
import sys
import math
from collections import deque ## stack


# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

w=0 #white
g=1 #green
r=2 #red
b=3 #blue
o=4 #orange
y=5 #yellow

t=0 #top
l=1 #left
f=2 #front
r=3 #right
b=4 #back
bo=5 #bottom

H=0 #Horizontal 
V=1 #Vertical
S=2 #Sideways


class Cube:
    def __init__(self):
        self.cube = [[[color for _ in range (3)] for _ in range(3)] for color in range (6)]
        self.mov = deque()
        self.char = u"\u25A0"

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
    
    def getColor(self,color):
        if color == 0:
            return WHITE
        elif color== 1:
            return GREEN
        elif color == 2:
            return RED
        elif color==3:
            return BLUE
        elif color==4:
            return ORANGE
        elif color==5:
            return YELLOW

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
        
        self.mov.append((self.movU,d))
    def movD(self,d):
        self.rotateCube(S,1)
        self.rotateCube(S,1)
        self.rotateChunk(-d)
        self.rotateCube(S,1)
        self.rotateCube(S,1)
        
        self.mov.append((self.movD,d))
    
    def movR(self,d):
        self.rotateCube(S,-1)
        self.rotateChunk(-d)
        self.rotateCube(S,1)
        
        self.mov.append((self.movR,d))
    def movL(self,d):
        self.rotateCube(S,1)
        self.rotateChunk(d)
        self.rotateCube(S,-1)
    
        self.mov.append((self.movL,d))
    
    def movF(self,d):
        self.rotateCube(V,1)
        self.rotateChunk(-d)
        self.rotateCube(V,-1)
        
        self.mov.append((self.movF,d))
    def movB(self,d):
        self.rotateCube(V,-1)
        self.rotateChunk(d)
        self.rotateCube(V,1)
        
        self.mov.append((self.movB,d))
        
    def cubeRedo(self):
        if len(self.mov)>0:
            ch = self.mov.pop()
            ch[0](ch[1]*-1)
            self.mov.pop()
    def cubeScramble(self):
        ran_iter = randint(10,50)
        for _ in range(ran_iter):
            ran_list = randint(0,1)
            if ran_list:
                ran_num = randint(0,5)
                ran_dir = randint(0,1)
                action = up_down_moves[ran_num]
                if ran_dir:
                    action[0](action[1])
                else:
                    action[0](action[1]*-1)
            else:
                ran_num = randint(0,3)
                ran_dir = randint(0,1)
                action = right_left_moves[ran_num]
                if ran_dir:
                    action[0](action[1])
                else:
                    action[0](action[1]*-1)
        
# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rubix Cube")

# Define the vertices of the cube
CUBE_SIZE = 200
half_size = CUBE_SIZE // 2
vertices = [(-half_size, -half_size, -half_size),
            (-half_size, half_size, -half_size),
            (half_size, half_size, -half_size),
            (half_size, -half_size, -half_size),
            (-half_size, -half_size, half_size),
            (-half_size, half_size, half_size),
            (half_size, half_size, half_size),
            (half_size, -half_size, half_size)]

# Define edges of the cube
edges = [(2, 3, 7, 6),  # Top face
        (0, 3, 7, 4),   # Left face
        (0, 1, 2, 3),   # Front face
        (1, 2, 6, 5),   # Right face
        (4, 5, 6, 7),   # Back face
        (0, 1, 5, 4)]   # Bottom face        


# Define faces of the cube and their colors
# Front, Back, Top, Bottom, Right, Left
face_colors = [RED, GREEN, YELLOW, WHITE, BLUE, ORANGE]


# Define rotation functions
def rotate_x(point, angle):
    x, y, z = point
    rad = math.radians(angle)
    new_y = y * math.cos(rad) - z * math.sin(rad)
    new_z = y * math.sin(rad) + z * math.cos(rad)
    return x, new_y, new_z

def rotate_y(point, angle):
    x, y, z = point
    rad = math.radians(angle)
    new_x = x * math.cos(rad) - z * math.sin(rad)
    new_z = x * math.sin(rad) + z * math.cos(rad)
    return new_x, y, new_z

def rotate_z(point, angle):
    x, y, z = point
    rad = math.radians(angle)
    new_x = x * math.cos(rad) - y * math.sin(rad)
    new_y = x * math.sin(rad) + y * math.cos(rad)
    return new_x, new_y, z

def is_inside_cube(point, vertices):
    min_x = min(vertex[0] for vertex in vertices) + WIDTH/2
    max_x = max(vertex[0] for vertex in vertices) + WIDTH/2
    min_y = min(vertex[1] for vertex in vertices) + HEIGHT/2
    max_y = max(vertex[1] for vertex in vertices) + HEIGHT/2

    if min_x <= point[0] <= max_x and min_y <= point[1] <= max_y:
        return True
    else:
        return False

# Calculate area of a face given its vertices
def face_area(face_vertices):
    # Calculate vectors between vertices
    u = [face_vertices[1][i] - face_vertices[0][i] for i in range(3)]
    v = [face_vertices[2][i] - face_vertices[0][i] for i in range(3)]
    
    # Compute cross product to get normal vector
    normal = [u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]]
    
    # Return area of parallelogram formed by the vectors
    return math.sqrt(sum(c**2 for c in normal))

# Calculate the distance between two points in 3D space
def euclid_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

# Calculate the distance from the viewer to a point in 3D space
def distance_to_viewer(point):
    x, y, z = point
    return (x*(abs(x))/10 + y*(abs(y))/10 + z*(abs(z))) #divide x,y by 10 to give z more weight


# Main loop
angle_x = 0
angle_y = 0
angle_z = 0
clock = pygame.time.Clock()
running = True
mouse_pressed = False
showFace=1
press_redo=False
clear = False
rotated_vertices = vertices
cube = Cube()


key_controls = {
        pygame.K_w : (cube.movU,-1),
        pygame.K_e : (cube.movU,1),
        pygame.K_r : (cube.movD,-1),
        pygame.K_t : (cube.movD,1),
        pygame.K_a : (cube.movR,1),
        pygame.K_s : (cube.movR,-1),
        pygame.K_d : (cube.movL,1),
        pygame.K_f : (cube.movL,-1),
        pygame.K_z : (cube.movF,-1),
        pygame.K_x : (cube.movF,1),
        pygame.K_c : (cube.movB,-1),
        pygame.K_v : (cube.movB,1),
        pygame.K_UP : (cube.rotateCube,V,1),
        pygame.K_DOWN : (cube.rotateCube,V,-1),
        pygame.K_LEFT : (cube.rotateCube,H,-1),
        pygame.K_RIGHT : (cube.rotateCube,H,1)
    }   

up_down_moves = [(cube.movL,1),(cube.movR,1),(cube.movL,1),(cube.movR,1),(cube.movF,-1),(cube.movB,-1)]
right_left_moves = [(cube.movB,1),(cube.movF,1),(cube.movU,1),(cube.movD,1)]
    
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if is_inside_cube(pygame.mouse.get_pos(), rotated_vertices):
                    mouse_pressed = False
                else:
                    mouse_pressed = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                mouse_pressed = False
        elif event.type == pygame.KEYDOWN:
            for key in key_controls.keys():
                if event.key==key:
                    action=key_controls.get(event.key)
                    if len(action)==2:
                        action[0](action[1])
                    else:
                        action[0](action[1],action[2])    
            if event.key== pygame.K_p:
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
            elif event.key == pygame.K_0:
                clear=True
            elif event.key == pygame.K_i:
                cube.cubeScramble()
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_o:
                press_redo = False
            if event.key == pygame.K_0:
                clear = False

    if mouse_pressed:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle_y += (mouse_x - WIDTH/2) / 50
        angle_x += (mouse_y - HEIGHT/2) / 50
    if clear:
        while len(cube.mov)>0:
            cube.cubeRedo()
    if press_redo:
        cube.cubeRedo()
        pygame.time.delay(100)
            

    screen.fill(BLACK)

    rotated_vertices = []
    for vertex in vertices:
        rotated = rotate_x(vertex, angle_x)
        rotated = rotate_y(rotated, angle_y)
        rotated = rotate_z(rotated, angle_z)
        rotated_vertices.append(rotated)

     # Calculate distance metric to the center of each face
    face_distances = [sum(distance_to_viewer(rotated_vertices[i]) for i in face) / len(face) for face in edges]

    # Sort faces based on distance metric
    sorted_faces = sorted(range(len(edges)), key=lambda i: face_distances[i], reverse=True)

    # Draw faces of the cube by distance metric, closest ones last
    for face_idx in sorted_faces:
        face = edges[face_idx]
        points = [rotated_vertices[i] for i in face]

        top_x = (points[1][0] - points[0][0]) / 3
        top_y = (points[1][1] - points[0][1]) / 3
        sid_x = (points[2][0] - points[1][0]) / 3
        sid_y = (points[2][1] - points[1][1]) / 3


        for j in range(3):
            for i in range(3):
                    cubie_points = [(points[0][0] + i * top_x + j * sid_x, points[0][1] + i * top_y + j * sid_y),
                                    (points[0][0] + (i + 1) * top_x + j * sid_x, points[0][1] + (i + 1) * top_y + j * sid_y),
                                    (points[0][0] + (i + 1) * top_x + (j + 1) * sid_x, points[0][1] + (i + 1) * top_y + (j + 1) * sid_y),
                                    (points[0][0] + i * top_x + (j + 1) * sid_x, points[0][1] + i * top_y + (j + 1) * sid_y)]
                    if face_idx == 3:
                        # blue: rotated value
                        cubie_color = cube.getColor(cube.cube[face_idx][2-i][j])
                    elif face_idx == 2:
                        # red : reflected value
                        cubie_color = cube.getColor(cube.cube[face_idx][2-j][i])
                    elif face_idx == 1:
                        # green double reflected value
                        cubie_color = cube.getColor(cube.cube[face_idx][2-i][2-j])
                    elif face_idx == 4 or face_idx == 0:
                        # orange or red double rotation value
                        cubie_color = cube.getColor(cube.cube[face_idx][2-j][2-i])
                    else:
                        cubie_color = cube.getColor(cube.cube[face_idx][j][i])

                    pygame.draw.polygon(screen, cubie_color, [(p[0] + WIDTH//2, p[1] + HEIGHT//2) for p in cubie_points])
                    pygame.draw.lines(screen, BLACK, True, [(p[0] + WIDTH//2, p[1] + HEIGHT//2) for p in cubie_points], 7)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

