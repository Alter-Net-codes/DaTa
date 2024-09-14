from github import Github
from github import Auth

# Prompt the user for their GitHub access token
access_token = input("Please enter your GitHub access token: ")

# Authenticate using the provided token
auth = Auth.Token(access_token)
github = Github(auth=auth)

# Prompt the user for the repository they want to look up (in format 'owner/repo')
repo_name = input("Enter the repository (owner/repo): ")

# Get the repository
try:
    repo = github.get_repo(repo_name)
    
    # Fetch and print contributors
    print(f"Contributors for {repo_name}:")
    for contributor in repo.get_contributors():
        print(f"{contributor.login} - {contributor.contributions} contributions")
except Exception as e:
    print(f"Error: {e}")
