# Fetch-take-home-exercise

This is an endpoint-uptime-analyzer written in Python.

Requirements can be found here: https://fetch-hiring.s3.us-east-1.amazonaws.com/site-reliability-engineer/health-check.pdf 

**Python:**
To run this script, do the following:
  1. Clone this repo
  2. cd Fetch-take-home
  3. Create the virtual environment: python3 -m venv env
  4. Activate the virtual environent: env/Scripts/acivate
  5. Install the dependencies: pip install -r requirements.txt
  6. Run the file: Python domain_uptime.py path/to/yaml.file
**Docker:**
  1. Clone this repo
  2. cd Fetch-take-home
  3. Build the docker image: docker build -t image_name .
  4. Run the file: docker run image_name path/to/.yaml



