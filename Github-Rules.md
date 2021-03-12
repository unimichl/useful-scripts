# Ten Simple Rules for Taking Advantage of Git and GitHub

[DOI:https://doi.org/10.1371/journal.pcbi.1004947](https://doi.org/10.1371/journal.pcbi.1004947)

## **Rule 1:** Use GitHub to Track Your Projects
+ Tony Rossini: “commit early, commit often, and commit in a repository from which we can easily roll-back your mistakes,”
+ Recommended Reading: [*A quick Introduction to Version Control with Git and GitHub*]( https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pcbi.1004947/1/pcbi.1004947.g001.PNG_I?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20210312%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210312T221517Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=c8b0cf21d3a5e2fb6a8910b1997ff0684992f35d86b5222327e6aef72c8534b4ec58aa44364d1639235414302f7fd7b0af3d760bd379440ffb1c279254a71560ece462319b2030c9ff84460e59a2c5cbd1a1e1ee1d2ffc5c50006b3ef4a4e5c5c068d6c6eefe754007276f6775b9e74a1da41ac4a40bfb3bc8b48abfc4e4e66e1bcf2745d2ea71be72252fef793cf34d099a9382147067418ce180ce0e941354456944e5f33588c4957c4cae375780fdc056f25e6840a7a01caa262d1b1ca4c41317cc58d8ee8fc5d20d0832ec7bb4c2ab6beba24ef86120c2145c15a73b5f03036b28547f067986e8ba5408c0f75ff9163f5c774752a0832b0261ebde2391ba)
**Figure 1** The structure of a GitHub-based project illustrating project structure and interactions with the community.

## **Rule 2:** GitHub for Single Users, Teams, and Organizations
+ Public projects on GitHub are visible to everyone, but write permission needs to be granted explicitly
+ As a repository owner, you can grant this right to other GitHub users
+ Repositories can also be created and managed as part of teams and organizations

## **Rule 3:** Developing and Collaborating on New Features: Branching and Forking
+ **Forking** a repository allows users to freely experiment with changes without affecting the original project and forms the basis of social coding
+ **Forking** a repository and providing **pull requests** constitutes a simple method for collaboration inside loosely defined teams
+ Many contributors can work on the same repository at the same time without running into edit conflicts -> Git **branches**
+ **But** there is a risk of applying incompatible changes in different branches/forks; these are said to become *out of sync*

## **Rule 4:** Naming Branches and Commits: Tags and Semantic Versions
+ Version numbering should follow “semantic versioning” practice, with the format **X.Y.Z.**, with **X** being the major, **Y** the minor, and **Z** the patch version of the release, including possible **meta information**

## **Rule 5:** Let GitHub Do Some Tasks for You: Integrate
+ Continuous integration provides a way to automatically and systematically run a series of tests to check integrity and performance of code, a task that can be automated through GitHub
+ GitHub offers a set of ***hooks*** (automatically executed scripts) that are run after **each push** to a repository
+ This way each version is automatically checked for errors

## **Rule 6:** Let GitHub Do More Tasks for You: Automate
+ GitHub ***hooks*** eg. [Codecov](https://about.codecov.io/) can be used to report how much of the code is ececuted
+ Document most or all of your commits for better traceability, use tools for automated documentation generation like [SPHINX](https://www.sphinx-doc.org/en/master/)

## **Rule 7:** Use GitHub to Openly and Collaboratively Discuss, Address, and Close Issues
+ **GitHub *issues*:** A great way to keep track of bugs, tasks, feature requests, and enhancements
+ Raising an issue only requires a title and, preferably, at least a short description
+ Issues have very clear formatting and provide space for optional comments, which allow anyone with a Github account to provide feedback.
+ Additional elements of issues are (i) color-coded labels that help to categorize and filter issues, (ii) milestones, and (iii) one assignee responsible for working on the issue.
+ They help developers to filter and prioritize tasks and turn an issue tracker into a planning tool for their project.

## **Rule 8:** Make Your Code Easily Citable, and Cite Source Code!
+ **README, CITATION and LICENSE** files are crucial
+ **LICENCE** file: clearly defines the permissions and restrictions attached to the code and other files in your repository
+ **README** file: provides, for example, a short description of the project, a quick start guide, information on how to contribute, a TODO list, and links to additional documentation
+ **CITATION** file: informs your users how to cite and credit your project, Digital Object Identifiers (DOI) also for data sets and code repos

## **Rule 9:** Promote and Discuss Your Projects: Web Page and More
+ Associated paper (traditionally to promote a software)
+ **GitHub *pages*** - simple websites freely hosted by GitHub
+ Reddit
+ **Gitter** (GitHub based chat tool)
+ **Gists** are a way to share code snippets, single files etc. – publicly and secretly

## **Rule 10:** Use GitHub to Be Social: Follow and Watch
+ Follow other GitHub users
+ Watch projects
