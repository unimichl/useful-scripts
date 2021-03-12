# Ten Simple Rules for Taking Advantage of Git and GitHub

[DOI:https://doi.org/10.1371/journal.pcbi.1004947](https://doi.org/10.1371/journal.pcbi.1004947)

## **Rule 1:** Use GitHub to Track Your Projects
+ Tony Rossini: “commit early, commit often, and commit in a repository from which we can easily roll-back your mistakes,”
+ Recommended Reading: [*A quick Introduction to Version Control with Git and GitHub*]( https://doi.org/10.1371/journal.pcbi.1004668)
![alt text](https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pcbi.1004947/1/pcbi.1004947.g001.PNG_L?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20210312%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210312T203406Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=9ef4f51ea4537b38ca624c9e66a9d39db1de7168d409077496b3565d264f7e46181af24c5144c82c60ef9bbee05c9236afd99d2b4a06f0445d74f15ee69bdae28c82ba3a5f8b73291a8e97c300c2da71a7d75735397179cf40df4a48d56bc1490560d3ed19ac4094a7bf6f566fe6253ac1051d18352224cdcc50e1088db2a448a7d151f7d68941d56b5de3fe11922fe80c9d7c474e0a163e285c01600e6f053983a92ffa8b57f77ee1ff27649f394d89d350ca41149a0cad3bb08ef0719378adfaa33f656683420208d93efa9a7ff6bc8a5a61ae45e8aae2f718e8e7a17633d39a3fd46692cdac90b3b6cd9f358537a5448110767a63cfa42bfe3a8083944892)
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
