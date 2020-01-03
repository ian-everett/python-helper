'''
GitPython example
'''
from git import Repo

def main():
    ''' main() '''

    # Open git repo, use the actual python project
    repo = Repo('../')

    # Get branches
    for branch in repo.branches:
        print('Branch = %s' % branch.name)

    print("* %s" % repo.head.name)

if __name__ == "__main__":
    main()
