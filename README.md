# ITF+ Flashcards Breh

Welcome to ITF+ Flashcards Breh, a simple and interactive flashcard application powered by Flask! This README will guide you through setting up and running the application.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you can run the application, make sure you have the following prerequisites installed:

- Python 3.x
- Flask (You can install it using `pip install Flask`)
- Python dotenv (You can install it using `pip install python-dotenv`)

## Installation

1. Clone this repository to your local machine:

`git clone https://github.com/yourusername/itf-flashcards-breh.git`

2. Navigate to the project directory:

`cd itf-flashcards-breh`

3. Create a virtual environment (optional but recommended):

`python -m venv venv`

4. Activate the virtual environment:

- On Windows:

  `venv\Scripts\activate`


- On macOS and Linux:

  `source venv/bin/activate`

5. Install the required dependencies:

`pip install -r requirements.txt`

6. Create a `.env` file in the project directory and add your secret key. You can generate a secret key using Python:

SECRET_KEY=your_secret_key_here

## Usage
To run the application, execute the following command in your project directory:

`python3 app.py`

The application will start and be accessible at http://localhost:5000.

## Features

- Choose the number of flashcards to study from the menu.
- Click "Start" to begin the flashcard session.
- Reveal flashcard answers by clicking "Reveal The Wisdom."
- Navigate to the next flashcard with the "Proceed" button.
- Return to the menu at any time by clicking "Main Menu."

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

