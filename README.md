# Streamlit Project Structure

This document outlines the project structure for a Streamlit application interfacing with a Snowflake database. The structure is designed to promote modularity, scalability, and clear separation of concerns.

# Table of Contents

- [Streamlit Project Structure](#streamlit-project-structure)
- [Table of Contents](#table-of-contents)
  - [How to Setup?](#how-to-setup)
  - [Directory Structure](#directory-structure)
    - [`credentials/`](#credentials)
    - [`images/`](#images)
    - [`models/`](#models)
    - [`pages/`](#pages)
    - [`repositories/`](#repositories)
    - [`scripts/`](#scripts)
    - [`services/`](#services)
  - [General Guidelines](#general-guidelines)
  - [Conclusion](#conclusion)


## How to Setup?

Follow these steps to set up the Streamlit app:

1. **Create a Virtual Environment:** Start by creating a virtual environment for your project. This ensures that your project dependencies are managed effectively. You can find a guide on how to create a virtual environment [here](https://nimbusintelligence.com/2023/12/virtual-environments-python/).

2. **Install Required Libraries:** Run the installation of libraries using the `requirements.txt` file. This file contains all the necessary Python libraries that your Streamlit app will need.

  ```
  pip install -r requirements.txt
  ```

3. **Create Credentials File:** You need to create a `Credentials.py` file using the `Credentials_Template.py` as a guide. This file will be used for the Snowflake connection.

4. **Run the Streamlit App:** Finally, to run the Streamlit app, use the following command in your terminal:

    ```bash
    streamlit run home.py
    ```

    Replace `home.py` with the name of your main Python file.

Follow these steps to ensure a smooth setup of your Streamlit app.


## Directory Structure

### `credentials/`
This folder contains the Snowflake credentials. It is crucial to handle this data securely and ensure it is not exposed in version control (e.g., by using `.gitignore`).

### `images/`
Used for storing images that are part of the user interface in the Streamlit app. This could include logos, icons, and any other static image resources.

### `models/`
Here, we define our data models. Each model represents a structure of data, typically mirroring the structure of a corresponding table in the database. Models should be focused on representing data and should not contain business logic or database interaction code.

### `pages/`
In a multi-page Streamlit application, this directory contains the individual pages. Each page is a separate Streamlit script that represents a different view or section of the application.

### `repositories/`
This folder is crucial for the direct management of model interactions with the Snowflake database. It contains classes or functions for database queries and operations. The repository layer abstracts the database interaction away from the business logic, making the codebase more maintainable.

### `scripts/`
Contains miscellaneous scripts and utilities that do not naturally fit into other directories. These scripts should be general-purpose and potentially reusable in different parts of the application.

### `services/`
The services directory holds the business logic of the application. It acts as a bridge between the repositories (data access layer) and the pages (presentation layer). The service layer is responsible for processing data, implementing business rules, and ensuring that data passed between the repositories and pages is appropriate and correctly formatted.

## General Guidelines

- **Security:** Be particularly mindful of the `credentials` folder. Never commit sensitive information to version control.
- **Modularity:** Keep different aspects of the app (data handling, business logic, presentation) in their respective directories. This makes the code easier to navigate and maintain.
- **Documentation:** Document each part of the application clearly, especially when the functionality might not be immediately obvious to someone new to the project.

## Conclusion

This project structure is designed to facilitate the development of scalable, maintainable, and secure Streamlit applications. By adhering to these guidelines, the application should remain organized and more manageable as it evolves and grows.
