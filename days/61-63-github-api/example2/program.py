'''Demonstration of PyGithub: How to automatically create a gist.'''
import os
import github_credentials

from github import Github, InputFileContent

def program():
    """1. Go to your Github Settings and create Personal access token
       2. Define a name and choose the type of access you want to grant.
       3. Copy the token and store it somewhere safe, as best practice I stored it as a env variable called GH_GIST_CREATE_TOKEN """

    token = github_credentials.GH_GIST_CREATE_TOKEN

    gh = Github(token)
    print(gh.rate_limiting)
    me = gh.get_user()
    print(me)

    code = '''
    from collections import namedtuple

    Repo = namedtuple('Repo', 'name stars forks')


    def get_repo_stats(user, n=5):
        """Takes a Github user object and returns the top n most popular repos by star count,
       skips forks."""
        repos = []
        for repo in user.get_repos():
            if repo.fork:
                continue

            repos.append(Repo(name=repo.name,
                          stars=repo.stargazers_count,
                          forks=repo.forks_count))
        
        return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]
       
    '''

    me.create_gist(True,
                   {"repo_stats.py": InputFileContent(code)},
                   "Get GH user's most popular repos")




if __name__ == '__main__':
    program()