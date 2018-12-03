#!/usr/bin/env python3

import argparse
import json


def main():
    text_template = """  (gr_text "%s" (at %.3f %.3f) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )"""

    args = parse_arguments()

    DEFAULT_WIDTH = 1
    DEFAULT_HEIGHT = 1
    
    with open(args.file) as f:
        data = json.load(f)
    
    spacing = 19.05
    
    v_position = 0
    
    if args.diode:
        offset = [-8.15, -3]
    elif args.resistor:
        offset = [-6, -5]
    elif args.text:
        offset = [0, 8]
    else:
        offset = [0, 0]

    if args.offset:
        offset[0] += float(args.offset[0])
        offset[1] += float(args.offset[1])

    for row in data:
        # Ignore the keyboard properties values
        if isinstance(row, dict):
            continue
    
        width = DEFAULT_WIDTH
        height = DEFAULT_HEIGHT
    
        h_position = 0
    
        v_position += (spacing * height) / 2
    
        for key in row:
            if isinstance(key, dict):
                # Adjust position for gaps
                # I think y will only show up as the first key in a row since a
                # change in the y value would just start a new row
                if 'x' in key.keys():
                    h_position += (key['x'] * spacing)
                if 'y' in key.keys():
                    v_position += (key['y'] * spacing)
    
                # Change the size of the next key
                if 'w' in key.keys():
                    width = key['w']
                if 'h' in key.keys():
                    height = key['h']
            else:
                # We only care about the main (lowest) legend
                legend = key.split('\n')[-1]
    
                h_position += (spacing * width) / 2
    
                extra_height = 0
                if height != DEFAULT_HEIGHT:
                    extra_height = (spacing * (height - 1)) / 2
    
                if args.text:
                    print(text_template % (legend, round(h_position + offset[0], 3), round(v_position + extra_height + offset[1], 3)))
                else:
                    print("(%.5f, %.5f)" % (h_position + offset[0], v_position + extra_height + offset[1]))
    
                h_position += (spacing * width) / 2
    
                width = DEFAULT_WIDTH
                height = DEFAULT_HEIGHT
    
        v_position += (spacing * height) / 2


def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('file',
                        help='JSON keyboard data file')
    parser.add_argument('-o', dest='offset',
                        help='Global offset for all coordinates. Example: \'10,10\'')

    coordinate_group = parser.add_mutually_exclusive_group()
    coordinate_group.add_argument('-s', dest='switch', action='store_true',
                                  help='Print switch coordinates (default)')
    coordinate_group.add_argument('-d', dest='diode', action='store_true',
                                  help='Print diode coordinates')
    coordinate_group.add_argument('-r', dest='resistor', action='store_true',
                                  help='Print LED resistor coordinates')
    coordinate_group.add_argument('-t', dest='text', action='store_true',
                                  help='Print silkscreen text')

    args = parser.parse_args()

    if args.offset:
        args.offset = args.offset.split(',')

    return args


if __name__ == '__main__':
    main()
