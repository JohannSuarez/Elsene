#!/bin/bash

total_time=30
for (( i=0; i<=$total_time; i++ ))
do
    percentage=$(($i * 100 / $total_time))
    echo "$percentage%"
    sleep 1
done
