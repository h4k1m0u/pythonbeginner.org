`Pillow` (`PIL` fork) is installed with:

    pip install Pillow

-- We will need the `random` built-in python module, and the `Image`, `ImageDraw` and `ImageColor` classes from the `Pillow` library:

    import random
    from PIL import Image, ImageDraw, ImageColor    
    

<!--more-->

-- First, we define the `constants` that we will need: the `WIDTH` and `HEIGHT` of the image and the `color names` list:

    COLORS = ImageColor.colormap.keys()
    WIDTH = 640
    HEIGHT = 480
    

-- Then, we instantiate the image in the `RGB` mode with the `WIDTH` and `HEIGHT` defined earlier. The `draw` object will be used later to draw `circles` on the image:

    im = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(im)
    

-- After that, we loop `100` times to draw `100` circles:

    for i in xrange(100):
    

-- In each iteration, we pick a random (`circle_x`, `circle_y`) and a `circle_size`. These will determine the `circle`'s bounding box. We will pick a random `circle_color` from the list of colors too, for the `circle`'s contour. Next, we draw a circle having its outline in `circle_color` color, inside the `[(circle_x, circle_y), (circle_x + circle_size, circle_y + circle_size)]` rectangle:

    circle_x, circle_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    circle_size = random.randint(10, 100)
    circle_color = random.choice(COLORS)
    
    draw.ellipse(
        [(circle_x, circle_y), (circle_x + circle_size, circle_y + circle_size)],
        outline=ImageColor.getrgb(circle_color)
    )
    

-- Finally, we show our `circles screensaver` image:

    im.show()
    

The full source code: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-circles-screensaver-with-pil.py" target="_blank">Python Circles Screensaver with PIL on Github</a>
