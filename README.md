# maine-rcv
A collection of scripts and tools to analyze the Maine RCV data from the 2018 2nd Congressional District election

# Usage:
Run each sequentially-numbered script in order. The outputs of the 3rd and 4th scripts are the most useful.
1. Downloads the raw data from the Maine Secretary of State website and compares md5 hashes
2. Converts the `xlsx` files into CSV format, using `@` as the field separator (and taking only the last 5 columns -- e.g. dropping id and location information).
3. Codes the CSV-formatted files into a sequence of 5-character votes, denoting the ranking from left to right by the last initial of candidate. A "U" or "O" represents an undervote or overvote, respectively.
4. Formats and tabulates the 5-string input per official ballot rules (double undervotes, overvotes, etc).
5. Simulates the instant run-off process, outputting intermediate and final results straight to the console.

# Requirements:
Scripts 1-4 use a combination of `wget`, `md5sum`, `csvkit`, `awk`, and `sed`. The simulation uses only a base install of Python 3.

# Notes:
Do whatever you want with these scripts! Please let me know if you find something interesting or substantively improve the data import/cleaning steps.

