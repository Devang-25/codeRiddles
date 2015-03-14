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
.
├── algorithms
├── amazon_challenge
│   └── problems
│       ├── fibonacci_factor.txt
│       └── shortest_sub_segment.txt
├── checkio
│   ├── Elementary
│   ├── liked_posts
│   ├── Missions
│   ├── station_home
│   ├── station_hubspot
│   └── station_library_2_0
├── codechef
│   └── CDCS2014
├── code-eval
│   └── testcases
│       ├── fizz.txt
│       ├── primes.txt
│       └── reverse_add.txt
├── codeJam
│   ├── 2014
│   │   └── cookie_clicker_alpha.txt
│   └── final
│       └── p1.txt
├── gordian_knot_14
│   ├── codecraft
│   └── threads2k
├── gramener
│   ├── data.txt
│   ├── diamond.txt
│   ├── final
│   │   └── gr.txt
│   └── gr.txt
├── hackerEarth
│   ├── algorithms
│   │   └── final
│   ├── CodeBuster
│   ├── CommonFloor
│   ├── february-love
│   ├── mobiwik
│   ├── sourcebits
│   └── thoughtworks-challenge
├── hacker_rank
│   └── expansion-challenge
│       ├── dumps
│       └── testcases
│           ├── minima.txt
│           └── temperature.txt
├── kaggle
│   └── higgs
├── lab@college
│   ├── java
│   └── prolog
├── practice
│   ├── a.txt
│   ├── c
│   └── codeGolfs
├── proj_euler
│   └── final
├── pychallenge
│   ├── 0.txt
│   ├── 1
│   └── 2
│       └── ocr.txt
├── pythonds
├── spoj
│   └── final
├── topcoder
│   ├── final
│   ├── practice_rooms
│   │   └── SRM_499_DIV_1
│   └── SRM_600_div1
└── udacity

57 directories, 16 files

```
