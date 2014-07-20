from jira.client import JIRA


server_details = {
    'server': 'https://???.atlassian.net'
}

def open_bugs_list():
    jira = JIRA(options=server_details, basic_auth=('username', 'password'))
    open_bugs_in_project = jira.search_issues('project = "project_name" AND  type = bug AND status not in (UAT, "QA Passed")', maxResults=False)

    # results_list = ""
    myArray=[["" for j in range(7)] for i in range(len(open_bugs_in_project))]
    row_index = 0
    for issue in open_bugs_in_project:
        affectsVersion = issue.fields.versions[0].name if len(issue.fields.versions) > 0 else "-"
        fixVersionsList = ""
        for version in issue.fields.fixVersions:
            fixVersionsList += version.name +" "
        fixVersionsList = fixVersionsList[:-1]


        myArray[row_index][0] = issue.key
        myArray[row_index][1] = issue.fields.summary
        myArray[row_index][2] = issue.fields.priority.name
        myArray[row_index][3] = issue.fields.customfield_11100.value if issue.fields.customfield_11100 is not None else ""
        myArray[row_index][4] = issue.fields.status.name
        myArray[row_index][5] = affectsVersion
        myArray[row_index][6] = fixVersionsList

        row_index += 1
    return myArray