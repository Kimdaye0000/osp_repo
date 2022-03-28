#!/bin/bash

a=$(<num1.txt)
b=$(<num2.txt)

PS3='select menu: '

select cal in "add" "sub" "div" "mul"
do
	break
done

echo "num1:$a"
echo "num2:$b"
echo "op:$cal"

if [ ${cal} == "add" ]
then
	add=`expr $a + $b`
	echo "result:$add"
elif [ ${cal} == "sub" ]
then
	sub=`expr $a - $b`
	echo "result:$sub"
elif [ ${cal} == "div" ]
then
	div=`expr $a / $b`
	echo "result:$div"
else
	mul=`expr $a \* $b`
	echo "result:$mul"
fi 
