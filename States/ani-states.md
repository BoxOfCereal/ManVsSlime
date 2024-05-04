d_zombieDoor0
IDLE,10
IDLE75,10
IDLE50,10
IDLE25,10
IDLETO75,10
75TO50,10
50TO25,10
25TO0,10
0TO25,10
25TO50,10
50TO75,10
75TOIDLE,10
0DESTROYED,10
SPAWNZOMBIE,10
DEATH,10
DEAD,10
//SET I TO 0

d_zombieDoorLogic0.states
IDLE,10
TICK,10
SPAWNLOGIC,10
SPAWNZOMBIE0,10
SPAWNZOMBIE1,10
SPAWNZOMBIE2,10
SPAWNZOMBIE3,10
DEATH,10
DEAD,10

frame 13 0.25 0 0 0 CUSTOMPARTICLE 42 20 0,64,32 0,0,0 1 -0.001

What is the exact file path that I need to store custom particles in?

 Currently they're located here:
`C:\Users\ME\OneDrive\Desktop\Projects\MyGame\Sprites\Particles`

 But I can't get them to show up at all in a state machine with this:
`frame 13 0.25 0 0 0 CUSTOMPARTICLE 42 20 0,64,32 0,0,0 1 -0.001`

 I'm expecting that on frame 13, A custom particle at location `C:\Users\ME\OneDrive\Desktop\Projects\MyGame\Sprites\Particles\Custom42.png` , Will be displayed 64 units above the entity and 32 units in front of the entity with zero velocity at a scale of 1 at negative .001 gravity.