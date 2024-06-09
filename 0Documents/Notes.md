 I thought about doing something like this myself by taking the coordinates of the player in predefined coordinates on the map somewhere and then checking the distance and if the player is in that distance and not `isCrouched`

## progress


6/9/2024
I've been able to get the model into EFPSE.However I suspect from some weird geometry and blockbench some of the geometry didn't load and I'm having a hell of a time baking textures in blender so it seems to me the best step would be is to find the textures that I want to use combine it into a map and block bench before I export it so I don't have to bake any textures afterwards.

I still would like a quick concrete flow of what I'm doing so potentially I could make a model in like 15 minutes animate it in 15 minutes and bring it into EFPSE in 15 minutes that's what I would like

I would also like this written down and referencible and maybe collaborate With another person on it



6/8/2024

### Questions
Currently I make the model in blockbench or blender. Then I bring it into blender, Where I have a one tile cube so I scale the model I'm working with to match EFPSE's scale. Then animate it. Then I export from blender to GLB and then I import into `noesis`. Where I do the rotate by 90 degrees and set everything for md3.

### Problem
My only problem is is I've gotten things to show up in the world but they crash if they go into my weapons

I'm having trouble real big trouble having a good workflow from 3D model to EFPSE. I think I'm gonna have to just spend a couple weeks just doing that just workflow cause I can't even get one thing in there and get it working smoothly.

What's interesting though is that I can get it working in the map but as soon as the character picks it up the game crashes.


`📁C:\...\Desktop\Projects\ManVsSlime\States\w_hammer.states`
```
image w_hammer 0 8

state IDLE NONE 0
frame 0 0.25 0 0 0 NONE
frame 1 0.25 0 0 0 READY

state ATTACK IDLE 0
frame 2 1 0 0 0 NONE
frame 3 0.25 0 0 0 ATTACK
```

```
(base) PS C:\...\Desktop\Projects\ManVsSlime\Models>  tree /F
Folder PATH listing for volume Acer
Volume serial number is D934-0B50
C:.
    vw_hammer.md3
    vw_hammer.png
    ww_hammer.md3
    ww_hammer.png
```

### Answer
I just fixed my problem by pasting in the default weapon fsm as provided by the manual:
```
sound WeaponFire
sound WeaponReload

state IDLE NONE 0
frame 1 0.25 0 0 0 NONE
frame 1 0.25 0 0 0 READY

state ATTACK IDLE 0
frame 2 1 0 0 0 NONE
frame 3 1 0 0 0 SOUNDANDATTACK 0
frame 4 1 0 0 0 MUZZLEFLASH
frame 5 1 0 0 0 READY
frame 6 1 0 0 0 NONE
frame 7 1 0 0 0 NONE
frame 1 0.25 0 0 0 NONE
frame 1 0.25 0 0 0 NONE

state RELOAD IDLE 0
frame 1 0 0 0 0 NONE
frame 1 0.1 0 0 0 NONE
frame 1 0.1 0 200 0 NONE
frame 1 0.1 0 200 0 RELOAD
frame 1 0.1 0 0 0 SOUND 1
```


6/7/2024
Most of The core logic for the game is working through individual trial and error testing. I have yet to "play" the game. For this to happen I need to look at the rounds and set them all to like 30 seconds I think they're all 10 rounds I put four zombie doors in the the level and a couple dog spawners and I just do it in one single room. So I'll be emulating one single room with a door on each side and two weapon vendors. 

I still need to add percent chance for drops for all of them to the enemies.

5/27/2024
Committed a bunch of stuff


5/22/2024
I added score logic to the monster stuff script and also to the zombie states and I added weapon vendors script and state



5/22/2024
OK right now the game crashes when you use the Dog spawner because for whatever reason random generation **** is just not right.

I can now extend round logic and I need to work on:

- HUD
  - round
    - round timer                                                        
  - player health
  - power up
- score logic
    - player score
    - totalscore
    - highscore
    - display score
    - zombie points system [wip]
    - purchase weapons/ammo[wip]
      - vendors
      - animations
      - sounds
      - logic
      - model
- Decorations
  - d_zombieDoorProp0 
    - It needs a model
    - animations
    - sounds
    - ~logic~
  - d_dogSpawner
    - logic
      - `d_dogSpawner0.states` The way it's set up now is that there's a spawner corresponding to which zone has been unlocked in this case we have zero. The formula for the dog spawners goes as such: `b + (b * r / 3)` where `b` is the `base number of dogs` and `r` is the `number of rounds`. The `base number of dogs` is `map.baseDogsPerSpawner` and `number of rounds` is `map.currentRound` Both located in the monster stuff script what's handy is that because rounds will always be the visible by three I don't have to bother with floating points. AND, Because the first round is actually round six in the back end that means that it'll be `base` `*` `3 / 6` which is `2` which means it'll be `six dogs per spawner` on the `first dog round`.
  - d_playerMetrognome
    - logic
  - drops ❌
    - 1hko
      - logic [finished] ✅
        - 📁`Scripts\d_p_1hko.script` Flips a switch that activates 📁`States\d_metrognome_1hko.states`. `States\d_metrognome_1hko.states` Keeps track of a timer that counts down until one hit KO is over. As a consequence of the architecture the player can pick up an extra one hit KO to have "buffer" That will reactivate when the current one hit KO runs out. However, this does not stack any others put on top of this buffer will be lost.
    - repair 
      - logic [finished]✅
      - model [unfinished]❌
    - nuke 
      - logic [finished]✅
      - model [unfinished]❌
    - doublePoints 
      - logic [finished]✅
      - model [unfinished]❌
    - maxAmmo ✅
      - logic [finished]✅
      - model [unfinished]❌

- Enemies
 - e_dog
  - logic
    - For the most part logic is good right now and just attacks and runs away might need some tweaking
  - animations
  - model
  - sounds
- e_zombie
  - logic
    - For the most part logic is good right now tweaking
  - animations
  - model
  - sounds
- guns ❌
  - guntlet
  - pistol
  - xbow
  - staff
  - fireball
  - hammer
  - sword
   
To get the one hit KO working I have to use a variable flag and then in a state machine that has a count timer for it and then inside decorations I have to check it blast hp is lower than this hp then sticking damage and then I can go to the take damage stay and then I can check if it's instant kill


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

