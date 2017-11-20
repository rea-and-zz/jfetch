# jfetch 

This script helps pulling stats about defects trend.
The script runs a set of query on:
* total number of open defects in for a given EMBD jira project
* total number of open defects in for a given EMBD jira project, with a further filter on component
* total number of open defects in for a given EMBD jira project, with a further filter on component and filter on blocked tickets

The script runs the query for one single date (provided as parameter) or for a list of dates via input text file.

## Setup
1. Clone the repo
2. Make sure you have jira-python installed in your environment [See here](http://jira.readthedocs.io/en/latest/examples.html#initialization)

## How to use

Run *python jfetch.py -h* to get all the instructions.
