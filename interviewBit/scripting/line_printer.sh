IFS=', ' read -r -a array <<< "$(head -n 1 input)"
sed -n ''"${array[0]}"',$p;'"${array[1]}"'q' input 
