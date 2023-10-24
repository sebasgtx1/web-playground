**Technologies:** Python (Django), HTML/CSS (Bootstrap)

**Test User for Admin Panel (/admin):**

- **User:** hector
- **Password:** Test1234*

**Super User for Admin Panel (/admin):**

- **User:** SebasGTX1
- **Password:** PWD0227**

Note: You can use this user to test the CRUD operations for pages.

## Getting Your Project Up and Running

**Requirements:**
- Python 3.8 or higher is recommended.

**Step 1: Clone the Repository**

To clone the repository from the `develop` branch, you can use the `git clone` command. Make sure you have Git installed on your system. Run the following command:

```shell
git clone https://github.com/sebasgtx1/web-playground.git
```

**Step 2: Install Dependencies**

1. Ensure that you're in the appropriate Python virtual environment (if you're using one).

2. Access to the repository folder. Run the following command:
   ```shell
   cd web-playground/
   ```

3. Install the dependencies from the `requirements.txt` file using `pip`. Run the following command:

   ```shell
   pip install -r requirements.txt
   ```

**Step 3: Access the Project Folder**

1. Access the project folder where the `manage.py` file is located. Run the following command:

   ```shell
   cd webplayground/
   ```

**Step 4: Perform Migrations**

1. To apply initial migrations and set up the database, run the following commands:

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

**Step 5: Launch the Project**

1. Finally, start the project by running the following command:

   ```shell
   python manage.py runserver
   ```

**Note:** Please configure the `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` components with a Hotmail account for email sending; otherwise, this functionality will not work.

**Example:**
- `EMAIL_HOST_USER = 'your_hotmail@example.com'`
- `EMAIL_HOST_PASSWORD = 'your_password'`

You can find these properties in the `webplayground/settings.py` file 
