#!/bin/sh

tar xf libs.tar.gz

echo "source gdb_walk_call_stack.py" | gdb -q -n check_flag_format
