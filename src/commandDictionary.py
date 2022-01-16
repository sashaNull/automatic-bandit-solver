
solutionDictionary = {'solution_level0': [b'cat readme'],
                      'solution_level1': [b'cat ./-'],
                      'solution_level2': [b'cat spaces\\ in\\ this\\ filename'],
                      'solution_level3': [b'cd inhere/', b'cat .hidden'],
                      'solution_level4': [b'cd inhere/', b'find . | xargs file | grep ASCII | cut -d ":" -f 1 | xargs cat'],
                      'solution_level5': [b'cd inhere/', b'find . -type f -size 1033c | xargs cat'],
                      'solution_level6': [b'find / -user bandit7 -group bandit6 -size 33c 2>&1 | grep -v  -e \'Permission denied\' -e \'No such\' | xargs cat'],
                      'solution_level7': [b'cat data.txt | grep \'millionth\' | cut -f 2'],
                      'solution_level8': [b'sort data.txt | uniq -u'],
                      'solution_level9': [b'strings data.txt | grep \'&=\' | cut -d " " -f 2'],
                      'solution_level10': [b'base64 -d data.txt | cut -d \' \' -f 4'],
                      }


