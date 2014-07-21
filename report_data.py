
class ReportData:
    def __init__(self,jira,project_name,sprint):
        self.jira = jira
        self.project_name =project_name
        self.sprint = sprint
        
    def blocker_bugs_in_sprint(self):
         return len(self.jira.search_issues('project = "{}" AND Sprint = "{}" AND type = bug AND priority = Blocker'.format(self.project_name, self.sprint), maxResults=False))
    
    def critical_bugs_in_sprint(self):
        return len(self.jira.search_issues('project = "{}" AND Sprint = "{}" AND type = bug AND priority = Critical'.format(self.project_name, self.sprint), maxResults=False))
    
    def major_bugs_in_sprint(self):
        return len(self.jira.search_issues('project = "{}" AND Sprint = "{}" AND type = bug AND priority = Major'.format(self.project_name, self.sprint), maxResults=False))
    
    def minor_bugs_in_sprint(self):
        return len(self.jira.search_issues('project = "{}" AND Sprint = "{}" AND type = bug AND priority = Minor'.format(self.project_name, self.sprint), maxResults=False))
    
    def trivial_bugs_in_sprint(self):
        return len(self.jira.search_issues('project = "{}" AND Sprint = "{}" AND type = bug AND priority = Trivial'.format(self.project_name, self.sprint), maxResults=False))
    
    def bugs_opened_in_sprint(self):
        return len(self.jira.search_issues('project = "{}" AND Sprint = "{}" AND type = bug'.format(self.project_name, self.sprint), maxResults=False))
    
    def bugs_fixed_in_sprint(self):
        return len(self.jira.search_issues('project = "{}" AND fixVersion in ("{}") AND type = bug  AND status in (UAT, "QA Passed")'.format(self.project_name, self.sprint), maxResults=False))
    
    def open_bugs_list(self):
        open_bugs_in_project = self.jira.search_issues('project = "{}" AND  type = bug AND status not in (UAT, "QA Passed")'.format(self.project_name), maxResults=False)
    
        data_array=[["" for j in range(7)] for i in range(len(open_bugs_in_project))]
        row_index = 0
        for issue in open_bugs_in_project:
            affectsVersion = issue.fields.versions[0].name if len(issue.fields.versions) > 0 else "-"
            fixVersionsList = ""
            for version in issue.fields.fixVersions:
                fixVersionsList += version.name +" "
            fixVersionsList = fixVersionsList[:-1]
    
            data_array[row_index][0] = issue.key
            data_array[row_index][1] = issue.fields.summary
            data_array[row_index][2] = issue.fields.priority.name
            data_array[row_index][3] = issue.fields.customfield_11100.value if issue.fields.customfield_11100 is not None else ""
            data_array[row_index][4] = issue.fields.status.name
            data_array[row_index][5] = affectsVersion
            data_array[row_index][6] = fixVersionsList
    
            row_index += 1
        return data_array
    
    
    def stories_passed_by_qa(self):
        qa_passed_stories_in_sprint = self.jira.search_issues('project = "{}" AND  Sprint = "{}" AND type = story AND status = "QA passed"'.format(self.project_name, self.sprint), maxResults=False)
    
        data_array=[["" for j in range(3)] for i in range(len(qa_passed_stories_in_sprint))]
        row_index = 0
        for issue in qa_passed_stories_in_sprint:
    
            data_array[row_index][0] = issue.key
            data_array[row_index][1] = issue.fields.summary
            data_array[row_index][2] = issue.fields.status.name
    
            row_index += 1
        return data_array