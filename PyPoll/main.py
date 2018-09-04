import csv
import os

resource_dir="/Users/jyj/OneDrive/A_A_Data_Analysis/MINSTP201808DATA2/03-Python/Homework/PyPoll/Resources"

file_path=os.path.join(resource_dir,"election_data.csv")

with open(file_path,newline="") as data_file:
    csvreader=csv.reader(data_file,delimiter=",")
    next(csvreader)
    i=0
    Votes=[] 
    for row in csvreader:
         Votes.append(row[2])
    print("Election Results")
    print("____________________")
    Tot=len(Votes)
    print("Total Votes:{}".format(Tot))
    print("____________________")
    candidates = set(Votes)
    print(f"candidates: {candidates}")
    
    winner=list(candidates)[0]
    ss0=Votes.count(winner)
    for name in candidates:
        ss=Votes.count(name)
        ss1=ss/Tot
        print(f"{name}: "+ "{0:.0%}".format(ss1)+f" ({ss})")
        if ss>ss0:
            winner=name
            ss0=ss

    print("____________________")
    print(f"Winner:  {winner}")
    print("____________________")


