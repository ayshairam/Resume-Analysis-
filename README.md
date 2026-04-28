# Resume Analysis

AI-powered resume analyzer using local LLM (Ollama + Llama3) that evaluates job fit, generates ATS score, identifies skill gaps, and provides actionable feedback through a Streamlit interface.

## Features

- **Resume Analysis**: Comprehensive evaluation of resumes against job descriptions
- **ATS Score Generation**: Analyze how well your resume performs with Applicant Tracking Systems
- **Job Fit Evaluation**: Get detailed insights on how well your resume matches job requirements
- **Skill Gap Identification**: Discover missing skills and competencies needed for target positions
- **Actionable Feedback**: Receive specific recommendations to improve your resume
- **Local LLM Processing**: Uses Ollama with Llama3 for privacy-focused analysis

## Tech Stack

- **Python**: Core programming language
- **Streamlit**: Interactive web interface
- **Ollama**: Local LLM runtime
- **Llama3**: Language model for analysis

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) with Llama3 model
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayshairam/Resume-Analysis-.git
   cd Resume-Analysis-
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Ollama**
   - Download and install Ollama from [ollama.ai](https://ollama.ai/)
   - Pull the Llama3 model:
     ```bash
     ollama pull llama3
     ```

## Usage

1. **Start Ollama** (in a separate terminal)
   ```bash
   ollama serve
   ```

2. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

3. **Access the application**
   - Open your browser and navigate to `http://localhost:8501`
   - Upload your resume (PDF or text format)
   - Paste the job description you're interested in
   - Click analyze and receive comprehensive feedback

## Features in Detail

### Resume Analysis
Upload your resume and get a detailed breakdown of your qualifications, experience, and education.

### ATS Score
Receive a quantitative score (0-100) indicating how well your resume is optimized for Applicant Tracking Systems.

### Job Fit Analysis
Compare your resume against specific job descriptions to understand how well you match the position requirements.

### Skill Gap Report
Identify the skills mentioned in the job description that are missing from your resume and get recommendations for improvement.

### Actionable Recommendations
Get specific, actionable suggestions to improve your resume and increase your chances of landing an interview.

## Project Structure

```
Resume-Analysis-/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── [additional files]
```

## Configuration

The application uses Ollama's default configuration. Ensure:
- Ollama is running on `http://localhost:11434` (default)
- Llama3 model is installed and available

## Troubleshooting

### Ollama Connection Issues
- Ensure Ollama service is running
- Check that Ollama is accessible at `http://localhost:11434`
- Restart Ollama if connection fails

### Model Not Found
- Verify Llama3 is installed: `ollama list`
- If not installed, run: `ollama pull llama3`

### Streamlit Issues
- Clear Streamlit cache: `streamlit cache clear`
- Check Python version compatibility (3.8+)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

## Acknowledgments

- [Streamlit](https://streamlit.io/) - For the interactive web framework
- [Ollama](https://ollama.ai/) - For local LLM deployment
- [Meta Llama3](https://www.meta.com/llama/) - For the language model

---

Made with ❤️ for job seekers everywhere
