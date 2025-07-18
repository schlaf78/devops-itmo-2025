#!/bin/bash
set -v
String="UserGate is the best NGFW ever."
echo ${#String}
echo ${String:26}
echo ${String:21:4}
echo ${String::8}
echo ${String#*\ }
echo ${String%\ *}
echo ${String##*\ }
echo ${String%%\ *}
echo ${String/NGFW/SIEM}
echo ${String/%ever./in the World.}
#echo "${String^^}"
VARS=${!BASH*}
echo $VARS
exec 6<&0
exec < pretty-vars.sh
while read LINE; do
ARRAY[$count]=$LINE
((count++))
done
exec 0<&6 6<&-
exec 1>&6
exec > test.test
for ((i=0;i < ${#ARRAY[@]};i++)); do
echo ${ARRAY[$i]}
done
exec 6>&1 
