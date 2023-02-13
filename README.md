# ernesto_albarez_teladoc_challenge
BDD automation with Python

## Setting up

1. Install Selenium
2. Install pytest
3. Configure the virtual env for this project


### Run the file `webtable/tests/test_suite/test_runner.py`
This project is going to

1. **Create a new user**
    
    By clicking on the Add New User Button and entering:

      - user first name
      - username
      - user role
      - user phone number

    > Then validate user was creating by looking for the username on the table

2. **Delete user**
    > Before deleting, the scripts is going to save the total count of user rows
   - Searches for 'novak' on the table
   - Clicks on the delete option from the user row
    > Finally validates total count of rows after user deletion vs before user deletion