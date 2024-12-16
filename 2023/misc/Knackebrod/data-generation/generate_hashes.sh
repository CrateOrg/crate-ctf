#!/bin/bash

for file in ./*.pws; do
  while read -r line; do printf %s "$line" | sha1sum | cut -f1 -d' '; done < $file
done
