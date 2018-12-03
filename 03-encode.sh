#!/usr/bin/env bash

mkdir -p data/03-coded
awk -f data/00-base/encode.awk data/02-csv/votes.csv > data/03-coded/votes.dat

