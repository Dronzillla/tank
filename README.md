# Project "Tank"

## Video Demo
[youtube-link](https://youtu.be/dgJGVP-OM5Y)

## Description

This is my implementation of a simple command-line interface tank game. It was developed and tested using **Python 3.12.3**. The specification for this program is provided in a file '[tank-game-description](https://github.com/Dronzillla/tank/blob/main/tank-game-description.md)'.

## Dependencies

This program is designed to run using only the standard Python library, meaning you don't need to install any additional packages or libraries. However, to run tests **pytest** should be installed.

## Executing program

1. **Create folder for your project**:
    ```sh
    mkdir tank_project
    cd tank_project
    ```

2. **Create and activate virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Clone github repository**:
    ```sh
    git clone git@github.com:Dronzillla/tank.git
    cd tank/
    ```

4. **Install requirements**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the program**:
    ```sh
    python3 project.py
    ```

## Testing

During development, manual tests were performed to ensure that the program works as intended. 

For automated testing, **pytest** is used. Automated tests were created only for the main functionality, many additional automated tests are still needed.

1. **To run tests**: 
    ```sh
    pytest
    ```

## Authors

Contributors names and contact info:
* Dominykas (https://github.com/Dronzillla)