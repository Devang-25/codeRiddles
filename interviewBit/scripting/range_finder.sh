IFS=', ' read -r -a array <<< "$(head -n 1 input)"

# IFS=$'\n'
# unset IFS
IFS=$'\n'
for line in `tail -n +2 input`; do
    # echo $line
    curr=$(echo "$line" | grep -Po '[0-9]+')
    if [[ "$curr" -le "${array[1]}" && "$curr" -ge "${array[0]}" ]]; then
	echo "$line"
    fi
done
