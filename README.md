# AI Web Scraper

A Docker-based application that combines web scraping with AI to extract specific information from websites.

## Features

- Web scraping using Selenium with headless Chrome
- Content cleaning and processing with BeautifulSoup
- AI-powered content parsing using Ollama LLM
- User-friendly interface with Streamlit
- Full containerization with Docker

## Architecture

This project uses a microservices architecture with the following components:

- **App**: Python-based web application
- **Selenium**: Headless Chrome browser for web scraping
- **Ollama**: Local LLM for parsing and extracting information
- **Ollama WebUI**: Web interface for the Ollama model
- **PostgreSQL**: Database for storing results (ready for implementation)

## Requirements

- Docker and Docker Compose
- VS Code with Dev Containers extension (recommended)

## Getting Started

### Using Dev Containers

1. Clone the repository
2. Open the project in VS Code
3. When prompted, click "Reopen in Container"
4. VS Code will build and start all the required containers

### Manual Setup

1. Clone the repository
2. Build and run the containers:
3. Access the application at http://localhost:8501 (Streamlit default port)

## Usage

1. Enter a website URL in the text field
2. Click "Scrape Site" to retrieve the website content
3. View the extracted DOM content by expanding the "View DOM Content" section
4. Describe what information you want to extract in the text area
5. Click "Parse Content" to use AI to extract the specified information

## How It Works

1. `scrape_website` function connects to a Selenium server to load the target webpage
2. Content is processed through the `extract_body_content` and `clean_body_content` functions
3. Content is split into chunks using `split_dom_content`
4. Each chunk is processed by Ollama using `parse_with_ollama`
5. Results are displayed in the Streamlit interface

## Project Structure

- `app/`: Main application code
	- `src/`: Source code
		- `main.py`: Streamlit interface
		- `scrape.py`: Web scraping functions
		- `parse.py`: AI parsing functions
	- `.config/`: Configuration files
	- `requirements.txt`: Python dependencies
- `bin/`: Scripts
	- `setup`: Setup script
- `.devcontainer/`: Development container configuration
	- `docker-compose-v3.yaml`: Docker services configuration
	- `devcontainer.json`: VS Code Dev Container configuration
	- `Dockerfile`: Python container definition

## Notes

- The application includes commented code for captcha handling (to be implemented)
- Currently using llama3.2:1b model, but can be configured to use other Ollama models

## Development

To add new features, modify the Python scripts in the src directory.

To run the application outside the dev container:

```bash
cd app
python -m streamlit run src/main.py
```