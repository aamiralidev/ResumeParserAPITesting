# Resume Parsing API Tester

## Overview

This Python-based tool allows users to test and compare the results of different resume parsing APIs. It provides a simple graphical user interface (GUI) to select APIs, upload resumes, and receive parsed results in JSON format.

## Features

- **API Support:** Easily test multiple resume parsing APIs in one go.
- **Comparison:** Compare the output of each API for a given resume.
- **Configurability:** Set API keys using environment variables or a .env file.
- **User-Friendly:** Intuitive GUI for seamless testing.

## Requirements

- Python 3.x
- Install dependencies using `pipenv install`
- API keys for the chosen resume parsing APIs (obtained from respective providers).

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/aamirali-dev/ResumeParserAPITesting.git
    cd ResumeParserAPITesting
    ```

2. Install dependencies:

    ```bash
    pipenv install
    ```

3. Set up API keys:

    - For each API, add the corresponding API key to your environment variables or create a `.env` file in the project root. Example:

        ```env
        SUPER_PARSER_API_KEY=""
        APILAYER_API_KEY=""
        SOVREN_ACCOUNT_ID=""
        SOVREN_API_KEY=""
        AFFINDA_API_KEY=""
        AWS_BUCKET_NAME=""
        AWS_SECRET_KEY=""
        AWS_ACCESS_KEY=""
        AWS_REGION=""
        HIRIZE_API_KEY=""
        EDEN_AI_RESUME_PARSING_API_KEY=""
        HRFLOW_API_KEY=""
        HRFLOW_API_USER_EMAIL=""
        HRFLOW_APPLICATION_REFERENCE=""
        HRFLOW_SOURCE_KEY=""
        ```

4. Run the application:

    ```bash
    python main.py
    ```

## Usage

1. Open the application using `python main.py`.
2. Check the box next to the APIs you want to test.
3. Upload a resume file.
4. Select the output folder for parsed results.
5. Click the "Generate Result" button.

The tool will send requests to the selected APIs, parse the resume, and save the results as JSON files in the specified output folder.

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or suggest improvements.

## License

This project is licensed under the [MIT License](LICENSE).
