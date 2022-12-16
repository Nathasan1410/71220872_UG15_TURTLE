Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
animation = pyglet.image.load('c57.gif')
animSprite = pyglet.sprite.Sprite(animation)

w = animSprite.width
h = animSprite.height

window = pyglet.window.Window(widsth=w, height=h)

r,g,b,alpha = 0.5, 0.5, 0.8, 0.5

pyglet.gl.glClearColor(r,g,b,alpha)

def on_draw():
    window.clear()
    pyglet.animsprite.draw()

on_draw()
SyntaxError: multiple statements found while compiling a single statement
