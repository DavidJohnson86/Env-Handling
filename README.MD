## Purpose

In this example, `load_dotenv()` loads environment variables from a `.env` file, and these values are then used to instantiate the Pydantic models.

The Pydantic model enforces the data types and validation rules specified in the model.

Combining `python-dotenv` and Pydantic provides a clean and organized way to manage configuration settings in your Python projects, ensuring separation of concerns and ease of validation.

## If you want to run

When you pull the repo create a .env file and copy the contents of env.example to .env.

To manage your project dependencies and create a virtual environment, you can use Poetry. Follow these steps to set up Poetry:

- Install Poetry
   ```
   pip install poetry
   ```

- Navigate to the `./env-handling` folder.

- Set up the virtual environment and package management using Poetry:
   ```
   poetry shell
   poetry install
   ```