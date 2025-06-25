#!/bin/bash

WORKINGPATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILE=$WORKINGPATH/count-cubes.txt
#clear
> $FILE
echo
echo

SUM=0

for I in {1..100}; do
  CUBE=$(echo "$I^3" | bc)
  SUM=$(echo "$SUM + $CUBE" | bc)
done
echo "Summ of the Cubes of 1 to 100 is $SUM"
echo $SUM >> $FILE

for i in {1..10}; do 
  NUMB=$(( (RANDOM % 80) + 1 ));
  echo  "10 Random numbers {1..80} are: $NUMB"
  echo $NUMB >> $FILE
  done
echo
echo

tail -n +2 "$FILE" | while read GISTNUM; do
  echo -n $GISTNUM;
  for ((i = 0; i < GISTNUM; i += 3)); do
    echo -n "*"
  done
  echo
done
