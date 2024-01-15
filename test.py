import yaml
import os
print("Current working directory:", os.getcwd())

# Load configuration from file
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
print(config)

