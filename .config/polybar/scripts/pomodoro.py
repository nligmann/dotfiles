#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
        '-f',
        '--file',
        type=str,
        metavar='file path',
        dest='file_path'
        )

args = parser.parse_args()

with open(args.file_path, 'r') as file:
    data = file.readline()
    print(data)
    
