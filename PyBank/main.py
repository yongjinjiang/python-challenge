import csv
import os

resource_dir="/Users/jyj/OneDrive/A_A_Data_Analysis/MINSTP201808DATA2/03-Python/Homework/PyBank/Resources"
file_path=os.path.join(resource_dir,"budget_data.csv")

with open(file_path,newline="") as data_file:
     csvreader=csv.reader(data_file,delimiter=",")
     next(csvreader)
     i=0
     Num_month=0
     Pro_each_month=[]
     months=[]
     for row in csvreader:
         #print(row)
         months.append(row[0])
         Pro_each_month.append(float(row[1]))
        #  if i==5:
        #      break
        #  i=i+1
         
         Num_month=Num_month+1
     print("Financial Analysis")
     print("____________________")
     print("Total Months:{}".format(Num_month))
     print("Total:${}".format(sum(Pro_each_month)))

     ss1=Pro_each_month[:-1]
     ss2=Pro_each_month[1:]
     ss=[ss2[i]-ss1[i] for i in range(Num_month-1)]

     print("Average change:${}".format(sum(ss)/(Num_month-1)))
     print("Greatest increase in Profits :{} (${})".format(months[ss.index(max(ss))+1],max(ss)))
     print("Greatest Decrease in Profits :{} (${})".format(months[ss.index(min(ss))+1],min(ss)))
    