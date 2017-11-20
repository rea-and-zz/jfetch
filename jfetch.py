from jira import JIRA
import re
import argparse


def query_on_day(day):
    day = day.rstrip()
    # query for all open defects in the space, on that day
    q1 = 'project = EMBD AND issuetype = Bug AND status was in  (\"In Progress\", Backlog, \"Under Review\", \"To Do\", \"Under investigation\") DURING (\"' + day + "\",\"" + day + "\")"
    r1 = jira.search_issues(jql_str=q1, json_result=False, fields="key")
    # query for all defects in the space, except one with DLC, CTL or Playback component
    q2 = 'project = EMBD AND issuetype = Bug AND status was in  (\"In Progress\", Backlog, \"Under Review\", \"To Do\", \"Under investigation\") DURING (\"' + day + "\",\"" + day + "\") AND \"EMBD Component / Owner\" in (Embedded, Unspecified)"
    r2 = jira.search_issues(jql_str=q2, json_result=False, fields="key")
    # query for all defects in the space, except one with DLC, CTL or Playback component and except ones that are flagged
    q3 = 'project = EMBD AND issuetype = Bug AND status was in  (\"In Progress\", Backlog, \"Under Review\", \"To Do\", \"Under investigation\") DURING (\"' + day + "\",\"" + day + "\") AND \"EMBD Component / Owner\" in (Embedded, Unspecified) AND Flagged is EMPTY"
    r3 = jira.search_issues(jql_str=q3, json_result=False, fields="key")
    print("ON " + day + ":\t" + str(len(r1)) + "\t" + str(len(r2)) + "\t" + str(len(r3)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", help="your jira user account (default is andreac)", type=str)
    parser.add_argument("password", help="your jira account password", type=str)
    parser.add_argument("--days_list_file", help="the name of a file you want to use as input, to run the query on each date", type=str)
    parser.add_argument("--day", help="the specific date you want to get the stats for (format YYYY/MM/DD)", type=str)
    args = parser.parse_args()

    jira_options = {
        'server': 'https://jira.spotify.net'}

    print("Connecting to JIRA server...")

    if args.user:
        jira = JIRA(jira_options, basic_auth=(args.user, args.password))
    else:
        jira = JIRA(jira_options, basic_auth=('andreac', args.password))

    print("Successfully connected. Starting to pull data...")

    if args.day:
        query_on_day(args.day)
    else:
        days_list_file = "weeks.txt"
        if args.days_list_file:
            days_list_file = args.days_list_file

        with open(days_list_file) as f:
            for day in f:
                query_on_day(day)



