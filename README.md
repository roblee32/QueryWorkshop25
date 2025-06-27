# Setup
## UV

This project used UV to manage dependencies. Use any of the installation methods described in the documentation to install it.

https://docs.astral.sh/uv/getting-started/installation/


## Install dependencies
```bash
uv venv
uv sync
```


## Populate the database
I've created a script to populate the database with some sample data. You can run it using the following command:

```bash
python manage.py migrate
python manage.py seeder

```