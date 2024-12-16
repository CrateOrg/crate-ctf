#!/usr/bin/python3
#coding: utf-8
import sys, argparse, random, itertools, bitarray, hashlib, struct, time, string
from bisect import bisect_left

CLI=argparse.ArgumentParser()
CLI.add_argument("-f", "--file_system_file_name", required=True, help='The name of the big file to write the allocated data into.')
CLI.add_argument("-o", "--op_file_name", required=True, help='The name of the file containing the file operations.')
CLI.add_argument("-b", "--bitmap_file_name", required=True, help='The file name of the bitmap file to use for allocation.')
CLI.add_argument("-c", "--cluster_size", default=1, type=int, help='The size (in sectors) of the clusters to write to the file system file. Default is 1')
CLI.add_argument("-s", "--string_as_file_content", default='', help='A string to fill the file(s) with. Default is an empty string.')
CLI.add_argument("-l", "--length_of_pattern", type=int, default=1, help='The length of the repeating pattern of the file content. Default is 1.')
CLI.add_argument("-p", "--printable_chars_only", action="store_true", help='Use only printable characters when generating content of the fragments.')
#CLI.add_argument("-r", "--random_dists", action="store_true", help='Use a randomly generated diff between the consecutive sizes of the fragments and also a randomly generated allocated area length between the fragments. Each range is given as (1,diff_value)')
# parse the command line

args = CLI.parse_args()

def get_sorted_free_alloc_list(current_bitarray):
    alloc = []
    for k, g in itertools.groupby(enumerate(current_bitarray), lambda x : x[1] == 0):
        if k:
            temp = list(g)
            alloc.append([temp[0][0], len(temp)])
    alloc.sort(key=lambda x : x[1])
    return alloc

def create_bitmap(bitarray_file):
    ba = bitarray.bitarray()
    ba.fromfile(bitarray_file)
    return ba

def calc_string_repetitions(pattern_length):
    if pattern_length > 8 or pattern_length < 1:
        pattern_length = 1
    str_reps = 512//pattern_length
    bin_str = '@'
    if pattern_length == 1:
        bin_str += 'B'
    elif pattern_length == 2 or pattern_length == 3:
        bin_str += 'H'
    elif pattern_length > 3 and pattern_length < 8:
        bin_str += 'I'
    else:
        bin_str += 'L'
    return bin_str, str_reps
            

def write_file_data(op_file,fs_file,bm_array,frags,clu_size,pat_len,flag):
    #Filformat (allt angivet i 512 B block): 'crea' seq_no filename size blk_wrt
    curr_unalloc_list = get_sorted_free_alloc_list(bm_array)
    storlekar = [x[1] for x in curr_unalloc_list]
    for rad in op_file:
        raddelar = rad.split(' ')
        if len(raddelar) > 2:
            filstorlek = int(raddelar[3])
            f_name = raddelar[2]
            frag_no = 0
            ackum_slump_data = '0x'
            bokstaver = ''
            binary_format, string_repetitions = calc_string_repetitions(pat_len)
            while filstorlek > 0:
                if len(curr_unalloc_list) > 0:
                    alloc_bitmap_item = bisect_left(storlekar,filstorlek)
                    if alloc_bitmap_item == len(curr_unalloc_list):
                        alloc_bitmap_item -= 1
                    poppat = curr_unalloc_list.pop(alloc_bitmap_item)
                    del storlekar[alloc_bitmap_item]
                    start = poppat[0]
                    langd = poppat[1]
                    filstorlek -= langd
                    if is_custom_string and len(flag) > 0:
                        slump_data = flag.pop()
                    else:
                        slump_data = random.randint(1,256**pat_len)
                    ackum_slump_data += hex(slump_data)[2:].upper()
                    if args.printable_chars_only:
                        bokstaver += chr(slump_data)
                    if filstorlek >= 0:
                        skriv_data = struct.pack(binary_format, slump_data)*(string_repetitions*clu_size*langd)
                        fraglangd = len(skriv_data)
                        remaining = 0
                        stopp = start + langd
                    else:
                        skriv_data = struct.pack(binary_format, slump_data)*(string_repetitions*clu_size*(langd+filstorlek))
                        fraglangd = len(skriv_data)
                        skriv_data += struct.pack('@B', 0)*512*clu_size*abs(filstorlek)
                        remaining = abs(filstorlek)
                        stopp = start + (langd+filstorlek)
                    bm_array[start:stopp] = True
                    fs_file.seek(start*512*clu_size,0)
                    fs_file.write(skriv_data)
                    hex_little_endian = slump_data.to_bytes(pat_len,"little").hex().upper()
                    start_pos = start*512*clu_size
                    frags.append([f_name,str(frag_no),str(start_pos),str(fraglangd),str(remaining),format(start_pos,'X'),format(fraglangd,'X'),format(remaining,'X'),hex_little_endian,ackum_slump_data,bokstaver])
                    frag_no += 1
                else:
                    sys.exit('No space left in %s' % (args.file_system_file_name))
    return bm_array, frags

######### Start of main code
if len(args.string_as_file_content) > 0 and not args.printable_chars_only:
    is_custom_string = True
    patt_length = 1
    flaggan = [ord(args.string_as_file_content[i:i + patt_length]) for i in range(0, len(args.string_as_file_content), patt_length)]
elif len(args.string_as_file_content) < 1 and not args.printable_chars_only:
    is_custom_string = False
    patt_length = args.length_of_pattern
    flaggan = []
elif len(args.string_as_file_content) < 1 and args.printable_chars_only:
    is_custom_string = True
    patt_length = 1
    s_printab = string.ascii_letters + string.digits + '+-._=!<>:#'
    flaggan_temp = [ord(s_printab[i:i + patt_length]) for i in range(0, len(s_printab), patt_length)]
    flaggan = random.sample(flaggan_temp,len(flaggan_temp))
else:
    sys.exit('You cannot use both -s and -p at the same time! Choose one of them!\n')
    

fragment = []
with open(args.op_file_name, 'r') as opfil:
    data_2_hash = opfil.read(100000000).encode('utf-8')
    random_seed_hash = hashlib.sha1(data_2_hash).hexdigest()
    random.seed(random_seed_hash)
    opfil.seek(0)
    opfil.readline()
    opfil.readline()
    with open(args.file_system_file_name, 'r+b') as fsfil:
        with open(args.bitmap_file_name, 'rb') as bmfil:
            bitm_array = create_bitmap(bmfil)
        klar_bm_array, fragment = write_file_data(opfil,fsfil,bitm_array,fragment,args.cluster_size,patt_length,flaggan)
with open(args.bitmap_file_name + '.finished', 'wb') as bmklarfil:
    klar_bm_array.tofile(bmklarfil)
with open(args.file_system_file_name + '.frag_list', 'w') as fragfil:
    frags_temp = [' '.join(x) for x in fragment]
    fragfil.write('\n'.join(frags_temp))
    fragfil.write('\n')
