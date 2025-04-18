# CostAnalyzer-as-a-Service

🚀 [Live Demo on Streamlit](https://costanalyzer-k5yhvafsdz2vuenkk9ao7a.streamlit.app)

A simple cloud resource recommendation tool that suggests the most cost-effective cloud instances for different workload types.

---

### Features
- 🧠 Describe your workload in natural language (powered by OpenAI)
- 📦 Choose from predefined workload profiles
- ⚙️ AI-generated resource estimates (CPU, RAM, GPU, duration)
- ☁️ Recommends Azure & AWS instances based on price
- 💸 Includes per-run and monthly cost estimations

---

### How to Run Locally
1. Clone the repo
```bash
git clone https://github.com/cavinkavi/CostAnalyzer.git
cd CostAnalyzer
```
2. Install the requirements
```bash
pip install -r requirements.txt
```
3. Set OpenAI API Key (On macOS/Linux)
```bash
export OPENAI_API_KEY=your_key_here
``` 
4. Run
```bash
streamlit run app.py
``` 

---
