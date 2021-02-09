
cp Solution.cpp validation/$1.cpp
g++ Solution.cpp -O2 -o validation/$1

fold=0
while [[ $fold -lt 5 ]]; 
do
  validation/$1 $fold 2> validation/$1_$fold.txt
  echo $fold
  let fold=fold+1
done


