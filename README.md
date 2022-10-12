# Rubix-Cube
A rubix cube simulation project: follow the development process through the different versions

This is a documentation of the progress I've had when starting this project to now. 

rubix.py : The initial algorithm for implementing the cube but no user input
rubixv2.py : Use curses interface to implement user input (now we can turn the cube faces, but its hard to see what's going on)
rubixv3.py : Use colors to make things more clear (still hard to see a 3D move in a 2D space)
rubixv4.py : Still in curses, but use shapes to represent a 3D cube. Different viewing modes too
rubixv5.py : Things are drastically changing: use pygame to have a 3d cube and now we can see the rubix cube movements pretty clearly
rubixv6.py : Made the cube look nicer
rubixv7.py : Added some other cool features like undo by one move, hold to undo moves, scramble and mouse swipes (esp good for touchscreen)


KEY COMMANDS:

Up - w
Up'- e
Down - r
Down'- t
Right - a
Right'- s
Left - d
Left'- f
Front - z
Front'- x
Back - c
Back'- v

Press l : Shift viewing mode
Press i : Scramble
Hold o : Undo moves
Press p : Undo one move
  






GOALS: create animations, experiment with AI to understand algorithms
