# Setup

## Prerequisites

- Python 3.6+ (tested with 3.7.2). This can be installed on macOS using
  [Homebrew package manager](https://brew.sh/):

    ```
    brew install python   
    ```

    **Note:** You may need to create links for python 3:

    ```
    brew link python
    ```

    To verify that you have the right version, run:

    ```
    python --version
    ```

## Environment

Create a new virtual python environment in the project root directory by
running the following command:

```
python -m venv venv
```

This will create the directory `venv/`. Active the virtual environment by
running:

```
source venv/bin/activate
```

## Packages

Install dependencies by running the following command from the project root
directory:

```
pip install -r requirements.txt
```


# Running

After setting up, run the following command from the project root to start the
server:

```
flask run
```

Then navigate to http://127.0.0.1:5000/ to access the app.

