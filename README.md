![Shodafinder](https://github.com/user-attachments/assets/10619533-b61a-4246-b169-efc75f1d5e9b)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) ![GitHub last commit](https://img.shields.io/github/last-commit/logm1lo/Shodafinder) ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/logm1lo/Shodafinder/total) ![GitHub License](https://img.shields.io/github/license/logm1lo/Shodafinder) 

```Shodafinder``` is a simple Python script to compute the Shodan hash for a website's favicon

![carbon](https://github.com/user-attachments/assets/0a146587-4b76-462c-ba7b-177df5365544)

## Features

- Validates and processes a URL to fetch the favicon.
- Computes a hash of the favicon using `mmh3`.
- Provides search links for Shodan and ZoomEye based on the favicon hash.

## Requirements

- Python 3.x
- `requests` library
- `mmh3` library
- `base64` library
- `favicon` library

## Installation

1. Clone this repository:

    ```sh
    git clone https://github.com/logm1lo/Shodafinder.git
    ```

2. Navigate to the project directory:

    ```sh
    cd Shodafinder
    ```

3. Install the required libraries:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```sh
    python get_favicon_hash.py
    ```

2. Enter a URL when prompted. Ensure the URL includes a schema (e.g., `http://` or `https://`).

3. The script will fetch the favicon, compute its hash, and display results with links to search in Shodan and ZoomEye.

## Example

```
# Prompt for user input
Enter URL to get the mmh3-HASH: https://example.com

# Output the computed hash of the favicon
Hash: 1234567890

# Provide Shodan search query link
Use this on Shodan for searching, http.favicon.hash:1234567890
    # Direct link to search in Shodan with the computed hash
    or press here: https://www.shodan.io/search?query=http.favicon.hash%3A1234567890

# Provide ZoomEye search query link
Use this on ZoomEye for searching, iconhash:"1234567890"
    # Direct link to search in ZoomEye with the computed hash
    or press here: https://www.zoomeye.org/searchResult?q=iconhash%3A%20%221234567890%22
```


## How to Contribute
  1. Clone repo and create a new branch: ```$ git checkout https://github.com/logm1lo/Shodafinder -b name_for_new_branch```.
  2. Make changes and test
  3. Submit Pull Request with comprehensive description of changes

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Shodan](https://www.shodan.io/) and [ZoomEye](https://www.zoomeye.org/) for providing search engines to explore favicon hashes.
