# Job Board

## Requirements

1. Make sure you have Python and pip installed on your system.

2. Clone the project to your project directory.

3. Navigate to the project's root directory using the command line or terminal.

4. Create a virtual environment using the following command:
virtualenv -p python3.8 environment


5. Navigate into the virtual environment. Run the appropriate command based on your operating system:
- For Linux/macOS users:
  ```
  source environment/bin/activate
  ```
- For Windows users:
  ```
  environment\Scripts\activate
  ```

6. Install project dependencies by running the following command in the project's root directory:
<code>pip install -r requirements.txt</code>


7. Run migrations to handle the models. Execute the following commands in the project's root directory:
- Create the migrations:
  ```
  python manage.py makemigrations
  ```
- Apply the migrations:
  ```
  python manage.py migrate
  ```

8. Finally, run your project using the following command in the project's root directory:
<code>python manage.py runserver</code>
