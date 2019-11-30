# flask-demo
Simple Flask API Demonstration Which Simulates a Users Database

# Installation

1. If you do not have Anaconda installed... Install it w/
    - `brew cask install anaconda` (OSX)
2. Clone this repo
3. Change directories to to the cloned repo
4. Create a Conda environment
    - `conda create -n flask-demo python=3.7`
5. Activate your new environment
    - `source activate flask-demo`
6. Install Dependencies
    - `pip install -r requirements.txt`
7. Export FLASK_APP variable
    - `export FLASK_APP=app.py`

# Start The Flask Server

1. Run Flask Server
    - `flask run`

# Setup Insomnia Workspace
1. Install Insomnia
    - OSX
        - `brew cask install insomnia`
    - All Platforms
        - [Insomnia Website](https://insomnia.rest/)
2. Import the `Insomnia.json` file into Insomnia