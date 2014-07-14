import bug_breakdown_for_sprint
import write_file
import stories_qa_passed_in_sprint

sprint = "Sprint 37"

print "Bugs opened in sprint: {}".format(bug_breakdown_for_sprint.bugs_opened_in_sprint())

print "Bugs fixed in sprint: {}".format(bug_breakdown_for_sprint.bugs_opened_in_sprint())

print "Blocker bugs: {}".format(bug_breakdown_for_sprint.blocker_bugs_in_sprint())

print "Critical bugs: {}".format(bug_breakdown_for_sprint.critical_bugs_in_sprint())

print "Major bugs: {}".format(bug_breakdown_for_sprint.major_bugs_in_sprint())

print "Minor bugs: {}".format(bug_breakdown_for_sprint.minor_bugs_in_sprint())

print "Trivial bugs: {}".format(bug_breakdown_for_sprint.trivial_bugs_in_sprint())

print "Generating list of open bugs in whole project -  ...."

write_file

print "Finished generating list of open bugs"

print "Generating list of stories passed by QA during sprint ..."

stories_qa_passed_in_sprint

print "Finished generating list of stories QA Passed"


