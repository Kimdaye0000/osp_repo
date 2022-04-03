#!/bin/bash

#a=$(<num1.txt)
#b=$(<num2.txt)
echo "project management in github"
arr=(`cat num1.txt` `cat num2.txt`)

PS3='select menu: '

select cal in "add" "sub" "div" "mul"
do
	break
done

echo "num1:${arr[0]}"
echo "num2:${arr[1]}"
echo "op:$cal"

if [ ${cal} == "add" ]
then
	add=`expr ${arr[0]} + ${arr[1]}`
	echo "result:$add"
elif [ ${cal} == "sub" ]
then
	sub=`expr ${arr[0]} - ${arr[1]}`
	echo "result:$sub"
elif [ ${cal} == "div" ]
then
	div=`expr ${arr[0]} / ${arr[1]}`
	echo "result:$div"
else
	mul=`expr ${arr[0]} \* ${arr[1]}`
	echo "result:$mul"
fi 
