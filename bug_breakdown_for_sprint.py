from jira.client import JIRA


server_details = {
    'server': 'https://???.atlassian.net'
}

jira = JIRA(options=server_details, basic_auth=('username', 'password'))

def blocker_bugs_in_sprint():
     return len(jira.search_issues('project = "carrierName - Phase 5" AND Sprint = "Sprint 37" AND type = bug AND priority = Blocker', maxResults=False))

def critical_bugs_in_sprint():
    return len(jira.search_issues('project = "carrierName - Phase 5" AND Sprint = "Sprint 37" AND type = bug AND priority = Critical', maxResults=False))

def major_bugs_in_sprint():
    return len(jira.search_issues('project = "carrierName - Phase 5" AND Sprint = "Sprint 37" AND type = bug AND priority = Major', maxResults=False))

def minor_bugs_in_sprint():
    return len(jira.search_issues('project = "carrierName - Phase 5" AND Sprint = "Sprint 37" AND type = bug AND priority = Minor', maxResults=False))

def trivial_bugs_in_sprint():
    return len(jira.search_issues('project = "carrierName - Phase 5" AND Sprint = "Sprint 37" AND type = bug AND priority = Trivial', maxResults=False))

def bugs_opened_in_sprint():
    return len(jira.search_issues('project = "carrierName - Phase 5" AND Sprint = "Sprint 37" AND type = bug', maxResults=False))

def bugs_fixed_in_sprint():
    return len(jira.search_issues('project = "carrierName - Phase 5" AND fixVersion in ("Sprint 37") AND type = bug  AND status in (UAT, "QA Passed") ', maxResults=False))

