# CloudComputing

## Assignment 1:
The first step in this project was to create the repository and learn to establish a basic workflow. Initially, the repo only needed to contain some basic code the contents of which were largely immaterial (main.py), a system for testing that code (pytest), a dependency management file (requirements.txt), and the aforementioned workflow which would run when changes were made in the repository or when manually prompted by a user. 

### The Workflow:
The workflow for assignment 1 is main.yml and (as with the other workflows) is located in the .github/workflows folder. When pushes or pull requests are made of the main branch it will be automatically activated. It will first take the necessary steps to be able to run the code; checking it out, setting up the specified version of python, and installing the dependencies outlined in the requirements.txt file. Once all that is achieved, it will run the relevant pytest tests on the code in main.py to make sure the code functions as it should. While this workflow will run automatically when changes are made, it can also be initiated manually by going to the actions tab for the repo, select the relevant workflow from the list on the left, it will be one of the ones labelled 'Python application' and when clicked on will have the name main.yml. At the top right will be a 'Run workflow' button which, if clicked, will manually trigger the workflow. 

### The Code: 
Since the main purpose of this assignment was to familiarize oneself with github workflows the actual code being run by the workflow was of secondary importance. In this case main.py is a simple addition function to sum two values and because a test for such a function is included in pytest there was no need to create a secondary file or function specific for testing. Running the workflow will execute a testrun of the code, but if you want to use it separate from the workflow all you have to do is clone the repo, create and activate a virtual environment in which to work, install the dependencies from requirements.txt in that repo and then you can either import the function from main.py into a python script to use it or, if all you want to do is test the function you can simply execute pytest. 

## Assignment 2: 
