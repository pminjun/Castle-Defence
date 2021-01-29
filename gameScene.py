import cocos.scene
import cocos.layer
import cocos.actions as ac
import pyglet.image
import cocos.sprite
import pyglet.app

import pygame
import math

import cocos.audio
import cocos.audio.pygame
import cocos.audio.pygame.mixer

import cocos.actions as ac
from collections import defaultdict
from cocos.director import director
from cocos.actions.interval_actions import MoveBy
from pyglet.image import Animation
from pyglet.image import load
from pyglet.image import *

from cocos.scenes.transitions import TurnOffTilesTransition
from cocos.scenes.transitions import FadeDownTransition
import cocos.euclid as eu
import cocos.collision_model as cm

import cocos.collision_model as cm
from collections import defaultdict
from pyglet.window import key
import time

import random

# Animation 
raw = pyglet.image.load('assets/castle1.png')
seq = pyglet.image.ImageGrid(raw, 1, 3)
background = Animation.from_image_sequence(seq, 0.3, True)

# Animation 
raw1 = pyglet.image.load('assets/sun.png')
seq1 = pyglet.image.ImageGrid(raw1, 1, 8)
sun = Animation.from_image_sequence(seq1, 0.2, True)

# Animation 
raw2 = pyglet.image.load('assets/bomb.png')
seq2 = pyglet.image.ImageGrid(raw2, 1, 3)
bomb = Animation.from_image_sequence(seq2, 0.3, True)

# Animation 
raw3 = pyglet.image.load('assets/shitAnimation.png')
seq3 = pyglet.image.ImageGrid(raw3, 1, 2)
shit = Animation.from_image_sequence(seq3, 0.2, True)

# Animation
raw5 = pyglet.image.load('assets/updown.png')
seq5 = pyglet.image.ImageGrid(raw5, 1, 2)
updown = Animation.from_image_sequence(seq5, 0.1, True)

# Animation
raw7 = pyglet.image.load('assets/gameBGOBJ/fire.png')
seq7 = pyglet.image.ImageGrid(raw7, 1, 7)
fire = Animation.from_image_sequence(seq7, 0.1, True)

# Animation
raw8 = pyglet.image.load('assets/bomb/bombEmotion4.png')
seq8 = pyglet.image.ImageGrid(raw8, 1, 10)
bombEmotion = Animation.from_image_sequence(seq8, 0.05, False)

# Animation
raw9 = pyglet.image.load('assets/bomb/bombEmotion12.png')
seq9 = pyglet.image.ImageGrid(raw9, 1, 7)
bombEmotion2 = Animation.from_image_sequence(seq9, 0.05, False)

# Animation
raw10 = pyglet.image.load('assets/gameBGOBJ/ice.png')
seq10 = pyglet.image.ImageGrid(raw10, 1, 4)
ice = Animation.from_image_sequence(seq10, 0.05, True)

# Animation
raw11 = pyglet.image.load('assets/remote/remote1.png')
seq11 = pyglet.image.ImageGrid(raw11, 1, 8)
remote1 = Animation.from_image_sequence(seq11, 0.05, True)

# Enemy1 Animation
#R
enemyRaw1 = pyglet.image.load('assets/enemy/enemyRun1AniR.png')
enemySeq1 = pyglet.image.ImageGrid(enemyRaw1, 1, 4)
enemyRun1AniR = Animation.from_image_sequence(enemySeq1, 0.2, True)
#L
enemyRaw2 = pyglet.image.load('assets/enemy/enemyRun1AniL.png')
enemySeq2 = pyglet.image.ImageGrid(enemyRaw2, 1, 4)
enemyRun1AniL = Animation.from_image_sequence(enemySeq2, 0.2, True)
#R
enemyRaw3 = pyglet.image.load('assets/enemy/enemyAttack1AniR.png')
enemySeq3 = pyglet.image.ImageGrid(enemyRaw3, 1, 2)
enemyAttack1AniR = Animation.from_image_sequence(enemySeq3, 0.1, True)
#L
enemyRaw4 = pyglet.image.load('assets/enemy/enemyAttack1AniL.png')
enemySeq4 = pyglet.image.ImageGrid(enemyRaw4, 1, 2)
enemyAttack1AniL = Animation.from_image_sequence(enemySeq4, 0.1, True)

# Enemy2 Animation
#R
enemyRaw5 = pyglet.image.load('assets/enemy/enemyRun2AniR.png')
enemySeq5 = pyglet.image.ImageGrid(enemyRaw5, 1, 2)
enemyRun2AniR = Animation.from_image_sequence(enemySeq5, 0.2, True)
#L
enemyRaw6 = pyglet.image.load('assets/enemy/enemyRun2AniL.png')
enemySeq6 = pyglet.image.ImageGrid(enemyRaw6, 1, 2)
enemyRun2AniL = Animation.from_image_sequence(enemySeq6, 0.2, True)
#R
enemyRaw7 = pyglet.image.load('assets/enemy/enemyAttack2AniR.png')
enemySeq7 = pyglet.image.ImageGrid(enemyRaw7, 1, 5)
enemyAttack2AniR = Animation.from_image_sequence(enemySeq7, 0.1, True)
#L
enemyRaw8 = pyglet.image.load('assets/enemy/enemyAttack2AniL.png')
enemySeq8 = pyglet.image.ImageGrid(enemyRaw8, 1, 5)
enemyAttack2AniL = Animation.from_image_sequence(enemySeq8, 0.1, True)

# Enemy3 Animation
#R
enemyRaw9 = pyglet.image.load('assets/enemy/enemyRun3AniR.png')
enemySeq9 = pyglet.image.ImageGrid(enemyRaw9, 1, 2)
enemyRun3AniR = Animation.from_image_sequence(enemySeq9, 0.2, True)
#L
enemyRaw10 = pyglet.image.load('assets/enemy/enemyRun3AniL.png')
enemySeq10 = pyglet.image.ImageGrid(enemyRaw10, 1, 2)
enemyRun3AniL = Animation.from_image_sequence(enemySeq10, 0.2, True)
#R
enemyRaw11 = pyglet.image.load('assets/enemy/enemyAttack3AniR.png')
enemySeq11 = pyglet.image.ImageGrid(enemyRaw11, 1, 4)
enemyAttack3AniR = Animation.from_image_sequence(enemySeq11, 0.3, True)
#L
enemyRaw12 = pyglet.image.load('assets/enemy/enemyAttack3AniL.png')
enemySeq12 = pyglet.image.ImageGrid(enemyRaw12, 1, 4)
enemyAttack3AniL = Animation.from_image_sequence(enemySeq12, 0.3, True)

# Enemy4 Animation
#R
enemyRaw13 = pyglet.image.load('assets/enemy/enemyRun4AniR.png')
enemySeq13 = pyglet.image.ImageGrid(enemyRaw13, 1, 2)
enemyRun4AniR = Animation.from_image_sequence(enemySeq13, 0.5, True)
#L
enemyRaw14 = pyglet.image.load('assets/enemy/enemyRun4AniL.png')
enemySeq14 = pyglet.image.ImageGrid(enemyRaw14, 1, 2)
enemyRun4AniL = Animation.from_image_sequence(enemySeq14, 0.5, True)


# Sound C
cocos.audio.pygame.mixer.init()
runSound = cocos.audio.pygame.mixer.Sound('audio/run.ogg')

cocos.audio.pygame.mixer.init()
gameSound = cocos.audio.pygame.mixer.Sound('audio/gameBackAudio.ogg')

cocos.audio.pygame.mixer.init()
pxSound = cocos.audio.pygame.mixer.Sound('audio/px.ogg')

cocos.audio.pygame.mixer.init()
spadeSound = cocos.audio.pygame.mixer.Sound('audio/spade.ogg')

cocos.audio.pygame.mixer.init()
ironSound = cocos.audio.pygame.mixer.Sound('audio/iron.ogg')

cocos.audio.pygame.mixer.init()
bombPowerSound = cocos.audio.pygame.mixer.Sound('audio/bombPower.ogg')

cocos.audio.pygame.mixer.init()
bombSound = cocos.audio.pygame.mixer.Sound('audio/bomb.ogg')
           
class Start(cocos.sprite.Sprite):
    def __init__(self, pos):
        self.emotions = {'start':load('assets/startEmotion.png'),
                         'empty':load('assets/123.png'),
                         'win':load('assets/win.png'),
                         'lose':load('assets/lose.png')}
        super(Start, self).__init__(self.emotions['start'], pos)
        self.time = 0
    
class Sky(cocos.sprite.Sprite):
    def __init__(self, pos):
        self.emotions = {'1':load('assets/sky/1.png'),
                         '2':load('assets/sky/2.png'),
                         '3':load('assets/sky/3.png'),
                         '4':load('assets/sky/4.png'),
                         '5':load('assets/sky/5.png'),
                         '6':load('assets/sky/6.png'),
                         '7':load('assets/sky/7.png'),
                         '8':load('assets/sky/8.png'),
                         '9':load('assets/sky/9.png'),
                         '10':load('assets/sky/10.png'),
                         '11':load('assets/sky/11.png'),
                         '12':load('assets/sky/12.png')}
        super(Sky, self).__init__(self.emotions['1'], pos)
        
