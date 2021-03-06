
import getopt
import sys
import json
import os.path
from jira.client import JIRA
import write_file
from report_data import ReportData


def main(argv):

    configuration = getConfiguration(argv)

    server_details = {
        'server': configuration.host
    }

    jira = JIRA(options=server_details, basic_auth=(configuration.username, configuration.password))
    report = ReportData(jira, configuration.project_name, configuration.sprint)
    write_file.write_bug_count_in_sprint(report)
    write_file.write_stories_passed_by_qa(report)
    write_file.write_open_bugs_in_project(report)


def printUsage():
    print "\n"
    print "Usage: python generate_sprint_report.py -u [username] -p [password]"
    print "optional: --config path/to/my_config.json"
    print "\n"


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
        print "Missing username or password"
        printUsage()
        sys.exit(-1)

    if not os.path.isfile(config_file_name):
        print "Missing configuration file (config.json)"
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
