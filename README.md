# jfetch 

This script helps pulling stats about defects trend. It was created for the Embdedded squad.
The script runs a set of query on:
* total number of open defects in te EMBD jira space
* total number of open defects in te EMBD jira space that are not assigned to another team
* total number of open defects in te EMBD jira space that are not assigned to another team, and that are not marked as blocked

The script runs the query for one single date (provided as parameter) or for a list of dates via input text file.

## Setup
1. Clone the repo
2. Make sure you have jira-python installed in your environment [See here](http://jira.readthedocs.io/en/latest/examples.html#initialization)

## How to use

Run *python jfetch.py -h* to get all the instructions.
# jfetch
