#!/bin/bash
awk -F',' '
{
    for (i=1; i<=NF; i++) {
        if (NR == 1) {
            header[i] = $i
        } else {
            data[i][NR-1] = $i
        }
    }
}
END {
    for (i=1; i<=NF; i++) {
        printf "%s", header[i]
        for (j=1; j<=NR-1; j++) {
            printf ",%s", data[i][j]
        }
        printf "\n"
    }
}' data.csv
