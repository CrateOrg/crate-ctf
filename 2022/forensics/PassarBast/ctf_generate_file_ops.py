#!/usr/bin/python3
#coding: utf-8
import sys, random, argparse, time, datetime
import alloc_prime_find_closest as pf

CLI=argparse.ArgumentParser()
CLI.add_argument("-n", "--name_of_direct_input_f_sizes_list_file", help='File name of the file holding an ascendingly sorted list of (duplicate) file sizes in 512 B sectors, i e "1 1 1 2 4 4 4 10 10" etcetera.')
CLI.add_argument("-f", "--file_sizes_list", nargs="+", type=int, help='A list of 512 B sectors given as range triplets "start stop step"')
# The order of the actions are in sync with the create_actions_list function (crea, incr, decr, dele)
CLI.add_argument("-a", "--actions_list", nargs=4, type=int, default=[1, 0, 0, 0], help='A list with the weights of the actions in the following order; crea, incr, decr, dele. The default is only crea [1, 0, 0, 0].')
CLI.add_argument("-i", "--increase_actions_list", nargs=4, type=int, default=[1, 0, 0, 0], help='A list with the weights of the action codes to be used when the file system is smaller than the minimum create limit. The weights are given in the following order; crea, incr, decr, dele. The default is [1, 0, 0, 0].')
CLI.add_argument("-d", "--decrease_actions_list", nargs=4, type=int, default=[0, 0, 0, 1], help='A list with the weights of the action codes to be used when the file system is larger than the maximum erase limit. The weights are given in the following order; crea, incr, decr, dele. The default is [0, 1, 0, 0].')
CLI.add_argument("-b", "--block_writing_list", nargs=2, type=int, default=[0, 1], help='A list with the weights of the type of writing for [block, dynamic/stream] writing action. The default is [0, 1].')
CLI.add_argument("-l", "--limit_for_block_writing", type=int, default=65536, help='The maximum size of a file in 512 B sectors that is written as a block, as not to exhaust the RAM of the virtual machine. The default is 65536 (32 MiB).')
CLI.add_argument("-m", "--max_file_size", type=int, default=131072, help='Maximum allowed size of a file in 512 B sectors, regardless of writing type. The default is 131072 (64 MiB).')
CLI.add_argument("-e", "--erase_limits", nargs="+", type=float, default=[.75, .95], help='A list of the [min, max] percentage limits when files are automatically erased. Default is [.75, .95].')
CLI.add_argument("-c", "--create_limits", nargs="+", type=float, default=[.05, .35], help='A list of the [min, max] percentage limits when files are automatically created. Default is [.05, .35].')
CLI.add_argument("-o", "--output_file", default='resulting.actions', help='File name to save the resulting file system operations in. Default is resulting.actions')
CLI.add_argument("-r", "--repetitions", type=int, default=8, help='Number of iterations (file operations) to make. Default is 8.')
CLI.add_argument("-s", "--size_of_filesystem", type=int, default=16384, help='Maximum allowed size of the file system in 512 B sectors (base for the create and erase limits, default 16384 (8 MiB))')
CLI.add_argument("-p", "--prime_file_size_value", action="store_true", help='Let the program convert the values in the file size list to the closest prime values.')

# parse the command line
args = CLI.parse_args()
random.seed()

if len(args.actions_list) != 4:
    sys.exit('All three actions lists should contain exactly 4 posts!')

if args.file_sizes_list == None and args.name_of_direct_input_f_sizes_list_file == None:
    sys.exit('You must use one of -n (file name of the file holding an ascendingly sorted list of file sizes in bytes.) or -f (a list with cluster sizes given as range triplets "start stop step").')
    
def bin_search_less(search_list, search_value):
    left = 0
    right = len(search_list)-1
    while left < right:
        search_pos = (left + right) // 2
        if search_list[search_pos] < search_value:
            left = search_pos + 1
        else:
            right = search_pos
    if left > 0 and search_list[left] > search_value:
        left -= 1
    return left

def bin_search_more(search_list, search_value):
    left = 0
    right = len(search_list)-1
    while left < right:
        search_pos = (left + right) // 2
        if search_list[search_pos] > search_value:
            right = search_pos
        else:
            left = search_pos + 1
    return right

def choose_action(a_list):
    action_prob = random.randint(0, len(a_list)-1)
    ac_tion = a_list[action_prob]
    return ac_tion

