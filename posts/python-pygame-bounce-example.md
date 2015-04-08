`Pygame` is a set of `Python` modules based on the `SDL` library and designed for writing video games

In this tutorial, we will code a simple bounce program to get started with `Pygame`. The `sprite` used moves diagonally and bounces when it collides with window's boundaries.

<!--more-->

-- We will import only the `pygame` module:

    import pygame
    

-- Then, we initialize our window or screen for display by providing a tuple which contains the width and height of the window:

    screen = pygame.display.set_mode((320, 240))
    

-- Next, we load an image from a file (The image is in the same folder as the `Python` script we are writing right now), with alpha transparency support using the `convert_alpha()` method:

    sprite = pygame.image.load('python-sprite.png').convert_alpha()
    

**Note**: The `screen` and `sprite` are both instances of the same class `pygame.surface`. The difference between the two objects is that the `sprite` will move, whereas the `screen` stays in its place and fills all the view in black.

-- After that, we retrieve the `sprite`'s `bounding box` (the rectangle surrounding it), that we will use inside the game loop to move the `sprite` and to check for collision. We define also the speed of the `sprite` using a list in the form `[speed_x, speed_y]`:

    sprite_rect = sprite.get_rect()
    speed = [2, 2]
    

-- We instantiate the `clock` that we are going to use to adjust our game's `fps` (Frames per second):

    clock = pygame.time.Clock()
    

-- The game loop is just an `infinite loop`, inside of which the first instruction will set the `fps` of the game:

    while 1:
        clock.tick(60)
    

-- Next thing to do is to move the `sprite`'s `rectangle` (sprite_rect variable) and then to check for `sprite`'s collision with the `screen`'s limits, by comparing `sprite`'s `(x, y)` coordinates with `(screen width, screen height)`. In case of a collision against a horizontal (resp. vertical) boundary, `speed_y` (resp. `speed_x`) is multiplied by `-1` , which makes the `sprite` move in the other direction:

    sprite_rect = sprite_rect.move(speed)
    
    if sprite_rect.left < 0 or sprite_rect.right > 320:
        speed[0] = -speed[0]
    if sprite_rect.top < 0 or sprite_rect.bottom > 240:
        speed[1] = -speed[1]
    

-- The last step in the `game loop` consists in filling the `screen` surface in `black`, and drawing the `sprite` surface onto the `screen` surface using the `sprite_rect` to position it with the `blit()` method. `pygame.display.flip` is needed to update the full display:

    screen.fill((0, 0, 0))
    screen.blit(sprite, sprite_rect)
    pygame.display.flip()
    

The full source code: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-pygame-bounce-example.py" target="_blank">Python Pygame Bounce Example on Github</a>

The 32x32 `Python` `sprite` used: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-sprite.png" target="_blank">Python Sprite on Github</a>
