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

    code2 = '''
    
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    from_addr = 'myemail@gmail.com'
    to_addr = 'toemail@gmail.com'
    bcc = ['other@gmail.com', 'myemail@gmail.com', 'email@gmail.com']
    
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'New Releases'
    
    body = """ New Releases and Sales!
        
    Click the links below to check them out!
       
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    
    smtp_server.ehlo()
    
    smtp_server.starttls()
    
    smtp_server.login(' myemail@gmail.com ', ' <application id> ')
    
    text = msg.as_string()
    
    smtp_server.sendmail(from_addr, [to_addr] + bcc, text)
    
    smtp_server.quit()
    
    print('Email sent successfully')
    
    '''

    code3 = '''
    #python tip:  zip() with star-arguments is great for transposing 2-D data:
    m = [(1, 2, 3), (4, 5, 6)]
    list(zip(*m))
    [(1, 4), (2, 5), (3, 6)]
    
    def transpose_list_of_tuples(data):
        if isinstance(data, dict):
            data = data.items()
        transposed = list(zip(*data))
        return transposed
    
    '''

    # me.create_gist(True,
    #                {"repo_stats.py": InputFileContent(code)},
    #                "Get GH user's most popular repos")
    me.create_gist(True,
                   {"transpose.py": InputFileContent(code3)},
                   'zip() with star-arguments is great for transposing 2-D data')


if __name__ == '__main__':
    program()
