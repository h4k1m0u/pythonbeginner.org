#!/usr/bin/env python
import random
from PIL import Image, ImageDraw, ImageColor

# define constants
COLORS = ImageColor.colormap.keys()
WIDTH = 640
HEIGHT = 480

# create a new image & draw
im = Image.new('RGB', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(im)

# loop generating circles
for i in xrange(100):
    circle_x, circle_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    circle_size = random.randint(10, 100)
    circle_color = random.choice(COLORS)

    draw.ellipse(
        [(circle_x, circle_y), (circle_x + circle_size, circle_y + circle_size)],
        outline=ImageColor.getrgb(circle_color)
    )

# show generated screensaver
im.show()
