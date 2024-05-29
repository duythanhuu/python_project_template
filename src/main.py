"""
Script: main.py
Author: Your Name
Date: Date of creation or last modification
Description: 
    This Python script controls CANoe via the COM interface. It uses the Canoe 
    class from the canoe module to interact with CANoe. The script takes a path 
    to a configuration file as a command-line argument, opens CANoe, loads the 
    configuration file, starts a measurement, and then stops the measurement 
    and closes CANoe.

Parameters:
    config_path (str): Path to the configuration file to load. This is a 
                       mandatory command-line argument.
    output_dir (str): Directory where the test report will be saved. This is 
                      an optional command-line argument. Default is './output/'.

Usage:
    python main.py <config_path> --output_dir <output_dir>

    Replace <config_path> with the path to your configuration file, and 
    <output_dir> with the directory where you want the test report to be saved. 
    If you don't provide an output directory, the script will use './output/' 
    by default.

Debug Mode:
    To run the script in debug mode please set DEBUG_CONFIG_PATH to the path of
    the configuration file you want to use for debugging.

Hints:
    If the script fails to open CANoe, ensure that CANoe is installed and that 
    the path to the CANoe executable is correctly set in the PATH environment 
    variable.

⚠️ WARNING ⚠️
    This script modifies the configuration file and the output directory. 
    Ensure to back up any important data before running the script.
"""

import os
import sys
import argparse
import shutil
import time
from libs import canoe

# ==============================
# Global Variables
# ==============================

# Debug mode flag. Set to True if the DEBUG environment variable is set.
DEBUG = os.getenv('DEBUG', False)

# Default output directory. This is where the test report will be saved.
DEFAULT_OUTPUT_DIR = './output/'

# Configuration file to use in debug mode.
DEBUG_CONFIG_PATH = './debug_config.cnf'

# Path to the slave_tool1 executable. 
# WARNING: This path is hard-coded and may need to be updated if the location of slave_tool1 changes.
SLAVE_TOOL1_RELATIVE_PATH = './slave_tool1/'
SLAVE_TOOL1_FILENAME = 'slave_tool1.exe'


def modify_config(config_path):
    """Modify the configuration file.

    This function opens the configuration file, makes some modifications, and then saves the changes.

    Parameters:
    config_path (str): The path to the configuration file to modify.
    """
    # Open the configuration file.
    with open(config_path, 'r+') as file:
        # Read the configuration file.
        config = file.read()

        # Make some modifications to the configuration.
        # For example, you might want to change some settings or add some new options.
        # This will depend on the format of your configuration file and what modifications you want to make.
        config = config.replace('old_value', 'new_value')

        # Write the modified configuration back to the file.
        file.seek(0)
        file.write(config)
        file.truncate()

def save_report(output_dir):
    """Save the test report to the specified directory.

    Parameters:
    output_dir (str): The directory where the test report should be saved.

    Returns:
    bool: True if the report was saved successfully, False otherwise.
    """
    # Implement the functionality to save the test report here.
    # For now, we'll just return True to indicate that the report was saved successfully.
    return True

def main(config_path, output_dir):
    """
    Main function.

    This function controls the interaction with CANoe.

    Parameters:
    config_path (str): The path to the configuration file to load.
    output_dir (str): The directory where the test report should be saved.
    """

    # ========================================
    # Part 1: Modify the configuration file
    # ========================================
    print("Modifying configuration file...")
    modify_config(config_path)

    # ========================================
    # Part 2: Process with CANoe
    # ========================================
    print("Starting CANoe processing...")
    canoe_app = canoe.Canoe()
    canoe_app.open()
    canoe_app.load_configuration(config_path)
    canoe_app.start_measurement()

    # You can add a sleep here if needed
    print("Processing... Please wait.")
    time.sleep(10)  # Sleep for 10 seconds

    # Do other stuff...
    # For example, you might want to send some CAN messages, or interact with
    # some other part of your system.

    canoe_app.stop_measurement()
    canoe_app.close()

    # ========================================
    # Part 3: Save the report
    # ========================================
    print("Saving test report...")
    if save_report(output_dir):
        print("Test report saved successfully.")
    else:
        print("Failed to save test report.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Control CANoe via the COM interface.')
    
    if DEBUG:
        print("Running in debug mode.")
        parser.add_argument('config_path', nargs='?', default=DEBUG_CONFIG_PATH, help='The path to the configuration file to load.')
        parser.add_argument('--output_dir', default=DEFAULT_OUTPUT_DIR, help='The directory where the test report should be saved.')
        args = parser.parse_args()
    else:
        print("Running in normal mode.")
        parser.add_argument('config_path', help='The path to the configuration file to load.')
        parser.add_argument('--output_dir', default=DEFAULT_OUTPUT_DIR, help='The directory where the test report should be saved.')
        args = parser.parse_args()

    # Verify the configuration file exists
    if not os.path.exists(args.config_path):
        print(f"Configuration file does not exist: {args.config_path}")
        exit(1)

    # Verify the output directory exists, if not create it
    if not os.path.exists(args.output_dir):
        print(f"Output directory does not exist, creating it: {args.output_dir}")
        os.makedirs(args.output_dir)
    else:
        # If the directory exists, you might want to remove it and create a new one
        print(f"Output directory exists, removing and creating a new one: {args.output_dir}")
        shutil.rmtree(args.output_dir)
        os.makedirs(args.output_dir)

    main(args.config_path, args.output_dir)