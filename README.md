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
        API_KEY_API1=your_api_key_for_api1
        API_KEY_API2=your_api_key_for_api2
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
