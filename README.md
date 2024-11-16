# Hello World API

This project implements a simple Hello World API based on the provided hello_world_api.yml specification. It also includes a web page to interact with the API.

## Instructions to Run the code

### Prerequisites
1. Ensure you have Python 3.8 or higher installed.
2. install pip(python package manager).

### Steps to run the API
1. Extract the Project:
- Extract the HelloWorldAPI.zip file.
- Open the command prompt and navigate to the project directory:
  cd helloworld_project

2. Install the dependencies:
- Install the dependencies which are mentioned in the requirements.txt file.

3. Run the API:
- Use the command below to start the API
  python manage.py runserver
- The API will run locally at http://127.0.0.1:8000/.
  - It will display Id and Message according to the selected Language.
  - It will display error message if Language is other than English, French and Hindi.

4. Test the API:
- Open the browser and use the following URLs to test:
  - http://127.0.0.1:8000/hello/?language=French
  - http://127.0.0.1:8000/hello/?language=English
  - http://127.0.0.1:8000/hello/?language=Hindi

## Steps to use the web page

1. Open the file templates/index.html in any browser.
2. Select the Language from the dropdown and click "Get Message".
3. The Corresponding "Hello World" message will displayed.


