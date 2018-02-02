#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
numberOfPOIs = 0
for key in enron_data:
  numberOfPOIs += enron_data[key]['poi']

numberOfSalaries = 0
for key in enron_data:
  if (enron_data[key]['salary'] != 'NaN'):
    numberOfSalaries += 1

numberOfEmails = 0
for key in enron_data:
  if (enron_data[key]['email_address'] != 'NaN'):
    numberOfEmails += 1

print "Total persons of interest: ", numberOfPOIs
print "Total salaries listed: ", numberOfSalaries
print "Total emails listed: ", numberOfEmails
print "Total pay to CEO: ", enron_data["SKILLING JEFFREY K"]["total_payments"] ,'$'
print "Total pay to Chairman: ", enron_data["LAY KENNETH L"]["total_payments"] ,'$'
print "Total pay to CFO: ", enron_data["FASTOW ANDREW S"]["total_payments"] ,'$'

