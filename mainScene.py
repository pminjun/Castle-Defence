from cocos.director import director

import pyglet.font
import pyglet.resource

from mainMenuScene import new_menu

if __name__ == '__main__':
    pyglet.resource.path.append('assets')
    pyglet.resource.reindex()

    director.init(caption='Castle Defense', width = 1500, height = 800)
    director.run(new_menu())