def generate_file_size(file_sizs, limit_idx):
    file_prob = random.randint(0, limit_idx)
    filesize = file_sizs[file_prob]
    return filesize

def choose_writing_type(types_list, file_sizs, block_lim):
    if block_lim >= 0:
        type_prob = random.randint(0, len(types_list)-1)
        type_e = types_list[type_prob]
        if type_e == '-b':
            max_file_siz_index = bin_search_less(file_sizs, block_lim)
            f_size = generate_file_size(file_sizs, max_file_siz_index)
        else:
            f_size = generate_file_size(file_sizs, len(file_sizs)-1)
    else:
        type_e = '-d'
        f_size = generate_file_size(file_sizs, len(file_sizs)-1)
    return type_e, f_size

def create_file(types_list, files_list, seq_number, filesys_size, filesizes, bl_lim):
    #starttid = time.time()
    failed = True
    file_name = str(seq_number)
    blk_wrt, file_size = choose_writing_type(types_list, filesizes, bl_lim)
    #crea1 = int(((time.time()-starttid))*1000000000)
    #nasta_tid = time.time()
    external_commands = 'crea ' + str(seq_number) + ' ' + file_name + ' ' + str(file_size) + ' ' + blk_wrt
    bitmap = write_external_command(external_commands)
    #crea2 = int(((time.time()-nasta_tid))*1000000000)
    #nasta_tid = time.time()
    if bitmap == 0:
        filesys_size += file_size
        files_list.append([file_name, file_size])
        #crea3 = int(((time.time()-nasta_tid))*1000000000)
        #nasta_tid = time.time()
        fs_util_file.write(str(filesys_size) + ' ' + str(round(float(filesys_size/max_fs_size)*1000)) + ' ' + str(len(files_list)) + '\n')
        #crea4 = int(((time.time()-nasta_tid))*1000000000)
        failed = False
    #print('CREA fkn: %s %s %s %s %s %s' % (int(((time.time()-starttid))*1000000000), crea1, crea2, crea3, crea4, seq_number))
    return files_list, filesys_size, failed

def delete_file(files_list, seq_number, filesys_size):
    starttid = time.time()
    failed = True
    if len(files_list) > 0:
        deleted_file = random.randint(0,len(files_list)-1)
        file_name = files_list[deleted_file][0]
        external_commands = 'dele ' + str(seq_number) + ' ' + file_name + ' ' + str(files_list[deleted_file][1])
        bitmap = write_external_command(external_commands)
        if bitmap == 0:
            filesys_size -= files_list[deleted_file][1]
            del files_list[deleted_file]
            fs_util_file.write(str(filesys_size) + ' ' + str(round(float(filesys_size/max_fs_size)*1000)) + ' ' + str(len(files_list)) + '\n')
            failed = False
#    print('DELE fkn: %s' % int(((time.time()-starttid))*1000000000))
    return files_list, filesys_size, failed

def increase_file(types_list, files_list, seq_number, filesys_size, filesizes, bl_lim, max_f_size):
    starttid = time.time()
    failed = True
    if len(files_list) > 0:
        max_idx = 1
        temp_files_list = files_list.copy()
        while len(temp_files_list) and max_idx < 2:
            increased_file = random.randint(0,len(temp_files_list)-1)
            file_name = temp_files_list[increased_file][0]
            limit = bl_lim - temp_files_list[increased_file][1]
            max_idx = bin_search_less(filesizes, max_f_size - temp_files_list[increased_file][1])
            del temp_files_list[increased_file]
        if len(temp_files_list) and max_idx > 1:
            increase_sizes = filesizes[:max_idx]
            blk_wrt, added_size = choose_writing_type(types_list, increase_sizes, limit)
            external_commands = 'incr ' + str(seq_number) + ' ' + file_name + ' ' + str(added_size) + ' ' + blk_wrt
            bitmap = write_external_command(external_commands)
            if bitmap == 0:
                filesys_size += added_size
                files_list[increased_file][1] += added_size
                fs_util_file.write(str(filesys_size) + ' ' + str(round(float(filesys_size/max_fs_size)*1000)) + ' ' + str(len(files_list)) + '\n')
                increase_sizes.clear()
                failed = False
#    print('INCR fkn: %s' % int(((time.time()-starttid))*1000000000))
    return files_list, filesys_size, failed

