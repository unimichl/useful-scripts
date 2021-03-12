# Ten Simple Rules for Taking Advantage of Git and GitHub

[DOI:https://doi.org/10.1371/journal.pcbi.1004947](https://doi.org/10.1371/journal.pcbi.1004947)

## **Rule 1:** Use GitHub to Track Your Projects
+ Tony Rossini: “commit early, commit often, and commit in a repository from which we can easily roll-back your mistakes,”
+ Recommended Reading: [*A quick Introduction to Version Control with Git and GitHub*]( https://doi.org/10.1371/journal.pcbi.1004668)
![alt text](https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pcbi.1004947/1/pcbi.1004947.g001.PNG_L?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20210312%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210312T192528Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=5ccd20c34d158c063564cb365c37afda689619a83f1c36057a57ca8d4a1b9a799ab3a9093cd57b502d3f86cb9d5733e32087c6290db6c73f40d294a91bb05840bb64dc2e3d2805f429910da475a60ae87d3d241b8c11fc8687f1e264a0e66c4b46c1c337eeac777e746c9e486d90260b54b7f62c6029942f9a7eaa79c98677fdfce21818453414f4c858daf3b24c85fb3d709e9364ff269f495999856df313d4c2e11aa09e920837be22434902bf255430f2fee83f091b7c3f87867972996e868336de9deea0b6fc74d051219731ca1b981b0bd566873fb50ed8fca0f4374319340c3eb7695f48b4d1a4bc229b3d3abd2e0da484c948a99fecb91916111894f3)
**Figure 1** The structure of a GitHub-based project illustrating project structure and interactions with the community.

## **Rule 2:** GitHub for Single Users, Teams, and Organizations
+ Public projects on GitHub are visible to everyone, but write permission needs to be granted explicitly
+ As a repository owner, you can grant this right to other GitHub users
+ Repositories can also be created and managed as part of teams and organizations

## **Rule 3:** Developing and Collaborating on New Features: Branching and Forking
+ Forking a repository allows users to freely experiment with changes without affecting the original project and forms the basis of social coding
+ Forking a repository and providing pull requests constitutes a simple method for collaboration inside loosely defined teams
+ Many contributors can work on the same repository at the same time without running into edit conflicts -> Git branches
+ BUT there is a risk of applying incompatible changes in different branches/forks; these are said to become *out of sync*

## **Rule 4:** Naming Branches and Commits: Tags and Semantic Versions
+ Version numbering shouldfollow “semantic versioning” practice, with the format X.Y.Z., with X being the major, Y the minor, and Z the patch version of the release, including possible meta information

## **Rule 5:** Let GitHub Do Some Tasks for You: Integrate
+ Hooks = automatically executed scripts for making sure every commit actually works
+ This way each version is automatically checked for errors

## **Rule 6:** Let GitHub Do More Tasks for You: Automate
+ Check that most of your code is covered by hooks eg. codecov.io
+ Document most or all of your commits for better traceability, use tools to ease this task eg. Sphinx
+ Reports and badges which can be included on your Github project page are created by the platforms 

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
+ GitHub *pages* - simple websites freely hosted by GitHub
+ Reddit
+ Gitter (GitHub based chat tool)
+ Gists are a way to share code snippets, single files etc. – publicly and secretly

## **Rule 10:** Use GitHub to Be Social: Follow and Watch
+ Follow other GitHub users
+ Watch projects
