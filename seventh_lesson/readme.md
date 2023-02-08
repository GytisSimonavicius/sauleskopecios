<!-- There are couple of ways to move from here and immediately github will describe opportunities to you if you open your newly created project.
first scenario

open up terminal:

git clone repository

create a file and check what can git say about the file:

git status

tell git to start tracking changes within the file:

git add <filename>

check status once again git status

What is different this time? Now we need to create a commit, which is simply a point in history of your project showing what was changed and who and when did the change. Let's create it!

git commit -m "first commit"

check status once again git status

We are ready to push now:

git push

congratulations you have now successfully tracked the changes and they are also visible on gitub! Check them out.
Second scenario

What if you already had a codebase and now suddenly you want to start tracking it? Not a problem. initiate git project in the directory of your choice.

git init

now you can check git status once again:

git status

to start tracking all files simply:

git add .
git commit -m "initial commit"

And just like that you now have a repo that is being tracked. But how do we share this with our colleagues? It is not yet connected to GitHub So for this project create a new GitHubproject. Now all you have to do is to grab origin link which you can find on GitHub project you have created.

git remote add origin https://github.com/vychiokas/test.git

now we have to 'push' it to remote:

git push -->