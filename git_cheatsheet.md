Git Cheat Sheet

GIT BASICS                                                                                   REWRITING GIT HISTORY

git init           Create empty Git repo in specified directory. Run with no                 git commit             Replace the last commit with the staged changes and last commit
<directory>        arguments to initialize the current directory as a git repository.        --amend                combined. Use with nothing staged to edit the last commit’s message.

                   Clone repo located at <repo> onto local machine. Original repo can be                            Rebase the current branch onto <base>. <base> can be a commit ID,
git clone <repo>                                                                             git rebase <base>
                   located on the local filesystem or on a remote machine via HTTP or SSH.                          branch name, a tag, or a relative reference to HEAD.

git config         Define author name to be used for all commits in current repo. Devs                              Show a log of changes to the local repository’s HEAD.
                                                                                             git reflog
user.name <name>   commonly use --global flag to set config options for current user.                               Add --relative-date flag to show date info or --all to show all refs.

git add            Stage all changes in <directory> for the next commit.
<directory>        Replace <directory> with a <file> to change a specific file.              GIT BRANCHES

git commit -m      Commit the staged snapshot, but instead of launching                                             List all of the branches in your repo. Add a <branch> argument to
                                                                                             git branch
"<message>"        a text editor, use <message> as the commit message.                                              create a new branch with the name <branch>.

                                                                                             git checkout -b        Create and check out a new branch named <branch>.
git status         List which files are staged, unstaged, and untracked.
                                                                                             <branch>               Drop the -b flag to checkout an existing branch.

                   Display the entire commit history using the default format.
git log                                                                                      git merge <branch>     Merge <branch> into the current branch.
                   For customization see additional options.

                   Show unstaged changes between your index and
git diff                                                                                     REMOTE REPOSITORIES
                   working directory.

                                                                                             git remote add         Create a new connection to a remote repo. After adding a remote,
UNDOING CHANGES                                                                              <name> <url>           you can use <name> as a shortcut for <url> in other commands.

git revert         Create new commit that undoes all of the changes made in                  git fetch              Fetches a specific <branch>, from the repo. Leave off <branch>
<commit>           <commit>, then apply it to the current branch.                            <remote> <branch>      to fetch all remote refs.

                   Remove <file> from the staging area, but leave the working directory                             Fetch the specified remote’s copy of current branch and
git reset <file>                                                                             git pull <remote>
                   unchanged. This unstages a file without overwriting any changes.                                 immediately merge it into the local copy.

                   Shows which files would be removed from working directory.                git push               Push the branch to <remote>, along with necessary commits and
git clean -n
                   Use the -f flag in place of the -n flag to execute the clean.             <remote> <branch>      objects. Creates named branch in the remote repo if it doesn’t exist.



                                                                                                            Visit atlassian.com/git for more information, training, and tutorials
Additional Options +
GIT CONFIG                                                                                        GIT DIFF

                                                                                                  git diff HEAD          Show difference between working directory and last commit.
git config --global
                       Define the author name to be used for all commits by the current user.
user.name <name>                                                                                  git diff --cached      Show difference between staged changes and last commit

git config --global
                       Define the author email to be used for all commits by the current user.    GIT RESET
user.email <email>

git config --global                                                                                                      Reset staging area to match most recent commit,
                       Create shortcut for a Git command. E.g. alias.glog “log --graph            git reset
alias. <alias-name>                                                                                                      but leave the working directory unchanged.
                       --oneline” will set ”git glog” equivalent to ”git log --graph --oneline.
<git-command>
                                                                                                                         Reset staging area and working directory to match most recent
git config --system    Set text editor used by commands for all users on the machine. <editor>    git reset --hard
                                                                                                                         commit and overwrites all changes in the working directory.
core.editor <editor>   arg should be the command that launches the desired editor (e.g., vi).

                                                                                                                         Move the current branch tip backward to <commit>, reset the
git config                                                                                        git reset <commit>
                       Open the global configuration file in a text editor for manual editing.                           staging area to match, but leave the working directory alone.
--global --edit

                                                                                                  git reset --hard       Same as previous, but resets both the staging area & working directory to
GIT LOG                                                                                           <commit>               match. Deletes uncommitted changes, and all commits after <commit>.

                       Limit number of commits by <limit>.
git log -<limit>
                       E.g. ”git log -5” will limit to 5 commits.                                 GIT REBASE

git log --oneline      Condense each commit to a single line.                                     git rebase -i          Interactively rebase current branch onto <base>. Launches editor to enter
git log -p             Display the full diff of each commit.                                      <base>                 commands for how each commit will be transferred to the new base.

                       Include which files were altered and the relative number of
git log --stat
                       lines that were added or deleted from each of them.                        GIT PULL

git log --author=                                                                                 git pull --rebase      Fetch the remote’s copy of current branch and rebases it into the local
                       Search for commits by a particular author.
”<pattern>”                                                                                       <remote>               copy. Uses git rebase instead of merge to integrate the branches.

git log                Search for commits with a commit message that
--grep=”<pattern>”     matches <pattern>.                                                         GIT PUSH

git log                Show commits that occur between <since> and <until>. Args can be a         git push <remote>      Forces the git push even if it results in a non-fast-forward merge. Do not use
<since>..<until>       commit ID, branch name, HEAD, or any other kind of revision reference.     --force                the --force flag unless you’re absolutely sure you know what you’re doing.

                                                                                                  git push <remote>
git log -- <file>      Only display commits that have the specified file.                                                Push all of your local branches to the specified remote.
                                                                                                  --all


git log --graph        --graph flag draws a text based graph of commits on left side of commit    git push <remote>      Tags aren’t automatically pushed when you push a branch or use the
--decorate             msgs. --decorate adds names of branches or tags of commits shown.          --tags                 --all flag. The --tags flag sends all of your local tags to the remote repo.



                                                                                                                  Visit atlassian.com/git for more information, training, and tutorials
