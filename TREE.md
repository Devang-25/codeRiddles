Directory Tree
==============

## Generate HTML Tree through:

### For some pattern:
```
tree . -P '*.txt' -H . -T 'codeRiddles summary' 
```

### To ignore patterns:
```
tree .  -I '*.py|*.java|*.c|*.cpp|*.scala|*.csv|*.pl|*.json'  -H . -T 'codeRiddles summary' 
```

### To exclude empty dirs:
```
tree . -P '*.txt' --prune -H . -T 'codeRiddles summary' 
```

## sample Tree below:

```
Directory Tree

.
├── amazon_challenge
│   └── problems
├── checkio
│   ├── liked_posts
│   ├── Missions
│   ├── station_home
│   ├── station_hubspot
│   └── station_library_2_0
├── codechef
│   └── CDCS2014
├── code-eval
│   └── testcases
├── codeJam
│   ├── 2014
│   └── final
├── gordian_knot_14
│   ├── codecraft
│   └── threads2k
├── gramener
│   └── final
├── hackerEarth
│   ├── algorithms
│   │   └── final
│   ├── CodeBuster
│   ├── CommonFloor
│   ├── february-love
│   ├── mobiwik
│   └── sourcebits
├── hacker_rank
│   └── expansion-challenge
│       ├── dumps
│       └── testcases
├── kaggle
│   └── higgs
├── lab@college
├── ls
├── practice
│   ├── c
│   └── codeGolfs
├── proj_euler
│   └── final
├── pychallenge
│   ├── 1
│   └── 2
├── pythonds
├── spoj
│   └── final
├── topcoder
│   ├── final
│   ├── practice_rooms
│   │   └── SRM_499_DIV_1
│   └── SRM_600_div1
└── udacity

```
