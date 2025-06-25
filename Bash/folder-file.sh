#!/bin/bash

#Variables block
WORKINGPATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STRING="file2"
TIMESTAMP=$(date +"%Y-%m-%d-%H:%M")

#Cleaning up garbage and prepare test folder for new run
rm $WORKINGPATH/*.txt
rm $WORKINGPATH/%STRING.old
touch $WORKINGPATH/$STRING
echo
#Get input from user for filename
echo "Guess The Filename:"
read InputFilename

VAR=$InputFilename
[[ "$STRING" = "$VAR" ]] && echo "Correct Filename! It's already existed, renaming to $STRING.old" || echo "Filename is wrong"
mv $WORKINGPATH/$STRING $WORKINGPATH/$STRING.old
echo
echo "Creating file with current timestamp"
touch $WORKINGPATH/$TIMESTAMP.txt
echo
echo "Writing $STRING.old Filename into file with timestamp"
echo $STRING.old >> $WORKINGPATH/$TIMESTAMP.txt
echo
echo "Printing the added filename:"; cat $WORKINGPATH/$TIMESTAMP.txt
echo
echo "Files after the script running"
echo
ls -l $WORKINGPATH
