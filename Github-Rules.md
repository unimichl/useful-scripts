# Ten Simple Rules for Taking Advantage of Git and GitHub

[DOI:https://doi.org/10.1371/journal.pcbi.1004947](https://doi.org/10.1371/journal.pcbi.1004947)

## **Rule 1:** Use GitHub to Track Your Projects
+ Tony Rossini: “commit early, commit often, and commit in a repository from which we can easily roll-back your mistakes,”
+ Recommended Reading: [*A quick Introduction to Version Control with Git and GitHub*]( https://doi.org/10.1371/journal.pcbi.1004668)
<br /> 
<br />

![alt text](https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pcbi.1004947/1/pcbi.1004947.g001.PNG_M?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20210312%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210312T222922Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=2c653e747389e58d10bd12d8e37851c69f8f533d4dafb070665550d8225eebab458c9922d82ad2b5f19a0cdb9552c72feefefdd382b7453e2d456c81cbb078ec7a4c2ef2f96bee9163423c4121a42674fe0f99e496413298a36148923f13df050158db74461c499f23216d047429c39f9a4bc192eac3ee7132505eeee547189d5e032028f5a3202fad57c3e2c056f75f76aaeead28011d57753ecc4f6cd4e2886d0c4d140d100c961cc37d6d120bbb225fedbb99c60dbd02f0f082464b30c17784baa97ba5f133fa1a7871609e3ffa1f8b2fc49b3a4a1ddbe9aef2f52b8cc8e84f0bd8d9ee3ccacd8b0b433b7a484f833b7127d7f0945870b0ecddd477a21e81)

**Figure 1.** The structure of a GitHub-based project illustrating project structure and interactions with the community.


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
