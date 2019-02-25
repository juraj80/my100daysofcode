'''Demonstration of PyGithub to retrieve public data from Github profiles.'''

from collections import namedtuple
import os
from github import Github, InputFileContent


gh = Github()

pb = gh.get_user('pybites')

Repo = namedtuple('Repo', 'name stars forks')

def get_repo_stats(user, n=5):
    """We did this exercise in our own 100 Days of Code:
           https://github.com/pybites/100DaysOfCode/blob/master/084/ghstats.py"""
    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue

        repos.append(Repo(name=repo.name,
                          stars=repo.stargazers_count,
                          forks=repo.forks_count))
    return sorted(repos, key = lambda x: x.stars, reverse=True)[:n]

jk = gh.get_user('juraj80')

print(get_repo_stats(pb))
print(get_repo_stats(jk))
