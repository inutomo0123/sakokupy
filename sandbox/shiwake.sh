#!/bin/bash

set -Cue

# comments
cat ftp* | grep "^#" > comment.txt

# header_version
cat ftp* | awk 'BEGIN{FS="|"} {print NF, $0}' | grep "^7 " |
    sed 's/^7 //g' | awk 'BEGIN{FS="|"} { if($1 ~ /^[0-9]/) {print $0}}' > header_version.txt

# available
cat ftp* | awk 'BEGIN{FS="|"} {print NF, $0}' | grep "^7 " |
    sed 's/^7 //g' | awk 'BEGIN{FS="|"} { if($1 !~ /^[0-9]/) {print $0}}' > available.txt

# header_summary
cat ftp* | awk 'BEGIN{FS="|"} {print NF, $0}' | grep "^6 " |
    sed 's/^6 //g' > header_summary.txt

# record
cat ftp* | awk 'BEGIN{FS="|"} {print NF, $0}' | grep "^8 " |
    sed 's/^8 //g' > record.txt
