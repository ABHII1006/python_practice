#greet_user() {
#	echo "hello, $1"

#}
#greet_user "aegon"
#

### Returning Values:
"""Functions don't return like in other languages, but you can use `echo` and capture it:
"""
add() {
  result=$(( $1 + $2 ))
  echo $result
}

sum=$(add 3 5)
echo "Sum: $sum"
add_nums() {
	sum=$(( $1 + $2 ))
	echo "$sum"
}
add_nums 10 5

#evenorodd(){
#  result=$(($1 % 2))
#  if [ $result -eq 0 ]; then
#    echo "the number is even"
#  else
#    echo "the number is odd"
#  fi
#}
#read -p "tell me the number : " num
#evenorodd $num