# S. Wallace
# setup.py

from setuptools import setup

# Call setup() function to define this project as a Python package
setup(
    name='mlproject-init',  # Install name for package run via CLI
    version='0.1',  # Initial version
    py_modules=['mlproject_init'],  # Tells setuptools which .py file to treat as the module
    install_requires=[],  # Required packages = blank/placeholder
    entry_points={  # Maps CLI commands to Python functions
        'console_scripts': [  # Creates a command-line executable
            'mlproject-init=mlproject_init:init_project_cli'  # Format: command=module:function
            # When user runs 'mlproject-init' call init_project_cli func. from mlproject_init
        ],
    },
    author="S. Wallace",
    description="CLI tool to scaffold reproducible machine learning project structures",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
