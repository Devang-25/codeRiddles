#  1: "I", 
#  5: "V", 
#  10: "X", 
#  50: "L", 
#  100: "C", 
#  500: "D", 
#  1000: "M",

SubIfValue()
{
    # if $decvalue >= $2 then add $3 to romanvalue
    # and subtract $2 from decvalue
    if [ $decvalue -ge $1 ] ; then
	romanvalue="${romanvalue}$2"
	decvalue=$(( $decvalue - $1 ))
    fi
}

# convert_to_roman() {
    
#     if [ $decvalue -ge 1000 ] ; then
# 	SubValue 1000 "M"
#     elif [ $decvalue -ge 900 ] ; then
# 	SubValue 900 "CM"
#     elif [ $decvalue -ge 500 ] ; then
# 	SubValue 500 "D"
#     elif [ $decvalue -ge 400 ] ; then
# 	SubValue 400 "CD"
#     elif [ $decvalue -ge 100 ] ; then
# 	SubValue 100 "C"
#     elif [ $decvalue -ge 90 ] ; then
# 	SubValue 90 "XC"
#     elif [ $decvalue -ge 50 ] ; then
# 	SubValue 50 "L"
#     elif [ $decvalue -ge 40 ] ; then
# 	SubValue 40 "XL"
#     elif [ $decvalue -ge 10 ] ; then
# 	SubValue 10 "X"
#     elif [ $decvalue -ge 9 ] ; then
# 	SubValue 9 "IX"
#     elif [ $decvalue -ge 5 ] ; then
# 	SubValue 5 "V"
#     elif [ $decvalue -ge 4 ] ; then
# 	SubValue 4 "IV"
#     elif [ $decvalue -ge 1 ] ; then
# 	SubValue 1 "I"
#     fi
# }

convert_to_roman() {
    decvalue=$1
    while [ $decvalue -gt 0 ] ; do
	if [ $decvalue -gt 1000 ] ; then
	    romanvalue="$romanvalue"M
	    decvalue=$(( $decvalue - 1000 ))
	elif [ $decvalue -gt 500 ] ; then
	    romanvalue="$romanvalue"D
	    decvalue=$(( $decvalue - 500 ))
	elif [ $decvalue -gt 100 ] ; then
	    romanvalue="$romanvalue"C
	    decvalue=$(( $decvalue - 100 ))
	elif [ $decvalue -gt 50 ] ; then
	    romanvalue="$romanvalue"L
	    decvalue=$(( $decvalue - 50 ))
	elif [ $decvalue -gt 10 ] ; then
	    romanvalue="$romanvalue"X
	    decvalue=$(( $decvalue - 10 ))
	elif [ $decvalue -gt 5 ] ; then
	    romanvalue="$romanvalue"V
	    decvalue=$(( $decvalue - 5 ))
	elif [ $decvalue -ge 1 ] ; then
	    romanvalue="$romanvalue"I
	    decvalue=$(( $decvalue - 1 ))
	fi
    done
    echo "$romanvalue"
}

# convert_to_roman $1

while IFS='$\n' read -r line; do
    echo $line
    convert_to_roman $line
done
