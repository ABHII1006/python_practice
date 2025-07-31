#!/bin/bash
echo "hello world!"

#single line comment
<<comm
this is multiline
comment
comm

#name="abhi"
#age=24
#echo "my name is $name and my age is $age"

#give linux command and store that output in the variable so hostname is linux command
#HOSTNAME=$(hostname)
#echo "the host name is $HOSTNAME"

#PWD=$(pwd)
#echo "present working directory is $PWD"

#readonly language="shell script"
#echo "language is $language"
#language="python"
#echo "language is $language"

array=( 1 2 abhi "hello world")
#echo $array
#echo ${array[0]}
#echo ${array[3]}
#echo ${array[@]}
#echo ${array[*]}
#echo ${array[*]:1}
#echo ${array[*]:0:3}
#array+=(new 5 6 "new array")
#echo ${array[*]}

#declare -A array1
#array1=([name]=xyz [city]=hyd [age]=24)
#echo ${array1[*]}
#echo ${array1[0]}
#echo ${array1['city']}
#echo ${array1[age]}
#
#
str="welcome to script"
#echo ${#str}

#echo "upper case---${str^^}"
#echo "lower case---${str,,}"
#echo "${str/script/python}"
#echo $str

#slicing variable:starting index:number of characters
#echo "${str:0:7}"
#echo "${str:11:6}"

#read -p "enter the name" var
#echo $var

x=10
y=10

sum=$x+$y
let sum1=$x+$y

echo "sum of two numbers $sum"
echo "sum of two numbers $sum1"
echo "product of two numbers $(($x*$y))"



read choice
case $choice in
	1)date;;
	2)ls;;
	3)pwd;;
	*)echo "invalid i/p"
esac

random=$RANDOM        # Generates a random integer between 0 and 32767
id -u                 # Prints the current user's UID (User ID)
nohup command &       # Runs a command immune to hangups, even after logout
command > file        # Redirects stdout to file (overwrite)
command >> file       # Appends stdout to file (doesn't overwrite)
at 10:00              # Schedules a one-time command to run at 10:00 AM