class BombEmotion2(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(BombEmotion2, self).__init__(bombEmotion2, pos)
        self.rotation = 60

class BombEmotion3(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(BombEmotion3, self).__init__(bombEmotion2, pos)
        self.rotation = -60
        
class BombEmotion(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(BombEmotion, self).__init__(bombEmotion, pos)
        
class Background(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(Background, self).__init__(background, pos)

class Sun(cocos.sprite.Sprite):
    def __init__(self, pos):
        self.emotions = {'empty':load('assets/startButton.png')}
        super(Sun, self).__init__(sun, pos)
        self.position = pos
        self.cshape = cm.CircleShape(pos, self.width/2)

class Shit(cocos.sprite.Sprite):
    
    def __init__(self, pos):
        super(Shit, self).__init__(shit, pos)

class Bomb(cocos.sprite.Sprite):
    def __init__(self, x, y):
        self.emotions = {'rightBomb':load('assets/bomb/bombR.png'),
                         'leftBomb':load('assets/bomb/bombL.png'),
                         'bomb':load('assets/bomb/bomb1.png'),
                         'bombEmotion':bombEmotion,
                         'iceBomb':load('assets/bomb/icebomb1.png')}
        super(Bomb, self).__init__(self.emotions['rightBomb'])
        self.tryStart = True
        self.tryShot = False
        self.iceTryShot = False
        
        self.bombPowerCheck = False
        self.trySlow = False
        self.bombCheck = False
        self.iceCheck = False
        self.bombEnter = False

        self.bombBob = False

        self.position = pos = eu.Vector2(x, y)
        self.cshape = cm.CircleShape(pos, self.width/2)
        
class checkTry(cocos.sprite.Sprite):
    def __init__(self, x, y):
        self.emotions = {'bomb':load('assets/bomb/bombCheck.png'),
                         'bombClear':load('assets/bomb/bomb1.png'),
                         'ice':load('assets/bomb/iceCheck.png'),
                         'iceClear':load('assets/bomb/iceCheckClear.png'),
                         'bombPower':load('assets/bomb/bombCheckPowerCheck.png'),
                         'bombPowerClear':load('assets/bomb/bombCheckPowerCheck1.png'),
                         'mineCheck0':load('assets/bomb/allCheck0.png'),
                         'mineCheck1':load('assets/bomb/allCheck1.png'),
                         'mineCheck2':load('assets/bomb/allCheck2.png'),
                         'mineCheck3':load('assets/bomb/allCheck3.png'),
                         'mineCheck4':load('assets/bomb/allCheck4.png'),
                         'mineCheck5':load('assets/bomb/allCheck5.png'),
                         'ironCheck':load('assets/bomb/ironCheck.png'),
                         'ironClear':load('assets/bomb/iron.png')}
        super(checkTry, self).__init__(self.emotions['bomb'])
        self.position = pos = eu.Vector2(x, y)
        self.cshape = cm.CircleShape(pos, self.width/2)
        self.mineCheckTime = 0

    def zero(self):
        self.image = self.emotions['mineCheck0']
    def one(self):
        self.image = self.emotions['mineCheck1']
    def two(self):
        self.image = self.emotions['mineCheck2']
    def three(self):
        self.image = self.emotions['mineCheck3']
    def four(self):
        self.image = self.emotions['mineCheck4']    
    def five(self):
        self.image = self.emotions['mineCheck5']    

        

class Actor(cocos.sprite.Sprite):
    def __init__(self, x, y):
        self.emotions = {'start':load('assets/human.png'),
                        'shit':load('assets/shit1.png'),
                         'slideL':load('assets/slideHuman1.png'),
                         'slideR':load('assets/slideHuman2.png'),
                         'updown1':load('assets/updown1.png'),
                         'updown2':load('assets/updown2.png'),
                         'runR1':load('assets/run1.png'),
                         'runR2':load('assets/run2.png'),
                         'runR3':load('assets/run3.png'),
                         'runR4':load('assets/run4.png'),
                         'runR5':load('assets/run5.png'),
                         'runL1':load('assets/runL1.png'),
                         'runL2':load('assets/runL2.png'),
                         'runL3':load('assets/runL3.png'),
                         'runL4':load('assets/runL4.png'),
                         'runL5':load('assets/runL5.png'),
                         'bombPowerFarming1':load('assets/bombPowerHuman1.png'),
                         'bombPowerFarming2':load('assets/bombPowerHuman2.png'),
                         'bombPowerFarming3':load('assets/bombPowerHuman3.png'),
                         'ironFarming1':load('assets/ironHuman1.png'),
                         'ironFarming2':load('assets/ironHuman2.png'),
                         'ironFarming3':load('assets/ironHuman3.png'),
                         'ironTrainning1':load('assets/ironTrainHuman1.png'),
                         'ironTrainning2':load('assets/ironTrainHuman2.png'),
                         'ironTrainning3':load('assets/ironTrainHuman3.png'),
                         'ironTrainning4':load('assets/ironTrainHuman4.png'),
                         'iceFarming1':load('assets/iceFarming1.png'),
                         'iceFarming2':load('assets/iceFarming2.png'),
                         'iceFarming3':load('assets/iceFarming3.png')}

        super(Actor, self).__init__(self.emotions['start'])
        
        self.position = pos = eu.Vector2(x, y)
        self.cshape = cm.CircleShape(pos, self.width/2)
        self.farmingTime = 0
        self.stamina = 5
        self.bombCheck = False
        self.ironCheck = False
        self.bombPowerCheck = False
        self.iceCheck = False
        self.speed = 100.0

    def action(self):
        self.image = self.emotions['shit']

    def defaultAction(self):
        self.image = self.emotions['start']

    def sildeActionL(self):
        self.image = self.emotions['slideL']

    def sildeActionR(self):
        self.image = self.emotions['slideR']

    def upDown1(self):
        self.image = self.emotions['updown1']

    def upDown2(self):
        self.image = self.emotions['updown2']
        
    def runR1(self):
        self.image = self.emotions['runR1']

    def runR2(self):
        self.image = self.emotions['runR2']

    def runR3(self):
        self.image = self.emotions['runR3']

    def runR4(self):
        self.image = self.emotions['runR4']

    def runR5(self):
        self.image = self.emotions['runR5']

    def runL1(self):
        self.image = self.emotions['runL1']

    def runL2(self):
        self.image = self.emotions['runL2']

    def runL3(self):
        self.image = self.emotions['runL3']

    def runL4(self):
        self.image = self.emotions['runL4']

    def runL5(self):
        self.image = self.emotions['runL5']

    def bombPowerFarming1(self):
        self.image = self.emotions['bombPowerFarming1']

    def bombPowerFarming2(self):
        self.image = self.emotions['bombPowerFarming2']

    def bombPowerFarming3(self):
        self.image = self.emotions['bombPowerFarming3']

    def ironFarming1(self):
        self.image = self.emotions['ironFarming1']

    def ironFarming2(self):
        self.image = self.emotions['ironFarming2']

    def ironFarming3(self):
        self.image = self.emotions['ironFarming3']

    def ironTrainning1(self):
        self.image = self.emotions['ironTrainning1']

    def ironTrainning2(self):
        self.image = self.emotions['ironTrainning2']

    def ironTrainning3(self):
        self.image = self.emotions['ironTrainning3']

    def ironTrainning4(self):
        self.image = self.emotions['ironTrainning3']

    def iceFarming1(self):
        self.image = self.emotions['iceFarming1']

    def iceFarming2(self):
        self.image = self.emotions['iceFarming2']

    def iceFarming3(self):
        self.image = self.emotions['iceFarming3']
            
class Health(cocos.sprite.Sprite):
    def __init__(self,x, y):
        self.emotions = {'5':load('assets/health/5.png'),
                         '4':load('assets/health/4.png'),
                         '3':load('assets/health/3.png'),
                         '2':load('assets/health/2.png'),
                         '1':load('assets/health/1.png'),
                         'castle100':load('assets/CastleHealth/1.png'),
                         'castle99':load('assets/CastleHealth/2.png'),
                         'castle98':load('assets/CastleHealth/3.png'),
                         'castle97':load('assets/CastleHealth/4.png'),
                         'castle96':load('assets/CastleHealth/5.png'),
                         'castle95':load('assets/CastleHealth/6.png'),
                         'castle94':load('assets/CastleHealth/7.png'),
                         'castle93':load('assets/CastleHealth/8.png'),
                         'castle92':load('assets/CastleHealth/9.png'),
                         'castle91':load('assets/CastleHealth/10.png'),
                         'castle90':load('assets/CastleHealth/11.png'),
                         'castle89':load('assets/CastleHealth/12.png'),
                         'castle88':load('assets/CastleHealth/13.png'),
                         'castle87':load('assets/CastleHealth/14.png'),
                         'castle86':load('assets/CastleHealth/15.png'),
                         'castle85':load('assets/CastleHealth/16.png'),
                         'castle84':load('assets/CastleHealth/17.png'),
                         'castle83':load('assets/CastleHealth/18.png'),
                         'castle82':load('assets/CastleHealth/19.png'),
                         'castle81':load('assets/CastleHealth/20.png'),
                         'castle80':load('assets/CastleHealth/21.png'),
                         'castle79':load('assets/CastleHealth/22.png'),
                         'castle78':load('assets/CastleHealth/23.png'),
                         'castle77':load('assets/CastleHealth/24.png'),
                         'castle76':load('assets/CastleHealth/25.png'),
                         'castle75':load('assets/CastleHealth/26.png'),
                         'castle74':load('assets/CastleHealth/27.png'),
                         'castle73':load('assets/CastleHealth/28.png'),
                         'castle72':load('assets/CastleHealth/29.png'),
                         'castle71':load('assets/CastleHealth/30.png'),
                         'castle70':load('assets/CastleHealth/31.png'),
                         'castle69':load('assets/CastleHealth/32.png'),
                         'castle68':load('assets/CastleHealth/33.png'),
                         'castle67':load('assets/CastleHealth/34.png'),
                         'castle66':load('assets/CastleHealth/35.png'),
                         'castle65':load('assets/CastleHealth/36.png'),
                         'castle64':load('assets/CastleHealth/37.png'),
                         'castle63':load('assets/CastleHealth/38.png'),
                         'castle62':load('assets/CastleHealth/39.png'),
                         'castle61':load('assets/CastleHealth/40.png'),
                         'castle60':load('assets/CastleHealth/41.png'),
                         'castle59':load('assets/CastleHealth/42.png'),
                         'castle58':load('assets/CastleHealth/43.png'),
                         'castle57':load('assets/CastleHealth/44.png'),
                         'castle56':load('assets/CastleHealth/45.png'),
                         'castle55':load('assets/CastleHealth/46.png'),
                         'castle54':load('assets/CastleHealth/47.png'),
                         'castle53':load('assets/CastleHealth/48.png'),
                         'castle52':load('assets/CastleHealth/49.png'),
                         'castle51':load('assets/CastleHealth/50.png'),
                         'castle50':load('assets/CastleHealth/51.png'),
                         'castle49':load('assets/CastleHealth/52.png'),
                         'castle48':load('assets/CastleHealth/53.png'),
                         'castle47':load('assets/CastleHealth/54.png'),
                         'castle46':load('assets/CastleHealth/55.png'),
                         'castle45':load('assets/CastleHealth/56.png'),
                         'castle44':load('assets/CastleHealth/57.png'),
                         'castle43':load('assets/CastleHealth/58.png'),
                         'castle42':load('assets/CastleHealth/59.png'),
                         'castle41':load('assets/CastleHealth/60.png'),
                         'castle40':load('assets/CastleHealth/61.png'),
                         'castle39':load('assets/CastleHealth/62.png'),
                         'castle38':load('assets/CastleHealth/63.png'),
                         'castle37':load('assets/CastleHealth/64.png'),
                         'castle36':load('assets/CastleHealth/65.png'),
                         'castle35':load('assets/CastleHealth/66.png'),
                         'castle34':load('assets/CastleHealth/67.png'),
                         'castle33':load('assets/CastleHealth/68.png'),
                         'castle32':load('assets/CastleHealth/69.png'),
                         'castle31':load('assets/CastleHealth/70.png'),
                         'castle30':load('assets/CastleHealth/71.png'),
                         'castle29':load('assets/CastleHealth/72.png'),
                         'castle28':load('assets/CastleHealth/73.png'),
                         'castle27':load('assets/CastleHealth/74.png'),
                         'castle26':load('assets/CastleHealth/75.png'),
                         'castle25':load('assets/CastleHealth/76.png'),
                         'castle24':load('assets/CastleHealth/77.png'),
                         'castle23':load('assets/CastleHealth/78.png'),
                         'castle22':load('assets/CastleHealth/79.png'),
                         'castle21':load('assets/CastleHealth/80.png'),
                         'castle20':load('assets/CastleHealth/81.png'),
                         'castle19':load('assets/CastleHealth/82.png'),
                         'castle18':load('assets/CastleHealth/83.png'),
                         'castle17':load('assets/CastleHealth/84.png'),
                         'castle16':load('assets/CastleHealth/85.png'),
                         'castle15':load('assets/CastleHealth/86.png'),
                         'castle14':load('assets/CastleHealth/87.png'),
                         'castle13':load('assets/CastleHealth/88.png'),
                         'castle12':load('assets/CastleHealth/89.png'),
                         'castle11':load('assets/CastleHealth/90.png'),
                         'castle10':load('assets/CastleHealth/91.png'),
                         'castle9':load('assets/CastleHealth/92.png'),
                         'castle8':load('assets/CastleHealth/93.png'),
                         'castle7':load('assets/CastleHealth/94.png'),
                         'castle6':load('assets/CastleHealth/95.png'),
                         'castle5':load('assets/CastleHealth/96.png'),
                         'castle4':load('assets/CastleHealth/97.png'),
                         'castle3':load('assets/CastleHealth/98.png'),
                         'castle2':load('assets/CastleHealth/99.png'),
                         'castle1':load('assets/CastleHealth/100.png')}
        super(Health, self).__init__(self.emotions['5'])
        self.position = pos = eu.Vector2(x, y)
        self.cshape = cm.CircleShape(pos, self.width/2)

        self.hp = 1000
        
    def one(self):
        self.image = self.emotions['1']
    def two(self):
        self.image = self.emotions['2']
    def three(self):
        self.image = self.emotions['3']
    def four(self):
        self.image = self.emotions['4']
    def five(self):
        self.image = self.emotions['5']

    def castleHealthCheck(self, check):
        if check == '100':
            self.image = self.emotions['castle100']
        elif check == '99':
            self.image = self.emotions['castle99']
        elif check == '98':
            self.image = self.emotions['castle98']
        elif check == '97':
            self.image = self.emotions['castle97']
        elif check == '96':
            self.image = self.emotions['castle4']
        elif check == '95':
            self.image = self.emotions['castle5']
        elif check == '94':
            self.image = self.emotions['castle6']
        elif check == '93':
            self.image = self.emotions['castle7']
        elif check == '92':
            self.image = self.emotions['castle8']
        elif check == '91':
            self.image = self.emotions['castle9']

class Enemy(cocos.sprite.Sprite):
    def __init__(self, pos):
        self.emotions = {'enemyRun1R':enemyRun1AniR,
                         'enemyRun1L':enemyRun1AniL,
                         'enemyAttack1R':enemyAttack1AniR,
                         'enemyAttack1L':enemyAttack1AniL,
                         'enemyAttack1L1':load('assets/enemy/enemyAttack1L1.png'),
                         'enemyAttack1L2':load('assets/enemy/enemyAttack1L2.png'),
                         'enemyAttack1R1':load('assets/enemy/enemyAttack1R1.png'),
                         'enemyAttack1R2':load('assets/enemy/enemyAttack1R2.png'),
                         'enemydie1R':load('assets/enemy/enemydie1R.png'),
                         'enemydie1L':load('assets/enemy/enemydie1L.png'),
                         'enemyRun2R':enemyRun2AniR,
                         'enemyRun2L':enemyRun2AniL,
                         'enemyAttack2L1':load('assets/enemy/enemyAttack2L1.png'),
                         'enemyAttack2L2':load('assets/enemy/enemyAttack2L2.png'),
                         'enemyAttack2R1':load('assets/enemy/enemyAttack2R1.png'),
                         'enemyAttack2R2':load('assets/enemy/enemyAttack2R2.png'),
                         'enemydie2R':load('assets/enemy/enemyAttack2L2.png'),
                         'enemydie2L':load('assets/enemy/enemyAttack2R2.png'),
                         'enemyRun3R':enemyRun3AniR,
                         'enemyRun3L':enemyRun3AniL,
                         'enemyAttack3L1':load('assets/enemy/enemyAttack3L1.png'),
                         'enemyAttack3L2':load('assets/enemy/enemyAttack3L2.png'),
                         'enemyAttack3L3':load('assets/enemy/enemyAttack3L3.png'),
                         'enemyAttack3L4':load('assets/enemy/enemyAttack3L4.png'),
                         'enemyAttack3R1':load('assets/enemy/enemyAttack3R1.png'),
                         'enemyAttack3R2':load('assets/enemy/enemyAttack3R2.png'),
                         'enemyAttack3R3':load('assets/enemy/enemyAttack3R3.png'),
                         'enemyAttack3R4':load('assets/enemy/enemyAttack3R4.png'),
                         'enemydie3R':load('assets/enemy/enemydie3R.png'),
                         'enemydie3L':load('assets/enemy/enemydie3L.png'),
                         'enemyRun4R':enemyRun4AniR,
                         'enemyRun4L':enemyRun4AniL,
                         'enemyAttack4L1':load('assets/enemy/enemyAttack4L1.png'),
                         'enemyAttack4L2':load('assets/enemy/enemyAttack4L2.png'),
                         'enemyAttack4R1':load('assets/enemy/enemyAttack4R1.png'),
                         'enemyAttack4R2':load('assets/enemy/enemyAttack4R2.png'),
                         'enemydie4R':load('assets/enemy/enemydie4.png'),
                         'enemydie4L':load('assets/enemy/enemydie4.png')}
        super(Enemy, self).__init__(self.emotions['enemyRun1L'])

        self.position = pos
        self.cshape = cm.CircleShape(pos, self.width/2)
        self.enemyAttackTime = 0
        self.health = 60
        self.destroyed = False
        self.lifeTime = 0
        self.life = True
        self.speed = 100.0
        self.RunUser = True         # 걷는 중
        self.AtkUser = False        # 공격 중
        self.hp = 100
        
        # 원거리랑 근접 공격 어떻게 구별할것인지?

    def hit(self):
        if self.health <= 0:
            self.destroyed = True
            self.kill()
                
    def enemyR1R(self):
        self.image = self.emotions['enemyRun1R']
    def enemyR1L(self):
        self.image = self.emotions['enemyRun1L']
    def enemyA1R(self):
        self.image = self.emotions['enemyAttack1R']
    def enemyA1L(self):
        self.image = self.emotions['enemyAttack1L']
    def enemyDie1L(self):
        self.image = self.emotions['enemydie1L']
    def enemyDie1R(self):
        self.image = self.emotions['enemydie1R']
            
    def enemyR2R(self):
        self.image = self.emotions['enemyRun2R']
    def enemyR2L(self):
        self.image = self.emotions['enemyRun2L']
    def enemyA2R(self):
        self.image = self.emotions['enemyAttack2R']
    def enemyA2L(self):
        self.image = self.emotions['enemyAttack2L']
    def enemyDie2L(self):
        self.image = self.emotions['enemydie2L']
    def enemyDie2R(self):
        self.image = self.emotions['enemydie2R']
        
    def enemyR3R(self):
        self.image = self.emotions['enemyRun3R']
    def enemyR3L(self):
        self.image = self.emotions['enemyRun3L']
    def enemyA3R(self):
        self.image = self.emotions['enemyAttack3R']
    def enemyA3L(self):
        self.image = self.emotions['enemyAttack3L']
    def enemyDie3L(self):
        self.image = self.emotions['enemydie3L']
    def enemyDie3R(self):
        self.image = self.emotions['enemydie3R']

    def enemyDie4L(self):
        self.image = self.emotions['enemydie4L']
    def enemyDie4R(self):
        self.image = self.emotions['enemydie4R']
     
class Resource(cocos.sprite.Sprite):
    def __init__(self, pos):
        self.emotions = {'rock1':load('assets/gameBGOBJ/rock3.png'),
                         'rock2':load('assets/gameBGOBJ/rock2.png'),
                         'rock3':load('assets/gameBGOBJ/rock1.png'),
                         'bomb1':load('assets/gameBGOBJ/bomb.png'),
                         'space':load('assets/gameBGOBJ/space.png'),
                         'fire':fire,
                         'goalMine':load('assets/gameBGOBJ/goalMine1.png'),
                         'ice':ice,
                         'iceFan':load('assets/gameBGOBJ/iceFan.png'),
                         'empty':load('assets/remote/empty.png')}
        super(Resource, self).__init__(self.emotions['rock1'])
        self.position = pos
        self.cshape = cm.CircleShape(pos, self.width/2)
        self.ironCheck = False
        self.ice = False
        self.iceTime = 0


class Line(cocos.sprite.Sprite):
    def __init__(self,x, y):
        self.emotions = {'empty':load('assets/line/empty.png'),
                         '1':load('assets/line/11.png'),
                         '2':load('assets/line/22.png'),
                         '3':load('assets/line/33.png'),
                         '4':load('assets/line/44.png')}
        super(Line, self).__init__(self.emotions['empty'])
        self.position = pos = eu.Vector2(x, y)
        self.cshape = cm.CircleShape(pos, self.width/2)
    def empty(self):
        self.image = self.emotions['empty']
    def one(self):
        self.image = self.emotions['1']
    def two(self):
        self.image = self.emotions['2']
    def three(self):
        self.image = self.emotions['3']
    def four(self):
        self.image = self.emotions['4']

class Remote(cocos.sprite.Sprite):
    def __init__(self,x, y):
        self.emotions = {'remote1':load('assets/remote/1.png'),
                         'remote2':load('assets/remote/2.png'),
                         'remote3':load('assets/remote/3.png'),
                         'remote4':load('assets/remote/4.png'),
                         'remote5':load('assets/remote/5.png'),
                         'remote6':load('assets/remote/6.png'),
                         'remote7':load('assets/remote/7.png'),
                         'empty':load('assets/remote/empty.png'),
                         'remote1L':load('assets/remote/12.png'),
                         'remote1R':load('assets/remote/11.png')
                         }
        super(Remote, self).__init__(self.emotions['empty'])
        self.position = pos = eu.Vector2(x, y)
        self.cshape = cm.CircleShape(pos, self.width/2)
        self.lifeTime = 0
        
    def empty(self):
        self.image = self.emotions['empty']
        
class MainLayer(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super(MainLayer, self).__init__()

        self.emptySun = Sun((1500, 700))
        self.emptySun.image = self.emptySun.emotions['empty']
        
        self.add(self.emptySun)
        
        self.start = Start((750, 400))
        self.start1 = Start((750, 400))
        
        self.playTime = 0

        self.line1 = Line(1230, 180)
        self.line2 = Line(1230, 170)

        self.line3 = Line(430, 180)
        self.line4 = Line(175, 170)
        
        self.add(self.line1)
        self.add(self.line2)
        self.add(self.line3)
        self.add(self.line4)
        
        self.player = Actor(750, 45)

        self.iceFan1 = Resource((1340, 70))
        self.iceFan1.image = self.iceFan1.emotions['empty']
        self.add(self.iceFan1)

        self.iceFan2 = Resource((1130, 70))
        self.iceFan2.image = self.iceFan2.emotions['empty']
        self.add(self.iceFan2)

        self.iceFan3 = Resource((60, 70))
        self.iceFan3.image = self.iceFan3.emotions['empty']
        self.add(self.iceFan3)

        self.iceFan4 = Resource((270, 70))
        self.iceFan4.image = self.iceFan4.emotions['empty']
        self.add(self.iceFan4)
        
        # 적 추가(근접 1좌)
        self.enemy1L = list()        
        self.enemy1 = Enemy((random.randrange(-2000, -100), random.randrange(55, 70)))
        self.enemy2 = Enemy((random.randrange(-2000, -100), random.randrange(55, 70)))
        self.enemy3 = Enemy((random.randrange(-2000, -100), random.randrange(55, 70)))
        self.enemy4 = Enemy((random.randrange(-3000, -2000), random.randrange(55, 70)))
        self.enemy5 = Enemy((random.randrange(-3000, -2000), random.randrange(55, 70)))
        self.enemy6 = Enemy((random.randrange(-3000, -2000), random.randrange(55, 70)))
        self.enemy7 = Enemy((random.randrange(-4000, -3000), random.randrange(55, 70)))
        self.enemy8 = Enemy((random.randrange(-4000, -3000), random.randrange(55, 70)))
        self.enemy9 = Enemy((random.randrange(-5000, -4000), random.randrange(55, 70)))
        self.enemy10 = Enemy((random.randrange(-5000, -4000), random.randrange(55, 70)))

        self.enemy1L.append(self.enemy1)
        self.enemy1L.append(self.enemy2)
        self.enemy1L.append(self.enemy3)
        self.enemy1L.append(self.enemy4)
        self.enemy1L.append(self.enemy5)
        self.enemy1L.append(self.enemy6)
        self.enemy1L.append(self.enemy7)
        self.enemy1L.append(self.enemy8)
        self.enemy1L.append(self.enemy9)
        self.enemy1L.append(self.enemy10)

        # 적 추가(근접 1우)
        self.enemy1R = list()
        self.enemy11 = Enemy((random.randrange(1600, 3500), random.randrange(55, 70)))
        self.enemy12 = Enemy((random.randrange(1600, 3500), random.randrange(55, 70)))
        self.enemy13 = Enemy((random.randrange(1600, 3500), random.randrange(55, 70)))
        self.enemy14 = Enemy((random.randrange(3500, 4500), random.randrange(55, 70)))
        self.enemy15 = Enemy((random.randrange(3500, 4500), random.randrange(55, 70)))
        self.enemy16 = Enemy((random.randrange(4500, 5500), random.randrange(55, 70)))
        self.enemy17 = Enemy((random.randrange(5500, 6500), random.randrange(55, 70)))
        self.enemy18 = Enemy((random.randrange(5500, 6500), random.randrange(55, 70)))
        self.enemy19 = Enemy((random.randrange(6500, 7500), random.randrange(55, 70)))
        self.enemy20 = Enemy((random.randrange(6500, 7500), random.randrange(55, 70)))

        self.enemy1R.append(self.enemy11)
        self.enemy1R.append(self.enemy12)
        self.enemy1R.append(self.enemy13)
        self.enemy1R.append(self.enemy14)
        self.enemy1R.append(self.enemy15)
        self.enemy1R.append(self.enemy16)
        self.enemy1R.append(self.enemy17)
        self.enemy1R.append(self.enemy18)
        self.enemy1R.append(self.enemy19)
        self.enemy1R.append(self.enemy20)

        # 적 추가(원거리 2좌)
        self.enemy2L = list()
        self.enemy21 = Enemy((random.randrange(-3000, -2000), random.randrange(55, 70)))
        self.enemy22 = Enemy((random.randrange(-3000, -2000), random.randrange(55, 70)))
        self.enemy23 = Enemy((random.randrange(-4000, -3000), random.randrange(55, 70)))
        self.enemy24 = Enemy((random.randrange(-5000, -4000), random.randrange(55, 70)))
        self.enemy25 = Enemy((random.randrange(-6000, -5000), random.randrange(55, 70)))

        self.enemy2L.append(self.enemy21)
        self.enemy2L.append(self.enemy22)
        self.enemy2L.append(self.enemy23)
        self.enemy2L.append(self.enemy24)
        self.enemy2L.append(self.enemy25)

        # 적 원거리 공격 추가(2좌)
        self.enemy2LAttack = list()
        self.enemy21Attack = Remote(414, random.randrange(35, 100))
        self.enemy22Attack = Remote(420, random.randrange(35, 100))
        self.enemy23Attack = Remote(419, random.randrange(35, 100))
        self.enemy24Attack = Remote(412, random.randrange(35, 100))
        self.enemy25Attack = Remote(410, random.randrange(35, 100))

        self.enemy2LAttack.append(self.enemy21Attack)
        self.enemy2LAttack.append(self.enemy22Attack)
        self.enemy2LAttack.append(self.enemy23Attack)
        self.enemy2LAttack.append(self.enemy24Attack)
        self.enemy2LAttack.append(self.enemy25Attack)

        # 적 추가(원거리 2우)
        self.enemy2R = list()
        self.enemy26 = Enemy((random.randrange(2500, 3500), random.randrange(55, 70)))
        self.enemy27 = Enemy((random.randrange(2500, 3500), random.randrange(55, 70)))
        self.enemy28 = Enemy((random.randrange(3500, 4500), random.randrange(55, 70)))
        self.enemy29 = Enemy((random.randrange(4500, 5500), random.randrange(55, 70)))
        self.enemy30 = Enemy((random.randrange(6500, 7500), random.randrange(55, 70)))

        self.enemy2R.append(self.enemy26)
        self.enemy2R.append(self.enemy27)
        self.enemy2R.append(self.enemy28)
        self.enemy2R.append(self.enemy29)
        self.enemy2R.append(self.enemy30)

        # 적 원거리 공격 추가(2우)
        self.enemy2RAttack = list()
        self.enemy26Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))
        self.enemy27Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))
        self.enemy28Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))
        self.enemy29Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))
        self.enemy30Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))

        self.enemy2RAttack.append(self.enemy26Attack)
        self.enemy2RAttack.append(self.enemy27Attack)
        self.enemy2RAttack.append(self.enemy28Attack)
        self.enemy2RAttack.append(self.enemy29Attack)
        self.enemy2RAttack.append(self.enemy30Attack)        

        # 적 추가(근접 2좌)
        self.enemy3L = list()        
        self.enemy31 = Enemy((random.randrange(-3000, -1000), random.randrange(40, 140)))
        self.enemy32 = Enemy((random.randrange(-4000, -2000), random.randrange(40, 140)))
        self.enemy33 = Enemy((random.randrange(-5000, -3000), random.randrange(40, 140)))
        self.enemy34 = Enemy((random.randrange(-6000, -4000), random.randrange(40, 140)))
        self.enemy35 = Enemy((random.randrange(-7000, -5000), random.randrange(40, 140)))
        
        self.enemy3L.append(self.enemy31)
        self.enemy3L.append(self.enemy32)
        self.enemy3L.append(self.enemy33)
        self.enemy3L.append(self.enemy34)
        self.enemy3L.append(self.enemy35)

        # 적 추가(근접 2우)
        self.enemy3R = list()        
        self.enemy36 = Enemy((random.randrange(4500, 5500), random.randrange(40, 140)))
        self.enemy37 = Enemy((random.randrange(5500, 6500), random.randrange(40, 140)))
        self.enemy38 = Enemy((random.randrange(7500, 9000), random.randrange(40, 140)))
        self.enemy39 = Enemy((random.randrange(5500, 6500), random.randrange(40, 140)))
        self.enemy40 = Enemy((random.randrange(6500, 8000), random.randrange(40, 140)))
        
        self.enemy3R.append(self.enemy36)
        self.enemy3R.append(self.enemy37)
        self.enemy3R.append(self.enemy38)
        self.enemy3R.append(self.enemy39)
        self.enemy3R.append(self.enemy40)

        # 적 추가(원거리 4좌)
        self.enemy4L = list()        
        self.enemy41 = Enemy((random.randrange(-3000, -1000), random.randrange(40, 140)))
        self.enemy42 = Enemy((random.randrange(-4000, -2000), random.randrange(40, 140)))
        self.enemy43 = Enemy((random.randrange(-5000, -3000), random.randrange(40, 140)))
        self.enemy44 = Enemy((random.randrange(-6000, -4000), random.randrange(40, 140)))
        self.enemy45 = Enemy((random.randrange(-7000, -5000), random.randrange(40, 140)))
        
        self.enemy4L.append(self.enemy41)
        self.enemy4L.append(self.enemy42)
        self.enemy4L.append(self.enemy43)
        self.enemy4L.append(self.enemy44)
        self.enemy4L.append(self.enemy45)

        # 적 원거리 공격 추가(4좌)
        self.enemy4LAttack = list()
        self.enemy41Attack = Remote(random.randrange(400, 450), random.randrange(35, 100))
        self.enemy42Attack = Remote(random.randrange(400, 450), random.randrange(35, 100))
        self.enemy43Attack = Remote(random.randrange(400, 450), random.randrange(35, 100))
        self.enemy44Attack = Remote(random.randrange(400, 450), random.randrange(35, 100))
        self.enemy45Attack = Remote(random.randrange(400, 450), random.randrange(35, 100))

        self.enemy4LAttack.append(self.enemy41Attack)
        self.enemy4LAttack.append(self.enemy42Attack)
        self.enemy4LAttack.append(self.enemy43Attack)
        self.enemy4LAttack.append(self.enemy44Attack)
        self.enemy4LAttack.append(self.enemy45Attack)

        # 적 추가(원거리 4우)
        self.enemy4R = list()        
        self.enemy46 = Enemy((random.randrange(4500, 5500), random.randrange(40, 140)))
        self.enemy47 = Enemy((random.randrange(5500, 6500), random.randrange(40, 140)))
        self.enemy48 = Enemy((random.randrange(7500, 9000), random.randrange(40, 140)))
        self.enemy49 = Enemy((random.randrange(5500, 6500), random.randrange(40, 140)))
        self.enemy50 = Enemy((random.randrange(6500, 8000), random.randrange(40, 140)))
        
        self.enemy4R.append(self.enemy46)
        self.enemy4R.append(self.enemy47)
        self.enemy4R.append(self.enemy48)
        self.enemy4R.append(self.enemy49)
        self.enemy4R.append(self.enemy50)

        # 적 원거리 공격 추가(4우)
        self.enemy4RAttack = list()
        self.enemy46Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))
        self.enemy47Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))
        self.enemy48Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))
        self.enemy49Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))
        self.enemy50Attack = Remote(random.randrange(1050, 1080), random.randrange(35, 100))

        self.enemy4RAttack.append(self.enemy46Attack)
        self.enemy4RAttack.append(self.enemy47Attack)
        self.enemy4RAttack.append(self.enemy48Attack)
        self.enemy4RAttack.append(self.enemy49Attack)
        self.enemy4RAttack.append(self.enemy50Attack)

        self.enemy = list()
        self.enemy.append(self.enemy1)
        self.enemy.append(self.enemy2)
        self.enemy.append(self.enemy3)
        self.enemy.append(self.enemy4)
        self.enemy.append(self.enemy5)
        self.enemy.append(self.enemy6)
        self.enemy.append(self.enemy7)
        self.enemy.append(self.enemy8)
        self.enemy.append(self.enemy9)
        self.enemy.append(self.enemy10)
        self.enemy.append(self.enemy11)
        self.enemy.append(self.enemy12)
        self.enemy.append(self.enemy13)
        self.enemy.append(self.enemy14)
        self.enemy.append(self.enemy15)
        self.enemy.append(self.enemy16)
        self.enemy.append(self.enemy17)
        self.enemy.append(self.enemy18)
        self.enemy.append(self.enemy19)
        self.enemy.append(self.enemy20)
        self.enemy.append(self.enemy21)
        self.enemy.append(self.enemy22)
        self.enemy.append(self.enemy23)
        self.enemy.append(self.enemy24)
        self.enemy.append(self.enemy25)
        self.enemy.append(self.enemy26)
        self.enemy.append(self.enemy27)
        self.enemy.append(self.enemy28)
        self.enemy.append(self.enemy29)
        self.enemy.append(self.enemy30)
        self.enemy.append(self.enemy31)
        self.enemy.append(self.enemy32)
        self.enemy.append(self.enemy33)
        self.enemy.append(self.enemy34)
        self.enemy.append(self.enemy35)
        self.enemy.append(self.enemy36)
        self.enemy.append(self.enemy37)
        self.enemy.append(self.enemy38)
        self.enemy.append(self.enemy39)
        self.enemy.append(self.enemy40)
        self.enemy.append(self.enemy41)
        self.enemy.append(self.enemy42)
        self.enemy.append(self.enemy43)
        self.enemy.append(self.enemy44)
        self.enemy.append(self.enemy45)
        self.enemy.append(self.enemy46)
        self.enemy.append(self.enemy47)
        self.enemy.append(self.enemy48)
        self.enemy.append(self.enemy49)
        self.enemy.append(self.enemy50)        

        for i in self.enemy2LAttack:
            self.add(i)

        for i in self.enemy2RAttack:
            self.add(i)

        for i in self.enemy4LAttack:
            self.add(i)

        for i in self.enemy4RAttack:
            self.add(i)
            
        for i in self.enemy1R:
            i.image = i.emotions['enemyRun1R']

        for i in self.enemy2L:
            i.image = i.emotions['enemyRun2L']

        for i in self.enemy2R:
            i.image = i.emotions['enemyRun2R']

        for i in self.enemy3L:
            i.image = i.emotions['enemyRun3L']

        for i in self.enemy3R:
            i.image = i.emotions['enemyRun3R']

        for i in self.enemy4L:
            i.image = i.emotions['enemyRun4L']

        for i in self.enemy4R:
            i.image = i.emotions['enemyRun4R']
            
        for i in self.enemy1L:
            self.add(i)

        for i in self.enemy1R:        
            self.add(i)

        for i in self.enemy2L:
            self.add(i)

        for i in self.enemy2R:
            self.add(i)

        for i in self.enemy3L:
            self.add(i)

        for i in self.enemy3R:
            self.add(i)

        for i in self.enemy4L:
            i.hp = 300
            self.add(i)

        for i in self.enemy4R:
            i.hp = 300
            self.add(i)
            
        self.rock1 = Resource((600, 190))

        # ice 장소 추가
        self.ice1 = Resource((740,450))
        self.ice1.image = self.ice1.emotions['ice']
        self.add(self.ice1)
        self.icing = checkTry(self.ice1.position[0] + 50, self.ice1.position[1])
        self.icing.zero()
        self.add(self.icing)
        
        self.space = Resource((750, 320))
        self.space.image = self.space.emotions['space']

        self.ironCheck = checkTry(self.space.position[0] + 30, self.space.position[1] + 60)
        self.ironCheck.image = self.ironCheck.emotions['ironCheck']
        self.add(self.ironCheck)
        
        self.goalMine = Resource((845, 47))
        self.goalMine.image = self.goalMine.emotions['goalMine']
        
        self.fire = Resource((778, 344))
        self.fire.image = self.fire.emotions['fire']
        
        self.healthPos = self.player.position

        self.heal = Health(self.healthPos[0], self.healthPos[1] + 60)

        self.mining1 = checkTry(self.rock1.position[0] + 80, self.rock1.position[1])
        self.mining1.zero()
        self.add(self.mining1)

        self.mining2 = checkTry(self.space.position[0] + 80, self.space.position[1])
        self.mining2.zero()
        self.add(self.mining2)
        
        # 성 체력
        self.castleHealth = Health(410, 625)
        self.castleHealth.image = self.castleHealth.emotions['castle100']
        self.add(self.castleHealth)
        
        # Bomb1(우하)
        self.bomb1 = Bomb(1030, 179)
        self.add(self.bomb1)
        
        # Bomb1 check
        self.bombCheck1 = checkTry(self.bomb1.position[0] - 35, self.bomb1.position[1] + 50)
        self.iceCheck1 = checkTry(self.bomb1.position[0] + 35, self.bomb1.position[1] + 50)
        self.iceCheck1.image = self.iceCheck1.emotions['ice']

        self.mining = checkTry(1010, 47)
        self.mining.zero()
        self.add(self.mining)
        
        self.bombPowerCheck1 = checkTry(self.bomb1.position[0], self.bomb1.position[1] + 50)
        self.bombPowerCheck1.image = self.bombPowerCheck1.emotions['bombPower']
        self.add(self.bombPowerCheck1)        
        self.add(self.iceCheck1)

        # Bomb2(우상)
        self.bomb2 = Bomb(1030, 425)

        # checkTry
        self.bombCheck2 = checkTry(self.bomb2.position[0] - 35, self.bomb2.position[1] + 50)
        self.iceCheck2 = checkTry(self.bomb2.position[0] + 35, self.bomb2.position[1] + 50)
        self.iceCheck2.image = self.iceCheck2.emotions['ice']
        self.bombPowerCheck2 = checkTry(self.bomb2.position[0], self.bomb2.position[1] + 50)
        self.bombPowerCheck2.image = self.bombPowerCheck2.emotions['bombPower']
        self.add(self.bombPowerCheck2)
        self.add(self.bomb2)
        self.add(self.bombCheck2)
        self.add(self.iceCheck2)

        self.bomb3 = Bomb(480, 179)
        self.bomb3.image = self.bomb3.emotions['leftBomb']

        # checkTry
        self.bombCheck3 = checkTry(self.bomb3.position[0] - 35, self.bomb3.position[1] + 50)
        self.iceCheck3 = checkTry(self.bomb3.position[0] + 35, self.bomb3.position[1] + 50)
        self.iceCheck3.image = self.iceCheck3.emotions['ice']
        self.bombPowerCheck3 = checkTry(self.bomb3.position[0], self.bomb3.position[1] + 50)
        self.bombPowerCheck3.image = self.bombPowerCheck3.emotions['bombPower']
        self.add(self.bombPowerCheck3)
        self.add(self.bomb3)
        self.add(self.bombCheck3)
        self.add(self.iceCheck3)
        
        self.bomb4 = Bomb(480, 425)
        self.bomb4.image = self.bomb4.emotions['leftBomb']

        # checkTry
        self.bombCheck4 = checkTry(self.bomb4.position[0] - 35, self.bomb4.position[1] + 50)
        self.iceCheck4 = checkTry(self.bomb4.position[0] + 35, self.bomb4.position[1] + 50)
        self.iceCheck4.image = self.iceCheck4.emotions['ice']
        self.bombPowerCheck4 = checkTry(self.bomb4.position[0], self.bomb4.position[1] + 50)
        self.bombPowerCheck4.image = self.bombPowerCheck4.emotions['bombPower']
        self.add(self.bombPowerCheck4)
        self.add(self.bomb4)
        self.add(self.bombCheck4)
        self.add(self.iceCheck4)

        # 폭탄 생성 및 발사
        self.bombShot1 = Bomb(self.bomb1.position[0] + 100, self.bomb1.position[1] + 30)
        self.bombShot1.image = self.bombShot1.emotions['bomb']

        self.bombShot2 = Bomb(self.bomb2.position[0] + 100, self.bomb2.position[1] + 30)
        self.bombShot2.image = self.bombShot2.emotions['bomb']

        self.bombShot3 = Bomb(self.bomb3.position[0] - 100, self.bomb3.position[1] + 30)
        self.bombShot3.image = self.bombShot3.emotions['bomb']

        self.bombShot4 = Bomb(self.bomb4.position[0] - 100, self.bomb4.position[1] + 30)
        self.bombShot4.image = self.bombShot4.emotions['bomb']
        
        self.add(self.heal)
        self.add(self.rock1)
        self.add(self.space)
        self.add(self.fire)
        self.add(self.goalMine)
        self.add(self.player)
        
        self.add(self.bombCheck1)
        
        self.time = 0
        self.time1 = 0
        self.soundTime = 0
        self.enemyAttackTime = 0


        
        self.down_check = False
        self.up_check = False
        
        self.add(self.start)
        self.add(self.start1)
        
        cell = self.player.width * 1.25
        self.collman = cm.CollisionManagerGrid(0, 640, 0, 480, cell, cell)
        self.speed = 100.0
        
        self.pressed = defaultdict(int)
        
        self.schedule(self.update)
        
    def on_key_press(self, k, m):
        self.pressed[k] = 1

    def on_key_release(self, k, m):
        self.pressed[k] = 0

    def update(self, dt):
        self.collman.clear()
        self.start1.time += 0.05
        
        self.time += 0.05
        if self.time > 1:
            self.time = 0

        self.playTime += 0.01

            
        self.soundTime += 0.05
        if self.soundTime > 3.2:
            self.soundTime = 0
            
        self.time1 += 0.05
        if self.time1 > 0.6:
            self.time1 = 0

        
        # 적 1 이동
        for i in self.enemy1L:
            i.enemyAttackTime += 0.05
            if i.enemyAttackTime > 0.6:
                i.enemyAttackTime = 0
        for i in self.enemy1R:
            i.enemyAttackTime += 0.05
            if i.enemyAttackTime > 0.6:
                i.enemyAttackTime = 0
        for i in self.enemy2L:
            i.enemyAttackTime += 0.05
            if i.enemyAttackTime > 0.6:
                i.enemyAttackTime = 0
        for i in self.enemy2R:
            i.enemyAttackTime += 0.05
            if i.enemyAttackTime > 0.6:
                i.enemyAttackTime = 0
        for i in self.enemy3L:
            i.enemyAttackTime += 0.05
            if i.enemyAttackTime > 0.6:
                i.enemyAttackTime = 0
        for i in self.enemy3R:
            i.enemyAttackTime += 0.05
            if i.enemyAttackTime > 0.6:
                i.enemyAttackTime = 0
        for i in self.enemy4L:
            i.enemyAttackTime += 0.05
            if i.enemyAttackTime > 0.6:
                i.enemyAttackTime = 0
        for i in self.enemy4R:
            i.enemyAttackTime += 0.05
            if i.enemyAttackTime > 0.6:
                i.enemyAttackTime = 0
                
        self.player.stamina += 0.01
        if self.player.stamina > 5:
            self.player.stamina = 5

        if self.player.stamina > -1 and self.player.stamina < 1:
            self.heal.one()
        if self.player.stamina >= 1 and self.player.stamina < 2:
            self.heal.two()
        if self.player.stamina >= 2 and self.player.stamina < 3:
            self.heal.three()
        if self.player.stamina >= 3 and self.player.stamina < 4:
            self.heal.four()
        if self.player.stamina >= 4 and self.player.stamina < 6:
            self.heal.five()
                        
        self.heal.position = (self.player.position[0], self.player.position[1] + 60)






        
        # ENEMY
        for i in self.enemy1L:
            if i.life == True:
                i.enemyAttackTime += 0.01
                dx = 0.5
                dy = 0
                if i.position[0] < 400:
                    if dx != 0 or dy != 0:
                        pos = i.position
                        new_x = pos[0] + i.speed * dx * dt
                        new_y = pos[1] + i.speed * dy * dt
                        i.position = (new_x, new_y)
                        i.cshape.center = i.position
                elif i.position[0] == 400:
                    i.position = (400, i.position[1])
                    i.enemyAttackTime = 0
                    i.RunUser = False
                    i.AtkUser = True
                else:
                    i.AtkUser = True
                    i.image = i.emotions['enemyAttack1L1']
                    if i.enemyAttackTime >= 0.5 and i.enemyAttackTime < 1.0:
                       i.image = i.emotions['enemyAttack1L2']
                       i.enemyAttackTime = 0
            if i.life == False:
                i.image = i.emotions['enemydie1L']
     
        for i in self.enemy1R:
            if i.life == True:
                i.enemyAttackTime += 0.01
                dx = -0.5
                dy = 0
                if i.position[0] > 1100:
                    if dx != 0 or dy != 0:
                        pos = i.position
                        new_x = pos[0] + i.speed * dx * dt
                        new_y = pos[1] + i.speed * dy * dt
                        i.position = (new_x, new_y)
                        i.cshape.center = i.position
                elif i.position[0] == 1100:
                    i.position = (1100, i.position[1])
                    i.enemyAttackTime = 0
                    i.RunUser = False
                    i.AtkUser = True
                else:
                    i.AtkUser = True
                    i.image = i.emotions['enemyAttack1R1']
                    if i.enemyAttackTime >= 0.5 and i.enemyAttackTime < 1.0:
                       i.image = i.emotions['enemyAttack1R2']
                       i.enemyAttackTime = 0
            if i.life == False:
                i.image = i.emotions['enemydie1R']

        for i in self.enemy2L:
            if i.life == True:
                i.enemyAttackTime += 0.01
                dx = 0.5
                dy = 0
                if i.position[0] < 210:
                    if dx != 0 or dy != 0:
                        pos = i.position
                        new_x = pos[0] + i.speed * dx * dt
                        new_y = pos[1] + i.speed * dy * dt
                        i.position = (new_x, new_y)
                        i.cshape.center = i.position
                        i.RunUser = True
                        i.AtkUser = False
                elif i.position[0] == 210:
                    i.position = (210, i.position[1])
                    i.enemyAttackTime = 0
                    i.RunUser = False
                    i.AtkUser = True
                else:
                    for j in self.enemy2LAttack:
                        j.lifeTime += 0.01
                        i.RunUser = False
                        i.AtkUser = True
                        j.position = (random.randrange(400, 450),random.randrange(35, 100))
                        if i.enemyAttackTime >= 0 and i.enemyAttackTime < 0.2:
                            i.image = i.emotions['enemyAttack2L1']
                        elif i.enemyAttackTime >= 0.2 and i.enemyAttackTime < 0.4:
                            i.image = i.emotions['enemyAttack2L2']
                        else:
                            i.enemyAttackTime = 0
                        if j.lifeTime >= 0 and j.lifeTime < 0.05:
                            j.image = j.emotions['empty']
                        elif j.lifeTime >= 0.05 and j.lifeTime < 0.1:
                            j.image = j.emotions['remote1']
                        elif j.lifeTime >= 0.1 and j.lifeTime < 0.15:
                            j.image = j.emotions['remote2']
                        elif j.lifeTime >= 0.15 and j.lifeTime < 0.25:
                            j.image = j.emotions['remote3']
                        elif j.lifeTime >= 0.25 and j.lifeTime < 0.35:
                            j.image = j.emotions['remote4']
                        elif j.lifeTime >= 0.35 and j.lifeTime < 0.45:
                            j.image = j.emotions['remote5']
                        elif j.lifeTime >= 0.45 and j.lifeTime < 0.50:
                            j.image = j.emotions['remote6']
                        else:
                            j.image = j.emotions['empty']
                            j.lifeTime = 0         
            elif i.life == False:
                i.image = i.emotions['enemyAttack2L1']

        for i in self.enemy2R:
            if i.life == True:
                i.enemyAttackTime += 0.01
                dx = -0.5
                dy = 0
                if i.position[0] > 1250:
                    if dx != 0 or dy != 0:
                        pos = i.position
                        new_x = pos[0] + i.speed * dx * dt
                        new_y = pos[1] + i.speed * dy * dt
                        i.position = (new_x, new_y)
                        i.cshape.center = i.position
                        i.RunUser = True
                        i.AtkUser = False
                elif i.position[0] == 1250:
                    i.position = (1250, i.position[1])
                    i.enemyAttackTime = 0
                    i.RunUser = False
                    i.AtkUser = True
                else:
                    for j in self.enemy2RAttack:
                        j.lifeTime += 0.01
                        i.AtkUser = True
                        i.RunUser = False
                        j.position = (random.randrange(1050, 1080),random.randrange(35, 100))
                        if i.enemyAttackTime >= 0 and i.enemyAttackTime < 0.2:
                            i.image = i.emotions['enemyAttack2R1']
                        elif i.enemyAttackTime >= 0.2 and i.enemyAttackTime < 0.4:
                            i.image = i.emotions['enemyAttack2R2']
                        else:
                            i.enemyAttackTime = 0
                        if j.lifeTime >= 0 and j.lifeTime < 0.05:
                            j.image = j.emotions['empty']
                        elif j.lifeTime >= 0.05 and j.lifeTime < 0.1:
                            j.image = j.emotions['remote1']
                        elif j.lifeTime >= 0.1 and j.lifeTime < 0.15:
                            j.image = j.emotions['remote2']
                        elif j.lifeTime >= 0.15 and j.lifeTime < 0.25:
                            j.image = j.emotions['remote3']
                        elif j.lifeTime >= 0.25 and j.lifeTime < 0.35:
                            j.image = j.emotions['remote4']
                        elif j.lifeTime >= 0.35 and j.lifeTime < 0.45:
                            j.image = j.emotions['remote5']
                        elif j.lifeTime >= 0.45 and j.lifeTime < 0.50:
                            j.image = j.emotions['remote6']
                        else:
                            j.image = j.emotions['empty']
                            j.lifeTime = 0         
            elif i.life == False:
                i.image = i.emotions['enemyAttack2R1']

        for i in self.enemy3L:
            if i.life == True:
                i.enemyAttackTime += 0.01
                dx = 0.5
                dy = 0
                if i.position[0] < 350:
                    if dx != 0 or dy != 0:
                        pos = i.position
                        new_x = pos[0] + i.speed * dx * dt
                        new_y = pos[1] + i.speed * dy * dt
                        i.position = (new_x, new_y)
                        i.cshape.center = i.position
                        i.RunUser = True
                        i.AtkUser = False
                elif i.position[0] == 350:
                    i.position = (random.randrange(345,360), i.position[1])
                    i.enemyAttackTime = 0
                    i.RunUser = False
                    i.AtkUser = True
                else:
                    i.RunUser = False
                    i.AtkUser = True
                    if i.enemyAttackTime >= 0 and i.enemyAttackTime < 0.2:
                        i.image = i.emotions['enemyAttack3L1']
                    elif i.enemyAttackTime >= 0.2 and i.enemyAttackTime < 0.3:
                        i.image = i.emotions['enemyAttack3L2']
                    elif i.enemyAttackTime >= 0.3 and i.enemyAttackTime < 0.4:
                        i.image = i.emotions['enemyAttack3L3']
                    elif i.enemyAttackTime >= 0.4 and i.enemyAttackTime < 0.5:
                        i.image = i.emotions['enemyAttack3L4']
                    else:
                        i.image = i.emotions['enemyAttack3L1']
                        i.enemyAttackTime = 0
            if i.life == False:
                i.image = i.emotions['enemydie3L']

        for i in self.enemy3R:
            if i.life == True:
                i.enemyAttackTime += 0.01
                dx = -0.5
                dy = 0
                if i.position[0] > 1100:
                    if dx != 0 or dy != 0:
                        pos = i.position
                        new_x = pos[0] + i.speed * dx * dt
                        new_y = pos[1] + i.speed * dy * dt
                        i.position = (new_x, new_y)
                        i.cshape.center = i.position
                        i.RunUser = True
                        i.AtkUser = False
                elif i.position[0] == 1100:
                    i.position = (random.randrange(1100,1150), i.position[1])
                    i.enemyAttackTime = 0
                    i.RunUser = False
                    i.AtkUser = True
                else:
                    i.RunUser = False
                    i.AtkUser = True
                    if i.enemyAttackTime >= 0 and i.enemyAttackTime < 0.2:
                        i.image = i.emotions['enemyAttack3R1']
                    elif i.enemyAttackTime >= 0.2 and i.enemyAttackTime < 0.3:
                        i.image = i.emotions['enemyAttack3R2']
                    elif i.enemyAttackTime >= 0.3 and i.enemyAttackTime < 0.4:
                        i.image = i.emotions['enemyAttack3R3']
                    elif i.enemyAttackTime >= 0.4 and i.enemyAttackTime < 0.5:
                        i.image = i.emotions['enemyAttack3R4']
                    else:
                        i.image = i.emotions['enemyAttack3R1']
                        i.enemyAttackTime = 0
            if i.life == False:
                i.image = i.emotions['enemydie3R']

        for i in self.enemy4L:
            if i.life == True:
                i.enemyAttackTime += 0.01
                dx = 0.5
                dy = 0
                if i.position[0] < 210:
                    if dx != 0 or dy != 0:
                        pos = i.position
                        new_x = pos[0] + i.speed * dx * dt
                        new_y = pos[1] + i.speed * dy * dt
                        i.position = (new_x, new_y)
                        i.cshape.center = i.position
                        i.RunUser = True
                        i.AtkUser = False
                elif i.position[0] == 210:
                    i.position = (210, i.position[1])
                    i.enemyAttackTime = 0
                    i.RunUser = False
                    i.AtkUser = True
                else:
                    for j in self.enemy4LAttack:
                        j.lifeTime += 0.01
                        i.RunUser = False
                        i.AtkUser = True
                        j.position = (random.randrange(400, 450),random.randrange(35, 100))
                        if i.enemyAttackTime >= 0 and i.enemyAttackTime < 0.4:
                            i.image = i.emotions['enemyAttack4L1']
                        elif i.enemyAttackTime >= 0.4 and i.enemyAttackTime < 0.8:
                            i.image = i.emotions['enemyAttack4L2']
                        else:
                            i.enemyAttackTime = 0
                        if j.lifeTime >= 0 and j.lifeTime < 0.05:
                            j.image = j.emotions['remote1L']
                            j.position = (random.randrange(420, 450),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.05 and j.lifeTime < 0.1:
                            j.image = j.emotions['remote1L']
                            j.position = (random.randrange(420, 450),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.1 and j.lifeTime < 0.15:
                            j.image = j.emotions['remote1L']
                            j.position = (random.randrange(420, 450),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.15 and j.lifeTime < 0.25:
                            j.image = j.emotions['remote1L']
                            j.position = (random.randrange(420, 450),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.25 and j.lifeTime < 0.35:
                            j.image = j.emotions['remote1L']
                            j.position = (random.randrange(420, 450),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.35 and j.lifeTime < 0.45:
                            j.image = j.emotions['remote1L']
                            j.position = (random.randrange(420, 450),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.45 and j.lifeTime < 0.50:
                            j.image = j.emotions['remote1L']
                            j.position = (random.randrange(420, 450),random.randrange(random.randrange(40,100)))
                        else:
                            j.image = j.emotions['empty']
                            j.lifeTime = 0         
            elif i.life == False:
                i.image = i.emotions['enemyAttack4L1']

        for i in self.enemy4R:
            if i.life == True:
                i.enemyAttackTime += 0.01
                dx = -0.5
                dy = 0
                if i.position[0] > 1250:
                    if dx != 0 or dy != 0:
                        pos = i.position
                        new_x = pos[0] + i.speed * dx * dt
                        new_y = pos[1] + i.speed * dy * dt
                        i.position = (new_x, new_y)
                        i.cshape.center = i.position
                        i.RunUser = True
                        i.AtkUser = False
                elif i.position[0] == 1250:
                    i.position = (1250, i.position[1])
                    i.enemyAttackTime = 0
                    i.RunUser = False
                    i.AtkUser = True
                else:
                    for j in self.enemy4LAttack:
                        j.lifeTime += 0.01
                        i.RunUser = False
                        i.AtkUser = True
                        j.position = (random.randrange(1050, 1080),random.randrange(35, 100))
                        if i.enemyAttackTime >= 0 and i.enemyAttackTime < 0.4:
                            i.image = i.emotions['enemyAttack4R1']
                        elif i.enemyAttackTime >= 0.4 and i.enemyAttackTime < 0.8:
                            i.image = i.emotions['enemyAttack4R2']
                        else:
                            i.enemyAttackTime = 0
                        if j.lifeTime >= 0 and j.lifeTime < 0.05:
                            j.image = j.emotions['remote1R']
                            j.position = (random.randrange(1040, 1080),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.05 and j.lifeTime < 0.1:
                            j.image = j.emotions['remote1R']
                            j.position = (random.randrange(1040, 1080),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.1 and j.lifeTime < 0.15:
                            j.image = j.emotions['remote1R']
                            j.position = (random.randrange(1040, 1080),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.15 and j.lifeTime < 0.25:
                            j.image = j.emotions['remote1R']
                            j.position = (random.randrange(1040, 1080),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.25 and j.lifeTime < 0.35:
                            j.image = j.emotions['remote1R']
                            j.position = (random.randrange(1040, 1080),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.35 and j.lifeTime < 0.45:
                            j.image = j.emotions['remote1R']
                            j.position = (random.randrange(1040, 1080),random.randrange(random.randrange(40,100)))
                        elif j.lifeTime >= 0.45 and j.lifeTime < 0.50:
                            j.image = j.emotions['remote1R']
                            j.position = (random.randrange(1040, 1080),random.randrange(random.randrange(40,100)))
                        else:
                            j.image = j.emotions['empty']
                            j.lifeTime = 0         
            elif i.life == False:
                i.image = i.emotions['enemyAttack4R1']
                
        # 중력 부분
        # 1층 중력부분
        if (self.player.position[0] > 473 and self.player.position[0] < 671) and (self.player.position[1] < 183.9 and self.player.position[1] >= 45): 
            x = 0
            y = -1
            if x != 0 or y != 0:
                pos = self.player.position
                new_x = pos[0] + self.player.speed * x * dt
                new_y = pos[1] + self.player.speed * y * dt
                self.player.position = (new_x, new_y)
                self.player.cshape.center = self.player.position
        elif (self.player.position[0] > 772 and self.player.position[0] < 1040) and (self.player.position[1] < 183.9 and self.player.position[1] >= 45): 
            x = 0
            y = -1
            if x != 0 or y != 0:
                pos = self.player.position
                new_x = pos[0] + self.player.speed * x * dt
                new_y = pos[1] + self.player.speed * y * dt
                self.player.position = (new_x, new_y)
                self.player.cshape.center = self.player.position

        # 2층 중력부분
        elif (self.player.position[0] >= 473 and self.player.position[0] <= 833) and (self.player.position[1] > 184 and self.player.position[1] <= 315): 
            x = 0
            y = -1
            if x != 0 or y != 0:
                pos = self.player.position
                new_x = pos[0] + self.player.speed * x * dt
                new_y = pos[1] + self.player.speed * y * dt
                self.player.position = (new_x, new_y)
                self.player.cshape.center = self.player.position
        elif (self.player.position[0] >= 924 and self.player.position[0] <= 1040) and (self.player.position[1] > 184 and self.player.position[1] <= 315): 
            x = 0
            y = -1
            if x != 0 or y != 0:
                pos = self.player.position
                new_x = pos[0] + self.player.speed * x * dt
                new_y = pos[1] + self.player.speed * y * dt
                self.player.position = (new_x, new_y)
                self.player.cshape.center = self.player.position

        # 3층 중력부분
        elif (self.player.position[0] >= 473 and self.player.position[0] <= 519) and (self.player.position[1] > 316 and self.player.position[1] <= 430): 
            x = 0
            y = -1
            if x != 0 or y != 0:
                pos = self.player.position
                new_x = pos[0] + self.player.speed * x * dt
                new_y = pos[1] + self.player.speed * y * dt
                self.player.position = (new_x, new_y)
                self.player.cshape.center = self.player.position
        elif (self.player.position[0] >= 602 and self.player.position[0] <= 1040) and (self.player.position[1] > 316 and self.player.position[1] <= 430):
            x = 0
            y = -1
            if x != 0 or y != 0:
                pos = self.player.position
                new_x = pos[0] + self.player.speed * x * dt
                new_y = pos[1] + self.player.speed * y * dt
                self.player.position = (new_x, new_y)
                self.player.cshape.center = self.player.position
                
        # 4층 중력부분
        elif (self.player.position[0] >= 473 and self.player.position[0] <= 1040) and (self.player.position[1] > 431 and self.player.position[1] <= 500): 
            x = 0
            y = -1
            if x != 0 or y != 0:
                pos = self.player.position
                new_x = pos[0] + self.player.speed * x * dt
                new_y = pos[1] + self.player.speed * y * dt
                self.player.position = (new_x, new_y)
                self.player.cshape.center = self.player.position
        
        # 층을 위한 구현
        # 1층
        if self.player.position[1] < 45 :
            self.player.position = (self.player.position[0], 45)
        # 2층
        if self.player.position[1] > 183  and self.player.position[1] <= 186:
            self.player.position = (self.player.position[0], 184)
        # 3층
        if self.player.position[1] > 315  and self.player.position[1] <= 318:
            self.player.position = (self.player.position[0], 316)
        # 4층
        if self.player.position[1] >= 430  and self.player.position[1] <= 433:
            self.player.position = (self.player.position[0], 431)
        
        # 사다리를 위한 구현
        # 1층
        if (self.player.position[0] >= 671 and self.player.position[0] < 772) and (self.player.position[1] >= 45 and self.player.position[1] <= 184):
            self.down_check = True
        # 2층
        elif (self.player.position[0] >= 833 and self.player.position[0] < 924) and (self.player.position[1] >= 184 and self.player.position[1] <= 316):
            self.down_check = True
        # 3층
        elif (self.player.position[0] >= 514 and self.player.position[0] < 607) and (self.player.position[1] >= 316 and self.player.position[1] <= 500):
            self.down_check = True
        # 4층
        else:
            self.down_check = False

        self.up_check = True
        
        # 건물밖 제어
        if self.player.position[0] < 473:
            self.player.position = (473, self.player.position[1])
        elif self.player.position[0] > 1040:
            self.player.position = (1040, self.player.position[1])
        
        # 제일 윗부분 범위
        top_check_pos = self.player.position
        if top_check_pos[1] < 433:
            self.top_check = True
        else:
            self.top_check = False

                
        if self.pressed[key.DOWN] and self.down_check:
            x = 0
            y = -2

            if self.time1 >= 0 and self.time1 < 0.3:
                self.player.upDown1()
            elif self.time1 >= 0.3 and self.time1 <= 0.6:
                self.player.upDown2()

            if x != 0 or y != 0:
                pos = self.player.position
                new_x = pos[0] + self.player.speed * x * dt
                new_y = pos[1] + self.player.speed * y * dt
                self.player.position = (new_x, new_y)
                self.player.cshape.center = self.player.position
                
        elif self.pressed[key.DOWN] and not self.down_check:
            self.player.action()
            
        elif self.pressed[key.UP] and self.down_check and self.top_check:
            x = 0
            y = 2

            if self.time1 >= 0 and self.time1 < 0.3:
                self.player.upDown1()
            elif self.time1 >= 0.3 and self.time1 <= 0.6:
                self.player.upDown2()

            if x != 0 or y != 0:
                pos = self.player.position
                new_x = pos[0] + self.player.speed * x * dt
                new_y = pos[1] + self.player.speed * y * dt
                self.player.position = (new_x, new_y)
                self.player.cshape.center = self.player.position


       # 고드름(ice) 파밍(690 883 431)
        elif (self.player.position[0] > 690 and self.player.position[0] < 883) and (self.player.position[1] < 432 and self.player.position[1] >= 430) and self.pressed[key.SPACE]: 
            self.player.farmingTime += 0.18

            sound = True
            if sound == True:
                spadeSound.play()
                sound = False
            
            if self.player.farmingTime > 1.8:
                self.player.farmingTime = 0
            if self.player.farmingTime > -1 and self.player.farmingTime < 0.6:
                self.player.iceFarming1()
            if self.player.farmingTime >= 0.6 and self.player.farmingTime < 1.2:
                self.player.iceFarming2()
            if self.player.farmingTime >= 1.2 and self.player.farmingTime < 1.8:
                self.player.iceFarming3()
            self.icing.mineCheckTime += 0.03
            if self.icing.mineCheckTime > 3:
                self.icing.mineCheckTime = 0

            if self.icing.mineCheckTime > -1 and self.icing.mineCheckTime < 0.6:
                self.icing.one()
            if self.icing.mineCheckTime >= 0.6 and self.icing.mineCheckTime < 1.2:
                self.icing.two()
            if self.icing.mineCheckTime >= 1.2 and self.icing.mineCheckTime < 1.8:
                self.icing.three()
            if self.icing.mineCheckTime >= 1.8 and self.icing.mineCheckTime < 2.4:
                self.icing.four()
            if self.icing.mineCheckTime >= 2.4 and self.icing.mineCheckTime < 4:
                self.icing.five()
                self.player.iceCheck = True
                sound = True
 


        # 화약(BombPower) 파밍(810 966 45)
        elif (self.player.position[0] > 810 and self.player.position[0] < 966) and (self.player.position[1] < 46 and self.player.position[1] >= 44) and self.pressed[key.SPACE]: 
            self.player.farmingTime += 0.18

            sound = True
            if sound == True:
                spadeSound.play()
                sound = False
            
            if self.player.farmingTime > 1.8:
                self.player.farmingTime = 0
            if self.player.farmingTime > -1 and self.player.farmingTime < 0.6:
                self.player.bombPowerFarming1()
            if self.player.farmingTime >= 0.6 and self.player.farmingTime < 1.2:
                self.player.bombPowerFarming2()
            if self.player.farmingTime >= 1.2 and self.player.farmingTime < 1.8:
                self.player.bombPowerFarming3()
            self.mining.mineCheckTime += 0.03
            if self.mining.mineCheckTime > 3:
                self.mining.mineCheckTime = 0

            if self.mining.mineCheckTime > -1 and self.mining.mineCheckTime < 0.6:
                self.mining.one()
            if self.mining.mineCheckTime >= 0.6 and self.mining.mineCheckTime < 1.2:
                self.mining.two()
            if self.mining.mineCheckTime >= 1.2 and self.mining.mineCheckTime < 1.8:
                self.mining.three()
            if self.mining.mineCheckTime >= 1.8 and self.mining.mineCheckTime < 2.4:
                self.mining.four()
            if self.mining.mineCheckTime >= 2.4 and self.mining.mineCheckTime < 4:
                self.mining.five()
                self.player.bombPowerCheck = True
                sound = True
            

        # 철광석(iron) 파밍(565 630 184)
        elif (self.player.position[0] > 565 and self.player.position[0] < 630) and (self.player.position[1] < 185 and self.player.position[1] >= 183) and self.pressed[key.SPACE]: 
            ironSound.play()
            self.player.farmingTime += 0.18
            if self.player.farmingTime > 1.8:
                self.player.farmingTime = 0
            if self.player.farmingTime > -1 and self.player.farmingTime < 0.6:
                self.player.ironFarming1()
            if self.player.farmingTime >= 0.6 and self.player.farmingTime < 1.2:
                self.player.ironFarming2()
            if self.player.farmingTime >= 1.2 and self.player.farmingTime < 1.8:
                self.player.ironFarming3()

            
            self.mining1.mineCheckTime += 0.03
            if self.mining1.mineCheckTime > 3:
                self.mining1.mineCheckTime = 0

            if self.mining1.mineCheckTime > -1 and self.mining1.mineCheckTime < 0.6:
                self.mining1.one()
            if self.mining1.mineCheckTime >= 0.6 and self.mining1.mineCheckTime < 1.2:
                self.mining1.two()
            if self.mining1.mineCheckTime >= 1.2 and self.mining1.mineCheckTime < 1.8:
                self.mining1.three()
            if self.mining1.mineCheckTime >= 1.8 and self.mining1.mineCheckTime < 2.4:
                self.mining1.four()
            if self.mining1.mineCheckTime >= 2.4 and self.mining1.mineCheckTime < 4:
                self.mining1.five()
                self.player.ironCheck = True
                
        else:
            self.mining.zero()
            self.mining1.zero()
            self.icing.zero()
            self.mining.mineCheckTime = 0
            self.mining1.mineCheckTime = 0
            self.icing.mineCheckTime = 0
            if ((self.player.position[0] > 675 and self.player.position[0] < 760) and (self.player.position[1] >= 45 and self.player.position[1] <= 183)) or ((self.player.position[0] > 835 and self.player.position[0] < 921) and (self.player.position[1] > 181 and self.player.position[1] <= 315)):
                x = (self.pressed[key.RIGHT] - self.pressed[key.LEFT]) * 2
                y = 0

                if self.time1 >= 0 and self.time1 < 0.3:
                    self.player.upDown1()
                elif self.time1 >= 0.3 and self.time1 <= 0.6:
                    self.player.upDown2()
                
                if x != 0 or y != 0:
                    pos = self.player.position
                    new_x = pos[0] + self.player.speed * x * dt
                    new_y = pos[1] + self.player.speed * y * dt
                    self.player.position = (new_x, new_y)
                    self.player.cshape.center = self.player.position              
                    
            elif self.pressed[key.RIGHT]:
                x = (self.pressed[key.RIGHT] - self.pressed[key.LEFT]) * 2
                y = 0
                
                if self.soundTime == 0:                      
                    runSound.play(1, 1000)

                if self.time >= 0 and self.time < 0.2:
                    self.player.runR1()
                elif self.time >= 0.2 and self.time <= 0.4:
                    self.player.runR2()
                elif self.time >= 0.4 and self.time < 0.6:
                    self.player.runR3()
                elif self.time >= 0.6 and self.time <= 0.8:
                    self.player.runR4()
                elif self.time >= 0.8 and self.time <= 1:
                    self.player.runR5()                    
        
                if x != 0 or y != 0:
                    pos = self.player.position
                    new_x = pos[0] + self.player.speed * x * dt
                    new_y = pos[1] + self.player.speed * y * dt
                    self.player.position = (new_x, new_y)
                    self.player.cshape.center = self.player.position              
                    
            elif self.pressed[key.LEFT]:
                x = (self.pressed[key.RIGHT] - self.pressed[key.LEFT]) * 2
                y = 0
                
                if self.soundTime == 0:                
                    runSound.play(1, 1000)

                if self.time >= 0 and self.time < 0.2:
                    self.player.runL1()
                elif self.time >= 0.2 and self.time <= 0.4:
                    self.player.runL2()
                elif self.time >= 0.4 and self.time < 0.6:
                    self.player.runL3()
                elif self.time >= 0.6 and self.time <= 0.8:
                    self.player.runL4()
                elif self.time >= 0.8 and self.time <= 1:
                    self.player.runL5()
                if x != 0 or y != 0:
                    pos = self.player.position
                    new_x = pos[0] + self.player.speed * x * dt
                    new_y = pos[1] + self.player.speed * y * dt
                    self.player.position = (new_x, new_y)
                    self.player.cshape.center = self.player.position              
                    
            else:
                self.player.defaultAction()
                    
            if self.player.position[0] < 473:
                x = 1
                y = 0
                if x != 0 or y != 0:
                    pos = self.player.position
                    new_x = pos[0] + self.player.speed * x * dt
                    new_y = pos[1] + self.player.speed * y * dt
                    self.player.position = (new_x, new_y)
                    self.player.cshape.center = self.player.position              
            elif self.player.position[0] > 1013:
                x = -1
                y = 0
                if x != 0 or y != 0:
                    pos = self.player.position
                    new_x = pos[0] + self.player.speed * x * dt
                    new_y = pos[1] + self.player.speed * y * dt
                    self.player.position = (new_x, new_y)
                    self.player.cshape.center = self.player.position              
                    

        
        if self.player.stamina > 0:
            if self.pressed[key.SPACE] and self.pressed[key.LEFT] and self.up_check:
                self.player.stamina -= 0.1
                self.player.sildeActionL()
                x = -2
                y = 0
                if x != 0 or y != 0:
                    pos = self.player.position
                    new_x = pos[0] + self.player.speed * x * dt
                    new_y = pos[1] + self.player.speed * y * dt
                
                    self.player.position = (new_x, new_y)
                    self.player.cshape.center = self.player.position
                    if self.player.position[0] < 473:
                        self.player.position = (473, self.player.position[1])

            if self.pressed[key.SPACE] and self.pressed[key.RIGHT] and self.up_check:
                self.player.stamina -= 0.1
                self.player.sildeActionR()
                x = 2
                y = 0
                if x != 0 or y != 0:
                    pos = self.player.position
                    new_x = pos[0] + self.player.speed * x * dt
                    new_y = pos[1] + self.player.speed * y * dt
                    
                    self.player.position = (new_x, new_y)
                    self.player.cshape.center = self.player.position
                    if self.player.position[0] > 1013:
                        self.player.position = (1013, self.player.position[1])
        
        # 폭탄 가이드라인
        if self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 180 and self.player.position[1] < 190:
            self.line1.one()
        elif self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 430 and self.player.position[1] < 432:
            self.line2.two()
        elif self.player.position[0] < 514 and self.player.position[1] > 180 and self.player.position[1] < 190:
            self.line3.three()
        elif self.player.position[0] < 514 and self.player.position[1] > 430 and self.player.position[1] < 432:
            self.line4.four()    
        else:
            self.line1.empty()
            self.line2.empty()
            self.line3.empty()
            self.line4.empty()

        # 화약 Check
        if self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 180 and self.player.position[1] < 190 and self.player.bombPowerCheck == True:
            self.bomb1.bombPowerCheck = True
            self.player.bombPowerCheck = False
            self.bombPowerCheck1.image = self.bombPowerCheck1.emotions['bombPowerClear']
        elif self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 430 and self.player.position[1] < 432 and self.player.bombPowerCheck == True:
            self.bomb2.bombPowerCheck = True
            self.player.bombPowerCheck = False
            self.bombPowerCheck2.image = self.bombPowerCheck2.emotions['bombPowerClear']
        elif self.player.position[0] < 514 and self.player.position[1] > 180 and self.player.position[1] < 190 and self.player.bombPowerCheck == True:
            self.bomb3.bombPowerCheck = True
            self.player.bombPowerCheck = False
            self.bombPowerCheck3.image = self.bombPowerCheck3.emotions['bombPowerClear']            
        elif self.player.position[0] < 514 and self.player.position[1] > 430 and self.player.position[1] < 432 and self.player.bombPowerCheck == True:
            self.bomb4.bombPowerCheck = True
            self.player.bombPowerCheck = False
            self.bombPowerCheck4.image = self.bombPowerCheck4.emotions['bombPowerClear']

        # 철광석 Check
        if self.player.position[0] > 699 and self.player.position[0] < 771 and self.player.position[1] > 315 and self.player.position[1] < 317 and self.player.ironCheck == True:
            self.space.ironCheck = True
            self.ironCheck.image = self.ironCheck.emotions['ironClear']
        
        # 얼음 Check
        if self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 180 and self.player.position[1] < 190 and self.player.iceCheck == True:
            self.bomb1.iceCheck = True
            self.player.iceCheck = False
            self.iceCheck1.image = self.iceCheck1.emotions['iceClear']
        elif self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 430 and self.player.position[1] < 432 and self.player.iceCheck == True:
            self.bomb2.iceCheck = True
            self.player.iceCheck = False
            self.iceCheck2.image = self.iceCheck2.emotions['iceClear']
        elif self.player.position[0] < 514 and self.player.position[1] > 180 and self.player.position[1] < 190 and self.player.iceCheck == True:
            self.bomb3.iceCheck = True
            self.player.iceCheck = False
            self.iceCheck3.image = self.iceCheck3.emotions['iceClear']            
        elif self.player.position[0] < 514 and self.player.position[1] > 430 and self.player.position[1] < 432 and self.player.iceCheck == True:
            self.bomb4.iceCheck = True
            self.player.iceCheck = False
            self.iceCheck4.image = self.iceCheck4.emotions['iceClear']

        # 탄환 파밍
        if self.player.position[0] > 699 and self.player.position[0] < 771 and self.player.position[1] > 315 and self.player.position[1] < 317 and self.space.ironCheck == True and self.pressed[key.SPACE]:
            pxSound.play()
            self.player.farmingTime += 0.2
            if self.player.farmingTime > 2.0:
                self.player.farmingTime = 0
            if self.player.farmingTime > -1 and self.player.farmingTime < 0.5:
                self.player.ironTrainning1()
            if self.player.farmingTime >= 0.5 and self.player.farmingTime < 1.0:
                self.player.ironTrainning2()
            if self.player.farmingTime >= 1.0 and self.player.farmingTime < 1.5:
                self.player.ironTrainning3()
            if self.player.farmingTime >= 1.5 and self.player.farmingTime < 2.0:
                self.player.ironTrainning4()
            
            self.mining2.mineCheckTime += 0.03
            if self.mining2.mineCheckTime > 3:
                self.mining2.mineCheckTime = 0
            if self.mining2.mineCheckTime > -1 and self.mining2.mineCheckTime < 0.6:
                self.mining2.one()
            if self.mining2.mineCheckTime >= 0.6 and self.mining2.mineCheckTime < 1.2:
                self.mining2.two()
            if self.mining2.mineCheckTime >= 1.2 and self.mining2.mineCheckTime < 1.8:
                self.mining2.three()
            if self.mining2.mineCheckTime >= 1.8 and self.mining2.mineCheckTime < 2.4:
                self.mining2.four()
            if self.mining2.mineCheckTime >= 2.4 and self.mining2.mineCheckTime < 4:
                self.mining2.five()
                self.player.ironCheck = False
                self.player.bombCheck = True
                self.space.ironCheck = False
                self.ironCheck.image = self.ironCheck.emotions['ironCheck']
        else:
            self.mining2.mineCheckTime = 0
            self.mining2.zero()
            
        # 탄환 Check
        if self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 180 and self.player.position[1] < 190 and self.player.bombCheck == True:
            self.player.bombCheck = False
            self.bomb1.bombCheck = True
            self.bombCheck1.image = self.bombCheck1.emotions['bombClear']
        elif self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 430 and self.player.position[1] < 432 and self.player.bombCheck == True:
            self.player.bombCheck = False
            self.bomb2.bombCheck = True
            self.bombCheck2.image = self.bombCheck2.emotions['bombClear']
        elif self.player.position[0] < 514 and self.player.position[1] > 180 and self.player.position[1] < 190 and self.player.bombCheck == True:
            self.player.bombCheck = False
            self.bomb3.bombCheck = True
            self.bombCheck3.image = self.bombCheck3.emotions['bombClear']       
        elif self.player.position[0] < 514 and self.player.position[1] > 430 and self.player.position[1] < 432 and self.player.bombCheck == True:
            self.player.bombCheck = False
            self.bomb4.bombCheck = True
            self.bombCheck4.image = self.bombCheck4.emotions['bombClear']

        # 폭탄 발사 가능
        if self.bomb1.bombCheck == True and self.bomb1.bombPowerCheck == True:
            self.bomb1.tryShot = True
            if self.bomb1.iceCheck == True:
                self.bomb1.iceTryShot = True
        if self.bomb2.bombCheck == True and self.bomb2.bombPowerCheck == True:
            self.bomb2.tryShot = True
            if self.bomb2.iceCheck == True:
                self.bomb2.iceTryShot = True
        if self.bomb3.bombCheck == True and self.bomb3.bombPowerCheck == True:
            self.bomb3.tryShot = True
            if self.bomb3.iceCheck == True:
                self.bomb3.iceTryShot = True
        if self.bomb4.bombCheck == True and self.bomb4.bombPowerCheck == True:
            self.bomb4.tryShot = True
            if self.bomb4.iceCheck == True:
                self.bomb4.iceTryShot = True
                
        # 폭탄 발사(bomb1)
        if self.bomb1.tryShot == True and self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 180 and self.player.position[1] < 190 and self.pressed[key.SPACE]:
            if self.bomb1.iceTryShot == False and self.bomb1.iceCheck == False:
                self.add(self.bombShot1)
                self.bomb1.bombEnter = True
                self.bombShot1.position = (self.bomb1.position[0] + 100, self.bomb1.position[1] + 30)
                self.add(BombEmotion2((self.bomb1.position[0] + 55, self.bomb1.position[1] + 30)))
                bombPowerSound.play()
                self.bombShot1.image = self.bombShot1.emotions['bomb']
                
            elif self.bomb1.iceTryShot == True and self.bomb1.iceCheck == True:
                self.add(self.bombShot1)
                self.bombShot1.image = self.bombShot1.emotions['iceBomb']
                self.bomb1.bombEnter = True
                self.bombShot1.position = (self.bomb1.position[0] + 100, self.bomb1.position[1] + 30)
                self.add(BombEmotion2((self.bomb1.position[0] + 55, self.bomb1.position[1] + 30)))
                bombPowerSound.play()
                
        # 폭탄 발사(bomb2)
        if self.bomb2.tryShot == True and self.player.position[0] > 980 and self.player.position[0] < 1040 and self.player.position[1] > 430 and self.player.position[1] < 432 and self.pressed[key.SPACE]:
            if self.bomb2.iceTryShot == False and self.bomb2.iceCheck == False:
                self.add(self.bombShot2)
                self.bomb2.bombEnter = True
                self.bombShot2.position = (self.bomb2.position[0] + 100, self.bomb2.position[1] + 30)
                self.add(BombEmotion2((self.bomb2.position[0] + 55, self.bomb2.position[1] + 30)))
                bombPowerSound.play()
                self.bombShot2.image = self.bombShot2.emotions['bomb']
                
            elif self.bomb2.iceTryShot == True and self.bomb2.iceCheck == True:
                self.add(self.bombShot2)
                self.bombShot2.image = self.bombShot2.emotions['iceBomb']
                self.bomb2.bombEnter = True
                self.bombShot2.position = (self.bomb2.position[0] + 100, self.bomb2.position[1] + 30)
                self.add(BombEmotion2((self.bomb2.position[0] + 55, self.bomb2.position[1] + 30)))
                bombPowerSound.play()

        # 폭탄 발사(bomb3)
        if self.bomb3.tryShot == True and self.player.position[0] > 180 and self.player.position[0] < 514 and self.player.position[1] > 180 and self.player.position[1] < 190 and self.pressed[key.SPACE]:
            if self.bomb3.iceTryShot == False and self.bomb3.iceCheck == False:
                self.add(self.bombShot3)
                self.bomb3.bombEnter = True
                self.bombShot3.position = (self.bomb3.position[0] - 100, self.bomb3.position[1] + 30)
                self.add(BombEmotion3((self.bomb3.position[0] - 55, self.bomb3.position[1] + 30)))
                bombPowerSound.play()
                self.bombShot3.image = self.bombShot3.emotions['bomb']
                
            elif self.bomb3.iceTryShot == True and self.bomb3.iceCheck == True:
                self.add(self.bombShot3)
                self.bombShot3.image = self.bombShot3.emotions['iceBomb']
                self.bomb3.bombEnter = True
                self.bombShot3.position = (self.bomb3.position[0] - 100, self.bomb3.position[1] + 30)
                self.add(BombEmotion3((self.bomb3.position[0] - 55, self.bomb3.position[1] + 30)))
                bombPowerSound.play()
                
        # 폭탄 발사(bomb4)
        if self.bomb4.tryShot == True and self.player.position[0] > 180 and self.player.position[0] < 514 and self.player.position[1] > 430 and self.player.position[1] < 432 and self.pressed[key.SPACE]:
            if self.bomb4.iceTryShot == False and self.bomb4.iceCheck == False:
                self.add(self.bombShot4)
                self.bomb4.bombEnter = True
                self.bombShot4.position = (self.bomb4.position[0] - 100, self.bomb4.position[1] + 30)
                self.add(BombEmotion3((self.bomb4.position[0] - 55, self.bomb4.position[1] + 30)))
                bombPowerSound.play()
                self.bombShot4.image = self.bombShot4.emotions['bomb']

            elif self.bomb4.iceTryShot == True and self.bomb4.iceCheck == True:
                self.add(self.bombShot4)
                self.bombShot4.image = self.bombShot4.emotions['iceBomb']
                self.bomb4.bombEnter = True
                self.bombShot4.position = (self.bomb4.position[0] - 100, self.bomb4.position[1] + 30)
                self.add(BombEmotion3((self.bomb4.position[0] - 55, self.bomb4.position[1] + 30)))
                bombPowerSound.play()

        ##        
        if self.bomb1.bombEnter == True:
            dRotate = 1
            self.bombShot1.rotation = self.bombShot1.rotation + 30 * dRotate * dt
            dx = 0.5
            dy = 0
            if dx != 0 or dy != 0:
                if dx != 0 or dy != 0:
                    pos = self.bombShot1.position
                    new_x = pos[0] + 100 * dx * dt
                    new_y = pos[1] + 100 * dy * dt
                    self.bombShot1.position = (new_x, new_y)
                    self.bombShot1.cshape.center = self.bombShot1.position
            gx = 0
            gy = -1.8
            if gx != 0 or gy != 0:
                pos = self.bombShot1.position
                new_x = pos[0] + 100 * gx * dt
                new_y = pos[1] + 100 * gy * dt
                self.bombShot1.position = (new_x, new_y)
                self.bombShot1.cshape.center = self.bombShot1.position
            if self.bombShot1.position[1] < 50:
                bombSound.play()
                self.bomb1.tryShot = False
                self.bomb1.bombEnter = False
                self.bomb1.bombCheck = False
                self.bomb1.bombPowerCheck = False
                
                self.iceCheck1.image = self.iceCheck1.emotions['ice']
                self.bombCheck1.image = self.bombCheck1.emotions['bomb']
                self.bombPowerCheck1.image = self.bombPowerCheck1.emotions['bombPower']
                self.add(BombEmotion(self.bombShot1.position))
                self.bombShot1.position = (2000, 500)
                self.bombShot1.bombBob = True
                if self.bomb1.iceTryShot == True and self.bomb1.iceCheck == True:
                    self.iceFan2.ice = True
                    self.bomb1.iceCheck = False
                    self.bomb1.iceTryShot = False
        ##       
        if self.iceFan2.ice == True:
            self.iceFan2.iceTime += 0.01
            if self.iceFan2.iceTime >= 0 and self.iceFan2.iceTime < 8:
                self.iceFan2.image = self.iceFan2.emotions['iceFan']
                for i in self.enemy:
                    if i.position[0] >= 1000 and i.position[0] < 1280:
                        i.speed = 0
                    else:
                        i.speed = 100.0
            elif self.iceFan2.iceTime >= 8:
                self.iceFan2.image = self.iceFan2.emotions['empty']
                self.iceFan2.ice = False
                self.iceFan2.iceTime = 0
                for i in self.enemy:
                    i.speed = 100.0
         ##
        if self.bomb2.bombEnter == True:
            dRotate = 1
            self.bombShot2.rotation = self.bombShot2.rotation + 30 * dRotate * dt
            dx = 1
            dy = 1
            if dx != 0 or dy != 0:
                if dx != 0 or dy != 0:
                    pos = self.bombShot2.position
                    new_x = pos[0] + 100 * dx * dt
                    new_y = pos[1] + 100 * dy * dt
                    self.bombShot2.position = (new_x, new_y)
                    self.bombShot2.cshape.center = self.bombShot2.position
            gx = 0
            gy = -3
            if gx != 0 or gy != 0:
                pos = self.bombShot2.position
                new_x = pos[0] + 100 * gx * dt
                new_y = pos[1] + 100 * gy * dt
                self.bombShot2.position = (new_x, new_y)
                self.bombShot2.cshape.center = self.bombShot2.position
            if self.bombShot2.position[1] < 50:
                bombSound.play()
                self.bomb2.tryShot = False
                self.bomb2.bombEnter = False
                self.bomb2.bombCheck = False
                self.bomb2.bombPowerCheck = False
                
                self.iceCheck2.image = self.iceCheck2.emotions['ice']
                self.bombCheck2.image = self.bombCheck2.emotions['bomb']
                self.bombPowerCheck2.image = self.bombPowerCheck2.emotions['bombPower']
                self.add(BombEmotion(self.bombShot2.position))
                self.bombShot2.position = (2000, 500)
                self.bombShot2.bombBob = True
                if self.bomb2.iceTryShot == True and self.bomb2.iceCheck == True:
                    self.iceFan1.ice = True
                    self.bomb2.iceCheck = False
                    self.bomb2.iceTryShot = False
        ##            
        if self.iceFan1.ice == True:
            self.iceFan1.iceTime += 0.01
            if self.iceFan1.iceTime >= 0 and self.iceFan1.iceTime < 8:
                self.iceFan1.image = self.iceFan1.emotions['iceFan']
                for i in self.enemy:
                    if i.position[0] >= 1280 and i.position[0] < 1450:
                        i.speed = 0
                    else:
                        i.speed = 100.0
            elif self.iceFan1.iceTime >= 8:
                self.iceFan1.image = self.iceFan1.emotions['empty']
                self.iceFan1.ice = False
                self.iceFan1.iceTime = 0
                for i in self.enemy:
                    i.speed = 100.0

        ##            
        if self.bomb3.bombEnter == True:
            dRotate = 1
            self.bombShot3.rotation = self.bombShot3.rotation + 30 * dRotate * dt
            dx = -0.5
            dy = 0
            if dx != 0 or dy != 0:
                if dx != 0 or dy != 0:
                    pos = self.bombShot3.position
                    new_x = pos[0] + 100 * dx * dt
                    new_y = pos[1] + 100 * dy * dt
                    self.bombShot3.position = (new_x, new_y)
                    self.bombShot3.cshape.center = self.bombShot3.position
            gx = 0
            gy = -1.8
            if gx != 0 or gy != 0:
                pos = self.bombShot3.position
                new_x = pos[0] + 100 * gx * dt
                new_y = pos[1] + 100 * gy * dt
                self.bombShot3.position = (new_x, new_y)
                self.bombShot3.cshape.center = self.bombShot3.position
            
            if self.bombShot3.position[1] < 50:
                bombSound.play()
                self.bomb3.tryShot = False
                self.bomb3.bombEnter = False
                self.bomb3.bombCheck = False
                self.bomb3.bombPowerCheck = False
                self.iceCheck3.image = self.iceCheck3.emotions['ice']
                self.bombCheck3.image = self.bombCheck3.emotions['bomb']
                self.bombPowerCheck3.image = self.bombPowerCheck3.emotions['bombPower']
                self.add(BombEmotion(self.bombShot3.position))
                self.bombShot3.position = (2000, -100)
                self.bombShot3.bombBob = True
                if self.bomb3.iceTryShot == True and self.bomb3.iceCheck == True:
                    self.iceFan4.ice = True
                    self.bomb3.iceCheck = False
                    self.bomb3.iceTryShot = False
         ##           
        if self.iceFan4.ice == True:
            self.iceFan4.iceTime += 0.01
            if self.iceFan4.iceTime >= 0 and self.iceFan4.iceTime < 8:
                self.iceFan4.image = self.iceFan4.emotions['iceFan']
                for i in self.enemy:
                    if i.position[0] >= 280 and i.position[0] < 500:
                        i.speed = 0
                    else:
                        i.speed = 100.0
            elif self.iceFan4.iceTime >= 8:
                self.iceFan4.image = self.iceFan4.emotions['empty']
                self.iceFan4.ice = False
                self.iceFan4.iceTime = 0
                for i in self.enemy:
                    i.speed = 100.0
        ##            
        if self.bomb4.bombEnter == True:
            dRotate = 1
            self.bombShot4.rotation = self.bombShot4.rotation + 30 * dRotate * dt
            dx = -1
            dy = 1
            if dx != 0 or dy != 0:
                if dx != 0 or dy != 0:
                    pos = self.bombShot4.position
                    new_x = pos[0] + 100 * dx * dt
                    new_y = pos[1] + 100 * dy * dt
                    self.bombShot4.position = (new_x, new_y)
                    self.bombShot4.cshape.center = self.bombShot4.position
            gx = 0
            gy = -3
            if gx != 0 or gy != 0:
                pos = self.bombShot4.position
                new_x = pos[0] + 100 * gx * dt
                new_y = pos[1] + 100 * gy * dt
                self.bombShot4.position = (new_x, new_y)
                self.bombShot4.cshape.center = self.bombShot4.position
            
            if self.bombShot4.position[1] < 50:
                bombSound.play()
                self.bomb4.tryShot = False
                self.bomb4.bombEnter = False
                self.bomb4.bombCheck = False
                self.bomb4.bombPowerCheck = False
                self.iceCheck4.image = self.iceCheck4.emotions['ice']
                self.bombCheck4.image = self.bombCheck4.emotions['bomb']
                self.bombPowerCheck4.image = self.bombPowerCheck4.emotions['bombPower']
                self.add(BombEmotion(self.bombShot4.position))
                self.bombShot4.position = (2000, -100)
                self.bombShot4.bombBob = True

                if self.bomb4.iceTryShot == True and self.bomb4.iceCheck == True:
                    self.iceFan3.ice = True
                    self.bomb4.iceCheck = False
                    self.bomb4.iceTryShot = False
         ##           
        if self.iceFan3.ice == True:
            self.iceFan3.iceTime += 0.01
            if self.iceFan3.iceTime >= 0 and self.iceFan3.iceTime < 8:
                self.iceFan3.image = self.iceFan3.emotions['iceFan']
                for i in self.enemy:
                    if i.position[0] >= 50 and i.position[0] < 280:
                        i.speed = 0
                    else:
                        i.speed = 100.0
            elif self.iceFan3.iceTime >= 8:
                self.iceFan3.image = self.iceFan3.emotions['empty']
                self.iceFan3.ice = False
                self.iceFan3.iceTime = 0
                for i in self.enemy:
                    i.speed = 100.0
                    
        # 범위공격 폭탄 확인 및 적 제거
        if self.bombShot1.bombBob == True:
            for i in self.enemy1L:
                if i.position[0] >= 1000 and i.position[0] < 1250:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie1L()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot1.bombBob = False
                        i.position = (1500, -100)
                        
            for i in self.enemy1R:
                if i.position[0] >= 1000 and i.position[0] < 1250:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie1R()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot1.bombBob = False
                        i.position = (1500, -100)

            for i in self.enemy3R:
                if i.position[0] >= 1000 and i.position[0] < 1250:
                    i.hp -= 1.2
                    if i.hp <= 0:
                        if i.lifeTime >= 0 and i.lifeTime < 3.0:
                            i.enemyDie3R()
                            i.lifeTime += 0.05
                        elif i.lifeTime >= 3.0:
                            i.position = (1500, -100)
                            i.lifeTime = 0
                            i.life = False
                            i.RunUser = True
                            i.AtkUser = False
                            self.bombShot1.bombBob = False
                            
        if self.bombShot2.bombBob == True:
            for i in self.enemy1L:
                if i.position[0] >= 1250 and i.position[0] < 1450:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie1L()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot2.bombBob = False
                        i.position = (1500, -100)

            for i in self.enemy1R:
                if i.position[0] >= 1250 and i.position[0] < 1450:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie1R()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot2.bombBob = False
                        i.position = (1500, -100)

            for i in self.enemy2R:
                if i.position[0] >= 1240 and i.position[0] < 1450:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie2R()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot1.bombBob = False
                        i.position = (1500, -100)
                        for j in self.enemy2RAttack:
                            j.position = (1500, -100)

            for i in self.enemy3R:
                if i.position[0] >= 1240 and i.position[0] < 1450:
                    i.hp -= 1.2
                    if i.hp <= 0:
                        if i.lifeTime >= 0 and i.lifeTime < 3.0:
                            i.enemyDie3R()
                            i.lifeTime += 0.05
                        elif i.lifeTime >= 3.0:
                            i.position = (1500, -100)
                            i.lifeTime = 0
                            i.life = False
                            i.RunUser = True
                            i.AtkUser = False
                            self.bombShot2.bombBob = False
                            
            for i in self.enemy4R:
                if i.position[0] >= 1240 and i.position[0] < 1450:
                    i.hp -= 0.5
                    if i.hp <= 0:
                        if i.lifeTime >= 0 and i.lifeTime < 3.0:
                            i.enemyDie4R()
                            i.lifeTime += 0.05
                        elif i.lifeTime >= 3.0:
                            i.position = (1500, -100)
                            i.lifeTime = 0
                            i.life = False
                            i.RunUser = True
                            i.AtkUser = False
                            self.bombShot2.bombBob = False
                        for j in self.enemy4RAttack:
                            j.position = (1500, -100)
                            
        if self.bombShot3.bombBob == True:
            for i in self.enemy1L:
                if i.position[0] >= 250 and i.position[0] < 500:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie1L()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot3.bombBob = False
                        i.position = (1500, -100)
            
            for i in self.enemy1L:
                if i.position[0] >= 250 and i.position[0] < 500:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie1L()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot3.bombBob = False
                        i.position = (1500, -100)

            for i in self.enemy3L:
                if i.position[0] >= 250 and i.position[0] < 500:
                    i.hp -= 1.2
                    if i.hp <= 0:
                        if i.lifeTime >= 0 and i.lifeTime < 3.0:
                            i.enemyDie3L()
                            i.lifeTime += 0.05
                        elif i.lifeTime >= 3.0:
                            i.position = (1500, -100)
                            i.lifeTime = 0
                            i.life = False
                            i.RunUser = True
                            i.AtkUser = False
                            self.bombShot3.bombBob = False                 
                        
        if self.bombShot4.bombBob == True:
            for i in self.enemy1L:
                if i.position[0] >= 50 and i.position[0] < 250:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie1L()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot4.bombBob = False
                        i.position = (1500, -100)

            for i in self.enemy1L:
                if i.position[0] >= 50 and i.position[0] < 250:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie1R()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot4.bombBob = False
                        i.position = (1500, -100)

            for i in self.enemy2L:
                if i.position[0] >= 50 and i.position[0] < 250:
                    i.lifeTime += 0.05
                    if i.lifeTime > 4.0:
                        i.lifeTime = 0
                    i.enemyDie2L()
                    if i.lifeTime > 3.0:
                        i.life = False
                        i.RunUser = True
                        i.AtkUser = False
                        self.bombShot4.bombBob = False
                        i.position = (1500, -100)
                        for j in self.enemy2LAttack:
                            j.position = (1500, -100)

            for i in self.enemy3L:
                if i.position[0] >= 50 and i.position[0] < 250:
                    i.hp -= 1
                    if i.hp <= 0:
                        if i.lifeTime >= 0 and i.lifeTime < 3.0:
                            i.enemyDie3L()
                            i.lifeTime += 0.05
                        elif i.lifeTime >= 3.0:
                            i.position = (1500, -100)
                            i.lifeTime = 0
                            i.life = False
                            i.RunUser = True
                            i.AtkUser = False
                            self.bombShot4.bombBob = False

            for i in self.enemy4L:
                if i.position[0] >= 50 and i.position[0] < 250:
                    i.hp -= 0.5
                    if i.hp <= 0:
                        if i.lifeTime >= 0 and i.lifeTime < 3.0:
                            i.enemyDie4L()
                            i.lifeTime += 0.05
                        elif i.lifeTime >= 3.0:
                            i.position = (1500, -100)
                            i.lifeTime = 0
                            i.life = False
                            i.RunUser = True
                            i.AtkUser = False
                            self.bombShot4.bombBob = False
                        for j in self.enemy4LAttack:
                            j.position = (1500, -100)
                            
        for i in self.enemy1L:       
            if i.AtkUser == True:
                self.castleHealth.hp -= 0.01
                if self.castleHealth.hp <= 990 and self.castleHealth.hp > 980:
                    self.castleHealth.image = self.castleHealth.emotions['castle99']
                elif self.castleHealth.hp <= 980 and self.castleHealth.hp > 970:
                    self.castleHealth.image = self.castleHealth.emotions['castle98']
                elif self.castleHealth.hp <= 970 and self.castleHealth.hp > 960:
                    self.castleHealth.image = self.castleHealth.emotions['castle97']
                elif self.castleHealth.hp <= 960 and self.castleHealth.hp > 950:
                    self.castleHealth.image = self.castleHealth.emotions['castle96']
                elif self.castleHealth.hp <= 950 and self.castleHealth.hp > 940:
                    self.castleHealth.image = self.castleHealth.emotions['castle95']
                elif self.castleHealth.hp <= 940 and self.castleHealth.hp > 930:
                    self.castleHealth.image = self.castleHealth.emotions['castle94']
                elif self.castleHealth.hp <= 930 and self.castleHealth.hp > 920:
                    self.castleHealth.image = self.castleHealth.emotions['castle93']
                elif self.castleHealth.hp <= 920 and self.castleHealth.hp > 910:
                    self.castleHealth.image = self.castleHealth.emotions['castle92']
                elif self.castleHealth.hp <= 910 and self.castleHealth.hp > 900:
                    self.castleHealth.image = self.castleHealth.emotions['castle91']
                elif self.castleHealth.hp <= 900 and self.castleHealth.hp > 890:
                    self.castleHealth.image = self.castleHealth.emotions['castle90']
                elif self.castleHealth.hp <= 890 and self.castleHealth.hp > 880:
                    self.castleHealth.image = self.castleHealth.emotions['castle89']
                elif self.castleHealth.hp <= 880 and self.castleHealth.hp > 870:
                    self.castleHealth.image = self.castleHealth.emotions['castle88']
                elif self.castleHealth.hp <= 870 and self.castleHealth.hp > 860:
                    self.castleHealth.image = self.castleHealth.emotions['castle87']
                elif self.castleHealth.hp <= 860 and self.castleHealth.hp > 850:
                    self.castleHealth.image = self.castleHealth.emotions['castle86']
                elif self.castleHealth.hp <= 850 and self.castleHealth.hp > 840:
                    self.castleHealth.image = self.castleHealth.emotions['castle85']
                elif self.castleHealth.hp <= 840 and self.castleHealth.hp > 830:
                    self.castleHealth.image = self.castleHealth.emotions['castle84']
                elif self.castleHealth.hp <= 830 and self.castleHealth.hp > 820:
                    self.castleHealth.image = self.castleHealth.emotions['castle83']
                elif self.castleHealth.hp <= 820 and self.castleHealth.hp > 810:
                    self.castleHealth.image = self.castleHealth.emotions['castle82']
                elif self.castleHealth.hp <= 810 and self.castleHealth.hp > 800:
                    self.castleHealth.image = self.castleHealth.emotions['castle81']
                elif self.castleHealth.hp <= 800 and self.castleHealth.hp > 790:
                    self.castleHealth.image = self.castleHealth.emotions['castle80']
                elif self.castleHealth.hp <= 790 and self.castleHealth.hp > 780:
                    self.castleHealth.image = self.castleHealth.emotions['castle79']
                elif self.castleHealth.hp <= 780 and self.castleHealth.hp > 770:
                    self.castleHealth.image = self.castleHealth.emotions['castle78']
                elif self.castleHealth.hp <= 770 and self.castleHealth.hp > 760:
                    self.castleHealth.image = self.castleHealth.emotions['castle77']
                elif self.castleHealth.hp <= 760 and self.castleHealth.hp > 750:
                    self.castleHealth.image = self.castleHealth.emotions['castle76']
                elif self.castleHealth.hp <= 750 and self.castleHealth.hp > 740:
                    self.castleHealth.image = self.castleHealth.emotions['castle75']
                elif self.castleHealth.hp <= 740 and self.castleHealth.hp > 730:
                    self.castleHealth.image = self.castleHealth.emotions['castle74']
                elif self.castleHealth.hp <= 730 and self.castleHealth.hp > 720:
                    self.castleHealth.image = self.castleHealth.emotions['castle73']
                elif self.castleHealth.hp <= 720 and self.castleHealth.hp > 710:
                    self.castleHealth.image = self.castleHealth.emotions['castle72']
                elif self.castleHealth.hp <= 710 and self.castleHealth.hp > 700:
                    self.castleHealth.image = self.castleHealth.emotions['castle71']
                elif self.castleHealth.hp <= 700 and self.castleHealth.hp > 690:
                    self.castleHealth.image = self.castleHealth.emotions['castle70']
                elif self.castleHealth.hp <= 690 and self.castleHealth.hp > 680:
                    self.castleHealth.image = self.castleHealth.emotions['castle69']
                elif self.castleHealth.hp <= 680 and self.castleHealth.hp > 670:
                    self.castleHealth.image = self.castleHealth.emotions['castle68']
                elif self.castleHealth.hp <= 670 and self.castleHealth.hp > 660:
                    self.castleHealth.image = self.castleHealth.emotions['castle67']
                elif self.castleHealth.hp <= 660 and self.castleHealth.hp > 650:
                    self.castleHealth.image = self.castleHealth.emotions['castle66']
                elif self.castleHealth.hp <= 650 and self.castleHealth.hp > 640:
                    self.castleHealth.image = self.castleHealth.emotions['castle65']
                elif self.castleHealth.hp <= 640 and self.castleHealth.hp > 630:
                    self.castleHealth.image = self.castleHealth.emotions['castle64']
                elif self.castleHealth.hp <= 630 and self.castleHealth.hp > 620:
                    self.castleHealth.image = self.castleHealth.emotions['castle63']
                elif self.castleHealth.hp <= 620 and self.castleHealth.hp > 610:
                    self.castleHealth.image = self.castleHealth.emotions['castle62']
                elif self.castleHealth.hp <= 610 and self.castleHealth.hp > 600:
                    self.castleHealth.image = self.castleHealth.emotions['castle61']
                elif self.castleHealth.hp <= 600 and self.castleHealth.hp > 590:
                    self.castleHealth.image = self.castleHealth.emotions['castle60']
                elif self.castleHealth.hp <= 590 and self.castleHealth.hp > 580:
                    self.castleHealth.image = self.castleHealth.emotions['castle59']
                elif self.castleHealth.hp <= 580 and self.castleHealth.hp > 570:
                    self.castleHealth.image = self.castleHealth.emotions['castle58']
                elif self.castleHealth.hp <= 570 and self.castleHealth.hp > 560:
                    self.castleHealth.image = self.castleHealth.emotions['castle57']
                elif self.castleHealth.hp <= 560 and self.castleHealth.hp > 550:
                    self.castleHealth.image = self.castleHealth.emotions['castle56']
                elif self.castleHealth.hp <= 550 and self.castleHealth.hp > 540:
                    self.castleHealth.image = self.castleHealth.emotions['castle55']
                elif self.castleHealth.hp <= 540 and self.castleHealth.hp > 530:
                    self.castleHealth.image = self.castleHealth.emotions['castle54']
                elif self.castleHealth.hp <= 530 and self.castleHealth.hp > 520:
                    self.castleHealth.image = self.castleHealth.emotions['castle53']
                elif self.castleHealth.hp <= 520 and self.castleHealth.hp > 510:
                    self.castleHealth.image = self.castleHealth.emotions['castle52']
                elif self.castleHealth.hp <= 510 and self.castleHealth.hp > 500:
                    self.castleHealth.image = self.castleHealth.emotions['castle51']
                elif self.castleHealth.hp <= 500 and self.castleHealth.hp > 490:
                    self.castleHealth.image = self.castleHealth.emotions['castle50']
                elif self.castleHealth.hp <= 490 and self.castleHealth.hp > 480:
                    self.castleHealth.image = self.castleHealth.emotions['castle49']
                elif self.castleHealth.hp <= 480 and self.castleHealth.hp > 470:
                    self.castleHealth.image = self.castleHealth.emotions['castle48']
                elif self.castleHealth.hp <= 470 and self.castleHealth.hp > 460:
                    self.castleHealth.image = self.castleHealth.emotions['castle47']
                elif self.castleHealth.hp <= 460 and self.castleHealth.hp > 450:
                    self.castleHealth.image = self.castleHealth.emotions['castle46']
                elif self.castleHealth.hp <= 450 and self.castleHealth.hp > 440:
                    self.castleHealth.image = self.castleHealth.emotions['castle45']
                elif self.castleHealth.hp <= 440 and self.castleHealth.hp > 430:
                    self.castleHealth.image = self.castleHealth.emotions['castle44']
                elif self.castleHealth.hp <= 430 and self.castleHealth.hp > 420:
                    self.castleHealth.image = self.castleHealth.emotions['castle43']
                elif self.castleHealth.hp <= 420 and self.castleHealth.hp > 410:
                    self.castleHealth.image = self.castleHealth.emotions['castle42']
                elif self.castleHealth.hp <= 410 and self.castleHealth.hp > 400:
                    self.castleHealth.image = self.castleHealth.emotions['castle41']
                elif self.castleHealth.hp <= 400 and self.castleHealth.hp > 390:
                    self.castleHealth.image = self.castleHealth.emotions['castle40']
                elif self.castleHealth.hp <= 390 and self.castleHealth.hp > 380:
                    self.castleHealth.image = self.castleHealth.emotions['castle39']
                elif self.castleHealth.hp <= 380 and self.castleHealth.hp > 370:
                    self.castleHealth.image = self.castleHealth.emotions['castle38']
                elif self.castleHealth.hp <= 370 and self.castleHealth.hp > 360:
                    self.castleHealth.image = self.castleHealth.emotions['castle37']
                elif self.castleHealth.hp <= 360 and self.castleHealth.hp > 350:
                    self.castleHealth.image = self.castleHealth.emotions['castle36']
                elif self.castleHealth.hp <= 350 and self.castleHealth.hp > 340:
                    self.castleHealth.image = self.castleHealth.emotions['castle35']
                elif self.castleHealth.hp <= 340 and self.castleHealth.hp > 330:
                    self.castleHealth.image = self.castleHealth.emotions['castle34']
                elif self.castleHealth.hp <= 330 and self.castleHealth.hp > 320:
                    self.castleHealth.image = self.castleHealth.emotions['castle33']
                elif self.castleHealth.hp <= 320 and self.castleHealth.hp > 310:
                    self.castleHealth.image = self.castleHealth.emotions['castle32']
                elif self.castleHealth.hp <= 310 and self.castleHealth.hp > 300:
                    self.castleHealth.image = self.castleHealth.emotions['castle31']
                elif self.castleHealth.hp <= 300 and self.castleHealth.hp > 290:
                    self.castleHealth.image = self.castleHealth.emotions['castle30']
                elif self.castleHealth.hp <= 290 and self.castleHealth.hp > 280:
                    self.castleHealth.image = self.castleHealth.emotions['castle29']
                elif self.castleHealth.hp <= 280 and self.castleHealth.hp > 270:
                    self.castleHealth.image = self.castleHealth.emotions['castle28']
                elif self.castleHealth.hp <= 270 and self.castleHealth.hp > 260:
                    self.castleHealth.image = self.castleHealth.emotions['castle27']
                elif self.castleHealth.hp <= 260 and self.castleHealth.hp > 250:
                    self.castleHealth.image = self.castleHealth.emotions['castle26']
                elif self.castleHealth.hp <= 250 and self.castleHealth.hp > 240:
                    self.castleHealth.image = self.castleHealth.emotions['castle25']
                elif self.castleHealth.hp <= 240 and self.castleHealth.hp > 230:
                    self.castleHealth.image = self.castleHealth.emotions['castle24']
                elif self.castleHealth.hp <= 230 and self.castleHealth.hp > 220:
                    self.castleHealth.image = self.castleHealth.emotions['castle23']
                elif self.castleHealth.hp <= 220 and self.castleHealth.hp > 210:
                    self.castleHealth.image = self.castleHealth.emotions['castle22']
                elif self.castleHealth.hp <= 210 and self.castleHealth.hp > 200:
                    self.castleHealth.image = self.castleHealth.emotions['castle21']
                elif self.castleHealth.hp <= 200 and self.castleHealth.hp > 190:
                    self.castleHealth.image = self.castleHealth.emotions['castle20']
                elif self.castleHealth.hp <= 190 and self.castleHealth.hp > 180:
                    self.castleHealth.image = self.castleHealth.emotions['castle19']
                elif self.castleHealth.hp <= 180 and self.castleHealth.hp > 170:
                    self.castleHealth.image = self.castleHealth.emotions['castle18']
                elif self.castleHealth.hp <= 170 and self.castleHealth.hp > 160:
                    self.castleHealth.image = self.castleHealth.emotions['castle17']
                elif self.castleHealth.hp <= 160 and self.castleHealth.hp > 150:
                    self.castleHealth.image = self.castleHealth.emotions['castle16']
                elif self.castleHealth.hp <= 150 and self.castleHealth.hp > 140:
                    self.castleHealth.image = self.castleHealth.emotions['castle15']
                elif self.castleHealth.hp <= 140 and self.castleHealth.hp > 130:
                    self.castleHealth.image = self.castleHealth.emotions['castle14']
                elif self.castleHealth.hp <= 130 and self.castleHealth.hp > 120:
                    self.castleHealth.image = self.castleHealth.emotions['castle13']
                elif self.castleHealth.hp <= 120 and self.castleHealth.hp > 110:
                    self.castleHealth.image = self.castleHealth.emotions['castle12']
                elif self.castleHealth.hp <= 110 and self.castleHealth.hp > 100:
                    self.castleHealth.image = self.castleHealth.emotions['castle11']
                elif self.castleHealth.hp <= 100 and self.castleHealth.hp > 90:
                    self.castleHealth.image = self.castleHealth.emotions['castle10']
                elif self.castleHealth.hp <= 90 and self.castleHealth.hp > 80:
                    self.castleHealth.image = self.castleHealth.emotions['castle9']
                elif self.castleHealth.hp <= 80 and self.castleHealth.hp > 70:
                    self.castleHealth.image = self.castleHealth.emotions['castle8']
                elif self.castleHealth.hp <= 70 and self.castleHealth.hp > 60:
                    self.castleHealth.image = self.castleHealth.emotions['castle7']
                elif self.castleHealth.hp <= 60 and self.castleHealth.hp > 50:
                    self.castleHealth.image = self.castleHealth.emotions['castle6']
                elif self.castleHealth.hp <= 50 and self.castleHealth.hp > 40:
                    self.castleHealth.image = self.castleHealth.emotions['castle5']
                elif self.castleHealth.hp <= 40 and self.castleHealth.hp > 30:
                    self.castleHealth.image = self.castleHealth.emotions['castle4']
                elif self.castleHealth.hp <= 30 and self.castleHealth.hp > 20:
                    self.castleHealth.image = self.castleHealth.emotions['castle3']
                elif self.castleHealth.hp <= 20 and self.castleHealth.hp > 10:
                    self.castleHealth.image = self.castleHealth.emotions['castle2']
                elif self.castleHealth.hp <= 10 and self.castleHealth.hp > 0:
                    self.castleHealth.image = self.castleHealth.emotions['castle1']

        for i in self.enemy1R:       
            if i.AtkUser == True:
                self.castleHealth.hp -= 0.01
                if self.castleHealth.hp <= 990 and self.castleHealth.hp > 980:
                    self.castleHealth.image = self.castleHealth.emotions['castle99']
                elif self.castleHealth.hp <= 980 and self.castleHealth.hp > 970:
                    self.castleHealth.image = self.castleHealth.emotions['castle98']
                elif self.castleHealth.hp <= 970 and self.castleHealth.hp > 960:
                    self.castleHealth.image = self.castleHealth.emotions['castle97']
                elif self.castleHealth.hp <= 960 and self.castleHealth.hp > 950:
                    self.castleHealth.image = self.castleHealth.emotions['castle96']
                elif self.castleHealth.hp <= 950 and self.castleHealth.hp > 940:
                    self.castleHealth.image = self.castleHealth.emotions['castle95']
                elif self.castleHealth.hp <= 940 and self.castleHealth.hp > 930:
                    self.castleHealth.image = self.castleHealth.emotions['castle94']
                elif self.castleHealth.hp <= 930 and self.castleHealth.hp > 920:
                    self.castleHealth.image = self.castleHealth.emotions['castle93']
                elif self.castleHealth.hp <= 920 and self.castleHealth.hp > 910:
                    self.castleHealth.image = self.castleHealth.emotions['castle92']
                elif self.castleHealth.hp <= 910 and self.castleHealth.hp > 900:
                    self.castleHealth.image = self.castleHealth.emotions['castle91']
                elif self.castleHealth.hp <= 900 and self.castleHealth.hp > 890:
                    self.castleHealth.image = self.castleHealth.emotions['castle90']
                elif self.castleHealth.hp <= 890 and self.castleHealth.hp > 880:
                    self.castleHealth.image = self.castleHealth.emotions['castle89']
                elif self.castleHealth.hp <= 880 and self.castleHealth.hp > 870:
                    self.castleHealth.image = self.castleHealth.emotions['castle88']
                elif self.castleHealth.hp <= 870 and self.castleHealth.hp > 860:
                    self.castleHealth.image = self.castleHealth.emotions['castle87']
                elif self.castleHealth.hp <= 860 and self.castleHealth.hp > 850:
                    self.castleHealth.image = self.castleHealth.emotions['castle86']
                elif self.castleHealth.hp <= 850 and self.castleHealth.hp > 840:
                    self.castleHealth.image = self.castleHealth.emotions['castle85']
                elif self.castleHealth.hp <= 840 and self.castleHealth.hp > 830:
                    self.castleHealth.image = self.castleHealth.emotions['castle84']
                elif self.castleHealth.hp <= 830 and self.castleHealth.hp > 820:
                    self.castleHealth.image = self.castleHealth.emotions['castle83']
                elif self.castleHealth.hp <= 820 and self.castleHealth.hp > 810:
                    self.castleHealth.image = self.castleHealth.emotions['castle82']
                elif self.castleHealth.hp <= 810 and self.castleHealth.hp > 800:
                    self.castleHealth.image = self.castleHealth.emotions['castle81']
                elif self.castleHealth.hp <= 800 and self.castleHealth.hp > 790:
                    self.castleHealth.image = self.castleHealth.emotions['castle80']
                elif self.castleHealth.hp <= 790 and self.castleHealth.hp > 780:
                    self.castleHealth.image = self.castleHealth.emotions['castle79']
                elif self.castleHealth.hp <= 780 and self.castleHealth.hp > 770:
                    self.castleHealth.image = self.castleHealth.emotions['castle78']
                elif self.castleHealth.hp <= 770 and self.castleHealth.hp > 760:
                    self.castleHealth.image = self.castleHealth.emotions['castle77']
                elif self.castleHealth.hp <= 760 and self.castleHealth.hp > 750:
                    self.castleHealth.image = self.castleHealth.emotions['castle76']
                elif self.castleHealth.hp <= 750 and self.castleHealth.hp > 740:
                    self.castleHealth.image = self.castleHealth.emotions['castle75']
                elif self.castleHealth.hp <= 740 and self.castleHealth.hp > 730:
                    self.castleHealth.image = self.castleHealth.emotions['castle74']
                elif self.castleHealth.hp <= 730 and self.castleHealth.hp > 720:
                    self.castleHealth.image = self.castleHealth.emotions['castle73']
                elif self.castleHealth.hp <= 720 and self.castleHealth.hp > 710:
                    self.castleHealth.image = self.castleHealth.emotions['castle72']
                elif self.castleHealth.hp <= 710 and self.castleHealth.hp > 700:
                    self.castleHealth.image = self.castleHealth.emotions['castle71']
                elif self.castleHealth.hp <= 700 and self.castleHealth.hp > 690:
                    self.castleHealth.image = self.castleHealth.emotions['castle70']
                elif self.castleHealth.hp <= 690 and self.castleHealth.hp > 680:
                    self.castleHealth.image = self.castleHealth.emotions['castle69']
                elif self.castleHealth.hp <= 680 and self.castleHealth.hp > 670:
                    self.castleHealth.image = self.castleHealth.emotions['castle68']
                elif self.castleHealth.hp <= 670 and self.castleHealth.hp > 660:
                    self.castleHealth.image = self.castleHealth.emotions['castle67']
                elif self.castleHealth.hp <= 660 and self.castleHealth.hp > 650:
                    self.castleHealth.image = self.castleHealth.emotions['castle66']
                elif self.castleHealth.hp <= 650 and self.castleHealth.hp > 640:
                    self.castleHealth.image = self.castleHealth.emotions['castle65']
                elif self.castleHealth.hp <= 640 and self.castleHealth.hp > 630:
                    self.castleHealth.image = self.castleHealth.emotions['castle64']
                elif self.castleHealth.hp <= 630 and self.castleHealth.hp > 620:
                    self.castleHealth.image = self.castleHealth.emotions['castle63']
                elif self.castleHealth.hp <= 620 and self.castleHealth.hp > 610:
                    self.castleHealth.image = self.castleHealth.emotions['castle62']
                elif self.castleHealth.hp <= 610 and self.castleHealth.hp > 600:
                    self.castleHealth.image = self.castleHealth.emotions['castle61']
                elif self.castleHealth.hp <= 600 and self.castleHealth.hp > 590:
                    self.castleHealth.image = self.castleHealth.emotions['castle60']
                elif self.castleHealth.hp <= 590 and self.castleHealth.hp > 580:
                    self.castleHealth.image = self.castleHealth.emotions['castle59']
                elif self.castleHealth.hp <= 580 and self.castleHealth.hp > 570:
                    self.castleHealth.image = self.castleHealth.emotions['castle58']
                elif self.castleHealth.hp <= 570 and self.castleHealth.hp > 560:
                    self.castleHealth.image = self.castleHealth.emotions['castle57']
                elif self.castleHealth.hp <= 560 and self.castleHealth.hp > 550:
                    self.castleHealth.image = self.castleHealth.emotions['castle56']
                elif self.castleHealth.hp <= 550 and self.castleHealth.hp > 540:
                    self.castleHealth.image = self.castleHealth.emotions['castle55']
                elif self.castleHealth.hp <= 540 and self.castleHealth.hp > 530:
                    self.castleHealth.image = self.castleHealth.emotions['castle54']
                elif self.castleHealth.hp <= 530 and self.castleHealth.hp > 520:
                    self.castleHealth.image = self.castleHealth.emotions['castle53']
                elif self.castleHealth.hp <= 520 and self.castleHealth.hp > 510:
                    self.castleHealth.image = self.castleHealth.emotions['castle52']
                elif self.castleHealth.hp <= 510 and self.castleHealth.hp > 500:
                    self.castleHealth.image = self.castleHealth.emotions['castle51']
                elif self.castleHealth.hp <= 500 and self.castleHealth.hp > 490:
                    self.castleHealth.image = self.castleHealth.emotions['castle50']
                elif self.castleHealth.hp <= 490 and self.castleHealth.hp > 480:
                    self.castleHealth.image = self.castleHealth.emotions['castle49']
                elif self.castleHealth.hp <= 480 and self.castleHealth.hp > 470:
                    self.castleHealth.image = self.castleHealth.emotions['castle48']
                elif self.castleHealth.hp <= 470 and self.castleHealth.hp > 460:
                    self.castleHealth.image = self.castleHealth.emotions['castle47']
                elif self.castleHealth.hp <= 460 and self.castleHealth.hp > 450:
                    self.castleHealth.image = self.castleHealth.emotions['castle46']
                elif self.castleHealth.hp <= 450 and self.castleHealth.hp > 440:
                    self.castleHealth.image = self.castleHealth.emotions['castle45']
                elif self.castleHealth.hp <= 440 and self.castleHealth.hp > 430:
                    self.castleHealth.image = self.castleHealth.emotions['castle44']
                elif self.castleHealth.hp <= 430 and self.castleHealth.hp > 420:
                    self.castleHealth.image = self.castleHealth.emotions['castle43']
                elif self.castleHealth.hp <= 420 and self.castleHealth.hp > 410:
                    self.castleHealth.image = self.castleHealth.emotions['castle42']
                elif self.castleHealth.hp <= 410 and self.castleHealth.hp > 400:
                    self.castleHealth.image = self.castleHealth.emotions['castle41']
                elif self.castleHealth.hp <= 400 and self.castleHealth.hp > 390:
                    self.castleHealth.image = self.castleHealth.emotions['castle40']
                elif self.castleHealth.hp <= 390 and self.castleHealth.hp > 380:
                    self.castleHealth.image = self.castleHealth.emotions['castle39']
                elif self.castleHealth.hp <= 380 and self.castleHealth.hp > 370:
                    self.castleHealth.image = self.castleHealth.emotions['castle38']
                elif self.castleHealth.hp <= 370 and self.castleHealth.hp > 360:
                    self.castleHealth.image = self.castleHealth.emotions['castle37']
                elif self.castleHealth.hp <= 360 and self.castleHealth.hp > 350:
                    self.castleHealth.image = self.castleHealth.emotions['castle36']
                elif self.castleHealth.hp <= 350 and self.castleHealth.hp > 340:
                    self.castleHealth.image = self.castleHealth.emotions['castle35']
                elif self.castleHealth.hp <= 340 and self.castleHealth.hp > 330:
                    self.castleHealth.image = self.castleHealth.emotions['castle34']
                elif self.castleHealth.hp <= 330 and self.castleHealth.hp > 320:
                    self.castleHealth.image = self.castleHealth.emotions['castle33']
                elif self.castleHealth.hp <= 320 and self.castleHealth.hp > 310:
                    self.castleHealth.image = self.castleHealth.emotions['castle32']
                elif self.castleHealth.hp <= 310 and self.castleHealth.hp > 300:
                    self.castleHealth.image = self.castleHealth.emotions['castle31']
                elif self.castleHealth.hp <= 300 and self.castleHealth.hp > 290:
                    self.castleHealth.image = self.castleHealth.emotions['castle30']
                elif self.castleHealth.hp <= 290 and self.castleHealth.hp > 280:
                    self.castleHealth.image = self.castleHealth.emotions['castle29']
                elif self.castleHealth.hp <= 280 and self.castleHealth.hp > 270:
                    self.castleHealth.image = self.castleHealth.emotions['castle28']
                elif self.castleHealth.hp <= 270 and self.castleHealth.hp > 260:
                    self.castleHealth.image = self.castleHealth.emotions['castle27']
                elif self.castleHealth.hp <= 260 and self.castleHealth.hp > 250:
                    self.castleHealth.image = self.castleHealth.emotions['castle26']
                elif self.castleHealth.hp <= 250 and self.castleHealth.hp > 240:
                    self.castleHealth.image = self.castleHealth.emotions['castle25']
                elif self.castleHealth.hp <= 240 and self.castleHealth.hp > 230:
                    self.castleHealth.image = self.castleHealth.emotions['castle24']
                elif self.castleHealth.hp <= 230 and self.castleHealth.hp > 220:
                    self.castleHealth.image = self.castleHealth.emotions['castle23']
                elif self.castleHealth.hp <= 220 and self.castleHealth.hp > 210:
                    self.castleHealth.image = self.castleHealth.emotions['castle22']
                elif self.castleHealth.hp <= 210 and self.castleHealth.hp > 200:
                    self.castleHealth.image = self.castleHealth.emotions['castle21']
                elif self.castleHealth.hp <= 200 and self.castleHealth.hp > 190:
                    self.castleHealth.image = self.castleHealth.emotions['castle20']
                elif self.castleHealth.hp <= 190 and self.castleHealth.hp > 180:
                    self.castleHealth.image = self.castleHealth.emotions['castle19']
                elif self.castleHealth.hp <= 180 and self.castleHealth.hp > 170:
                    self.castleHealth.image = self.castleHealth.emotions['castle18']
                elif self.castleHealth.hp <= 170 and self.castleHealth.hp > 160:
                    self.castleHealth.image = self.castleHealth.emotions['castle17']
                elif self.castleHealth.hp <= 160 and self.castleHealth.hp > 150:
                    self.castleHealth.image = self.castleHealth.emotions['castle16']
                elif self.castleHealth.hp <= 150 and self.castleHealth.hp > 140:
                    self.castleHealth.image = self.castleHealth.emotions['castle15']
                elif self.castleHealth.hp <= 140 and self.castleHealth.hp > 130:
                    self.castleHealth.image = self.castleHealth.emotions['castle14']
                elif self.castleHealth.hp <= 130 and self.castleHealth.hp > 120:
                    self.castleHealth.image = self.castleHealth.emotions['castle13']
                elif self.castleHealth.hp <= 120 and self.castleHealth.hp > 110:
                    self.castleHealth.image = self.castleHealth.emotions['castle12']
                elif self.castleHealth.hp <= 110 and self.castleHealth.hp > 100:
                    self.castleHealth.image = self.castleHealth.emotions['castle11']
                elif self.castleHealth.hp <= 100 and self.castleHealth.hp > 90:
                    self.castleHealth.image = self.castleHealth.emotions['castle10']
                elif self.castleHealth.hp <= 90 and self.castleHealth.hp > 80:
                    self.castleHealth.image = self.castleHealth.emotions['castle9']
                elif self.castleHealth.hp <= 80 and self.castleHealth.hp > 70:
                    self.castleHealth.image = self.castleHealth.emotions['castle8']
                elif self.castleHealth.hp <= 70 and self.castleHealth.hp > 60:
                    self.castleHealth.image = self.castleHealth.emotions['castle7']
                elif self.castleHealth.hp <= 60 and self.castleHealth.hp > 50:
                    self.castleHealth.image = self.castleHealth.emotions['castle6']
                elif self.castleHealth.hp <= 50 and self.castleHealth.hp > 40:
                    self.castleHealth.image = self.castleHealth.emotions['castle5']
                elif self.castleHealth.hp <= 40 and self.castleHealth.hp > 30:
                    self.castleHealth.image = self.castleHealth.emotions['castle4']
                elif self.castleHealth.hp <= 30 and self.castleHealth.hp > 20:
                    self.castleHealth.image = self.castleHealth.emotions['castle3']
                elif self.castleHealth.hp <= 20 and self.castleHealth.hp > 10:
                    self.castleHealth.image = self.castleHealth.emotions['castle2']
                elif self.castleHealth.hp <= 10 and self.castleHealth.hp > 0:
                    self.castleHealth.image = self.castleHealth.emotions['castle1']

        for i in self.enemy2L:       
            if i.AtkUser == True:
                self.castleHealth.hp -= 0.01
                if self.castleHealth.hp <= 990 and self.castleHealth.hp > 980:
                    self.castleHealth.image = self.castleHealth.emotions['castle99']
                elif self.castleHealth.hp <= 980 and self.castleHealth.hp > 970:
                    self.castleHealth.image = self.castleHealth.emotions['castle98']
                elif self.castleHealth.hp <= 970 and self.castleHealth.hp > 960:
                    self.castleHealth.image = self.castleHealth.emotions['castle97']
                elif self.castleHealth.hp <= 960 and self.castleHealth.hp > 950:
                    self.castleHealth.image = self.castleHealth.emotions['castle96']
                elif self.castleHealth.hp <= 950 and self.castleHealth.hp > 940:
                    self.castleHealth.image = self.castleHealth.emotions['castle95']
                elif self.castleHealth.hp <= 940 and self.castleHealth.hp > 930:
                    self.castleHealth.image = self.castleHealth.emotions['castle94']
                elif self.castleHealth.hp <= 930 and self.castleHealth.hp > 920:
                    self.castleHealth.image = self.castleHealth.emotions['castle93']
                elif self.castleHealth.hp <= 920 and self.castleHealth.hp > 910:
                    self.castleHealth.image = self.castleHealth.emotions['castle92']
                elif self.castleHealth.hp <= 910 and self.castleHealth.hp > 900:
                    self.castleHealth.image = self.castleHealth.emotions['castle91']
                elif self.castleHealth.hp <= 900 and self.castleHealth.hp > 890:
                    self.castleHealth.image = self.castleHealth.emotions['castle90']
                elif self.castleHealth.hp <= 890 and self.castleHealth.hp > 880:
                    self.castleHealth.image = self.castleHealth.emotions['castle89']
                elif self.castleHealth.hp <= 880 and self.castleHealth.hp > 870:
                    self.castleHealth.image = self.castleHealth.emotions['castle88']
                elif self.castleHealth.hp <= 870 and self.castleHealth.hp > 860:
                    self.castleHealth.image = self.castleHealth.emotions['castle87']
                elif self.castleHealth.hp <= 860 and self.castleHealth.hp > 850:
                    self.castleHealth.image = self.castleHealth.emotions['castle86']
                elif self.castleHealth.hp <= 850 and self.castleHealth.hp > 840:
                    self.castleHealth.image = self.castleHealth.emotions['castle85']
                elif self.castleHealth.hp <= 840 and self.castleHealth.hp > 830:
                    self.castleHealth.image = self.castleHealth.emotions['castle84']
                elif self.castleHealth.hp <= 830 and self.castleHealth.hp > 820:
                    self.castleHealth.image = self.castleHealth.emotions['castle83']
                elif self.castleHealth.hp <= 820 and self.castleHealth.hp > 810:
                    self.castleHealth.image = self.castleHealth.emotions['castle82']
                elif self.castleHealth.hp <= 810 and self.castleHealth.hp > 800:
                    self.castleHealth.image = self.castleHealth.emotions['castle81']
                elif self.castleHealth.hp <= 800 and self.castleHealth.hp > 790:
                    self.castleHealth.image = self.castleHealth.emotions['castle80']
                elif self.castleHealth.hp <= 790 and self.castleHealth.hp > 780:
                    self.castleHealth.image = self.castleHealth.emotions['castle79']
                elif self.castleHealth.hp <= 780 and self.castleHealth.hp > 770:
                    self.castleHealth.image = self.castleHealth.emotions['castle78']
                elif self.castleHealth.hp <= 770 and self.castleHealth.hp > 760:
                    self.castleHealth.image = self.castleHealth.emotions['castle77']
                elif self.castleHealth.hp <= 760 and self.castleHealth.hp > 750:
                    self.castleHealth.image = self.castleHealth.emotions['castle76']
                elif self.castleHealth.hp <= 750 and self.castleHealth.hp > 740:
                    self.castleHealth.image = self.castleHealth.emotions['castle75']
                elif self.castleHealth.hp <= 740 and self.castleHealth.hp > 730:
                    self.castleHealth.image = self.castleHealth.emotions['castle74']
                elif self.castleHealth.hp <= 730 and self.castleHealth.hp > 720:
                    self.castleHealth.image = self.castleHealth.emotions['castle73']
                elif self.castleHealth.hp <= 720 and self.castleHealth.hp > 710:
                    self.castleHealth.image = self.castleHealth.emotions['castle72']
                elif self.castleHealth.hp <= 710 and self.castleHealth.hp > 700:
                    self.castleHealth.image = self.castleHealth.emotions['castle71']
                elif self.castleHealth.hp <= 700 and self.castleHealth.hp > 690:
                    self.castleHealth.image = self.castleHealth.emotions['castle70']
                elif self.castleHealth.hp <= 690 and self.castleHealth.hp > 680:
                    self.castleHealth.image = self.castleHealth.emotions['castle69']
                elif self.castleHealth.hp <= 680 and self.castleHealth.hp > 670:
                    self.castleHealth.image = self.castleHealth.emotions['castle68']
                elif self.castleHealth.hp <= 670 and self.castleHealth.hp > 660:
                    self.castleHealth.image = self.castleHealth.emotions['castle67']
                elif self.castleHealth.hp <= 660 and self.castleHealth.hp > 650:
                    self.castleHealth.image = self.castleHealth.emotions['castle66']
                elif self.castleHealth.hp <= 650 and self.castleHealth.hp > 640:
                    self.castleHealth.image = self.castleHealth.emotions['castle65']
                elif self.castleHealth.hp <= 640 and self.castleHealth.hp > 630:
                    self.castleHealth.image = self.castleHealth.emotions['castle64']
                elif self.castleHealth.hp <= 630 and self.castleHealth.hp > 620:
                    self.castleHealth.image = self.castleHealth.emotions['castle63']
                elif self.castleHealth.hp <= 620 and self.castleHealth.hp > 610:
                    self.castleHealth.image = self.castleHealth.emotions['castle62']
                elif self.castleHealth.hp <= 610 and self.castleHealth.hp > 600:
                    self.castleHealth.image = self.castleHealth.emotions['castle61']
                elif self.castleHealth.hp <= 600 and self.castleHealth.hp > 590:
                    self.castleHealth.image = self.castleHealth.emotions['castle60']
                elif self.castleHealth.hp <= 590 and self.castleHealth.hp > 580:
                    self.castleHealth.image = self.castleHealth.emotions['castle59']
                elif self.castleHealth.hp <= 580 and self.castleHealth.hp > 570:
                    self.castleHealth.image = self.castleHealth.emotions['castle58']
                elif self.castleHealth.hp <= 570 and self.castleHealth.hp > 560:
                    self.castleHealth.image = self.castleHealth.emotions['castle57']
                elif self.castleHealth.hp <= 560 and self.castleHealth.hp > 550:
                    self.castleHealth.image = self.castleHealth.emotions['castle56']
                elif self.castleHealth.hp <= 550 and self.castleHealth.hp > 540:
                    self.castleHealth.image = self.castleHealth.emotions['castle55']
                elif self.castleHealth.hp <= 540 and self.castleHealth.hp > 530:
                    self.castleHealth.image = self.castleHealth.emotions['castle54']
                elif self.castleHealth.hp <= 530 and self.castleHealth.hp > 520:
                    self.castleHealth.image = self.castleHealth.emotions['castle53']
                elif self.castleHealth.hp <= 520 and self.castleHealth.hp > 510:
                    self.castleHealth.image = self.castleHealth.emotions['castle52']
                elif self.castleHealth.hp <= 510 and self.castleHealth.hp > 500:
                    self.castleHealth.image = self.castleHealth.emotions['castle51']
                elif self.castleHealth.hp <= 500 and self.castleHealth.hp > 490:
                    self.castleHealth.image = self.castleHealth.emotions['castle50']
                elif self.castleHealth.hp <= 490 and self.castleHealth.hp > 480:
                    self.castleHealth.image = self.castleHealth.emotions['castle49']
                elif self.castleHealth.hp <= 480 and self.castleHealth.hp > 470:
                    self.castleHealth.image = self.castleHealth.emotions['castle48']
                elif self.castleHealth.hp <= 470 and self.castleHealth.hp > 460:
                    self.castleHealth.image = self.castleHealth.emotions['castle47']
                elif self.castleHealth.hp <= 460 and self.castleHealth.hp > 450:
                    self.castleHealth.image = self.castleHealth.emotions['castle46']
                elif self.castleHealth.hp <= 450 and self.castleHealth.hp > 440:
                    self.castleHealth.image = self.castleHealth.emotions['castle45']
                elif self.castleHealth.hp <= 440 and self.castleHealth.hp > 430:
                    self.castleHealth.image = self.castleHealth.emotions['castle44']
                elif self.castleHealth.hp <= 430 and self.castleHealth.hp > 420:
                    self.castleHealth.image = self.castleHealth.emotions['castle43']
                elif self.castleHealth.hp <= 420 and self.castleHealth.hp > 410:
                    self.castleHealth.image = self.castleHealth.emotions['castle42']
                elif self.castleHealth.hp <= 410 and self.castleHealth.hp > 400:
                    self.castleHealth.image = self.castleHealth.emotions['castle41']
                elif self.castleHealth.hp <= 400 and self.castleHealth.hp > 390:
                    self.castleHealth.image = self.castleHealth.emotions['castle40']
                elif self.castleHealth.hp <= 390 and self.castleHealth.hp > 380:
                    self.castleHealth.image = self.castleHealth.emotions['castle39']
                elif self.castleHealth.hp <= 380 and self.castleHealth.hp > 370:
                    self.castleHealth.image = self.castleHealth.emotions['castle38']
                elif self.castleHealth.hp <= 370 and self.castleHealth.hp > 360:
                    self.castleHealth.image = self.castleHealth.emotions['castle37']
                elif self.castleHealth.hp <= 360 and self.castleHealth.hp > 350:
                    self.castleHealth.image = self.castleHealth.emotions['castle36']
                elif self.castleHealth.hp <= 350 and self.castleHealth.hp > 340:
                    self.castleHealth.image = self.castleHealth.emotions['castle35']
                elif self.castleHealth.hp <= 340 and self.castleHealth.hp > 330:
                    self.castleHealth.image = self.castleHealth.emotions['castle34']
                elif self.castleHealth.hp <= 330 and self.castleHealth.hp > 320:
                    self.castleHealth.image = self.castleHealth.emotions['castle33']
                elif self.castleHealth.hp <= 320 and self.castleHealth.hp > 310:
                    self.castleHealth.image = self.castleHealth.emotions['castle32']
                elif self.castleHealth.hp <= 310 and self.castleHealth.hp > 300:
                    self.castleHealth.image = self.castleHealth.emotions['castle31']
                elif self.castleHealth.hp <= 300 and self.castleHealth.hp > 290:
                    self.castleHealth.image = self.castleHealth.emotions['castle30']
                elif self.castleHealth.hp <= 290 and self.castleHealth.hp > 280:
                    self.castleHealth.image = self.castleHealth.emotions['castle29']
                elif self.castleHealth.hp <= 280 and self.castleHealth.hp > 270:
                    self.castleHealth.image = self.castleHealth.emotions['castle28']
                elif self.castleHealth.hp <= 270 and self.castleHealth.hp > 260:
                    self.castleHealth.image = self.castleHealth.emotions['castle27']
                elif self.castleHealth.hp <= 260 and self.castleHealth.hp > 250:
                    self.castleHealth.image = self.castleHealth.emotions['castle26']
                elif self.castleHealth.hp <= 250 and self.castleHealth.hp > 240:
                    self.castleHealth.image = self.castleHealth.emotions['castle25']
                elif self.castleHealth.hp <= 240 and self.castleHealth.hp > 230:
                    self.castleHealth.image = self.castleHealth.emotions['castle24']
                elif self.castleHealth.hp <= 230 and self.castleHealth.hp > 220:
                    self.castleHealth.image = self.castleHealth.emotions['castle23']
                elif self.castleHealth.hp <= 220 and self.castleHealth.hp > 210:
                    self.castleHealth.image = self.castleHealth.emotions['castle22']
                elif self.castleHealth.hp <= 210 and self.castleHealth.hp > 200:
                    self.castleHealth.image = self.castleHealth.emotions['castle21']
                elif self.castleHealth.hp <= 200 and self.castleHealth.hp > 190:
                    self.castleHealth.image = self.castleHealth.emotions['castle20']
                elif self.castleHealth.hp <= 190 and self.castleHealth.hp > 180:
                    self.castleHealth.image = self.castleHealth.emotions['castle19']
                elif self.castleHealth.hp <= 180 and self.castleHealth.hp > 170:
                    self.castleHealth.image = self.castleHealth.emotions['castle18']
                elif self.castleHealth.hp <= 170 and self.castleHealth.hp > 160:
                    self.castleHealth.image = self.castleHealth.emotions['castle17']
                elif self.castleHealth.hp <= 160 and self.castleHealth.hp > 150:
                    self.castleHealth.image = self.castleHealth.emotions['castle16']
                elif self.castleHealth.hp <= 150 and self.castleHealth.hp > 140:
                    self.castleHealth.image = self.castleHealth.emotions['castle15']
                elif self.castleHealth.hp <= 140 and self.castleHealth.hp > 130:
                    self.castleHealth.image = self.castleHealth.emotions['castle14']
                elif self.castleHealth.hp <= 130 and self.castleHealth.hp > 120:
                    self.castleHealth.image = self.castleHealth.emotions['castle13']
                elif self.castleHealth.hp <= 120 and self.castleHealth.hp > 110:
                    self.castleHealth.image = self.castleHealth.emotions['castle12']
                elif self.castleHealth.hp <= 110 and self.castleHealth.hp > 100:
                    self.castleHealth.image = self.castleHealth.emotions['castle11']
                elif self.castleHealth.hp <= 100 and self.castleHealth.hp > 90:
                    self.castleHealth.image = self.castleHealth.emotions['castle10']
                elif self.castleHealth.hp <= 90 and self.castleHealth.hp > 80:
                    self.castleHealth.image = self.castleHealth.emotions['castle9']
                elif self.castleHealth.hp <= 80 and self.castleHealth.hp > 70:
                    self.castleHealth.image = self.castleHealth.emotions['castle8']
                elif self.castleHealth.hp <= 70 and self.castleHealth.hp > 60:
                    self.castleHealth.image = self.castleHealth.emotions['castle7']
                elif self.castleHealth.hp <= 60 and self.castleHealth.hp > 50:
                    self.castleHealth.image = self.castleHealth.emotions['castle6']
                elif self.castleHealth.hp <= 50 and self.castleHealth.hp > 40:
                    self.castleHealth.image = self.castleHealth.emotions['castle5']
                elif self.castleHealth.hp <= 40 and self.castleHealth.hp > 30:
                    self.castleHealth.image = self.castleHealth.emotions['castle4']
                elif self.castleHealth.hp <= 30 and self.castleHealth.hp > 20:
                    self.castleHealth.image = self.castleHealth.emotions['castle3']
                elif self.castleHealth.hp <= 20 and self.castleHealth.hp > 10:
                    self.castleHealth.image = self.castleHealth.emotions['castle2']
                elif self.castleHealth.hp <= 10 and self.castleHealth.hp > 0:
                    self.castleHealth.image = self.castleHealth.emotions['castle1']

        for i in self.enemy2R:       
            if i.AtkUser == True:
                self.castleHealth.hp -= 0.01
                if self.castleHealth.hp <= 990 and self.castleHealth.hp > 980:
                    self.castleHealth.image = self.castleHealth.emotions['castle99']
                elif self.castleHealth.hp <= 980 and self.castleHealth.hp > 970:
                    self.castleHealth.image = self.castleHealth.emotions['castle98']
                elif self.castleHealth.hp <= 970 and self.castleHealth.hp > 960:
                    self.castleHealth.image = self.castleHealth.emotions['castle97']
                elif self.castleHealth.hp <= 960 and self.castleHealth.hp > 950:
                    self.castleHealth.image = self.castleHealth.emotions['castle96']
                elif self.castleHealth.hp <= 950 and self.castleHealth.hp > 940:
                    self.castleHealth.image = self.castleHealth.emotions['castle95']
                elif self.castleHealth.hp <= 940 and self.castleHealth.hp > 930:
                    self.castleHealth.image = self.castleHealth.emotions['castle94']
                elif self.castleHealth.hp <= 930 and self.castleHealth.hp > 920:
                    self.castleHealth.image = self.castleHealth.emotions['castle93']
                elif self.castleHealth.hp <= 920 and self.castleHealth.hp > 910:
                    self.castleHealth.image = self.castleHealth.emotions['castle92']
                elif self.castleHealth.hp <= 910 and self.castleHealth.hp > 900:
                    self.castleHealth.image = self.castleHealth.emotions['castle91']
                elif self.castleHealth.hp <= 900 and self.castleHealth.hp > 890:
                    self.castleHealth.image = self.castleHealth.emotions['castle90']
                elif self.castleHealth.hp <= 890 and self.castleHealth.hp > 880:
                    self.castleHealth.image = self.castleHealth.emotions['castle89']
                elif self.castleHealth.hp <= 880 and self.castleHealth.hp > 870:
                    self.castleHealth.image = self.castleHealth.emotions['castle88']
                elif self.castleHealth.hp <= 870 and self.castleHealth.hp > 860:
                    self.castleHealth.image = self.castleHealth.emotions['castle87']
                elif self.castleHealth.hp <= 860 and self.castleHealth.hp > 850:
                    self.castleHealth.image = self.castleHealth.emotions['castle86']
                elif self.castleHealth.hp <= 850 and self.castleHealth.hp > 840:
                    self.castleHealth.image = self.castleHealth.emotions['castle85']
                elif self.castleHealth.hp <= 840 and self.castleHealth.hp > 830:
                    self.castleHealth.image = self.castleHealth.emotions['castle84']
                elif self.castleHealth.hp <= 830 and self.castleHealth.hp > 820:
                    self.castleHealth.image = self.castleHealth.emotions['castle83']
                elif self.castleHealth.hp <= 820 and self.castleHealth.hp > 810:
                    self.castleHealth.image = self.castleHealth.emotions['castle82']
                elif self.castleHealth.hp <= 810 and self.castleHealth.hp > 800:
                    self.castleHealth.image = self.castleHealth.emotions['castle81']
                elif self.castleHealth.hp <= 800 and self.castleHealth.hp > 790:
                    self.castleHealth.image = self.castleHealth.emotions['castle80']
                elif self.castleHealth.hp <= 790 and self.castleHealth.hp > 780:
                    self.castleHealth.image = self.castleHealth.emotions['castle79']
                elif self.castleHealth.hp <= 780 and self.castleHealth.hp > 770:
                    self.castleHealth.image = self.castleHealth.emotions['castle78']
                elif self.castleHealth.hp <= 770 and self.castleHealth.hp > 760:
                    self.castleHealth.image = self.castleHealth.emotions['castle77']
                elif self.castleHealth.hp <= 760 and self.castleHealth.hp > 750:
                    self.castleHealth.image = self.castleHealth.emotions['castle76']
                elif self.castleHealth.hp <= 750 and self.castleHealth.hp > 740:
                    self.castleHealth.image = self.castleHealth.emotions['castle75']
                elif self.castleHealth.hp <= 740 and self.castleHealth.hp > 730:
                    self.castleHealth.image = self.castleHealth.emotions['castle74']
                elif self.castleHealth.hp <= 730 and self.castleHealth.hp > 720:
                    self.castleHealth.image = self.castleHealth.emotions['castle73']
                elif self.castleHealth.hp <= 720 and self.castleHealth.hp > 710:
                    self.castleHealth.image = self.castleHealth.emotions['castle72']
                elif self.castleHealth.hp <= 710 and self.castleHealth.hp > 700:
                    self.castleHealth.image = self.castleHealth.emotions['castle71']
                elif self.castleHealth.hp <= 700 and self.castleHealth.hp > 690:
                    self.castleHealth.image = self.castleHealth.emotions['castle70']
                elif self.castleHealth.hp <= 690 and self.castleHealth.hp > 680:
                    self.castleHealth.image = self.castleHealth.emotions['castle69']
                elif self.castleHealth.hp <= 680 and self.castleHealth.hp > 670:
                    self.castleHealth.image = self.castleHealth.emotions['castle68']
                elif self.castleHealth.hp <= 670 and self.castleHealth.hp > 660:
                    self.castleHealth.image = self.castleHealth.emotions['castle67']
                elif self.castleHealth.hp <= 660 and self.castleHealth.hp > 650:
                    self.castleHealth.image = self.castleHealth.emotions['castle66']
                elif self.castleHealth.hp <= 650 and self.castleHealth.hp > 640:
                    self.castleHealth.image = self.castleHealth.emotions['castle65']
                elif self.castleHealth.hp <= 640 and self.castleHealth.hp > 630:
                    self.castleHealth.image = self.castleHealth.emotions['castle64']
                elif self.castleHealth.hp <= 630 and self.castleHealth.hp > 620:
                    self.castleHealth.image = self.castleHealth.emotions['castle63']
                elif self.castleHealth.hp <= 620 and self.castleHealth.hp > 610:
                    self.castleHealth.image = self.castleHealth.emotions['castle62']
                elif self.castleHealth.hp <= 610 and self.castleHealth.hp > 600:
                    self.castleHealth.image = self.castleHealth.emotions['castle61']
                elif self.castleHealth.hp <= 600 and self.castleHealth.hp > 590:
                    self.castleHealth.image = self.castleHealth.emotions['castle60']
                elif self.castleHealth.hp <= 590 and self.castleHealth.hp > 580:
                    self.castleHealth.image = self.castleHealth.emotions['castle59']
                elif self.castleHealth.hp <= 580 and self.castleHealth.hp > 570:
                    self.castleHealth.image = self.castleHealth.emotions['castle58']
                elif self.castleHealth.hp <= 570 and self.castleHealth.hp > 560:
                    self.castleHealth.image = self.castleHealth.emotions['castle57']
                elif self.castleHealth.hp <= 560 and self.castleHealth.hp > 550:
                    self.castleHealth.image = self.castleHealth.emotions['castle56']
                elif self.castleHealth.hp <= 550 and self.castleHealth.hp > 540:
                    self.castleHealth.image = self.castleHealth.emotions['castle55']
                elif self.castleHealth.hp <= 540 and self.castleHealth.hp > 530:
                    self.castleHealth.image = self.castleHealth.emotions['castle54']
                elif self.castleHealth.hp <= 530 and self.castleHealth.hp > 520:
                    self.castleHealth.image = self.castleHealth.emotions['castle53']
                elif self.castleHealth.hp <= 520 and self.castleHealth.hp > 510:
                    self.castleHealth.image = self.castleHealth.emotions['castle52']
                elif self.castleHealth.hp <= 510 and self.castleHealth.hp > 500:
                    self.castleHealth.image = self.castleHealth.emotions['castle51']
                elif self.castleHealth.hp <= 500 and self.castleHealth.hp > 490:
                    self.castleHealth.image = self.castleHealth.emotions['castle50']
                elif self.castleHealth.hp <= 490 and self.castleHealth.hp > 480:
                    self.castleHealth.image = self.castleHealth.emotions['castle49']
                elif self.castleHealth.hp <= 480 and self.castleHealth.hp > 470:
                    self.castleHealth.image = self.castleHealth.emotions['castle48']
                elif self.castleHealth.hp <= 470 and self.castleHealth.hp > 460:
                    self.castleHealth.image = self.castleHealth.emotions['castle47']
                elif self.castleHealth.hp <= 460 and self.castleHealth.hp > 450:
                    self.castleHealth.image = self.castleHealth.emotions['castle46']
                elif self.castleHealth.hp <= 450 and self.castleHealth.hp > 440:
                    self.castleHealth.image = self.castleHealth.emotions['castle45']
                elif self.castleHealth.hp <= 440 and self.castleHealth.hp > 430:
                    self.castleHealth.image = self.castleHealth.emotions['castle44']
                elif self.castleHealth.hp <= 430 and self.castleHealth.hp > 420:
                    self.castleHealth.image = self.castleHealth.emotions['castle43']
                elif self.castleHealth.hp <= 420 and self.castleHealth.hp > 410:
                    self.castleHealth.image = self.castleHealth.emotions['castle42']
                elif self.castleHealth.hp <= 410 and self.castleHealth.hp > 400:
                    self.castleHealth.image = self.castleHealth.emotions['castle41']
                elif self.castleHealth.hp <= 400 and self.castleHealth.hp > 390:
                    self.castleHealth.image = self.castleHealth.emotions['castle40']
                elif self.castleHealth.hp <= 390 and self.castleHealth.hp > 380:
                    self.castleHealth.image = self.castleHealth.emotions['castle39']
                elif self.castleHealth.hp <= 380 and self.castleHealth.hp > 370:
                    self.castleHealth.image = self.castleHealth.emotions['castle38']
                elif self.castleHealth.hp <= 370 and self.castleHealth.hp > 360:
                    self.castleHealth.image = self.castleHealth.emotions['castle37']
                elif self.castleHealth.hp <= 360 and self.castleHealth.hp > 350:
                    self.castleHealth.image = self.castleHealth.emotions['castle36']
                elif self.castleHealth.hp <= 350 and self.castleHealth.hp > 340:
                    self.castleHealth.image = self.castleHealth.emotions['castle35']
                elif self.castleHealth.hp <= 340 and self.castleHealth.hp > 330:
                    self.castleHealth.image = self.castleHealth.emotions['castle34']
                elif self.castleHealth.hp <= 330 and self.castleHealth.hp > 320:
                    self.castleHealth.image = self.castleHealth.emotions['castle33']
                elif self.castleHealth.hp <= 320 and self.castleHealth.hp > 310:
                    self.castleHealth.image = self.castleHealth.emotions['castle32']
                elif self.castleHealth.hp <= 310 and self.castleHealth.hp > 300:
                    self.castleHealth.image = self.castleHealth.emotions['castle31']
                elif self.castleHealth.hp <= 300 and self.castleHealth.hp > 290:
                    self.castleHealth.image = self.castleHealth.emotions['castle30']
                elif self.castleHealth.hp <= 290 and self.castleHealth.hp > 280:
                    self.castleHealth.image = self.castleHealth.emotions['castle29']
                elif self.castleHealth.hp <= 280 and self.castleHealth.hp > 270:
                    self.castleHealth.image = self.castleHealth.emotions['castle28']
                elif self.castleHealth.hp <= 270 and self.castleHealth.hp > 260:
                    self.castleHealth.image = self.castleHealth.emotions['castle27']
                elif self.castleHealth.hp <= 260 and self.castleHealth.hp > 250:
                    self.castleHealth.image = self.castleHealth.emotions['castle26']
                elif self.castleHealth.hp <= 250 and self.castleHealth.hp > 240:
                    self.castleHealth.image = self.castleHealth.emotions['castle25']
                elif self.castleHealth.hp <= 240 and self.castleHealth.hp > 230:
                    self.castleHealth.image = self.castleHealth.emotions['castle24']
                elif self.castleHealth.hp <= 230 and self.castleHealth.hp > 220:
                    self.castleHealth.image = self.castleHealth.emotions['castle23']
                elif self.castleHealth.hp <= 220 and self.castleHealth.hp > 210:
                    self.castleHealth.image = self.castleHealth.emotions['castle22']
                elif self.castleHealth.hp <= 210 and self.castleHealth.hp > 200:
                    self.castleHealth.image = self.castleHealth.emotions['castle21']
                elif self.castleHealth.hp <= 200 and self.castleHealth.hp > 190:
                    self.castleHealth.image = self.castleHealth.emotions['castle20']
                elif self.castleHealth.hp <= 190 and self.castleHealth.hp > 180:
                    self.castleHealth.image = self.castleHealth.emotions['castle19']
                elif self.castleHealth.hp <= 180 and self.castleHealth.hp > 170:
                    self.castleHealth.image = self.castleHealth.emotions['castle18']
                elif self.castleHealth.hp <= 170 and self.castleHealth.hp > 160:
                    self.castleHealth.image = self.castleHealth.emotions['castle17']
                elif self.castleHealth.hp <= 160 and self.castleHealth.hp > 150:
                    self.castleHealth.image = self.castleHealth.emotions['castle16']
                elif self.castleHealth.hp <= 150 and self.castleHealth.hp > 140:
                    self.castleHealth.image = self.castleHealth.emotions['castle15']
                elif self.castleHealth.hp <= 140 and self.castleHealth.hp > 130:
                    self.castleHealth.image = self.castleHealth.emotions['castle14']
                elif self.castleHealth.hp <= 130 and self.castleHealth.hp > 120:
                    self.castleHealth.image = self.castleHealth.emotions['castle13']
                elif self.castleHealth.hp <= 120 and self.castleHealth.hp > 110:
                    self.castleHealth.image = self.castleHealth.emotions['castle12']
                elif self.castleHealth.hp <= 110 and self.castleHealth.hp > 100:
                    self.castleHealth.image = self.castleHealth.emotions['castle11']
                elif self.castleHealth.hp <= 100 and self.castleHealth.hp > 90:
                    self.castleHealth.image = self.castleHealth.emotions['castle10']
                elif self.castleHealth.hp <= 90 and self.castleHealth.hp > 80:
                    self.castleHealth.image = self.castleHealth.emotions['castle9']
                elif self.castleHealth.hp <= 80 and self.castleHealth.hp > 70:
                    self.castleHealth.image = self.castleHealth.emotions['castle8']
                elif self.castleHealth.hp <= 70 and self.castleHealth.hp > 60:
                    self.castleHealth.image = self.castleHealth.emotions['castle7']
                elif self.castleHealth.hp <= 60 and self.castleHealth.hp > 50:
                    self.castleHealth.image = self.castleHealth.emotions['castle6']
                elif self.castleHealth.hp <= 50 and self.castleHealth.hp > 40:
                    self.castleHealth.image = self.castleHealth.emotions['castle5']
                elif self.castleHealth.hp <= 40 and self.castleHealth.hp > 30:
                    self.castleHealth.image = self.castleHealth.emotions['castle4']
                elif self.castleHealth.hp <= 30 and self.castleHealth.hp > 20:
                    self.castleHealth.image = self.castleHealth.emotions['castle3']
                elif self.castleHealth.hp <= 20 and self.castleHealth.hp > 10:
                    self.castleHealth.image = self.castleHealth.emotions['castle2']
                elif self.castleHealth.hp <= 10 and self.castleHealth.hp > 0:
                    self.castleHealth.image = self.castleHealth.emotions['castle1']

        for i in self.enemy3L:       
            if i.AtkUser == True:
                self.castleHealth.hp -= 0.03
                if self.castleHealth.hp <= 990 and self.castleHealth.hp > 980:
                    self.castleHealth.image = self.castleHealth.emotions['castle99']
                elif self.castleHealth.hp <= 980 and self.castleHealth.hp > 970:
                    self.castleHealth.image = self.castleHealth.emotions['castle98']
                elif self.castleHealth.hp <= 970 and self.castleHealth.hp > 960:
                    self.castleHealth.image = self.castleHealth.emotions['castle97']
                elif self.castleHealth.hp <= 960 and self.castleHealth.hp > 950:
                    self.castleHealth.image = self.castleHealth.emotions['castle96']
                elif self.castleHealth.hp <= 950 and self.castleHealth.hp > 940:
                    self.castleHealth.image = self.castleHealth.emotions['castle95']
                elif self.castleHealth.hp <= 940 and self.castleHealth.hp > 930:
                    self.castleHealth.image = self.castleHealth.emotions['castle94']
                elif self.castleHealth.hp <= 930 and self.castleHealth.hp > 920:
                    self.castleHealth.image = self.castleHealth.emotions['castle93']
                elif self.castleHealth.hp <= 920 and self.castleHealth.hp > 910:
                    self.castleHealth.image = self.castleHealth.emotions['castle92']
                elif self.castleHealth.hp <= 910 and self.castleHealth.hp > 900:
                    self.castleHealth.image = self.castleHealth.emotions['castle91']
                elif self.castleHealth.hp <= 900 and self.castleHealth.hp > 890:
                    self.castleHealth.image = self.castleHealth.emotions['castle90']
                elif self.castleHealth.hp <= 890 and self.castleHealth.hp > 880:
                    self.castleHealth.image = self.castleHealth.emotions['castle89']
                elif self.castleHealth.hp <= 880 and self.castleHealth.hp > 870:
                    self.castleHealth.image = self.castleHealth.emotions['castle88']
                elif self.castleHealth.hp <= 870 and self.castleHealth.hp > 860:
                    self.castleHealth.image = self.castleHealth.emotions['castle87']
                elif self.castleHealth.hp <= 860 and self.castleHealth.hp > 850:
                    self.castleHealth.image = self.castleHealth.emotions['castle86']
                elif self.castleHealth.hp <= 850 and self.castleHealth.hp > 840:
                    self.castleHealth.image = self.castleHealth.emotions['castle85']
                elif self.castleHealth.hp <= 840 and self.castleHealth.hp > 830:
                    self.castleHealth.image = self.castleHealth.emotions['castle84']
                elif self.castleHealth.hp <= 830 and self.castleHealth.hp > 820:
                    self.castleHealth.image = self.castleHealth.emotions['castle83']
                elif self.castleHealth.hp <= 820 and self.castleHealth.hp > 810:
                    self.castleHealth.image = self.castleHealth.emotions['castle82']
                elif self.castleHealth.hp <= 810 and self.castleHealth.hp > 800:
                    self.castleHealth.image = self.castleHealth.emotions['castle81']
                elif self.castleHealth.hp <= 800 and self.castleHealth.hp > 790:
                    self.castleHealth.image = self.castleHealth.emotions['castle80']
                elif self.castleHealth.hp <= 790 and self.castleHealth.hp > 780:
                    self.castleHealth.image = self.castleHealth.emotions['castle79']
                elif self.castleHealth.hp <= 780 and self.castleHealth.hp > 770:
                    self.castleHealth.image = self.castleHealth.emotions['castle78']
                elif self.castleHealth.hp <= 770 and self.castleHealth.hp > 760:
                    self.castleHealth.image = self.castleHealth.emotions['castle77']
                elif self.castleHealth.hp <= 760 and self.castleHealth.hp > 750:
                    self.castleHealth.image = self.castleHealth.emotions['castle76']
                elif self.castleHealth.hp <= 750 and self.castleHealth.hp > 740:
                    self.castleHealth.image = self.castleHealth.emotions['castle75']
                elif self.castleHealth.hp <= 740 and self.castleHealth.hp > 730:
                    self.castleHealth.image = self.castleHealth.emotions['castle74']
                elif self.castleHealth.hp <= 730 and self.castleHealth.hp > 720:
                    self.castleHealth.image = self.castleHealth.emotions['castle73']
                elif self.castleHealth.hp <= 720 and self.castleHealth.hp > 710:
                    self.castleHealth.image = self.castleHealth.emotions['castle72']
                elif self.castleHealth.hp <= 710 and self.castleHealth.hp > 700:
                    self.castleHealth.image = self.castleHealth.emotions['castle71']
                elif self.castleHealth.hp <= 700 and self.castleHealth.hp > 690:
                    self.castleHealth.image = self.castleHealth.emotions['castle70']
                elif self.castleHealth.hp <= 690 and self.castleHealth.hp > 680:
                    self.castleHealth.image = self.castleHealth.emotions['castle69']
                elif self.castleHealth.hp <= 680 and self.castleHealth.hp > 670:
                    self.castleHealth.image = self.castleHealth.emotions['castle68']
                elif self.castleHealth.hp <= 670 and self.castleHealth.hp > 660:
                    self.castleHealth.image = self.castleHealth.emotions['castle67']
                elif self.castleHealth.hp <= 660 and self.castleHealth.hp > 650:
                    self.castleHealth.image = self.castleHealth.emotions['castle66']
                elif self.castleHealth.hp <= 650 and self.castleHealth.hp > 640:
                    self.castleHealth.image = self.castleHealth.emotions['castle65']
                elif self.castleHealth.hp <= 640 and self.castleHealth.hp > 630:
                    self.castleHealth.image = self.castleHealth.emotions['castle64']
                elif self.castleHealth.hp <= 630 and self.castleHealth.hp > 620:
                    self.castleHealth.image = self.castleHealth.emotions['castle63']
                elif self.castleHealth.hp <= 620 and self.castleHealth.hp > 610:
                    self.castleHealth.image = self.castleHealth.emotions['castle62']
                elif self.castleHealth.hp <= 610 and self.castleHealth.hp > 600:
                    self.castleHealth.image = self.castleHealth.emotions['castle61']
                elif self.castleHealth.hp <= 600 and self.castleHealth.hp > 590:
                    self.castleHealth.image = self.castleHealth.emotions['castle60']
                elif self.castleHealth.hp <= 590 and self.castleHealth.hp > 580:
                    self.castleHealth.image = self.castleHealth.emotions['castle59']
                elif self.castleHealth.hp <= 580 and self.castleHealth.hp > 570:
                    self.castleHealth.image = self.castleHealth.emotions['castle58']
                elif self.castleHealth.hp <= 570 and self.castleHealth.hp > 560:
                    self.castleHealth.image = self.castleHealth.emotions['castle57']
                elif self.castleHealth.hp <= 560 and self.castleHealth.hp > 550:
                    self.castleHealth.image = self.castleHealth.emotions['castle56']
                elif self.castleHealth.hp <= 550 and self.castleHealth.hp > 540:
                    self.castleHealth.image = self.castleHealth.emotions['castle55']
                elif self.castleHealth.hp <= 540 and self.castleHealth.hp > 530:
                    self.castleHealth.image = self.castleHealth.emotions['castle54']
                elif self.castleHealth.hp <= 530 and self.castleHealth.hp > 520:
                    self.castleHealth.image = self.castleHealth.emotions['castle53']
                elif self.castleHealth.hp <= 520 and self.castleHealth.hp > 510:
                    self.castleHealth.image = self.castleHealth.emotions['castle52']
                elif self.castleHealth.hp <= 510 and self.castleHealth.hp > 500:
                    self.castleHealth.image = self.castleHealth.emotions['castle51']
                elif self.castleHealth.hp <= 500 and self.castleHealth.hp > 490:
                    self.castleHealth.image = self.castleHealth.emotions['castle50']
                elif self.castleHealth.hp <= 490 and self.castleHealth.hp > 480:
                    self.castleHealth.image = self.castleHealth.emotions['castle49']
                elif self.castleHealth.hp <= 480 and self.castleHealth.hp > 470:
                    self.castleHealth.image = self.castleHealth.emotions['castle48']
                elif self.castleHealth.hp <= 470 and self.castleHealth.hp > 460:
                    self.castleHealth.image = self.castleHealth.emotions['castle47']
                elif self.castleHealth.hp <= 460 and self.castleHealth.hp > 450:
                    self.castleHealth.image = self.castleHealth.emotions['castle46']
                elif self.castleHealth.hp <= 450 and self.castleHealth.hp > 440:
                    self.castleHealth.image = self.castleHealth.emotions['castle45']
                elif self.castleHealth.hp <= 440 and self.castleHealth.hp > 430:
                    self.castleHealth.image = self.castleHealth.emotions['castle44']
                elif self.castleHealth.hp <= 430 and self.castleHealth.hp > 420:
                    self.castleHealth.image = self.castleHealth.emotions['castle43']
                elif self.castleHealth.hp <= 420 and self.castleHealth.hp > 410:
                    self.castleHealth.image = self.castleHealth.emotions['castle42']
                elif self.castleHealth.hp <= 410 and self.castleHealth.hp > 400:
                    self.castleHealth.image = self.castleHealth.emotions['castle41']
                elif self.castleHealth.hp <= 400 and self.castleHealth.hp > 390:
                    self.castleHealth.image = self.castleHealth.emotions['castle40']
                elif self.castleHealth.hp <= 390 and self.castleHealth.hp > 380:
                    self.castleHealth.image = self.castleHealth.emotions['castle39']
                elif self.castleHealth.hp <= 380 and self.castleHealth.hp > 370:
                    self.castleHealth.image = self.castleHealth.emotions['castle38']
                elif self.castleHealth.hp <= 370 and self.castleHealth.hp > 360:
                    self.castleHealth.image = self.castleHealth.emotions['castle37']
                elif self.castleHealth.hp <= 360 and self.castleHealth.hp > 350:
                    self.castleHealth.image = self.castleHealth.emotions['castle36']
                elif self.castleHealth.hp <= 350 and self.castleHealth.hp > 340:
                    self.castleHealth.image = self.castleHealth.emotions['castle35']
                elif self.castleHealth.hp <= 340 and self.castleHealth.hp > 330:
                    self.castleHealth.image = self.castleHealth.emotions['castle34']
                elif self.castleHealth.hp <= 330 and self.castleHealth.hp > 320:
                    self.castleHealth.image = self.castleHealth.emotions['castle33']
                elif self.castleHealth.hp <= 320 and self.castleHealth.hp > 310:
                    self.castleHealth.image = self.castleHealth.emotions['castle32']
                elif self.castleHealth.hp <= 310 and self.castleHealth.hp > 300:
                    self.castleHealth.image = self.castleHealth.emotions['castle31']
                elif self.castleHealth.hp <= 300 and self.castleHealth.hp > 290:
                    self.castleHealth.image = self.castleHealth.emotions['castle30']
                elif self.castleHealth.hp <= 290 and self.castleHealth.hp > 280:
                    self.castleHealth.image = self.castleHealth.emotions['castle29']
                elif self.castleHealth.hp <= 280 and self.castleHealth.hp > 270:
                    self.castleHealth.image = self.castleHealth.emotions['castle28']
                elif self.castleHealth.hp <= 270 and self.castleHealth.hp > 260:
                    self.castleHealth.image = self.castleHealth.emotions['castle27']
                elif self.castleHealth.hp <= 260 and self.castleHealth.hp > 250:
                    self.castleHealth.image = self.castleHealth.emotions['castle26']
                elif self.castleHealth.hp <= 250 and self.castleHealth.hp > 240:
                    self.castleHealth.image = self.castleHealth.emotions['castle25']
                elif self.castleHealth.hp <= 240 and self.castleHealth.hp > 230:
                    self.castleHealth.image = self.castleHealth.emotions['castle24']
                elif self.castleHealth.hp <= 230 and self.castleHealth.hp > 220:
                    self.castleHealth.image = self.castleHealth.emotions['castle23']
                elif self.castleHealth.hp <= 220 and self.castleHealth.hp > 210:
                    self.castleHealth.image = self.castleHealth.emotions['castle22']
                elif self.castleHealth.hp <= 210 and self.castleHealth.hp > 200:
                    self.castleHealth.image = self.castleHealth.emotions['castle21']
                elif self.castleHealth.hp <= 200 and self.castleHealth.hp > 190:
                    self.castleHealth.image = self.castleHealth.emotions['castle20']
                elif self.castleHealth.hp <= 190 and self.castleHealth.hp > 180:
                    self.castleHealth.image = self.castleHealth.emotions['castle19']
                elif self.castleHealth.hp <= 180 and self.castleHealth.hp > 170:
                    self.castleHealth.image = self.castleHealth.emotions['castle18']
                elif self.castleHealth.hp <= 170 and self.castleHealth.hp > 160:
                    self.castleHealth.image = self.castleHealth.emotions['castle17']
                elif self.castleHealth.hp <= 160 and self.castleHealth.hp > 150:
                    self.castleHealth.image = self.castleHealth.emotions['castle16']
                elif self.castleHealth.hp <= 150 and self.castleHealth.hp > 140:
                    self.castleHealth.image = self.castleHealth.emotions['castle15']
                elif self.castleHealth.hp <= 140 and self.castleHealth.hp > 130:
                    self.castleHealth.image = self.castleHealth.emotions['castle14']
                elif self.castleHealth.hp <= 130 and self.castleHealth.hp > 120:
                    self.castleHealth.image = self.castleHealth.emotions['castle13']
                elif self.castleHealth.hp <= 120 and self.castleHealth.hp > 110:
                    self.castleHealth.image = self.castleHealth.emotions['castle12']
                elif self.castleHealth.hp <= 110 and self.castleHealth.hp > 100:
                    self.castleHealth.image = self.castleHealth.emotions['castle11']
                elif self.castleHealth.hp <= 100 and self.castleHealth.hp > 90:
                    self.castleHealth.image = self.castleHealth.emotions['castle10']
                elif self.castleHealth.hp <= 90 and self.castleHealth.hp > 80:
                    self.castleHealth.image = self.castleHealth.emotions['castle9']
                elif self.castleHealth.hp <= 80 and self.castleHealth.hp > 70:
                    self.castleHealth.image = self.castleHealth.emotions['castle8']
                elif self.castleHealth.hp <= 70 and self.castleHealth.hp > 60:
                    self.castleHealth.image = self.castleHealth.emotions['castle7']
                elif self.castleHealth.hp <= 60 and self.castleHealth.hp > 50:
                    self.castleHealth.image = self.castleHealth.emotions['castle6']
                elif self.castleHealth.hp <= 50 and self.castleHealth.hp > 40:
                    self.castleHealth.image = self.castleHealth.emotions['castle5']
                elif self.castleHealth.hp <= 40 and self.castleHealth.hp > 30:
                    self.castleHealth.image = self.castleHealth.emotions['castle4']
                elif self.castleHealth.hp <= 30 and self.castleHealth.hp > 20:
                    self.castleHealth.image = self.castleHealth.emotions['castle3']
                elif self.castleHealth.hp <= 20 and self.castleHealth.hp > 10:
                    self.castleHealth.image = self.castleHealth.emotions['castle2']
                elif self.castleHealth.hp <= 10 and self.castleHealth.hp > 0:
                    self.castleHealth.image = self.castleHealth.emotions['castle1']

        for i in self.enemy3R:       
            if i.AtkUser == True:
                self.castleHealth.hp -= 0.03
                if self.castleHealth.hp <= 990 and self.castleHealth.hp > 980:
                    self.castleHealth.image = self.castleHealth.emotions['castle99']
                elif self.castleHealth.hp <= 980 and self.castleHealth.hp > 970:
                    self.castleHealth.image = self.castleHealth.emotions['castle98']
                elif self.castleHealth.hp <= 970 and self.castleHealth.hp > 960:
                    self.castleHealth.image = self.castleHealth.emotions['castle97']
                elif self.castleHealth.hp <= 960 and self.castleHealth.hp > 950:
                    self.castleHealth.image = self.castleHealth.emotions['castle96']
                elif self.castleHealth.hp <= 950 and self.castleHealth.hp > 940:
                    self.castleHealth.image = self.castleHealth.emotions['castle95']
                elif self.castleHealth.hp <= 940 and self.castleHealth.hp > 930:
                    self.castleHealth.image = self.castleHealth.emotions['castle94']
                elif self.castleHealth.hp <= 930 and self.castleHealth.hp > 920:
                    self.castleHealth.image = self.castleHealth.emotions['castle93']
                elif self.castleHealth.hp <= 920 and self.castleHealth.hp > 910:
                    self.castleHealth.image = self.castleHealth.emotions['castle92']
                elif self.castleHealth.hp <= 910 and self.castleHealth.hp > 900:
                    self.castleHealth.image = self.castleHealth.emotions['castle91']
                elif self.castleHealth.hp <= 900 and self.castleHealth.hp > 890:
                    self.castleHealth.image = self.castleHealth.emotions['castle90']
                elif self.castleHealth.hp <= 890 and self.castleHealth.hp > 880:
                    self.castleHealth.image = self.castleHealth.emotions['castle89']
                elif self.castleHealth.hp <= 880 and self.castleHealth.hp > 870:
                    self.castleHealth.image = self.castleHealth.emotions['castle88']
                elif self.castleHealth.hp <= 870 and self.castleHealth.hp > 860:
                    self.castleHealth.image = self.castleHealth.emotions['castle87']
                elif self.castleHealth.hp <= 860 and self.castleHealth.hp > 850:
                    self.castleHealth.image = self.castleHealth.emotions['castle86']
                elif self.castleHealth.hp <= 850 and self.castleHealth.hp > 840:
                    self.castleHealth.image = self.castleHealth.emotions['castle85']
                elif self.castleHealth.hp <= 840 and self.castleHealth.hp > 830:
                    self.castleHealth.image = self.castleHealth.emotions['castle84']
                elif self.castleHealth.hp <= 830 and self.castleHealth.hp > 820:
                    self.castleHealth.image = self.castleHealth.emotions['castle83']
                elif self.castleHealth.hp <= 820 and self.castleHealth.hp > 810:
                    self.castleHealth.image = self.castleHealth.emotions['castle82']
                elif self.castleHealth.hp <= 810 and self.castleHealth.hp > 800:
                    self.castleHealth.image = self.castleHealth.emotions['castle81']
                elif self.castleHealth.hp <= 800 and self.castleHealth.hp > 790:
                    self.castleHealth.image = self.castleHealth.emotions['castle80']
                elif self.castleHealth.hp <= 790 and self.castleHealth.hp > 780:
                    self.castleHealth.image = self.castleHealth.emotions['castle79']
                elif self.castleHealth.hp <= 780 and self.castleHealth.hp > 770:
                    self.castleHealth.image = self.castleHealth.emotions['castle78']
                elif self.castleHealth.hp <= 770 and self.castleHealth.hp > 760:
                    self.castleHealth.image = self.castleHealth.emotions['castle77']
                elif self.castleHealth.hp <= 760 and self.castleHealth.hp > 750:
                    self.castleHealth.image = self.castleHealth.emotions['castle76']
                elif self.castleHealth.hp <= 750 and self.castleHealth.hp > 740:
                    self.castleHealth.image = self.castleHealth.emotions['castle75']
                elif self.castleHealth.hp <= 740 and self.castleHealth.hp > 730:
                    self.castleHealth.image = self.castleHealth.emotions['castle74']
                elif self.castleHealth.hp <= 730 and self.castleHealth.hp > 720:
                    self.castleHealth.image = self.castleHealth.emotions['castle73']
                elif self.castleHealth.hp <= 720 and self.castleHealth.hp > 710:
                    self.castleHealth.image = self.castleHealth.emotions['castle72']
                elif self.castleHealth.hp <= 710 and self.castleHealth.hp > 700:
                    self.castleHealth.image = self.castleHealth.emotions['castle71']
                elif self.castleHealth.hp <= 700 and self.castleHealth.hp > 690:
                    self.castleHealth.image = self.castleHealth.emotions['castle70']
                elif self.castleHealth.hp <= 690 and self.castleHealth.hp > 680:
                    self.castleHealth.image = self.castleHealth.emotions['castle69']
                elif self.castleHealth.hp <= 680 and self.castleHealth.hp > 670:
                    self.castleHealth.image = self.castleHealth.emotions['castle68']
                elif self.castleHealth.hp <= 670 and self.castleHealth.hp > 660:
                    self.castleHealth.image = self.castleHealth.emotions['castle67']
                elif self.castleHealth.hp <= 660 and self.castleHealth.hp > 650:
                    self.castleHealth.image = self.castleHealth.emotions['castle66']
                elif self.castleHealth.hp <= 650 and self.castleHealth.hp > 640:
                    self.castleHealth.image = self.castleHealth.emotions['castle65']
                elif self.castleHealth.hp <= 640 and self.castleHealth.hp > 630:
                    self.castleHealth.image = self.castleHealth.emotions['castle64']
                elif self.castleHealth.hp <= 630 and self.castleHealth.hp > 620:
                    self.castleHealth.image = self.castleHealth.emotions['castle63']
                elif self.castleHealth.hp <= 620 and self.castleHealth.hp > 610:
                    self.castleHealth.image = self.castleHealth.emotions['castle62']
                elif self.castleHealth.hp <= 610 and self.castleHealth.hp > 600:
                    self.castleHealth.image = self.castleHealth.emotions['castle61']
                elif self.castleHealth.hp <= 600 and self.castleHealth.hp > 590:
                    self.castleHealth.image = self.castleHealth.emotions['castle60']
                elif self.castleHealth.hp <= 590 and self.castleHealth.hp > 580:
                    self.castleHealth.image = self.castleHealth.emotions['castle59']
                elif self.castleHealth.hp <= 580 and self.castleHealth.hp > 570:
                    self.castleHealth.image = self.castleHealth.emotions['castle58']
                elif self.castleHealth.hp <= 570 and self.castleHealth.hp > 560:
                    self.castleHealth.image = self.castleHealth.emotions['castle57']
                elif self.castleHealth.hp <= 560 and self.castleHealth.hp > 550:
                    self.castleHealth.image = self.castleHealth.emotions['castle56']
                elif self.castleHealth.hp <= 550 and self.castleHealth.hp > 540:
                    self.castleHealth.image = self.castleHealth.emotions['castle55']
                elif self.castleHealth.hp <= 540 and self.castleHealth.hp > 530:
                    self.castleHealth.image = self.castleHealth.emotions['castle54']
                elif self.castleHealth.hp <= 530 and self.castleHealth.hp > 520:
                    self.castleHealth.image = self.castleHealth.emotions['castle53']
                elif self.castleHealth.hp <= 520 and self.castleHealth.hp > 510:
                    self.castleHealth.image = self.castleHealth.emotions['castle52']
                elif self.castleHealth.hp <= 510 and self.castleHealth.hp > 500:
                    self.castleHealth.image = self.castleHealth.emotions['castle51']
                elif self.castleHealth.hp <= 500 and self.castleHealth.hp > 490:
                    self.castleHealth.image = self.castleHealth.emotions['castle50']
                elif self.castleHealth.hp <= 490 and self.castleHealth.hp > 480:
                    self.castleHealth.image = self.castleHealth.emotions['castle49']
                elif self.castleHealth.hp <= 480 and self.castleHealth.hp > 470:
                    self.castleHealth.image = self.castleHealth.emotions['castle48']
                elif self.castleHealth.hp <= 470 and self.castleHealth.hp > 460:
                    self.castleHealth.image = self.castleHealth.emotions['castle47']
                elif self.castleHealth.hp <= 460 and self.castleHealth.hp > 450:
                    self.castleHealth.image = self.castleHealth.emotions['castle46']
                elif self.castleHealth.hp <= 450 and self.castleHealth.hp > 440:
                    self.castleHealth.image = self.castleHealth.emotions['castle45']
                elif self.castleHealth.hp <= 440 and self.castleHealth.hp > 430:
                    self.castleHealth.image = self.castleHealth.emotions['castle44']
                elif self.castleHealth.hp <= 430 and self.castleHealth.hp > 420:
                    self.castleHealth.image = self.castleHealth.emotions['castle43']
                elif self.castleHealth.hp <= 420 and self.castleHealth.hp > 410:
                    self.castleHealth.image = self.castleHealth.emotions['castle42']
                elif self.castleHealth.hp <= 410 and self.castleHealth.hp > 400:
                    self.castleHealth.image = self.castleHealth.emotions['castle41']
                elif self.castleHealth.hp <= 400 and self.castleHealth.hp > 390:
                    self.castleHealth.image = self.castleHealth.emotions['castle40']
                elif self.castleHealth.hp <= 390 and self.castleHealth.hp > 380:
                    self.castleHealth.image = self.castleHealth.emotions['castle39']
                elif self.castleHealth.hp <= 380 and self.castleHealth.hp > 370:
                    self.castleHealth.image = self.castleHealth.emotions['castle38']
                elif self.castleHealth.hp <= 370 and self.castleHealth.hp > 360:
                    self.castleHealth.image = self.castleHealth.emotions['castle37']
                elif self.castleHealth.hp <= 360 and self.castleHealth.hp > 350:
                    self.castleHealth.image = self.castleHealth.emotions['castle36']
                elif self.castleHealth.hp <= 350 and self.castleHealth.hp > 340:
                    self.castleHealth.image = self.castleHealth.emotions['castle35']
                elif self.castleHealth.hp <= 340 and self.castleHealth.hp > 330:
                    self.castleHealth.image = self.castleHealth.emotions['castle34']
                elif self.castleHealth.hp <= 330 and self.castleHealth.hp > 320:
                    self.castleHealth.image = self.castleHealth.emotions['castle33']
                elif self.castleHealth.hp <= 320 and self.castleHealth.hp > 310:
                    self.castleHealth.image = self.castleHealth.emotions['castle32']
                elif self.castleHealth.hp <= 310 and self.castleHealth.hp > 300:
                    self.castleHealth.image = self.castleHealth.emotions['castle31']
                elif self.castleHealth.hp <= 300 and self.castleHealth.hp > 290:
                    self.castleHealth.image = self.castleHealth.emotions['castle30']
                elif self.castleHealth.hp <= 290 and self.castleHealth.hp > 280:
                    self.castleHealth.image = self.castleHealth.emotions['castle29']
                elif self.castleHealth.hp <= 280 and self.castleHealth.hp > 270:
                    self.castleHealth.image = self.castleHealth.emotions['castle28']
                elif self.castleHealth.hp <= 270 and self.castleHealth.hp > 260:
                    self.castleHealth.image = self.castleHealth.emotions['castle27']
                elif self.castleHealth.hp <= 260 and self.castleHealth.hp > 250:
                    self.castleHealth.image = self.castleHealth.emotions['castle26']
                elif self.castleHealth.hp <= 250 and self.castleHealth.hp > 240:
                    self.castleHealth.image = self.castleHealth.emotions['castle25']
                elif self.castleHealth.hp <= 240 and self.castleHealth.hp > 230:
                    self.castleHealth.image = self.castleHealth.emotions['castle24']
                elif self.castleHealth.hp <= 230 and self.castleHealth.hp > 220:
                    self.castleHealth.image = self.castleHealth.emotions['castle23']
                elif self.castleHealth.hp <= 220 and self.castleHealth.hp > 210:
                    self.castleHealth.image = self.castleHealth.emotions['castle22']
                elif self.castleHealth.hp <= 210 and self.castleHealth.hp > 200:
                    self.castleHealth.image = self.castleHealth.emotions['castle21']
                elif self.castleHealth.hp <= 200 and self.castleHealth.hp > 190:
                    self.castleHealth.image = self.castleHealth.emotions['castle20']
                elif self.castleHealth.hp <= 190 and self.castleHealth.hp > 180:
                    self.castleHealth.image = self.castleHealth.emotions['castle19']
                elif self.castleHealth.hp <= 180 and self.castleHealth.hp > 170:
                    self.castleHealth.image = self.castleHealth.emotions['castle18']
                elif self.castleHealth.hp <= 170 and self.castleHealth.hp > 160:
                    self.castleHealth.image = self.castleHealth.emotions['castle17']
                elif self.castleHealth.hp <= 160 and self.castleHealth.hp > 150:
                    self.castleHealth.image = self.castleHealth.emotions['castle16']
                elif self.castleHealth.hp <= 150 and self.castleHealth.hp > 140:
                    self.castleHealth.image = self.castleHealth.emotions['castle15']
                elif self.castleHealth.hp <= 140 and self.castleHealth.hp > 130:
                    self.castleHealth.image = self.castleHealth.emotions['castle14']
                elif self.castleHealth.hp <= 130 and self.castleHealth.hp > 120:
                    self.castleHealth.image = self.castleHealth.emotions['castle13']
                elif self.castleHealth.hp <= 120 and self.castleHealth.hp > 110:
                    self.castleHealth.image = self.castleHealth.emotions['castle12']
                elif self.castleHealth.hp <= 110 and self.castleHealth.hp > 100:
                    self.castleHealth.image = self.castleHealth.emotions['castle11']
                elif self.castleHealth.hp <= 100 and self.castleHealth.hp > 90:
                    self.castleHealth.image = self.castleHealth.emotions['castle10']
                elif self.castleHealth.hp <= 90 and self.castleHealth.hp > 80:
                    self.castleHealth.image = self.castleHealth.emotions['castle9']
                elif self.castleHealth.hp <= 80 and self.castleHealth.hp > 70:
                    self.castleHealth.image = self.castleHealth.emotions['castle8']
                elif self.castleHealth.hp <= 70 and self.castleHealth.hp > 60:
                    self.castleHealth.image = self.castleHealth.emotions['castle7']
                elif self.castleHealth.hp <= 60 and self.castleHealth.hp > 50:
                    self.castleHealth.image = self.castleHealth.emotions['castle6']
                elif self.castleHealth.hp <= 50 and self.castleHealth.hp > 40:
                    self.castleHealth.image = self.castleHealth.emotions['castle5']
                elif self.castleHealth.hp <= 40 and self.castleHealth.hp > 30:
                    self.castleHealth.image = self.castleHealth.emotions['castle4']
                elif self.castleHealth.hp <= 30 and self.castleHealth.hp > 20:
                    self.castleHealth.image = self.castleHealth.emotions['castle3']
                elif self.castleHealth.hp <= 20 and self.castleHealth.hp > 10:
                    self.castleHealth.image = self.castleHealth.emotions['castle2']
                elif self.castleHealth.hp <= 10 and self.castleHealth.hp > 0:
                    self.castleHealth.image = self.castleHealth.emotions['castle1']

        for i in self.enemy4L:       
            if i.AtkUser == True:
                self.castleHealth.hp -= 0.04
                if self.castleHealth.hp <= 990 and self.castleHealth.hp > 980:
                    self.castleHealth.image = self.castleHealth.emotions['castle99']
                elif self.castleHealth.hp <= 980 and self.castleHealth.hp > 970:
                    self.castleHealth.image = self.castleHealth.emotions['castle98']
                elif self.castleHealth.hp <= 970 and self.castleHealth.hp > 960:
                    self.castleHealth.image = self.castleHealth.emotions['castle97']
                elif self.castleHealth.hp <= 960 and self.castleHealth.hp > 950:
                    self.castleHealth.image = self.castleHealth.emotions['castle96']
                elif self.castleHealth.hp <= 950 and self.castleHealth.hp > 940:
                    self.castleHealth.image = self.castleHealth.emotions['castle95']
                elif self.castleHealth.hp <= 940 and self.castleHealth.hp > 930:
                    self.castleHealth.image = self.castleHealth.emotions['castle94']
                elif self.castleHealth.hp <= 930 and self.castleHealth.hp > 920:
                    self.castleHealth.image = self.castleHealth.emotions['castle93']
                elif self.castleHealth.hp <= 920 and self.castleHealth.hp > 910:
                    self.castleHealth.image = self.castleHealth.emotions['castle92']
                elif self.castleHealth.hp <= 910 and self.castleHealth.hp > 900:
                    self.castleHealth.image = self.castleHealth.emotions['castle91']
                elif self.castleHealth.hp <= 900 and self.castleHealth.hp > 890:
                    self.castleHealth.image = self.castleHealth.emotions['castle90']
                elif self.castleHealth.hp <= 890 and self.castleHealth.hp > 880:
                    self.castleHealth.image = self.castleHealth.emotions['castle89']
                elif self.castleHealth.hp <= 880 and self.castleHealth.hp > 870:
                    self.castleHealth.image = self.castleHealth.emotions['castle88']
                elif self.castleHealth.hp <= 870 and self.castleHealth.hp > 860:
                    self.castleHealth.image = self.castleHealth.emotions['castle87']
                elif self.castleHealth.hp <= 860 and self.castleHealth.hp > 850:
                    self.castleHealth.image = self.castleHealth.emotions['castle86']
                elif self.castleHealth.hp <= 850 and self.castleHealth.hp > 840:
                    self.castleHealth.image = self.castleHealth.emotions['castle85']
                elif self.castleHealth.hp <= 840 and self.castleHealth.hp > 830:
                    self.castleHealth.image = self.castleHealth.emotions['castle84']
                elif self.castleHealth.hp <= 830 and self.castleHealth.hp > 820:
                    self.castleHealth.image = self.castleHealth.emotions['castle83']
                elif self.castleHealth.hp <= 820 and self.castleHealth.hp > 810:
                    self.castleHealth.image = self.castleHealth.emotions['castle82']
                elif self.castleHealth.hp <= 810 and self.castleHealth.hp > 800:
                    self.castleHealth.image = self.castleHealth.emotions['castle81']
                elif self.castleHealth.hp <= 800 and self.castleHealth.hp > 790:
                    self.castleHealth.image = self.castleHealth.emotions['castle80']
                elif self.castleHealth.hp <= 790 and self.castleHealth.hp > 780:
                    self.castleHealth.image = self.castleHealth.emotions['castle79']
                elif self.castleHealth.hp <= 780 and self.castleHealth.hp > 770:
                    self.castleHealth.image = self.castleHealth.emotions['castle78']
                elif self.castleHealth.hp <= 770 and self.castleHealth.hp > 760:
                    self.castleHealth.image = self.castleHealth.emotions['castle77']
                elif self.castleHealth.hp <= 760 and self.castleHealth.hp > 750:
                    self.castleHealth.image = self.castleHealth.emotions['castle76']
                elif self.castleHealth.hp <= 750 and self.castleHealth.hp > 740:
                    self.castleHealth.image = self.castleHealth.emotions['castle75']
                elif self.castleHealth.hp <= 740 and self.castleHealth.hp > 730:
                    self.castleHealth.image = self.castleHealth.emotions['castle74']
                elif self.castleHealth.hp <= 730 and self.castleHealth.hp > 720:
                    self.castleHealth.image = self.castleHealth.emotions['castle73']
                elif self.castleHealth.hp <= 720 and self.castleHealth.hp > 710:
                    self.castleHealth.image = self.castleHealth.emotions['castle72']
                elif self.castleHealth.hp <= 710 and self.castleHealth.hp > 700:
                    self.castleHealth.image = self.castleHealth.emotions['castle71']
                elif self.castleHealth.hp <= 700 and self.castleHealth.hp > 690:
                    self.castleHealth.image = self.castleHealth.emotions['castle70']
                elif self.castleHealth.hp <= 690 and self.castleHealth.hp > 680:
                    self.castleHealth.image = self.castleHealth.emotions['castle69']
                elif self.castleHealth.hp <= 680 and self.castleHealth.hp > 670:
                    self.castleHealth.image = self.castleHealth.emotions['castle68']
                elif self.castleHealth.hp <= 670 and self.castleHealth.hp > 660:
                    self.castleHealth.image = self.castleHealth.emotions['castle67']
                elif self.castleHealth.hp <= 660 and self.castleHealth.hp > 650:
                    self.castleHealth.image = self.castleHealth.emotions['castle66']
                elif self.castleHealth.hp <= 650 and self.castleHealth.hp > 640:
                    self.castleHealth.image = self.castleHealth.emotions['castle65']
                elif self.castleHealth.hp <= 640 and self.castleHealth.hp > 630:
                    self.castleHealth.image = self.castleHealth.emotions['castle64']
                elif self.castleHealth.hp <= 630 and self.castleHealth.hp > 620:
                    self.castleHealth.image = self.castleHealth.emotions['castle63']
                elif self.castleHealth.hp <= 620 and self.castleHealth.hp > 610:
                    self.castleHealth.image = self.castleHealth.emotions['castle62']
                elif self.castleHealth.hp <= 610 and self.castleHealth.hp > 600:
                    self.castleHealth.image = self.castleHealth.emotions['castle61']
                elif self.castleHealth.hp <= 600 and self.castleHealth.hp > 590:
                    self.castleHealth.image = self.castleHealth.emotions['castle60']
                elif self.castleHealth.hp <= 590 and self.castleHealth.hp > 580:
                    self.castleHealth.image = self.castleHealth.emotions['castle59']
                elif self.castleHealth.hp <= 580 and self.castleHealth.hp > 570:
                    self.castleHealth.image = self.castleHealth.emotions['castle58']
                elif self.castleHealth.hp <= 570 and self.castleHealth.hp > 560:
                    self.castleHealth.image = self.castleHealth.emotions['castle57']
                elif self.castleHealth.hp <= 560 and self.castleHealth.hp > 550:
                    self.castleHealth.image = self.castleHealth.emotions['castle56']
                elif self.castleHealth.hp <= 550 and self.castleHealth.hp > 540:
                    self.castleHealth.image = self.castleHealth.emotions['castle55']
                elif self.castleHealth.hp <= 540 and self.castleHealth.hp > 530:
                    self.castleHealth.image = self.castleHealth.emotions['castle54']
                elif self.castleHealth.hp <= 530 and self.castleHealth.hp > 520:
                    self.castleHealth.image = self.castleHealth.emotions['castle53']
                elif self.castleHealth.hp <= 520 and self.castleHealth.hp > 510:
                    self.castleHealth.image = self.castleHealth.emotions['castle52']
                elif self.castleHealth.hp <= 510 and self.castleHealth.hp > 500:
                    self.castleHealth.image = self.castleHealth.emotions['castle51']
                elif self.castleHealth.hp <= 500 and self.castleHealth.hp > 490:
                    self.castleHealth.image = self.castleHealth.emotions['castle50']
                elif self.castleHealth.hp <= 490 and self.castleHealth.hp > 480:
                    self.castleHealth.image = self.castleHealth.emotions['castle49']
                elif self.castleHealth.hp <= 480 and self.castleHealth.hp > 470:
                    self.castleHealth.image = self.castleHealth.emotions['castle48']
                elif self.castleHealth.hp <= 470 and self.castleHealth.hp > 460:
                    self.castleHealth.image = self.castleHealth.emotions['castle47']
                elif self.castleHealth.hp <= 460 and self.castleHealth.hp > 450:
                    self.castleHealth.image = self.castleHealth.emotions['castle46']
                elif self.castleHealth.hp <= 450 and self.castleHealth.hp > 440:
                    self.castleHealth.image = self.castleHealth.emotions['castle45']
                elif self.castleHealth.hp <= 440 and self.castleHealth.hp > 430:
                    self.castleHealth.image = self.castleHealth.emotions['castle44']
                elif self.castleHealth.hp <= 430 and self.castleHealth.hp > 420:
                    self.castleHealth.image = self.castleHealth.emotions['castle43']
                elif self.castleHealth.hp <= 420 and self.castleHealth.hp > 410:
                    self.castleHealth.image = self.castleHealth.emotions['castle42']
                elif self.castleHealth.hp <= 410 and self.castleHealth.hp > 400:
                    self.castleHealth.image = self.castleHealth.emotions['castle41']
                elif self.castleHealth.hp <= 400 and self.castleHealth.hp > 390:
                    self.castleHealth.image = self.castleHealth.emotions['castle40']
                elif self.castleHealth.hp <= 390 and self.castleHealth.hp > 380:
                    self.castleHealth.image = self.castleHealth.emotions['castle39']
                elif self.castleHealth.hp <= 380 and self.castleHealth.hp > 370:
                    self.castleHealth.image = self.castleHealth.emotions['castle38']
                elif self.castleHealth.hp <= 370 and self.castleHealth.hp > 360:
                    self.castleHealth.image = self.castleHealth.emotions['castle37']
                elif self.castleHealth.hp <= 360 and self.castleHealth.hp > 350:
                    self.castleHealth.image = self.castleHealth.emotions['castle36']
                elif self.castleHealth.hp <= 350 and self.castleHealth.hp > 340:
                    self.castleHealth.image = self.castleHealth.emotions['castle35']
                elif self.castleHealth.hp <= 340 and self.castleHealth.hp > 330:
                    self.castleHealth.image = self.castleHealth.emotions['castle34']
                elif self.castleHealth.hp <= 330 and self.castleHealth.hp > 320:
                    self.castleHealth.image = self.castleHealth.emotions['castle33']
                elif self.castleHealth.hp <= 320 and self.castleHealth.hp > 310:
                    self.castleHealth.image = self.castleHealth.emotions['castle32']
                elif self.castleHealth.hp <= 310 and self.castleHealth.hp > 300:
                    self.castleHealth.image = self.castleHealth.emotions['castle31']
                elif self.castleHealth.hp <= 300 and self.castleHealth.hp > 290:
                    self.castleHealth.image = self.castleHealth.emotions['castle30']
                elif self.castleHealth.hp <= 290 and self.castleHealth.hp > 280:
                    self.castleHealth.image = self.castleHealth.emotions['castle29']
                elif self.castleHealth.hp <= 280 and self.castleHealth.hp > 270:
                    self.castleHealth.image = self.castleHealth.emotions['castle28']
                elif self.castleHealth.hp <= 270 and self.castleHealth.hp > 260:
                    self.castleHealth.image = self.castleHealth.emotions['castle27']
                elif self.castleHealth.hp <= 260 and self.castleHealth.hp > 250:
                    self.castleHealth.image = self.castleHealth.emotions['castle26']
                elif self.castleHealth.hp <= 250 and self.castleHealth.hp > 240:
                    self.castleHealth.image = self.castleHealth.emotions['castle25']
                elif self.castleHealth.hp <= 240 and self.castleHealth.hp > 230:
                    self.castleHealth.image = self.castleHealth.emotions['castle24']
                elif self.castleHealth.hp <= 230 and self.castleHealth.hp > 220:
                    self.castleHealth.image = self.castleHealth.emotions['castle23']
                elif self.castleHealth.hp <= 220 and self.castleHealth.hp > 210:
                    self.castleHealth.image = self.castleHealth.emotions['castle22']
                elif self.castleHealth.hp <= 210 and self.castleHealth.hp > 200:
                    self.castleHealth.image = self.castleHealth.emotions['castle21']
                elif self.castleHealth.hp <= 200 and self.castleHealth.hp > 190:
                    self.castleHealth.image = self.castleHealth.emotions['castle20']
                elif self.castleHealth.hp <= 190 and self.castleHealth.hp > 180:
                    self.castleHealth.image = self.castleHealth.emotions['castle19']
                elif self.castleHealth.hp <= 180 and self.castleHealth.hp > 170:
                    self.castleHealth.image = self.castleHealth.emotions['castle18']
                elif self.castleHealth.hp <= 170 and self.castleHealth.hp > 160:
                    self.castleHealth.image = self.castleHealth.emotions['castle17']
                elif self.castleHealth.hp <= 160 and self.castleHealth.hp > 150:
                    self.castleHealth.image = self.castleHealth.emotions['castle16']
                elif self.castleHealth.hp <= 150 and self.castleHealth.hp > 140:
                    self.castleHealth.image = self.castleHealth.emotions['castle15']
                elif self.castleHealth.hp <= 140 and self.castleHealth.hp > 130:
                    self.castleHealth.image = self.castleHealth.emotions['castle14']
                elif self.castleHealth.hp <= 130 and self.castleHealth.hp > 120:
                    self.castleHealth.image = self.castleHealth.emotions['castle13']
                elif self.castleHealth.hp <= 120 and self.castleHealth.hp > 110:
                    self.castleHealth.image = self.castleHealth.emotions['castle12']
                elif self.castleHealth.hp <= 110 and self.castleHealth.hp > 100:
                    self.castleHealth.image = self.castleHealth.emotions['castle11']
                elif self.castleHealth.hp <= 100 and self.castleHealth.hp > 90:
                    self.castleHealth.image = self.castleHealth.emotions['castle10']
                elif self.castleHealth.hp <= 90 and self.castleHealth.hp > 80:
                    self.castleHealth.image = self.castleHealth.emotions['castle9']
                elif self.castleHealth.hp <= 80 and self.castleHealth.hp > 70:
                    self.castleHealth.image = self.castleHealth.emotions['castle8']
                elif self.castleHealth.hp <= 70 and self.castleHealth.hp > 60:
                    self.castleHealth.image = self.castleHealth.emotions['castle7']
                elif self.castleHealth.hp <= 60 and self.castleHealth.hp > 50:
                    self.castleHealth.image = self.castleHealth.emotions['castle6']
                elif self.castleHealth.hp <= 50 and self.castleHealth.hp > 40:
                    self.castleHealth.image = self.castleHealth.emotions['castle5']
                elif self.castleHealth.hp <= 40 and self.castleHealth.hp > 30:
                    self.castleHealth.image = self.castleHealth.emotions['castle4']
                elif self.castleHealth.hp <= 30 and self.castleHealth.hp > 20:
                    self.castleHealth.image = self.castleHealth.emotions['castle3']
                elif self.castleHealth.hp <= 20 and self.castleHealth.hp > 10:
                    self.castleHealth.image = self.castleHealth.emotions['castle2']
                elif self.castleHealth.hp <= 10 and self.castleHealth.hp > 0:
                    self.castleHealth.image = self.castleHealth.emotions['castle1']

        for i in self.enemy4R:       
            if i.AtkUser == True:
                self.castleHealth.hp -= 0.04
                if self.castleHealth.hp <= 990 and self.castleHealth.hp > 980:
                    self.castleHealth.image = self.castleHealth.emotions['castle99']
                elif self.castleHealth.hp <= 980 and self.castleHealth.hp > 970:
                    self.castleHealth.image = self.castleHealth.emotions['castle98']
                elif self.castleHealth.hp <= 970 and self.castleHealth.hp > 960:
                    self.castleHealth.image = self.castleHealth.emotions['castle97']
                elif self.castleHealth.hp <= 960 and self.castleHealth.hp > 950:
                    self.castleHealth.image = self.castleHealth.emotions['castle96']
                elif self.castleHealth.hp <= 950 and self.castleHealth.hp > 940:
                    self.castleHealth.image = self.castleHealth.emotions['castle95']
                elif self.castleHealth.hp <= 940 and self.castleHealth.hp > 930:
                    self.castleHealth.image = self.castleHealth.emotions['castle94']
                elif self.castleHealth.hp <= 930 and self.castleHealth.hp > 920:
                    self.castleHealth.image = self.castleHealth.emotions['castle93']
                elif self.castleHealth.hp <= 920 and self.castleHealth.hp > 910:
                    self.castleHealth.image = self.castleHealth.emotions['castle92']
                elif self.castleHealth.hp <= 910 and self.castleHealth.hp > 900:
                    self.castleHealth.image = self.castleHealth.emotions['castle91']
                elif self.castleHealth.hp <= 900 and self.castleHealth.hp > 890:
                    self.castleHealth.image = self.castleHealth.emotions['castle90']
                elif self.castleHealth.hp <= 890 and self.castleHealth.hp > 880:
                    self.castleHealth.image = self.castleHealth.emotions['castle89']
                elif self.castleHealth.hp <= 880 and self.castleHealth.hp > 870:
                    self.castleHealth.image = self.castleHealth.emotions['castle88']
                elif self.castleHealth.hp <= 870 and self.castleHealth.hp > 860:
                    self.castleHealth.image = self.castleHealth.emotions['castle87']
                elif self.castleHealth.hp <= 860 and self.castleHealth.hp > 850:
                    self.castleHealth.image = self.castleHealth.emotions['castle86']
                elif self.castleHealth.hp <= 850 and self.castleHealth.hp > 840:
                    self.castleHealth.image = self.castleHealth.emotions['castle85']
                elif self.castleHealth.hp <= 840 and self.castleHealth.hp > 830:
                    self.castleHealth.image = self.castleHealth.emotions['castle84']
                elif self.castleHealth.hp <= 830 and self.castleHealth.hp > 820:
                    self.castleHealth.image = self.castleHealth.emotions['castle83']
                elif self.castleHealth.hp <= 820 and self.castleHealth.hp > 810:
                    self.castleHealth.image = self.castleHealth.emotions['castle82']
                elif self.castleHealth.hp <= 810 and self.castleHealth.hp > 800:
                    self.castleHealth.image = self.castleHealth.emotions['castle81']
                elif self.castleHealth.hp <= 800 and self.castleHealth.hp > 790:
                    self.castleHealth.image = self.castleHealth.emotions['castle80']
                elif self.castleHealth.hp <= 790 and self.castleHealth.hp > 780:
                    self.castleHealth.image = self.castleHealth.emotions['castle79']
                elif self.castleHealth.hp <= 780 and self.castleHealth.hp > 770:
                    self.castleHealth.image = self.castleHealth.emotions['castle78']
                elif self.castleHealth.hp <= 770 and self.castleHealth.hp > 760:
                    self.castleHealth.image = self.castleHealth.emotions['castle77']
                elif self.castleHealth.hp <= 760 and self.castleHealth.hp > 750:
                    self.castleHealth.image = self.castleHealth.emotions['castle76']
                elif self.castleHealth.hp <= 750 and self.castleHealth.hp > 740:
                    self.castleHealth.image = self.castleHealth.emotions['castle75']
                elif self.castleHealth.hp <= 740 and self.castleHealth.hp > 730:
                    self.castleHealth.image = self.castleHealth.emotions['castle74']
                elif self.castleHealth.hp <= 730 and self.castleHealth.hp > 720:
                    self.castleHealth.image = self.castleHealth.emotions['castle73']
                elif self.castleHealth.hp <= 720 and self.castleHealth.hp > 710:
                    self.castleHealth.image = self.castleHealth.emotions['castle72']
                elif self.castleHealth.hp <= 710 and self.castleHealth.hp > 700:
                    self.castleHealth.image = self.castleHealth.emotions['castle71']
                elif self.castleHealth.hp <= 700 and self.castleHealth.hp > 690:
                    self.castleHealth.image = self.castleHealth.emotions['castle70']
                elif self.castleHealth.hp <= 690 and self.castleHealth.hp > 680:
                    self.castleHealth.image = self.castleHealth.emotions['castle69']
                elif self.castleHealth.hp <= 680 and self.castleHealth.hp > 670:
                    self.castleHealth.image = self.castleHealth.emotions['castle68']
                elif self.castleHealth.hp <= 670 and self.castleHealth.hp > 660:
                    self.castleHealth.image = self.castleHealth.emotions['castle67']
                elif self.castleHealth.hp <= 660 and self.castleHealth.hp > 650:
                    self.castleHealth.image = self.castleHealth.emotions['castle66']
                elif self.castleHealth.hp <= 650 and self.castleHealth.hp > 640:
                    self.castleHealth.image = self.castleHealth.emotions['castle65']
                elif self.castleHealth.hp <= 640 and self.castleHealth.hp > 630:
                    self.castleHealth.image = self.castleHealth.emotions['castle64']
                elif self.castleHealth.hp <= 630 and self.castleHealth.hp > 620:
                    self.castleHealth.image = self.castleHealth.emotions['castle63']
                elif self.castleHealth.hp <= 620 and self.castleHealth.hp > 610:
                    self.castleHealth.image = self.castleHealth.emotions['castle62']
                elif self.castleHealth.hp <= 610 and self.castleHealth.hp > 600:
                    self.castleHealth.image = self.castleHealth.emotions['castle61']
                elif self.castleHealth.hp <= 600 and self.castleHealth.hp > 590:
                    self.castleHealth.image = self.castleHealth.emotions['castle60']
                elif self.castleHealth.hp <= 590 and self.castleHealth.hp > 580:
                    self.castleHealth.image = self.castleHealth.emotions['castle59']
                elif self.castleHealth.hp <= 580 and self.castleHealth.hp > 570:
                    self.castleHealth.image = self.castleHealth.emotions['castle58']
                elif self.castleHealth.hp <= 570 and self.castleHealth.hp > 560:
                    self.castleHealth.image = self.castleHealth.emotions['castle57']
                elif self.castleHealth.hp <= 560 and self.castleHealth.hp > 550:
                    self.castleHealth.image = self.castleHealth.emotions['castle56']
                elif self.castleHealth.hp <= 550 and self.castleHealth.hp > 540:
                    self.castleHealth.image = self.castleHealth.emotions['castle55']
                elif self.castleHealth.hp <= 540 and self.castleHealth.hp > 530:
                    self.castleHealth.image = self.castleHealth.emotions['castle54']
                elif self.castleHealth.hp <= 530 and self.castleHealth.hp > 520:
                    self.castleHealth.image = self.castleHealth.emotions['castle53']
                elif self.castleHealth.hp <= 520 and self.castleHealth.hp > 510:
                    self.castleHealth.image = self.castleHealth.emotions['castle52']
                elif self.castleHealth.hp <= 510 and self.castleHealth.hp > 500:
                    self.castleHealth.image = self.castleHealth.emotions['castle51']
                elif self.castleHealth.hp <= 500 and self.castleHealth.hp > 490:
                    self.castleHealth.image = self.castleHealth.emotions['castle50']
                elif self.castleHealth.hp <= 490 and self.castleHealth.hp > 480:
                    self.castleHealth.image = self.castleHealth.emotions['castle49']
                elif self.castleHealth.hp <= 480 and self.castleHealth.hp > 470:
                    self.castleHealth.image = self.castleHealth.emotions['castle48']
                elif self.castleHealth.hp <= 470 and self.castleHealth.hp > 460:
                    self.castleHealth.image = self.castleHealth.emotions['castle47']
                elif self.castleHealth.hp <= 460 and self.castleHealth.hp > 450:
                    self.castleHealth.image = self.castleHealth.emotions['castle46']
                elif self.castleHealth.hp <= 450 and self.castleHealth.hp > 440:
                    self.castleHealth.image = self.castleHealth.emotions['castle45']
                elif self.castleHealth.hp <= 440 and self.castleHealth.hp > 430:
                    self.castleHealth.image = self.castleHealth.emotions['castle44']
                elif self.castleHealth.hp <= 430 and self.castleHealth.hp > 420:
                    self.castleHealth.image = self.castleHealth.emotions['castle43']
                elif self.castleHealth.hp <= 420 and self.castleHealth.hp > 410:
                    self.castleHealth.image = self.castleHealth.emotions['castle42']
                elif self.castleHealth.hp <= 410 and self.castleHealth.hp > 400:
                    self.castleHealth.image = self.castleHealth.emotions['castle41']
                elif self.castleHealth.hp <= 400 and self.castleHealth.hp > 390:
                    self.castleHealth.image = self.castleHealth.emotions['castle40']
                elif self.castleHealth.hp <= 390 and self.castleHealth.hp > 380:
                    self.castleHealth.image = self.castleHealth.emotions['castle39']
                elif self.castleHealth.hp <= 380 and self.castleHealth.hp > 370:
                    self.castleHealth.image = self.castleHealth.emotions['castle38']
                elif self.castleHealth.hp <= 370 and self.castleHealth.hp > 360:
                    self.castleHealth.image = self.castleHealth.emotions['castle37']
                elif self.castleHealth.hp <= 360 and self.castleHealth.hp > 350:
                    self.castleHealth.image = self.castleHealth.emotions['castle36']
                elif self.castleHealth.hp <= 350 and self.castleHealth.hp > 340:
                    self.castleHealth.image = self.castleHealth.emotions['castle35']
                elif self.castleHealth.hp <= 340 and self.castleHealth.hp > 330:
                    self.castleHealth.image = self.castleHealth.emotions['castle34']
                elif self.castleHealth.hp <= 330 and self.castleHealth.hp > 320:
                    self.castleHealth.image = self.castleHealth.emotions['castle33']
                elif self.castleHealth.hp <= 320 and self.castleHealth.hp > 310:
                    self.castleHealth.image = self.castleHealth.emotions['castle32']
                elif self.castleHealth.hp <= 310 and self.castleHealth.hp > 300:
                    self.castleHealth.image = self.castleHealth.emotions['castle31']
                elif self.castleHealth.hp <= 300 and self.castleHealth.hp > 290:
                    self.castleHealth.image = self.castleHealth.emotions['castle30']
                elif self.castleHealth.hp <= 290 and self.castleHealth.hp > 280:
                    self.castleHealth.image = self.castleHealth.emotions['castle29']
                elif self.castleHealth.hp <= 280 and self.castleHealth.hp > 270:
                    self.castleHealth.image = self.castleHealth.emotions['castle28']
                elif self.castleHealth.hp <= 270 and self.castleHealth.hp > 260:
                    self.castleHealth.image = self.castleHealth.emotions['castle27']
                elif self.castleHealth.hp <= 260 and self.castleHealth.hp > 250:
                    self.castleHealth.image = self.castleHealth.emotions['castle26']
                elif self.castleHealth.hp <= 250 and self.castleHealth.hp > 240:
                    self.castleHealth.image = self.castleHealth.emotions['castle25']
                elif self.castleHealth.hp <= 240 and self.castleHealth.hp > 230:
                    self.castleHealth.image = self.castleHealth.emotions['castle24']
                elif self.castleHealth.hp <= 230 and self.castleHealth.hp > 220:
                    self.castleHealth.image = self.castleHealth.emotions['castle23']
                elif self.castleHealth.hp <= 220 and self.castleHealth.hp > 210:
                    self.castleHealth.image = self.castleHealth.emotions['castle22']
                elif self.castleHealth.hp <= 210 and self.castleHealth.hp > 200:
                    self.castleHealth.image = self.castleHealth.emotions['castle21']
                elif self.castleHealth.hp <= 200 and self.castleHealth.hp > 190:
                    self.castleHealth.image = self.castleHealth.emotions['castle20']
                elif self.castleHealth.hp <= 190 and self.castleHealth.hp > 180:
                    self.castleHealth.image = self.castleHealth.emotions['castle19']
                elif self.castleHealth.hp <= 180 and self.castleHealth.hp > 170:
                    self.castleHealth.image = self.castleHealth.emotions['castle18']
                elif self.castleHealth.hp <= 170 and self.castleHealth.hp > 160:
                    self.castleHealth.image = self.castleHealth.emotions['castle17']
                elif self.castleHealth.hp <= 160 and self.castleHealth.hp > 150:
                    self.castleHealth.image = self.castleHealth.emotions['castle16']
                elif self.castleHealth.hp <= 150 and self.castleHealth.hp > 140:
                    self.castleHealth.image = self.castleHealth.emotions['castle15']
                elif self.castleHealth.hp <= 140 and self.castleHealth.hp > 130:
                    self.castleHealth.image = self.castleHealth.emotions['castle14']
                elif self.castleHealth.hp <= 130 and self.castleHealth.hp > 120:
                    self.castleHealth.image = self.castleHealth.emotions['castle13']
                elif self.castleHealth.hp <= 120 and self.castleHealth.hp > 110:
                    self.castleHealth.image = self.castleHealth.emotions['castle12']
                elif self.castleHealth.hp <= 110 and self.castleHealth.hp > 100:
                    self.castleHealth.image = self.castleHealth.emotions['castle11']
                elif self.castleHealth.hp <= 100 and self.castleHealth.hp > 90:
                    self.castleHealth.image = self.castleHealth.emotions['castle10']
                elif self.castleHealth.hp <= 90 and self.castleHealth.hp > 80:
                    self.castleHealth.image = self.castleHealth.emotions['castle9']
                elif self.castleHealth.hp <= 80 and self.castleHealth.hp > 70:
                    self.castleHealth.image = self.castleHealth.emotions['castle8']
                elif self.castleHealth.hp <= 70 and self.castleHealth.hp > 60:
                    self.castleHealth.image = self.castleHealth.emotions['castle7']
                elif self.castleHealth.hp <= 60 and self.castleHealth.hp > 50:
                    self.castleHealth.image = self.castleHealth.emotions['castle6']
                elif self.castleHealth.hp <= 50 and self.castleHealth.hp > 40:
                    self.castleHealth.image = self.castleHealth.emotions['castle5']
                elif self.castleHealth.hp <= 40 and self.castleHealth.hp > 30:
                    self.castleHealth.image = self.castleHealth.emotions['castle4']
                elif self.castleHealth.hp <= 30 and self.castleHealth.hp > 20:
                    self.castleHealth.image = self.castleHealth.emotions['castle3']
                elif self.castleHealth.hp <= 20 and self.castleHealth.hp > 10:
                    self.castleHealth.image = self.castleHealth.emotions['castle2']
                elif self.castleHealth.hp <= 10 and self.castleHealth.hp > 0:
                    self.castleHealth.image = self.castleHealth.emotions['castle1']

        dx = -0.05
        dy = 0
        if self.emptySun.position[0] >= 0:
            if dx != 0 or dy != 0:
                pos = self.emptySun.position
                new_x = pos[0] + 100 * dx * dt
                new_y = pos[1] + 100 * dy * dt
                self.emptySun.position = (new_x, new_y)
                self.emptySun.cshape.center = self.emptySun.position
                    
        if self.start1.time >= 0 and self.start1.time < 2:
            self.start1.image = self.start.emotions['start']
        else:
            self.start1.image = self.start1.emotions['empty']
        
        if self.castleHealth.hp < 0 and self.emptySun.position[0] > 0:
            self.start.image = self.start.emotions['lose']
        elif self.castleHealth.hp >= 0 and self.emptySun.position[0] <= 0:
            self.start.image = self.start.emotions['win']
        else:
            self.start.image = self.start.emotions['empty']
                    
class SkyLayer(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super(SkyLayer, self).__init__()
        self.sky = Sky((750, 400))
        self.add(self.sky)
        self.sun = Sun((1500,700))
        self.add(self.sun)

        self.schedule(self.update)
        
    def update(self, dt):
        # Sun
        dx = -0.05
        dy = 0
        if self.sun.position[0] >= 0:
            if dx != 0 or dy != 0:
                pos = self.sun.position
                new_x = pos[0] + 100 * dx * dt
                new_y = pos[1] + 100 * dy * dt
                self.sun.position = (new_x, new_y)
                self.sun.cshape.center = self.sun.position
          
        if self.sun.position[0] <= 1500 and self.sun.position[0] > 1375:
            self.sky.image = self.sky.emotions['1']
        elif self.sun.position[0] <= 1375 and self.sun.position[0] > 1250:
            self.sky.image = self.sky.emotions['2']        
        elif self.sun.position[0] <= 1250 and self.sun.position[0] > 1125:
            self.sky.image = self.sky.emotions['3']
        elif self.sun.position[0] <= 1125 and self.sun.position[0] > 1000:
            self.sky.image = self.sky.emotions['4']          
        elif self.sun.position[0] <= 1000 and self.sun.position[0] > 975:
            self.sky.image = self.sky.emotions['5']
        elif self.sun.position[0] <= 975 and self.sun.position[0] > 950:
            self.sky.image = self.sky.emotions['6']        
        elif self.sun.position[0] <= 950 and self.sun.position[0] > 825:
            self.sky.image = self.sky.emotions['7']
        elif self.sun.position[0] <= 825 and self.sun.position[0] > 700:
            self.sky.image = self.sky.emotions['8'] 
        elif self.sun.position[0] <= 700 and self.sun.position[0] > 575:
            self.sky.image = self.sky.emotions['9']
        elif self.sun.position[0] <= 575 and self.sun.position[0] > 425:
            self.sky.image = self.sky.emotions['10']        
        elif self.sun.position[0] <= 425 and self.sun.position[0] > 300:
            self.sky.image = self.sky.emotions['11']
        elif self.sun.position[0] <= 300 and self.sun.position[0] >= 0:
            self.sky.image = self.sky.emotions['12']
            

            
        
def new_game():
    scene = cocos.scene.Scene()

    sky = SkyLayer()
    
    layer = MainLayer()

    scene.add(sky, z = 0)
    scene.add(layer, z = 3)

    gameSound.play(100)
    
    # scene center 280, 450
    position = 750, 400
    scene.add(Background(position), z = 1)

    cocos.director.director.run(scene)
    return scene


