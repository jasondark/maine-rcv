#!/usr/bin/env bash

mkdir -p data/04-reduced
sed -f ./data/00-base/reduce.sed ./data/03-coded/votes.dat | sort | uniq -c | sort -r | sed -e 's/^ *//' -e 's/ /\t/' > ./data/04-reduced/tabulate.txt

