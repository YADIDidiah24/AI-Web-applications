# AI Web Application for Text Summarization

## Overview

This project is a web-based application that leverages Artificial Intelligence (AI) for text summarization. Built using Flask, the application allows users to input long pieces of text and receive a summarized version based on a custom summary ratio. The project demonstrates how Natural Language Processing (NLP) techniques can be integrated into web applications to provide real-time, interactive solutions for content management, data summarization, and more.

## Features

- **Text Summarization**: The application processes text input by users and provides a condensed summary based on a ratio.
- **Sentence Scoring**: The application also provides sentence-level scoring to show which parts of the text are most important for the summary.
- **Customizable Summary Ratio**: Users can adjust the ratio between 0 and 1 to control the length of the summary.
- **Interactive Web Interface**: A user-friendly interface built with HTML, CSS, and JavaScript to enhance user experience.

## Technologies Used

- **Flask**: Python web framework for creating the backend of the application.
- **HTML/CSS**: For creating the structure and styling of the web pages.
- **JavaScript**: To handle form submission and display the results dynamically.
- **Python**: For implementing the text summarization logic and handling requests.
- **Natural Language Processing (NLP)**: For text summarization and sentence scoring.

## How to Run the Application

### Prerequisites

- Python 3.6+
- Flask
- Required Python libraries (e.g., `nltk`, `numpy`, etc.)

### Installation

1. Clone the repository or download the files:

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start the Flask development server:
    ```bash
    python app.py
    ```

4. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

1. Enter the text you want to summarize in the text area.
2. Set the **Summary Ratio** (between 0 and 1) to control the length of the summary.
3. Click **Summarize** to get the summarized text and sentence scores.

## Example

- **Input Text**:
    ```text
    Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. The term may also be applied to any machine that exhibits traits associated with a human mind such as "learning" and "problem-solving."
    ```

- **Summary Output**:
    ```text
    AI refers to the simulation of human intelligence in machines that are programmed to think and learn.
    ```

- **Sentence Scores**:
    - Sentence 1: 0.85
    - Sentence 2: 0.65


## Contributing

If you'd like to contribute to the project, feel free to fork the repository and submit pull requests. Please make sure to follow the standard coding conventions and write tests where applicable.

## License

 <p>© 2025 Text Summarizer. All Rights Reserved | Developed By Yadidiah Kanaparthi</p>



