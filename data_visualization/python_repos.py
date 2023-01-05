import requests

class APICall:
    
    def __init__(self):
        self.url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        self.headers = {"Accept":"application/vnd.github.v3+json"}

    def call_api(self,url,headers):
        r = requests.get(url,headers=headers)
        status = r.status_code
        response_dict = r.json()
        return [status, response_dict]

    def sum_api_call(response_dict):
        print(response_dict.keys())
        print(f"Total repositories: {response_dict['total_count']}")
        repo_dicts = response_dict["items"]
        print(f"Respositories returned: {len(repo_dicts)}")
        repo_dict = repo_dicts[0]
        print(f"Keys: {len(repo_dict)}")
        for key in sorted(repo_dict.keys()):
            print(key)
        return repo_dicts
            
    def sum_repos(repo_dicts):
        print("\nSelected information about each repository:")
        for repo_dict in repo_dicts:
            print(f"Name: {repo_dict['name']}")
            print(f"Owner: {repo_dict['owner']['login']}")
            print(f"Stars: {repo_dict['stargazers_count']}")
            print(f"Repository: {repo_dict['html_url']}")
            print(f"Created: {repo_dict['created_at']}")
            print(f"Updated: {repo_dict['updated_at']}")
            print(f"Description: {repo_dict['description']}")