import os
from atlassian import Jira

JIRA_SERVER = os.environ.get('JIRA_SERVER')
JIRA_USERNAME = os.environ.get('JIRA_USERNAME')
JIRA_API_TOKEN = os.environ.get('JIRA_API_TOKEN')

jira = Jira(
    url=JIRA_SERVER,
    username=JIRA_USERNAME,
    password=JIRA_API_TOKEN,
    cloud=True
)
