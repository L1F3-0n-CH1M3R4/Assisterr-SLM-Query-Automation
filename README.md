# Overview

This project automates the process of sending queries to the Sentie Small Language Model (SLM) API and retrieving responses. The script reads queries from a text file, sends them to the API, and writes the responses to an output file with a configurable delay between requests.

## Features

--Automated query submission

--Configurable request delay

--Error handling for API requests

--Response logging to output file

--Customizable API endpoint and query file


## Clone the repository:

```bash
git clone https://github.com/L1F3-0n-CH1M3R4/Assisterr-SLM-Query-Automation.git
cd Assisterr-SLM-Query-Automation
```

## Set up a virtual environment:

```
python -m venv .venv
source .venv/bin/activate   #For Linux/Mac
.\.venv\Scripts\activate    #For Windows
```

## Install dependencies:
``` bash
pip install -r requirements.txt
```

## Configuration

Create a .env file in the root directory to store your API key:

**API_KEY** = "your_api_key_here"

**HANDLE_NAME** = "your_handle_name_here"

### Update the following variables in the script as needed:

  **QUERY_FILE**: Path to the file containing queries
  
  **OUTPUT_FILE!**: Path to the file where responses will be saved
  
  **DELAY_BETWEEN_REQUESTS**: Delay time between API requests (in seconds)
  
## Usage

Place your queries in web3_queries.txt, with each query on a new line or use mine.

## Run the script:
```bash
python query.py
```

Responses will be saved in **responses.txt**.

## Error Handling

If any errors occur during API requests, they will be logged in the output file along with the corresponding query.

## Contributing

Feel free to fork the repository and submit pull requests.
