# Sixth Workshop for Programming IV

## Overview

This project is part of the sixth workshop for the Programming IV course. It includes multiple programs demonstrating various concepts in Python, including a music player application, a login interface, and a shape area calculator. The project follows Object-Oriented Programming (OOP) principles and adheres to the SOLID design principles.

## Features

### Program 1: Shape Area Calculator
- Calculate the area of different shapes: Square, Rectangle, Triangle, and Circle.
- User interface through the command line.

### Program 2: Person Management
- Create and manage `Worker` and `Student` objects.
- User interface through the command line.

### Program 3: Login Interface
- Simple login interface using Tkinter.
- Authentication with hardcoded credentials.

### Program 4: Music Player
- Play, pause, resume, and stop music files.
- Display cover images for MP3 and FLAC files.
- User interface built with Gradio.
- Supports MP3, FLAC, WAV, and MP4 file formats.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/adriancho91s/sixth-workshop-programming-IV.git
    cd sixth-workshop-programming-IV
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Program 1: Shape Area Calculator

1. Navigate to the `program-1` directory:
    ```sh
    cd program-1
    ```

2. Run the shape area calculator:
    ```sh
    python main.py
    ```

### Program 2: Person Management

1. Navigate to the `program-2` directory:
    ```sh
    cd program-2
    ```

2. Run the person management application:
    ```sh
    python main.py
    ```

### Program 3: Login Interface

1. Navigate to the `program-3` directory:
    ```sh
    cd program-3
    ```

2. Run the login interface application:
    ```sh
    python main.py
    ```

### Program 4: Music Player

1. Navigate to the `program-4` directory:
    ```sh
    cd program-4
    ```

2. Run the music player application:
    ```sh
    python main.py
    ```

## Project Structure

- `program-1/`: Contains the shape area calculator application.
  - `main.py`: Main script for the shape area calculator.
- `program-2/`: Contains the person management application.
  - `main.py`: Main script for the person management.
  - `person.py`: Contains the `Person`, `Worker`, and `Student` classes.
- `program-3/`: Contains the login interface application.
  - `main.py`: Main script for the login interface.
- `program-4/`: Contains the music player application.
  - `main.py`: Main script for the music player.
  - `play.png`, `pause.png`, `resume.png`, `stop.png`: Icon files for the buttons.
- `README.md`: Project documentation.

## Dependencies

- Python 3.12.2
- Pygame 2.6.1
- Gradio
- Mutagen
- Tkinter (comes with Python)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.