# 🔍 AI Image Analyzer

A local, private AI-powered image analyzer built with [Streamlit](https://streamlit.io), [Ollama](https://ollama.com), and [LangChain](https://www.langchain.com/). Upload an image, ask a question, and get detailed visual insights — all without sending data to the cloud.

---

## Tech Stack

- **Python 3.10+**
- **Streamlit** – for the web UI
- **Ollama** – for running local vision models (like `llava`)
- **LangChain** – for chaining LLM calls and vision bindings
- **Pillow** – image processing

---

## Prerequisites

### 1. Install Python 3.10+

Download Python 3.10 from [python.org](https://www.python.org/downloads/release/python-3100/).  
Verify Python and pip are available:

```bash
python --version
pip --version
```

### 2. Install Ollama

Download and install Ollama from [ollama.com](https://ollama.com/download).  
Start the Ollama server:

```bash
ollama serve
```

Pull the vision model (e.g., `llava`):

```bash
ollama pull llava
```

### 3. Set Up a Virtual Environment (Optional but Recommended)

Create a virtual environment:
Activate it


### 4. Verify System Requirements

Ensure your system meets the following requirements:
- **OS**: Windows, macOS, or Linux
- **RAM**: At least 8GB (16GB recommended for better performance with vision models)
- **Disk Space**: 10GB+ free for Ollama models and dependencies
- **GPU**: NVIDIA/AMD GPU at least 12 Gb for faster model inference (ensure CUDA compatibility for NVIDIA)

---

## Installation Steps
1. **Install Dependencies**  
   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Ollama Setup**  
   Ensure the Ollama server is running and the `llava` model is available:

   ```bash
   ollama list
   ```

---

## Running the Application

1. **Start the Streamlit App**  
   Run the application:

   ```bash
   streamlit run app.py
   ```

2. **Use the App**  
   - Upload an image via the web interface.
   - Enter a question (e.g., "What objects are in this image?").
   - View the analysis provided by the `llava` model.

---

## 🖼Usage

1. Upload an image of a park.
2. Ask: "What activities are people doing in this image?"
3. Example response: "People are jogging, sitting on benches, and walking dogs in a green park with trees and a pathway."

---

## Project Structure

```
vision-model-analyzer/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── venv/                  # Virtual environment (if created)
```
--- 

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgments

- [Ollama](https://ollama.com) for local vision models.
- [Streamlit](https://streamlit.io) for the web framework.
- [LangChain](https://www.langchain.com) for LLM integration.
- [Pillow](https://python-pillow.org) for image processing.
---

## 📬 Contact
For questions, email me merwin.pinto.in@gmail.com
