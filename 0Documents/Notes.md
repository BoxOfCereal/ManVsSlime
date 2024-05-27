 I thought about doing something like this myself by taking the coordinates of the player in predefined coordinates on the map somewhere and then checking the distance and if the player is in that distance and not `isCrouched`

## progress
5/22/2024
I added score logic to the monster stuff script and also to the zombie states and I added weapon vendors script and state



5/22/2024
OK right now the game crashes when you use the Dog spawner because for whatever reason random generation **** is just not right.

I can now extend round logic and I need to work on:

- score logic
    - player score
    - zombie points system [wip]
    - purchase weapons/ammo[wip]
      - vendors
      - animations
      - sounds
      - logic
      - model
    - totalscore
    - highscore
- d_zombieDoorProp0 
  - It needs a model
  - animations
  - sounds
  - ~logic~
- e_dog
  - logic
    - For the most part logic is good right now and just attacks and runs away might need some tweaking
  - animations
  - model
  - sounds
- d_playerMetrognome
  - logic
- drops
  - logic
    - I think this is going to have to be intertwined with the player metronome because once a power up is active I want to set variables and then when it comes unactive I'm going to change those variables back so I'll probably have to do something like that.
- guns
  - guntlet
  - pistol
  - xbow
  - staff
  - fireball
  - hammer
  - sword
   



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

