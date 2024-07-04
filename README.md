# Documentation Generator

This project provides a modular Python-based documentation generator using pydoctor. 
It automatically generates HTML documentation for specified Python packages and creates an index page with tabs for easy navigation.

## Features

- Generates documentation for multiple Python packages
- Creates an index.html with a tabbed interface for easy navigation
- Uses pydoctor for generating detailed API documentation

## Requirements

- Python 3.7+
- pydoctor
- Bootstrap 5.3 (loaded via CDN in the generated HTML)
- tkr_utils


## Setup your project

Create a directory for your project

``` sh
mkdir project_directory_name

cd project_directory_name

```

## Setup tkr_utils

Clone the tkr_utils into your project directory

``` sh
git clone http://github.com/tuckertucker/tkr_utils

cd tkr_utils

pip install -r requirements.txt

cd ..
```

## Setup tkr_docs

Clone the tkr_docs into your project directory

``` sh
git clone http://github.com/tuckertucker/tkr_docs

cd tkr_docs

pip install -r requirements.txt

cd ..
```

## Usage

1. Ensure all requirements are installed:
   ```
   pip install -r requirements.txt
   ```

2. Run the main script:
   ```
   python -m doc_generator.main
   ```

3. The generated documentation will be available in the `docs` directory.

## Customization

To document additional packages, modify the `packages_to_document` list in `doc_generator/main.py`.