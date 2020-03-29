import os
import csv
from statistics import mode

total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
Winner = []

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")


# Open the CSV
with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")

# Set Header row
  header = next(csvreader)

  for row in csvreader:
      total_votes += 1
      Winner.append(row[2])
      if row[2] == "Khan":
        Khan_votes += 1
      elif row[2] == "Correy":
        Correy_votes += 1
      elif row[2] == "Li":
        Li_votes += 1
      elif row[2] == "O'Tooley":
        OTooley_votes += 1

Khan_per = int(Khan_votes)/int(total_votes)
Correy_per = int(Correy_votes)/int(total_votes)
Li_per = int(Li_votes)/int(total_votes)
OTooley_per = int(OTooley_votes)/int(total_votes)


print("Election Results")
print("-----------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------")
print("Votes for Khan: " + "{:.3%}".format(Khan_per) + " (" + str(Khan_votes) + ")")
print("Votes for Correy: " + "{:.3%}".format(Correy_per) + " (" + str(Correy_votes) + ")")
print("Votes for Li: " + "{:.3%}".format(Li_per) + " (" + str(Li_votes) + ")" )
print("Votes for O'Tooley: " + "{:.3%}".format(OTooley_per) + " (" + str(OTooley_votes) + ")")
print("-----------------------")
print("Winner: " + mode(Winner))

with open("votes.txt", "w") as txt:
    print("Election Results", file=txt)
    print("-----------------------", file=txt)
    print("Total Votes: " + str(total_votes), file=txt)
    print("-----------------------", file=txt)
    print("Votes for Khan: " + "{:.3%}".format(Khan_per) + " (" + str(Khan_votes) + ")", file=txt)
    print("Votes for Correy: " + "{:.3%}".format(Correy_per) + " (" + str(Correy_votes) + ")", file=txt)
    print("Votes for Li: " + "{:.3%}".format(Li_per) + " (" + str(Li_votes) + ")", file=txt)
    print("Votes for O'Tooley: " + "{:.3%}".format(OTooley_per) + " (" + str(OTooley_votes) + ")", file=txt)
    print("-----------------------", file=txt)
    print("Winner: " + mode(Winner), file=txt)

