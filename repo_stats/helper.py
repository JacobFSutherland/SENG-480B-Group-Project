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

appPath = os.getcwd();

def getAllGitHashes(quarters):
    hashes = []
    subprocess.run(['git', 'clone', '--no-checkout' ,"${GIT_URL}", 'repoData'], stdout=subprocess.PIPE).stdout.decode()
    os.chdir('repoData')
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

def cloneRepo():
    os.chdir(appPath)
    cloneResult = subprocess.run(['git', 'clone' ,"${GIT_URL}" , 'data'], stdout=subprocess.PIPE).stdout.decode()
    os.chdir("data")

def switchToCommitAndRunSonarQube(hash):
    res = subprocess.run(['git', 'reset', '--hard', hash], stdout=subprocess.PIPE).stdout.decode()
    print("Checkout result: ", res)
    os.chdir(appPath) 
    run_sonar_scanner()
    os.chdir('data') 



def run_sonar_scanner():
    try:
        res = subprocess.run(['sonar-scanner'], stdout=subprocess.PIPE).stdout.decode()
        print(f"SonarScanner returned with exit code {res}")
    except Exception as e:
        print(f"Error when running SonarScanner: {e}")


def main():
    hashes = getAllGitHashes( 10)
    cloneRepo()
    for hash in hashes:
        print(f'Switching to hash {hash}')
        switchToCommitAndRunSonarQube(hash)

main()
