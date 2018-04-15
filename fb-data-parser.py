#!/usr/bin/env python3

import argparse
import os
import glob

import messages


def main():

    # Set up argparser
    parser = argparse.ArgumentParser(description='Parse Facebook data.')
    parser.add_argument('-d', '--data', dest='data_dir', 
            help='Path to facebook data directory', required=True)
    parser.add_argument('-t', '--output-type', dest='output_type', 
            help='Type of the output, only json for now', default='json')
    args = parser.parse_args()

    #
    # Parse messages
    #
    print("Parsing messages...")
    message_files = list(glob.glob(args.data_dir + "/messages/*.html"))
    message_parser = messages.Parser()
    message_parser.parseThreads(message_files)

    # Export the data to a file
    filename = "messages." + args.output_type
    message_parser.export(file_type=args.output_type, filename=filename)
    print("Parsed {} threads".format(len(message_parser.threads)))


if __name__ == "__main__":
    main()
