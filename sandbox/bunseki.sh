#!/bin/bash

set -Cue

_files=('ftp.afrinic.net' 'ftp.apnic.net' 'ftp.arin.net' \
                         'ftp.lacnic.net' 'ftp.ripe.net')

for e in "${_files[@]}" ; do
    echo "${e}"

    awk  ' BEGIN {FS="|"} { print NF }' "${e}" | sort  | uniq -c
done
