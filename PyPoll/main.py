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
    
    f=open('election_result.txt','w')

    print("Election Results")
    f.write("Election Results\n")
    print("____________________")
    f.write("____________________\n")
    Tot=len(Votes)
    print("Total Votes:{}".format(Tot))
    f.write("Total Votes:{}\n".format(Tot))
    print("____________________")
    f.write("____________________\n")
    candidates = set(Votes)
    print(f"candidates: {candidates}")
    f.write(f"candidates: {candidates}\n")
    
    winner=list(candidates)[0]
    ss0=Votes.count(winner)
    for name in candidates:
        ss=Votes.count(name)
        ss1=ss/Tot
        print(f"{name}: "+ "{0:.0%}".format(ss1)+f" ({ss})")
        f.write(f"{name}: "+ "{0:.0%}".format(ss1)+f" ({ss})\n")
        if ss>ss0:
            winner=name
            ss0=ss
    print("____________________")
    f.write("____________________\n")
    print(f"Winner:  {winner}")
    f.write(f"Winner:  {winner}\n")
    print("____________________")
    f.write("____________________\n")
    f.close()
    

