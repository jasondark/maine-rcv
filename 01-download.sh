#!/usr/bin/env bash

mkdir -p data/01-raw && cd data/01-raw && wget -i ../00-base/download.txt && cd ../..
if [[ $(md5sum data/01-raw/* | diff data/00-base/checksum.md5 -) ]]; then
    echo "checksums verified"
else
    echo "checksums do not match!"
fi

