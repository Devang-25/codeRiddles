# curr=( $(cut -d ',' -f5 input.csv ) )
# cut -d, -f5 -f7 --complement input.csv > input.new.csv
# mv input.new.csv  input.csv

code=( $(cut -d ',' -f5 input.csv ) )
phone=( $(cut -d ',' -f7 input.csv ) )

# cut -d, -f5,7  --complement input.csv

phones=()
cnt=$(wc -l < input.csv)

for ((i=0; i<cnt; i++)); do
    phones+=("+${code[i]}-${phone[i]}")
done

paste -d, <(cut -d, -f5,7 --complement input.csv) <( IFS=$'\n'; echo "${phones[*]}" )
