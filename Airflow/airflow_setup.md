# Apache Airflow Installation on macOS

## 1. Official Documentation
[Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html)

## 2. Installation Commands

- First, create a folder in the terminal named `airflow`:
  ```bash
  mkdir airflow && cd airflow
  ```

- Next, use `pip` to find the latest version of Airflow from the above link and run the following commands in the terminal:

  ```bash
  AIRFLOW_VERSION=2.10.2

  # Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
  # See above for supported versions.
  PYTHON_VERSION="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

  CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
  # For example, this would install 2.10.2 with Python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.10.2/constraints-3.8.txt

  pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
  ```

- Set the `AIRFLOW_HOME` variable by following these steps:

  1. Open the `~/.zshrc` file:
     ```bash
     nano ~/.zshrc
     ```

  2. Set the `AIRFLOW_HOME`:
     ```bash
     export AIRFLOW_HOME=/path/to/your/airflow
     ```
     (For example, if you installed Airflow in the folder created above, it would be something like `export AIRFLOW_HOME=/Users/username/airflow`.)

  3. Save and exit the file:
     - Press `CTRL + O` (then press `Enter` to confirm).
     - Press `CTRL + X` to exit.

  4. Apply the changes and restart the terminal:
     ```bash
     source ~/.zshrc
     ```

  5. Check if it has been set correctly:
     ```bash
     echo $AIRFLOW_HOME
     ```

- Now run the following command:
  - The `airflow standalone` command initializes the database, creates a user, and starts all components. You will have the username and password and can log in by visiting [http://localhost:8080/](http://localhost:8080/):
  ```bash
  airflow standalone
  ```

- To close the terminal and Airflow UI, use `CTRL + C`.

### Optional Step:

If you want to run the individual parts of Airflow manually rather than using the all-in-one standalone command, you can instead run:
```bash
airflow db migrate

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

airflow webserver --port 8080

airflow scheduler
```

## 3. Creating Your Own DAG Python Files

You can do any of the following to create your DAG files:

### A. Using an IDE

Open the `airflow` folder in any IDE and create a folder named `dags` (Airflow recognizes your Python files under this directory).

### B. Using Terminal

You can create a Python file through the terminal using several methods. Here are a couple of common ways:

#### Method 1: Using `nano`

1. Open your terminal.
2. Type the following command to create a new Python file (e.g., `my_script.py`):
   ```bash
   nano my_script.py
   ```
3. This will open the `nano` text editor. You can write your Python code here.
4. After writing your code, save and exit:
   - Press `CTRL + O` (then press `Enter` to confirm).
   - Press `CTRL + X` to exit.

#### Method 2: Using `touch`

If you want to create an empty Python file:

1. Open your terminal.
2. Use the `touch` command:
   ```bash
   touch my_script.py
   ```

This creates an empty file named `my_script.py`. You can then edit it with any text editor of your choice (like `nano`, `vim`, or an IDE).

#### Method 3: Using `echo`

You can also create a Python file and write a single line of code using the `echo` command:
```bash
echo 'print("Hello, World!")' > my_script.py
```

This creates a file called `my_script.py` with the specified content.
