#!/bin/bash

python3 simulate_binary.py > sampling.dat
for i in {0..100}; do
    python3 simulate_binary.py >> sampling.dat
    echo $i
done
