# Ten Simple Rules for Taking Advantage of Git and GitHub

[DOI:https://doi.org/10.1371/journal.pcbi.1004947](https://doi.org/10.1371/journal.pcbi.1004947)

## **Rule 1:** Use GitHub to Track Your Projects
+ Tony Rossini: “commit early, commit often, and commit in a repository from which we can easily roll-back your mistakes,”
+ Recommended Reading: [*A quick Introduction to Version Control with Git and GitHub*]( https://doi.org/10.1371/journal.pcbi.1004668)
![alt text](https://storage.googleapis.com/plos-corpus-prod/10.1371/journal.pcbi.1004947/1/pcbi.1004947.g001.PNG_L?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=wombat-sa%40plos-prod.iam.gserviceaccount.com%2F20210312%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210312T192047Z&X-Goog-Expires=3600&X-Goog-SignedHeaders=host&X-Goog-Signature=b1703cbfcbfac4cb40ff9fd056c172c58119b0485d350f0a5e615b92420807cd9f3dffdbd3c49c105344bae12b90cdb80e104fcea6cb00f4c1f3ca0131ddaadb565bcb9efe114d3800b754f50bd64a1938ac5665c426b270ad25bc29cc56f5ca342ad7be1cd8699b5db35da224584f1360c6ea6e8a2651af84e002866f9fe141f58301f666c0456fa38a7dc2dfc08813fbb5d9d91a05912e823d08d97c3d28464430cbdc49652eaf92a77edff67fe8653b41433015d39d8fde9ac0021910221f53d7d7dcb03e08c402ee0adf93efb4ed520e77d91a5ed7c521b1f13f6c0ed129f5d531d798c803e81e67f7080f30a84ec905ca690be234dbbcd7f8813cd109c8)

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
+ A great way to keep track of bugs, tasks, feature requests, and enhancements
+ Raising an issue only requires a title and, preferably, at least a short description
+ Define Milestones

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
+ Gists are a way to share code snippets etc – public and secret


## **Rule 10:** Use GitHub to Be Social: Follow and Watch
+ Follow other GitHub users
+ Watch projects