def decrease_file(types_list, files_list, seq_number, filesys_size, filesizes, bl_lim):
    starttid = time.time()
    failed = True
    if len(files_list) > 0:
        max_idx = 1
        temp_files_list = files_list.copy()
        while len(temp_files_list) and max_idx < 2:
            decreased_file = random.randint(0,len(temp_files_list)-1)
            curr_size = temp_files_list[decreased_file][1]
            max_idx = bin_search_less(filesizes, curr_size-1)
            del temp_files_list[decreased_file]
        if len(temp_files_list) and max_idx > 1:
            decr_sizes = filesizes[:max_idx]
            blk_wrt, new_size = choose_writing_type(types_list, decr_sizes, bl_lim)
            file_name = files_list[decreased_file][0]
            external_commands = 'decr ' + str(seq_number) + ' ' + file_name + ' ' + str(new_size) + ' ' + blk_wrt
            bitmap = write_external_command(external_commands)
            if bitmap == 0:
                filesys_size -= (curr_size - new_size)
                files_list[decreased_file][1] = new_size
                fs_util_file.write(str(filesys_size) + ' ' + str(round(float(filesys_size/max_fs_size)*1000)) + ' ' + str(len(files_list)) + '\n')
                decr_sizes.clear()
                failed = False
#    print('DECR fkn: %s' % int(((time.time()-starttid))*1000000000))
    return files_list, filesys_size, failed

def write_external_command(ext_commands):
    try:
        action_file.write(ext_commands + '\n')
        b_map = 0
    except:
        b_map = 1
    return b_map

# The order of the actions in the list are in sync with the order in the alloc_algo_generated_test_named_pipes_v5.py
def create_actions_list(a_list):
    act_no = 0
    a_types_list = ['crea', 'incr', 'decr', 'dele']
    acts = []
    for act_amount in a_list:
        temp_act = [a_types_list[act_no]]
        temp_act *= act_amount
        acts += temp_act
        act_no += 1
    return acts

stop_repetitions = args.repetitions
action_file = open(args.output_file, 'w')
fs_util_file = open(args.output_file + '.fs_util', 'w')
maximum_file_size = args.max_file_size
types = []
type_no = 0

# Create list of file sizes from file_sizes_list
prime_number_list = []
if args.file_sizes_list != None:
    file_sizes_list  = args.file_sizes_list
    if not len(file_sizes_list) % 3:
        raknare = 1
        lista = []
        temp_file_sizes = []
        for tal in file_sizes_list:
            if args.prime_file_size_value:
                tal = pf.main(tal)
            lista.append(tal)
            if not raknare % 3:
                prime_number_list.extend(lista)
                for del_range in range(lista[0],lista[1],lista[2]):
                    temp_file_sizes.append(del_range)
                lista = []
            raknare = ( raknare + 1 ) % 3
        temp_file_sizes.sort()
        max_index = bin_search_less(temp_file_sizes, maximum_file_size)
        file_sizes = temp_file_sizes[:max_index]
        temp_file_sizes.clear()
    else:
        action_file.close()
        fs_util_file.close()
        sys.exit('The cluster list should contain full tripplets, i e len(cluster_list) % 3 == 0')

# Convert a file with file sizes in either one column or two column (size, number of) format
if args.name_of_direct_input_f_sizes_list_file != None:
    with open(args.name_of_direct_input_f_sizes_list_file, 'r') as file_sizes_file:
        hela_filen = file_sizes_file.readlines()
        temp_file_sizes = []
        if hela_filen[0].find(' ') > 0:
            for line in hela_filen:
                pos, antal = line.strip().split(' ')
                if args.prime_file_size_value:
                    tal = str(pf.main(int(pos)))
                    pos = tal
                temp_lista = [pos]
                temp_lista *= int(antal)
                del_lista = [int(x) for x in temp_lista]
                temp_file_sizes.extend(del_lista)
        else:
            temp_file_sizes = [int(x) for x in hela_filen]
        temp_file_sizes.sort()
        max_index = bin_search_less(temp_file_sizes, maximum_file_size)
        file_sizes = temp_file_sizes[:max_index]
        temp_file_sizes.clear()
        
# Create list of writing types according to weights ([block, dynamic])
if args.block_writing_list[1] < 1 and args.limit_for_block_writing < max(file_sizes):
    action_file.close()
    fs_util_file.close()
    sys.exit('The block writing limit cannot be smaller than the maximum file size when only block writing is to be done (block_writing_list = [x,0]; x > 0).')
