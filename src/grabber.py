import webbrowser
from github import Github
from github import Auth

# Prompt the user for their GitHub access token
access_token = input("Please enter your GitHub access token: ")

# Authenticate using the provided token
auth = Auth.Token(access_token)
github = Github(auth=auth)

while True:
    # Prompt the user for the repository they want to look up (in format 'owner/repo')
    repo_name = input("Enter the repository (owner/repo): ")
    
    # Get the repository
    try:
        repo = github.get_repo(repo_name)
        
        contributors = []
        page = 1
        per_page = 50  # You can adjust this number (max 100 per page)
        
        print(f"Contributors for {repo_name}:\n")
        
        while True:
            # Fetch contributors for the current page
            current_page_contributors = repo.get_contributors().get_page(page - 1)
            
            if not current_page_contributors:
                break  # No more contributors to fetch
            
            contributors.extend(current_page_contributors)
            page += 1  # Move to the next page
        
        # Print the contributors and their contribution counts
        for idx, contributor in enumerate(contributors, start=1):
            print(f"{idx}. {contributor.login} - {contributor.contributions} contributions")
            
            # Fetch and display user profile data
            user = github.get_user(contributor.login)
            print(f"    Name: {user.name or 'N/A'}")
            print(f"    Bio: {user.bio or 'N/A'}")
            print(f"    Location: {user.location or 'N/A'}")
            print(f"    Public Repos: {user.public_repos}")
            print(f"    Followers: {user.followers}")
            print(f"    URL: {user.html_url}")
            
            # Ask user if they want to open the profile URL in the browser
            open_profile = input(f"Do you want to open {contributor.login}'s profile in the browser? (yes/no): ").lower()
            if open_profile == 'yes':
                webbrowser.open(user.html_url)
        
        print(f"\nTotal contributors fetched: {len(contributors)}\n")
    
    except Exception as e:
        print(f"Error: {e}\n")
