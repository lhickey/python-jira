import getopt
import sys
import json
# import bug_breakdown_for_sprint
# import write_file
# import stories_qa_passed_in_sprint

sprint = "Sprint 37"


def main(argv):

    configuration = getConfiguration(argv)
    print configuration.username
    print configuration.password
    print configuration.host
    print configuration.project_name
    print configuration.sprint

    if True:
        return

        # print "Bugs opened in sprint: {}".format(bug_breakdown_for_sprint.bugs_opened_in_sprint())
        #
        # print "Bugs fixed in sprint: {}".format(bug_breakdown_for_sprint.bugs_opened_in_sprint())
        #
        # print "Blocker bugs: {}".format(bug_breakdown_for_sprint.blocker_bugs_in_sprint())
        #
        # print "Critical bugs: {}".format(bug_breakdown_for_sprint.critical_bugs_in_sprint())
        #
        # print "Major bugs: {}".format(bug_breakdown_for_sprint.major_bugs_in_sprint())
        #
        # print "Minor bugs: {}".format(bug_breakdown_for_sprint.minor_bugs_in_sprint())
        #
        # print "Trivial bugs: {}".format(bug_breakdown_for_sprint.trivial_bugs_in_sprint())
        #
        # print "Generating list of open bugs in whole project -  ...."
        #
        # write_file
        #
        # print "Finished generating list of open bugs"
        #
        # print "Generating list of stories passed by QA during sprint ..."
        #
        # stories_qa_passed_in_sprint
        #
        # print "Finished generating list of stories QA Passed"


def printUsage():
    print "Usage: python generate_sprint_report.py -u [username] -p [password]"


def getConfiguration(argv):
    username = None
    password = None
    config_file_name = "./config.json"
    try:
        opts, args = getopt.getopt(argv, "hu:p:", ["config="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            printUsage()
            sys.exit()
        elif opt == "-u":
            username = arg
        elif opt == "-p":
            password = arg
        elif opt == "--config":
            config_file_name = arg

    if username is None or password is None:
        printUsage()
        sys.exit(-1)

    config_file = open(config_file_name, 'r')
    configuration_data = json.load(config_file)
    config_file.close()

    configuration = MyConfig(username,
                             password,
                             configuration_data['projectName'],
                             configuration_data['sprint'],
                             configuration_data['host'])

    return configuration


class MyConfig:
    def __init__(self, username, password, project_name, sprint, host):
        self.username = username
        self.password = password
        self.project_name = project_name
        self.sprint = sprint
        self.host = host

    def __str__(self):
        return "host: {}, username: {}, password: {}, project_name: {}, sprint: {}".format(
            self.host,
            self.username,
            self.password,
            self.project_name,
            self.sprint
        )


if __name__ == "__main__":
    main(sys.argv[1:])