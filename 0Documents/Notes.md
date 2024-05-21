
## Game components

### gd
python gd.py --input C:\Users\SeltT\OneDrive\Desktop\Projects\ManVsSlime\States\d_metrognome.states --output C:\Users\SeltT\OneDrive\Desktop\Projects\ManVsSlime\Sprites\Decorations  

If you get a permission denied it's probably because EFPSE editor is open

### Metrognome
The metronome is just one state machine that pretty much handles all logic in the game it updates a tick counter so that things run once every so many seconds that's my timer for basically everything. It handles the timer and the switching rounds so it's basically the game state machine.

### dogs
The dog components consist of the following

📁`\Projects\ManVsSlime\States\d_dogSpawner.states`
📁`\Projects\ManVsSlime\States\d_dogPortal.state`
📁`\Projects\ManVsSlime\States\e_dog.state`

The dog spawner is placed on a map. If `map.spawnDogsSwitch == 1` the dog spawner will spawn a `d_dogPortal` every X seconds based on `map.spawnDogsTimer`. Spawning location is determined by this logic:

📁`\Projects\ManVsSlime\States\d_dogSpawner.states`
```
state TICK NONE 0
frame 6 0.25 0 0 0 NONE
frame 2 0.25 0 0 0 JUMPIFEQUALS map.spawnDogSwitch 0 NOTHING
frame 1 0.25 0 0 0 SETVAR randomXCoordinate RANDOM(-64,64) 
frame 2 0.25 0 0 0 SETVAR randomYCoordinate RANDOM(-64,64)
frame 7 10 0 0 0 SPAWN d_dogPortal $randomXCoordinate,0,$randomYCoordinate 0,0
frame 8 0.25 0 0 0 NONE
```

From here the dog portal will spawn a `e_dog` ,and then transition into the dead state thereby destroying itself:

📁`\Projects\ManVsSlime\States\d_dogPortal.state`
```
state TICK DEAD 0
frame 6 0.25 0 0 0 NONE
frame 2 0.25 0 0 0 JUMPIFEQUALS map.spawnDogSwitch 0 NOTHING
frame 7 0.25 0 0 0 SPAWN d_dog 32,0,-32 0,0
frame 8 0.25 0 0 0 NONE
```

The dog attack pattern is programmed to run up to the player attack and then run away and then continue doing that.


## ZOMBIE DOOR ANIMATIONS
IDLE,10
IDLE75,10
IDLE50,10
IDLE25,10
75TO50,10
50TO25,10
25TO0,10
0TO25,10
25TO50,10
50TO75,10
75TO100,10
DEATH,10
DEAD,10

## Tools and links
Tools and links

Text to sound effects
https://app.audiogen.co/

