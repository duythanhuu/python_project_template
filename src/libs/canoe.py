"""
canoe.py

Author: Your Name
Date: Date of creation or last modification
Description: A Python module to control CANoe via the COM interface.

This module provides a Canoe class that can be used to interact with CANoe.
The Canoe class provides methods to open CANoe, load a configuration file,
start and stop a measurement, and close CANoe.

Parameters:
config_path (str): The path to the configuration file to load.

"""

import win32com.client

class Canoe:
    """A class to control CANoe via COM interface."""

    CANOE_APP_NAME = "CANoe.Application" # Common variable should be in here not outside of class 

    def __init__(self):
        self.canoe = win32com.client.Dispatch(self.CANOE_APP_NAME)

    def open(self):
        """Open CANoe."""
        self.canoe.Open()

    def load_configuration(self, config_path):
        """Load a configuration file."""
        self.canoe.Open(config_path)

    def start_measurement(self):
        """Start a measurement."""
        self.canoe.Measurement.Start()

    def stop_measurement(self):
        """Stop a measurement."""
        self.canoe.Measurement.Stop()

    def close(self):
        """Close CANoe."""
        self.canoe.Quit()