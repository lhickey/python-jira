from jira.client import JIRA


server_details = {
    'server': 'https://???.atlassian.net'
}

jira = JIRA(options=server_details, basic_auth=('username', 'password'))
qa_passed_stories_in_sprint = jira.search_issues('project = "carrierName - Phase 5" AND  Sprint = 418 AND type in (Story, "Change Request") AND status = "QA passed" ', maxResults=False)
storyFile = open("Stories passed by QA in sprint.csv", "w+")

for issue in qa_passed_stories_in_sprint:
    line = "{}, {}, {}\n".format(issue.key, issue.fields.summary, issue.fields.status)
    storyFile.write(line)

storyFile.close()



