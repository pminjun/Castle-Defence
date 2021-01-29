import cocos.menu
import cocos.scene
import cocos.layer
import cocos.actions as ac
import pyglet.image
import cocos.sprite
import pyglet.app

import pygame

import cocos.audio
import cocos.audio.pygame
import cocos.audio.pygame.mixer

from cocos.director import director
from cocos.actions.interval_actions import MoveBy
from pyglet.image import Animation
from cocos.scenes.transitions import TurnOffTilesTransition
from cocos.scenes.transitions import FadeDownTransition
from gameScene import new_game

# Animation humanRogo
raw = pyglet.image.load('assets/background.png')
seq = pyglet.image.ImageGrid(raw, 1, 3)
mainHuman = Animation.from_image_sequence(seq, 0.12, True)

# Animation 
raw1 = pyglet.image.load('assets/sun.png')
seq1 = pyglet.image.ImageGrid(raw1, 1, 8)
sun = Animation.from_image_sequence(seq1, 0.2, True)

# Animation startButton
raw2 = pyglet.image.load('assets/start1.png')
seq2 = pyglet.image.ImageGrid(raw2, 1, 4)
startButton = Animation.from_image_sequence(seq2, 0.07, True)

# Animation exitButton
raw3 = pyglet.image.load('assets/exit1.png')
seq3 = pyglet.image.ImageGrid(raw3, 1, 4)
exitButton = Animation.from_image_sequence(seq3, 0.07, True)

cocos.audio.pygame.mixer.init()
sound = cocos.audio.pygame.mixer.Sound('audio/backAudio.ogg')
sound1 = cocos.audio.pygame.mixer.Sound('audio/button.ogg')

class Sun(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(Sun, self).__init__(sun, pos)
        
class humanRogo(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(humanRogo, self).__init__(pyglet.image.load('assets/backGround2.png'), pos)

class titleRogo(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(titleRogo, self).__init__(titleText, pos)

class startBut(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(startBut, self).__init__(startButton, pos)

class exitBut(cocos.sprite.Sprite):
    def __init__(self, pos):
        super(exitBut, self).__init__(exitButton, pos) 
        
class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super(MainMenu, self).__init__('')
        
        items = list()
        items.append(cocos.menu.ImageMenuItem('assets/startButton.png', self.on_new_game))
        items.append(cocos.menu.ImageMenuItem('assets/startButton.png', self.exit))

        # Start Button
        items[0].position = 340, -150
        items[1].position = 340, -250

        self.create_menu(items, ac.ScaleTo(3.0, duration=0), ac.ScaleTo(3.0, duration=0))

        # items.append(cocos.menu.ToggleMenuItem('Show FPS: ', self.show_fps, director.show_FPS))
        # colors = [(255, 255, 255), (100, 200, 100), (200, 50, 50)]

    def on_new_game(self):
        sound.stop()
        sound1.play()        
        director.push(FadeDownTransition(new_game(), duration = 1))
        
    def exit(self):
        sound1.play()
        self.pyglet.app.exit
        

    def show_fps(self, val):
        director.show_FPS = val

        
def new_menu():
    scene = cocos.scene.Scene()
    color_layer = cocos.layer.ColorLayer(249, 224, 120, 255)
    scene.add(MainMenu(), z=1)
    scene.add(color_layer, z=0)

    sound.play()
    
    # scene center 280, 450
    mainHumanPos = 750, 400
    scene.add(humanRogo(mainHumanPos), z = 0)
    
    # scene center 280, 450
    startButtonPos = 1100, 300
    scene.add(startBut(startButtonPos), z = 0)

    # scene center 280, 450
    exitButtonPos = 1100, 150
    scene.add(exitBut(exitButtonPos), z = 0)

    return scene
