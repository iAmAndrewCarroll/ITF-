What best describes what this script does?

#!/bin/bash 

counter=1 
filename="$0" 
filenamefull="$filename$counter" 

while : 
do 
  cp $0 ./"$filenamefull" 
  let "counter+=1" 
  filenamefull="$filename$counter" 
  sleep 1 
done 

- The script will replicate the file it’s in, and continue to do as long as the script is left running

