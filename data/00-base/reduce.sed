
# invalidate overvote
s/O.*$//;

# invalidate double undervote
s/UU.*$//;

# automatically forward any remaining undervotes
s/U//g;

# remove any repeated rankings
s/\(.\)\(.*\)\1/\1\2/g;
s/\(.\)\(.*\)\1/\1\2/g;
s/\(.\)\(.*\)\1/\1\2/g;
s/\(.\)\(.*\)\1/\1\2/g;

# remove any resulting blank lines
/^$/d

