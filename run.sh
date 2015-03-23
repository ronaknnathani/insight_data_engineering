#!/usr/bin/env bash

#setting permissions
chmod a+x ./src/word_count_running_median.py

# executing the script
python ./src/word_count_running_median.py ./wc_input ./wc_output/wc_result.txt ./wc_output/med_result.txt
