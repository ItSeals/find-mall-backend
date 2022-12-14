# find-mall-backend

A few links:

[How to work with docker (mysql+adminer)](.docker/README.md)

## How we work with git:
1. get repo to my comp
```
git clone https://github.com/ItSeals/find-mall-backend.git
```
2. make a branch
```
git checkout -b NEW_BRANCH_NAME_DIFFERENT_EVERY_TIME
```
3. write your code in dir "src"
4. add and commit
```
git add .
git commit -m "what have I done"
```
5. push branch to repo
```
git push origin NEW_BRANCH_NAME_DIFFERENT_EVERY_TIME
```
6. on github site check your branch and create Pull Request via Graphical
   Interface
7. someone checks your changes in that Pull Request and clicks "Merge" if all is OK.
8. Before start work on new branch:
```
git checkout main
git pull origin main
```
and then go to step 2 to create new branch
