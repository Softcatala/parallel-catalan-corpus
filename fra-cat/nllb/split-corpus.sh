#!/bin/bash

split_and_rename() {
  local input_file=$1
  local prefix=$2
  local extension=$3

  split -l 2000000 -d "$input_file" "${prefix}-{extension}"

  # Rename the split files to add the specified suffix and start numbering from 1
  a=1
  for i in ${prefix}-{extension}*; do
    mv "$i" "${prefix}-$a.$extension"
    xz -9 -k "${prefix}-$a.$extension" &
    a=$((a+1))
  done
}

split_and_rename "nllb-fra-cat.ca-fr.fr" "nllb-fra-cat" "fr"
split_and_rename "nllb-fra-cat.ca-fr.ca" "nllb-fra-cat" "ca"

ls -ls nllb-fra*

#tmx-to-text convert -f ca-fr.tmx  -s ca -t fr -p nllb-fra-cat

