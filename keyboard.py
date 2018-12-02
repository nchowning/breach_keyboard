#!/usr/bin/env python

import argparse

rows = {
    'left': [
        # Row 1  Prev                     Esc
        [1, [[1, True], [0.5, False], [1, True]]],
        # Row 2    Play
        [0.5, [[1, True]]],  #   `          1          2          3          4          5          6
        [0.5, [[1.5, False], [1, True], [1, True], [1, True], [1, True], [1, True], [1, True], [1, True]]],
        # Row 3    Next
        [0.5, [[1, True]]],  #   Tab        Q          W          E          R          T
        [1, [[1.5, False], [1.5, True], [1, True], [1, True], [1, True], [1, True], [1, True]]],
        # Row 4  VolUp                       Ctrl       A          S          D          F          G
        [1, [[1, True], [0.5, False], [1.75, True], [1, True], [1, True], [1, True], [1, True], [1, True]]],
        # Row 5  Mute                        Shift      Z          X          C          V          B
        [1, [[1, True], [0.5, False], [2.25, True], [1, True], [1, True], [1, True], [1, True], [1, True]]],
        # Row 6  VolDn                       Ctrl          Super         Alt           Space      Fn
        [1, [[1, True], [0.5, False], [1.25, True], [1.25, True], [1.25, True], [2.75, True], [1, True]]],
    ],

    'right': [
        # Row 1 - Function Row
        [1, [[1.75, False], [1, True], [1, True], [1, True], [1, False], [1, True], [1, True], [1, True]]],
        # Gap
        [0.5, []],
        # Row 2                 7          8          9          0          -          =          <-
        [1, [[0.75, False], [1, True], [1, True], [1, True], [1, True], [1, True], [1, True], [2, True]]],
        # Row 3                 Y          U          I          O          P          [          ]            \
        [1, [[0.25, False], [1, True], [1, True], [1, True], [1, True], [1, True], [1, True], [1, True], [1.5, True]]],
        # Row 4                H          J          K          L          ;          '             Enter
        [1, [[0.5, False], [1, True], [1, True], [1, True], [1, True], [1, True], [1, True], [2.25, True]]],
        # Row 5              N          M          ,          .          /                         Up
        [1, [[1, False], [1, True], [1, True], [1, True], [1, True], [1, True], [0.75, False], [1, True]]],
        # Row 6  Fn         Space         Super         Ctrl                      Left       Down       Right
        [1, [[1, True], [2, True], [1.25, True], [1.25, True], [0.25, False], [1, True], [1, True], [1, True]]],
    ]
}


def main():

    # Switch spacing from middle to middle
    mtm = 19.05

    args = parse_arguments()

    side_rows = rows[args.side.lower()]
    
    v_position = 0
    
    for row in side_rows:
        v_position += mtm / 2
    
        h_position = 0
        for i, key in enumerate(row[1]):
            h_spacing = key[0]
    
            h_position += (h_spacing * mtm) / 2
    
            if key[1]:
                if args.diode:
                    # Doide placement
                    print("(%.5f, %.5f)" % (h_position - 8.15, v_position - 3))
                elif args.resistor:
                    # LED resistor placement
                    print("(%.5f, %.5f)" % (h_position - 6, v_position - 5))
                elif args.text:
                    # Silkscreen text placement
                    print("(%.5f, %.5f)" % (h_position, v_position + 8.475))
                else:
                    # Switch placement
                    print("(%.5f, %.5f)" % (h_position, v_position))
    
            h_position += (h_spacing * mtm) / 2
    
        v_spacing = row[0]
        if v_spacing >= 1:
            v_position += (v_spacing * mtm) / 2
        print()


def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('side',
                        help='Keyboard side (left or right)')

    coordinate_group = parser.add_mutually_exclusive_group()
    coordinate_group.add_argument('-s', dest='switch', action='store_true',
                                  help='Print switch coordinates (default)')
    coordinate_group.add_argument('-d', dest='diode', action='store_true',
                                  help='Print diode coordinates')
    coordinate_group.add_argument('-r', dest='resistor', action='store_true',
                                  help='Print LED resistor coordinates')
    coordinate_group.add_argument('-t', dest='text', action='store_true',
                                  help='Print silkscreen text coordinates')

    return parser.parse_args()


if __name__ == '__main__':
    main()
