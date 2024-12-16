#!/usr/bin/python3
#coding: utf-8

import argparse, os

CLI=argparse.ArgumentParser()
CLI.add_argument("-f", "--flag", required=True, help='The flag to be encoded.')
CLI.add_argument("-o", "--out_file_name", required=True, help='The file name of the output file.')
CLI.add_argument("-s", "--sound_file_name", required=True, help='The file name of the sound file holding the flag.')
CLI.add_argument("-e", "--extension_of_sound_files", required=True, help='The codec (extension) of the source sound files, f ex mp3, flac or ogg.')

# parse the command line
args = CLI.parse_args()

flag_list = [str(ord(x)).zfill(3) for x in args.flag]

nummer_strang = ''.join(flag_list)

with open(args.out_file_name, 'w') as utfil:
    utfil.write('#!/bin/bash\nffmpeg -i "concat:')
    temp_str = []
    for siffra in nummer_strang:
        temp_str.append(siffra + '.' + args.extension_of_sound_files + '|t.' + args.extension_of_sound_files)
    utfil.write('|'.join(temp_str))
    utfil.write('" -acodec copy %s\n' % (args.sound_file_name))
os.chmod(args.out_file_name, 0o755)
