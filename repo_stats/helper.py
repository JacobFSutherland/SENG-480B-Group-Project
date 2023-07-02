import datetime
import json
import subprocess
import os
from sonarqube import SonarQubeClient

map = {
    1: 10,
    2: 1,
    3: 1,
    4: 4,
    5: 4,
    6: 4,
    7: 4,
    8: 7,
    9: 7,
    10: 7,
    11: 10,
    12: 10,
}

prevQuarter = {
    1: 10,
    10: 7,
    7: 4,
    4: 1,
}

def getAllGitHashes(url, quarters):
    hashes = []
    subprocess.run(['git', 'clone', '--no-checkout' ,url, 'data'], stdout=subprocess.PIPE)
    os.chdir('data') 
    year = datetime.date.today().year
    currentQuarter = map[datetime.date.today().month]

    if(datetime.date.today().month == 1):
        year = year-1
        currentQuarter = prevQuarter(currentQuarter)

    for i in range(quarters):
        command = ['git', 'log', '--merges', '-n', '1', '--pretty=format:%H' , f'--since={year}-{currentQuarter}-01' ,f'--until={year}-{currentQuarter+2}-30']
        hashes.append(subprocess.run(command, stdout=subprocess.PIPE).stdout.decode())
        if(currentQuarter == 1):
            year = year - 1
        currentQuarter = prevQuarter[currentQuarter]

    return hashes; 

def switchToCommitAndRunSonarQube(client, commit):



testHashes = getAllGitHashes("https://github.com/tensorflow/tensorflow.git",  10)
print(testHashes);



