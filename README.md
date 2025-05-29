This project is an AI-powered agent framework designed to extract and analyze information from multiple input sources such as JSON data, emails, and PDF documents. The system orchestrates various specialized agents to process inputs, extract relevant information, and generate structured outputs in real-time.
Features

    Multi-source input processing: JSON, Email, PDF.

    Extraction of key information such as user details, email metadata, and document content.

    Modular agent-based architecture for scalability and easy maintenance.

    Simple command-line interface for running the orchestrator.

    Placeholder for PDF table extraction (to be implemented).

Technologies Used

    Python 3.x

    Huggingface Transformers (BART model)

    PyPDF2 (for PDF text extraction)

    Standard libraries: json, datetime, etc.

Project Structure

flowbit_project/
├── agents/              # Contains individual agent modules for JSON, Email, PDF parsing
├── mcp/                 # Main control process - orchestrator script
├── memory/              # Memory store management
├── utils/               # Helper functions and utilities
├── data/                # Sample input files (emails, JSON)
├── output.json          # Output generated after running the project
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation

Setup & Installation

    Clone the repository:

git clone https://github.com/NarsingDatha/ai-agent-project.git
cd ai-agent-project

(Optional) Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Run the orchestrator:

    PYTHONPATH=. python3 mcp/orchestrator.py

Usage

    Place your input files (JSON, email text, PDF) in the data/ folder.

    Run the orchestrator script.

    The output will be generated and displayed in the terminal and saved to output.json.

Future Enhancements

    Implement PDF table extraction and processing.

    Add support for more input formats.

    Build a web interface for easier interaction.

Author

Narsing Datha
Email: doothanarsingdatta07096@gmail.com
GitHub: https://github.com/NarsingDatha
