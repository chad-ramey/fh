# FireHydrant Lab

This repository contains Python scripts designed to automate tasks related to managing FireHydrant incidents and users.

## Table of Contents
  - [Table of Contents](#table-of-contents)
  - [Scripts Overview](#scripts-overview)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Scripts Overview
Here’s a list of all the scripts in this repository along with their descriptions:

1. **[fh_export_incidents.py](fh_export_incidents.py)**: Exports incident data from FireHydrant, allowing for incident reporting and analysis.
2. **[fh_users.py](fh_users.py)**: Retrieves a list of all users in FireHydrant, useful for managing user roles and permissions.

## Requirements
- **Python 3.x**: Ensure that Python 3 is installed on your system.
- **FireHydrant API**: Install the necessary Python libraries to interact with the FireHydrant API.
- **API Keys**: You will need FireHydrant API credentials to authenticate API requests.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-name/firehydrant-automation-scripts.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your FireHydrant API token and other necessary credentials in environment variables:
   ```bash
   export FIREHYDRANT_API_TOKEN="your-token-here"
   ```

## Usage
Run the desired script from the command line or integrate it into your existing workflows.

Example:
```bash
python3 fh_export_incidents.py
```

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality or add new features.

## License
This project is licensed under the MIT License.
