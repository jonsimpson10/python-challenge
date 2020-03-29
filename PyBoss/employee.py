import os
import csv
from datetime import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'Washington, D.C.': "D.C",
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# Set path for file
csvpath = os.path.join("employee_data.csv")

ID = []
Name = []
DOB = []
SSN = []
State = []
first_name = []
last_name = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")

# Set Header row
  header = next(csvreader)

  for row in csvreader:
     
      ID.append(row[0])
      Name.append(row[1])
      DOB.append(datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
      SSN_Split = row[3].split("-")
      SSN.append("***-**-" + str(SSN_Split[2]))
      
      State.append(us_state_abbrev.get(str(row[4])))
      
      split_name = row[1].split(" ")
      first_name.append(str(split_name[0]))
      last_name.append(str(split_name[1]))

new_csv = zip(ID, first_name, last_name, DOB, SSN, State)

output_file = os.path.join("new_emp.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(new_csv)
    
        




    


