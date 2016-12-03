# How to use github
Well, the repo is already made. So do something like  
`sudo apt-get install git`  
to install `git`  
then  
`git clone https://github.com/tom0527/MLwithFinance.git`  
will create a folder called `MLwithFinance`  
Make changes, to files and do something like
`git add filename.extension`  
`git commit -m "I added a file"`  
`git push origin branchname`
make branchname `master` if you want to update the main branch directly. Otherwise,  
`git branch branchname`  
creates a new branch called `branchname` and executing  
`git push origin branchname`
only modifies the files in `branchname` (I think...).

# About this program
This project is python3 based.

No GUI support.

get data from yahoo takes data from yahoo
main.py thingy just outputs it periodically with given interval (in seconds).

## To install additional python packages:
first, install pip (it's a package manager for python).    
`sudo apt-get install python-pip`  
Then  
`[sudo] pip install packagename`  
