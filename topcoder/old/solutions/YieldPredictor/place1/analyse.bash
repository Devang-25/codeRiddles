

fold=0
while [[ $fold -lt 5 ]]; 
do
  cat validation/$1_$fold.txt | grep 'prediction' | awk "BEGIN{best = 1000}{N++; if(\$4 < best) {best = \$4; best_N = N}}END{print $fold, best, best_N}"
  let fold=fold+1
done

cat validation/$1_*.txt |  grep 'prediction' | awk '{T[$2] += $4*$4; N[$2]++}
END{best_t = 1; for(t in T) if(T[t] < T[best_t]) best_t = t; print best_t, N[best_t], sqrt(T[best_t]/N[best_t])}'
