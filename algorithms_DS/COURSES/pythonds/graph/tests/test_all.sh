#!/bin/bash


set -u
# set -e

# echo $PWD
check_result(){    
    if [[ ! $? -eq 0 ]]; then
	echo -e "FAIL -- $*\n"
    else
	echo -e "PASS -- $*\n"
    fi
}

# 1
./adj_list_undirected_graph.py  data/undirected.txt  >> /dev/null
check_result Adj graph - undirected

# 2
./adj_list_directed_graph.py data/directed.csv  >> /dev/null
check_result Adj graph - directed

# 3
./ladder_prob_undirected.py  >> /dev/null
check_result word ladder construction - undirected 

# 4
./bfs_undirected.py 0  >> /dev/null
check_result word ladder BFS - undirected

# 5
./bfs_undirected.py 1  >> /dev/null
check_result BFS undirected - digits

# 6
# asks for input
printf '3\n23\n' | ./dfs_directed.py data/directed.csv >> /dev/null
check_result DFS directed

# 7
./knights_tour_graph.py  >> /dev/null
check_result knights tour construction - undirected

# 8
./knights_tour_dfs_undirected_colored.py  >> /dev/null
check_result knights tour DFS colored - undirected

# 9
./knights_tour_warnsdorffs_algo_dfs_undirected.py 8 >> /dev/null
check_result knights tour warnsdorffs algo - DFS colored - undirected
