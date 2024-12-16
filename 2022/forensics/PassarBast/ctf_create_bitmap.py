#!/usr/bin/python3
#coding: utf-8
import sys, random, os, time, struct, argparse, itertools, bitarray

CLI=argparse.ArgumentParser()
CLI.add_argument("-s", "--size_of_bitmap", default=16384, type=int, help='The size of the bitmap (in bits) to be created. Value will be rounded upwards to the nearest full byte (in bits). Default is 16384.')
CLI.add_argument("-d", "--diff_value", default=3, type=int, help='The difference (increase) in bits between each fragment. Default is 3.')
CLI.add_argument("-f", "--first_value", default=1, type=int, help='The size of the starting fragment. Default is 1.')
CLI.add_argument("-a", "--alloc_fragment_size", default=7, type=int, help='The size of the allocated areas between the fragments (in bits).')
CLI.add_argument("-o", "--output_file_name_of_bitmap", default='standard_bm.bin', help='The file name to save the created bitmap into.')
CLI.add_argument("-r", "--random_dists", action="store_true", help='Use a randomly generated diff between the consecutive sizes of the fragments and also a randomly generated allocated area length between the fragments. Each range is given as (1,diff_value)')
# parse the command line
args = CLI.parse_args()

random.seed()

bm_len = args.size_of_bitmap
is_rand = args.random_dists

def get_sorted_alloc_list(current_bitarray):
    alloc = []
    for k, g in itertools.groupby(enumerate(current_bitarray), lambda x : x[1] == 1):
        if k:
            temp = list(g)
            alloc.append([temp[0][0], len(temp)])
    alloc.sort(key=lambda x : x[1], reverse=True)
    return alloc

def create_bitmap(langd):
    length = ((langd//8)+1)*8
    ba = bitarray.bitarray(length)
    ba.setall(True)
    return ba

def make_unalloc_list(langd,p_diff,alloc_size,is_random):
    unall = []
    part_langd = args.first_value
    nmll = alloc_size
    part_diff = p_diff
    if is_random:
        part_diff = random.randint(args.first_value,args.first_value+p_diff)
        nmll = random.randint(1,alloc_size)
    total_langd = 0
    while total_langd < langd:
        unall.append([part_langd, nmll])
        if is_random:
            part_diff = random.randint(1,p_diff)
            nmll = random.randint(1,alloc_size)
        part_langd += part_diff
        total_langd += part_langd + nmll
    klar_unalloc = []
    pos = 0
    while len(unall):
        listindex = random.randrange(len(unall))
        unall_rad = unall[listindex].copy()
        unall_rad.append(pos)
        klar_unalloc.append(unall_rad)
        pos += unall_rad[0] + unall_rad[1]
        del unall[listindex]
    with open(args.output_file_name_of_bitmap + '.list', 'w') as listfil:
        # 
        listfil.write('\n'.join(['%s %s %s' % (x[2], x[0], x[1]) for x in klar_unalloc]))
        listfil.write('\n')
    klar_unalloc.reverse()
    return klar_unalloc

def populate_bitmap(bitmap,unalloc_list):
    start = 0
    while len(unalloc_list):
        rad = unalloc_list.pop()
        slut = start + rad[0]
        bitmap[start:slut] = False
        start = slut + rad[1]
    return bitmap

min_bitmap = create_bitmap(bm_len)
lista_m_unalloc = make_unalloc_list(bm_len,args.diff_value,args.alloc_fragment_size,is_rand)
antal_frags = len(lista_m_unalloc)
klar_bitmap = populate_bitmap(min_bitmap,lista_m_unalloc)
antal_lediga_block = klar_bitmap.count(False)
fyllnadsgrad = float((bm_len-antal_lediga_block)/bm_len)
with open(args.output_file_name_of_bitmap + '.stats', 'w') as statfil:
    statfil.write('Totalt antal block: %s\nOallokerade block: %s\nAntal fragment: %s\nFyllnadsgrad: %s\n' % (args.size_of_bitmap,antal_lediga_block,antal_frags,fyllnadsgrad))
with open(args.output_file_name_of_bitmap, 'wb') as utfil:
    klar_bitmap.tofile(utfil)
