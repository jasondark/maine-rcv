#!/usr/bin/env bash

command -v in2csv >/dev/null 2>&1 || { echo >&2 "csvkit not installed. please install csvkit to continue."; exit 1; }
mkdir -p data/02-csv
rm -rf data/02-csv/*
touch data/02-csv/votes.csv

for file in ./data/01-raw/*.xlsx
do
    in2csv $file | csvformat -D'@' | awk -F'@' 'BEGIN { OFS="@" } NR>1 {print $(NF-4), $(NF-3), $(NF-2), $(NF-1), $(NF)}' >> data/02-csv/votes.csv
done

