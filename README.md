# CloudComputing
Since all 3 assignments were completed in one repository instead of as 3 separate projects there are a few bits of weirdness in how the code evolved. For example, in the case of the dependency management file requirements.txt rather than creating a separate such file for each stage of the assignment only one was used and dependencies were added on a rolling basis as more were needed as the project gained complexiity. This means that, while the workflow for assignment 1 utilizes the same dependency management file as assignment 3, not all of the packages included in the file are actually required for assignment 1 as some were added for later assignments. Conversely, while assignment 3 builds very directly on assignment 2, instead of editing the files from assignment 2 to be more robust and meet the requirements of assignment 3, a second set of files were instead created to clearly reflect the changes made from assignment 2 to assignment 3 and differentiate between them as separate phases to each receive their own grade. This is reflected predominately by the existence of 2 versions of various files, one version with the base name (i.e. app.py) and the other with the same name followed by a 2 (i.e. app2.py) indicating that the latter are the second iteration of the initial files created as part of assignment 3. 

## Assignment 1:
The first step in this project was to create the repository and learn to establish a basic workflow. Initially, the repo only needed to contain some basic code the contents of which were largely immaterial (main.py), a system for testing that code (main_test.py and pytest), a dependency management file (requirements.txt), and the aforementioned workflow which would run when changes were made in the repository or when manually prompted by a user. 

### The Workflow:
The workflow for assignment 1 is main.yml and (as with the other workflows) is located in the .github/workflows folder. When pushes or pull requests are made of the main branch it will be automatically activated. It will first take the necessary steps to be able to run the code; checking it out, setting up the specified version of python, and installing the dependencies outlined in the requirements.txt file. Once all that is achieved, it will run the relevant tests on the code in main.py to make sure the code functions as it should. While this workflow will run automatically when changes are made, it can also be initiated manually by going to the actions tab for the repo, select the relevant workflow from the list on the left, it will be one of the ones labelled 'Python application' and when clicked on will have the name main.yml. At the top right will be a 'Run workflow' button which, if clicked, will manually trigger the workflow. 

### The Code: 
Since the main purpose of this assignment was to familiarize oneself with github workflows the actual code being run by the workflow was of secondary importance. In this case main.py is a simple addition function to sum two values. A test for such a function is included in pytest but a secondary file, main_test.py was also created for testing which includes a function with a few examples asserting that, for a variety of value pairings, the add function in main.py is working correctly. Running the workflow will execute a testrun of the code, but if you want to use it separate from the workflow all you have to do is clone the repo, create and activate a virtual environment in which to work, install the dependencies from requirements.txt in that repo and then you can either import the add function from main.py into a python script to use it or, if all you want to do is test the function you can import the test_add function from main.py or simply execute pytest. 

## Assignment 2: 
The second step in this project was to create a REST API with endpoints for GET, POST, PUT, and DELETE verbs, and tests for each endpoint. As part of this assignment the app.py, test_app.py, Dockerfile.api, Dockerfile.test, run_api.sh, run_tests.sh and python-app.yml files were created. 

### The Workflow: 
The workflow for assignment 2 is python-app.yml and was written to be triggered when pushes or pull requests are made of the main branch and can also be run manually from the actions tab as described for the workflow in assignment 1. As with the workflow from assignment 1, this workflow will check out the code, set up python, install the dependencies and then execute the specified tests (in this case test_app.py). 

### The Code: 
The app.py file contains code to get, create, update, and delete items and the test_app.py file has tests to ensure that each of those functions are working as they should. Dockerfile.api containerizes app.py and run_api.sh then uses Dockerfile.api to build an image, creates and starts a container for that image and exposes that container on port 5000. Dockerfile.test and run_tests.sh function in a similar manner but for the test_app.py file. The python-app.yml workflow was designed to run the codes but if you wanted to run any of the files separate from the workflow you would simply have to clone the repo and use the terminal and the commands ./run_api.sh and run_tests.sh to execute the app.py and test_app.py files respectively. 

## Assignment 3: 
The third step in this project was to improve on the work done in step 2 by adding functionality to create, read, update, and destroy items in a DynamoDB table and an S3 bucket and then using Localstack to run a mock of AWS as part of the application stack. The following testing requirements were added: 

- Sending a GET request with appropriate parameters returns expected JSON from the database
- Sending a GET request that finds no results returns the appropriate response
- Sending a GET request with no parameters returns the appropriate response
- Sending a GET request with incorrect parameters returns the appropriate response
- Sending a POST request results in the JSON body being stored as an item in the database, and an object in an S3 bucket
- Sending a duplicate POST request returns the appropriate response
- Sending a PUT request that targets an existing resource results in updates to the appropriate item in the database and object in the S3 bucket
- Sending a PUT request with no valid target returns the appropriate response
- Sending a DELETE request results in the appropriate item being removed from the database and object being removed from the S3 bucket
- Sending a DELETE request with no valid target returns the appropriate response

For each test, the database item and S3 object should match.

The files created for this particular assignment were app2.py, Dockerfile2.api, run_stack.sh, Dockerfile2.test, run_tests2.sh, docker-compose.yml and docker-compose.test.yml. 

### The Workflow
The workflow for assignment 2 is python-app2.yml and was written to be triggered when pushes or pull requests are made of the main branch and can also be run manually from the actions tab. This workflow will check out the code, set up docker build and compose, build docker image for API and for tests, run stack, and then run tests. 

### The Code: 
The app2.py file contains code to get, create, update, and delete items with the added dynamodb and s3 functionality. The same test file as was created for assignment 2, test_app.py 
was used to test app2.py. Dockerfile2.api containerizes app2.py and run_api2.sh then uses Dockerfile.api to build an image, creates and starts a container for that image and exposes that container on port 5000. Dockerfile2.test and run_tests2.sh function in a similar manner but for the test_app.py file. Docker-compose.yml 
