#!/bin/bash
# Usage: $ ./disease_sweep M 100 20 10 15 25 25 15
expDir=disease`date "+%Y-%m-%d_%H:%M:%S"`

mkdir $expDir
cp *.py $expDir
cp disease_sweep.sh $expDir
cd $expDir

# DEFAULT VALUES
steps=10
print="N"

# COMMAND LINE VALUES
neighbourhood=$1
pop=$2
infected=$3
rc_step=$4

low_row=$5
high_row=$6
low_col=$7
high_col=$8

echo 
echo "######## Parameters used ########"
echo "Neighbourhood type: " $neighbourhood
echo "Population: " $pop
echo "Number infected: " $infected
echo "Rows: " $low_row " to " $high_row
echo "Columns: " $low_col " to " $high_col
echo "Row and column interval: " $rc_step

echo 
echo "######## Default values used ########"
echo "Show plots: " $print
echo "Number of steps in each test: " $steps

for r in `seq $low_row $rc_step $high_row`;
do
    for c in `seq $low_col $rc_step $high_col`;
    do
        echo "Experiment: " $r $c
        outfile="Dosage_R"$r"_C"$c".txt"
        python3 diseaseSim.py $neighbourhood $pop $infected $c $r $steps $print > $outfile
    done
done