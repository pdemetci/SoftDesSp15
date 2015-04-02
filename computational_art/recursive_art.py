""" TODO: Put your header comment here """

import random
<<<<<<< HEAD
import Image
from random import randint
from PIL import Image
from math import cos, sin, pi
=======
from PIL import Image

>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983

def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
<<<<<<< HEAD
    depth=randint(min_depth,max_depth)
    def build_function(depth):
        options1=["prod","sin_pi","cos_pi"]
        options2=["x","y"]
        if depth == 1:
            i = randint(0,len(options2)-1)
            return [options2[i]]
# "x" and "y" can be in the last depth.
        else:
            i = randint(0,len(options1)-1)
            if options1[i]=="prod": #prod takes 2 inputs so:
                return [options1[i], build_function(depth-1),build_function(depth-1)]
            else: #others take only one input. so:
                return [options1[i], build_function(depth-1)]
    return build_function(depth)
=======
    # TODO: implement this
    pass
>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983


def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
<<<<<<< HEAD
    if f[0] == 'x':
        return x
    if f[0] == 'y':
        return y
    if f[0] == 'prod':
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    if f[0] == 'cos_pi':
        return cos(pi*evaluate_random_function(f[1],x,y))
    if f[0] == 'sin_pi':
        return sin(pi*evaluate_random_function(f[1],x,y))
    else: print 'You didnt take into account something'
=======
    # TODO: implement this
    pass

>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
<<<<<<< HEAD
    val= float(val)
    output_interval_end= float(output_interval_end)
    output_interval_start=float(output_interval_start)
    input_interval_start=float(input_interval_start)
    input_interval_end=float(input_interval_end)
    a= (output_interval_end - output_interval_start)/ (input_interval_end - input_interval_start)
    output = ((a*val) - ((a*input_interval_start)-output_interval_start))
    return output
=======
    # TODO: implement this
    pass

>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983

def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
<<<<<<< HEAD
    color = remap_interval(val, -1, 1, 0, 255)
    return int(color)


def generate_art(filename, x_size=350, y_size=350):
        """ Generate computational art and save as an image file.

            filename: string filename for image (should be .png)
            x_size, y_size: optional args to set image dimensions (default: 350)
        """
        # Functions for red, green, and blue channels - where the magic happens!
        im = Image.new("RGB",(x_size,y_size))
        random_art = im.load()
        red = build_random_function(5,10)
        blue = build_random_function(5,10)
        green = build_random_function(5,10)

        for x in range(0,349,1):
            for y in range(0,349,1):
                x_1=remap_interval(x,0.0,349.0,-1.0,1.0)
                y_1=remap_interval(y,0.0,349.0,-1.0,1.0)
                r_1= evaluate_random_function (red, x_1, y_1)
                b_1= evaluate_random_function (blue, x_1, y_1)
                g_1= evaluate_random_function (green, x_1, y_1)
                r_2 = remap_interval(r_1,-1,1,0,255)
                r = int(int(r_2)/5)
                b_2 = remap_interval(b_1,-1,1,0,255)
                b = int(b_2)
                g_2 = remap_interval(g_1,-1,1,0,255)
                g = int(int(g_2)/10)
                print r
                print b
                print g
                random_art[x,y] = (r,b,g)

        im.save('random_art55.png')

generate_art("random_art_1", x_size=350, y_size=350)
=======
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = ["x"]
    green_function = ["y"]
    blue_function = ["x"]

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)

>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    #generate_art("myart.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
<<<<<<< HEAD
=======
    test_image("noise.png")
>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983