for type_amount in args.block_writing_list:
    # -b is block writing and -d is the default stream writing
    type_alternatives = ['-b', '-d']
    while type_amount:
        types.append(type_alternatives[type_no])
        type_amount -= 1
    type_no += 1

# Write action_file header with all settings
if args.file_sizes_list != None:
    f_sizes_source = 'f_sizes_file'
    f_sizes_content = str(prime_number_list)
if args.name_of_direct_input_f_sizes_list_file != None:
    f_sizes_source = 'f_sizes_file'
    f_sizes_content = args.name_of_direct_input_f_sizes_list_file
action_file.write('%s#std_a_lst#inc_a_list#dec_a_list#bl_wr_lst#b_w_lim#erase#creat#iters#fs_size\n' % (f_sizes_source))
action_file.write(f_sizes_content + '#' + str(args.actions_list) + '#' + str(args.increase_actions_list) + '#' + str(args.decrease_actions_list) + '#' + str(args.block_writing_list) + '#' + str(args.limit_for_block_writing) + '#' + str(args.erase_limits) + '#' + str(args.create_limits) + '#' + str(args.repetitions) + '#' + str(args.size_of_filesystem) + '\n')
    
    
# Create list of actions according to weights ([create, increase, decrease, delete])
############ Fixa till en increase_actions och en decrease_actions också
std_actions = create_actions_list(args.actions_list)
inc_actions = create_actions_list(args.increase_actions_list)
dec_actions = create_actions_list(args.decrease_actions_list)

max_fs_size = args.size_of_filesystem
block_limit = args.limit_for_block_writing
fs_size = seq_no = 0
files = []
e_lim = args.erase_limits
c_lim = args.create_limits
if e_lim[0] > e_lim[1]:
    start_limit_erase = e_lim[0]
    stop_limit_erase = e_lim[1]
else:
    start_limit_erase = e_lim[1]
    stop_limit_erase = e_lim[0]
if c_lim[0] < c_lim[1]:
    start_limit_create = c_lim[0]
    stop_limit_create = c_lim[1]
else:
    start_limit_create = c_lim[1]
    stop_limit_create = c_lim[0]
mfs_start_erase = max_fs_size*start_limit_erase
mfs_stop_erase = max_fs_size*stop_limit_erase
mfs_start_create = max_fs_size*start_limit_create
mfs_stop_create = max_fs_size*stop_limit_create

# Start the main repetitions
actions = std_actions.copy()
increase = False
decrease = False
while stop_repetitions > 0:
    fail = False
    action = choose_action(actions)
    if not increase and fs_size < mfs_start_create:
        files, fs_size, fail = create_file(types, files, seq_no, fs_size, file_sizes, block_limit)
        increase = True
        actions = inc_actions.copy()
    elif increase and fs_size > mfs_stop_create:
        increase = False
        actions = std_actions.copy()
        fail = True
    elif increase and fs_size < mfs_start_create:
        files, fs_size, fail = create_file(types, files, seq_no, fs_size, file_sizes, block_limit)
    elif not decrease and fs_size > mfs_start_erase:
        files, fs_size, fail = delete_file(files, seq_no, fs_size)
        decrease = True
        actions = dec_actions.copy()
    elif decrease and fs_size < mfs_stop_erase:
        decrease = False
        actions = std_actions.copy()
        fail = True
    elif decrease and fs_size > mfs_start_erase:
        files, fs_size, fail = delete_file(files, seq_no, fs_size)            
    elif action == 'crea':
        files, fs_size, fail = create_file(types, files, seq_no, fs_size, file_sizes, block_limit)
    elif action == 'dele':
        files, fs_size, fail = delete_file(files, seq_no, fs_size)
    elif action == 'incr':
        files, fs_size, fail = increase_file(types, files, seq_no, fs_size, file_sizes, block_limit, maximum_file_size)
    elif action == 'decr':
        files, fs_size, fail = decrease_file(types, files, seq_no, fs_size, file_sizes, block_limit)
    stop_repetitions -= 1
    seq_no += 1
    if fail:
        stop_repetitions += 1
        seq_no -= 1
# Adding EoFIFO to the end of action_file to stop the client FIFO when done.
action_file.write('halt EoFIFO\n')
action_file.close()
fs_util_file.close()
