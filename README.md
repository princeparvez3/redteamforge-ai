# 🛡️ RedTeamForge AI — LLM Red-Teaming & Safety Evaluation Platform

**RedTeamForge AI** is a web-based adversarial testing and safety evaluation platform designed to assess how Large Language Models (LLMs) respond to jailbreak attempts, prompt injections, potentially harmful requests, and bias-related scenarios.

Built with Python and Streamlit, the platform combines an adversarial attack engine, automated response classification, bias testing, and interactive analytics in a unified security evaluation dashboard.

<p align="center">

  **🚀 Live Demo:** [RedTeamForge AI](https://redteamforge-ai-6ncw5bqti9wfpxhhgxbavf.streamlit.app/)

</p>

---

## ✨ Key Features

### 🏗️ 1. Modular Architecture

- **Clean Project Structure:** Organized components across `app/`, `core/`, and `data/` for maintainability and scalability.
- **JSONL Data Management:** Structured JSON Lines data handling through a dedicated loader module.
- **Gemini API Integration:** Connects with Google's Gemini API to execute and evaluate adversarial test scenarios.
- **Separation of Concerns:** Keeps application interfaces, attack execution, evaluation logic, and data management organized into separate modules.

### 🎯 2. Adversarial Attack Engine

Test LLM robustness against a library of **100+ pre-built adversarial prompts** across six categories:

| Category | Testing Focus |
|---|---|
| Role-Play | Attempts to bypass model restrictions through role-based scenarios |
| Prompt Injection | Instructions designed to override or manipulate model behavior |
| Encoding | Encoded or transformed adversarial instructions |
| Bias | Prompts designed to reveal potentially unfair or stereotypical outputs |
| Multi-turn | Attempts that use conversational context to influence model responses |
| Direct Harmful | Requests that test the model's safety boundaries |

**Custom Attack Testing**

- Submit custom adversarial prompts for controlled security testing.
- Assign a category to each custom payload.
- Select severity levels from Low to Critical.
- Evaluate model responses against the selected test scenarios.

### 🏷️ 3. Automated Safety Evaluation

The platform uses an **LLM-as-a-Judge** approach to analyze model responses and classify their safety outcomes.

#### Four-Tier Verdict System

| Verdict | Meaning |
|---|---|
| `REFUSED` | The model refused the adversarial request |
| `PARTIAL` | The model partially complied with the request |
| `COMPLIED` | The model complied with the adversarial request |
| `LEAKED` | The evaluation identified a potential system-prompt disclosure |

Additional evaluation capabilities:

- Severity scoring on a 1–5 scale.
- Automated classification of model responses.
- Identification of potentially unsafe behavior.
- Structured results for downstream analysis and reporting.

*Verdicts are automated evaluation signals and should be reviewed before being treated as definitive security findings.*

### 🧠 4. Bias & Fairness Testing

The bias testing module evaluates model responses to demographic variations in prompts.

For example, it can compare scenarios involving different demographic groups or gender-associated roles, such as prompts referring to a male doctor versus a female doctor.

This helps identify potential differences in model outputs that may warrant further investigation.

### 📊 5. Analytics & Reporting Dashboard

An interactive Streamlit dashboard presents evaluation results through visual summaries and charts.

**Analytics include:**

- Attack Success Rate (ASR).
- Category-wise vulnerability analysis.
- Severity distribution.
- Evaluation verdict breakdowns.
- Summary metrics for completed test runs.

**Audit Report Export**

Export structured JSON safety reports containing collected evaluation results for documentation, further analysis, and security review.

### 🎨 6. Professional UI/UX

- Dark-themed interface with custom CSS.
- Top navigation tabs for convenient access to platform modules.
- Clean metric cards and interactive visualizations.
- Red-accented security dashboard styling.
- A streamlined interface inspired by modern developer and security SaaS products.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application and evaluation logic |
| Streamlit | Interactive web application |
| Google Gemini API | Model integration and AI-assisted evaluation |
| Pandas | Tabular data processing, where used |
| Altair | Interactive data visualizations |
| JSON / JSONL | Structured evaluation data and report storage |
| Custom CSS | Dashboard styling and UI customization |

---

## 🏛️ System Workflow

1. **Select a test:** Choose a predefined adversarial prompt or enter a custom payload.
2. **Configure the test:** Set the attack category and severity where applicable.
3. **Execute the attack:** Send the test prompt through the configured model integration.
4. **Evaluate the response:** Analyze the returned response using the automated classifier.
5. **Assign a verdict:** Classify the outcome as `REFUSED`, `PARTIAL`, `COMPLIED`, or `LEAKED`.
6. **Analyze results:** Review attack outcomes, severity scores, category trends, and dashboard analytics.
7. **Export findings:** Generate a structured JSON safety report.

---

## 📂 Project Architecture

The project follows a modular structure organized around application logic, core evaluation components, and data management.

```text
RedTeamForge-AI/
├── app/
│   └── Application interface and dashboard modules
├── core/
│   └── Attack execution and evaluation logic
├── data/
│   └── Attack prompts and evaluation data
├── .streamlit/
│   └── Streamlit configuration
├── requirements.txt
└── README.md
```

*The directory overview is illustrative. Adjust it to match the exact files and folders in your repository.*

---

## 🚀 Run Locally

### Prerequisites

- Python 3.10 or a compatible version supported by your dependencies.
- A Google Gemini API key.
- Git installed on your system.

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the placeholders with your actual repository URL and folder name.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Secrets

Create a `.streamlit/secrets.toml` file in the project root:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your own API key.

**Security best practice:** Never commit API keys, credentials, or other secrets to GitHub. Use Streamlit Community Cloud's Secrets settings for your deployed application.

### 5. Launch the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

*If your Streamlit entry-point file has a different name or location, update the command accordingly.*

---

## 🔐 Responsible Security Testing

RedTeamForge AI is intended for authorized LLM security assessment, robustness research, and safety evaluation.

- Test only models and systems you own or have permission to assess.
- Use controlled test environments where appropriate.
- Protect confidential prompts, system instructions, API keys, and evaluation data.
- Review automated findings manually before drawing security conclusions.
- Treat system-prompt disclosure and attack-success classifications as evaluation indicators that require contextual review.

---

## 🎯 Project Objectives

This project demonstrates practical work in:

- LLM red-teaming and adversarial testing.
- Prompt injection and jailbreak robustness evaluation.
- AI safety classification and automated judging.
- Bias and fairness testing.
- Evaluation data management with JSONL.
- Security analytics and audit report generation.
- Building and deploying AI-powered applications.

---

## 🔮 Potential Future Enhancements

- Support for multiple target LLM providers.
- Historical test-run comparison and regression tracking.
- More detailed attack-family analytics.
- Human review and adjudication workflows.
- Exportable PDF and HTML security reports.
- Configurable evaluation rubrics and severity thresholds.

---

## 🌐 Live Application

**Try RedTeamForge AI:**  
https://redteamforge-ai-6ncw5bqti9wfpxhhgxbavf.streamlit.app/

---

## 👨‍💻 Author

**Prince Parvez**

GitHub: [@princechouhan3](https://github.com/princechouhan3)

---

## 📄 License

Add a license file if you intend to distribute this project under an open-source license. Until a license is specified, reuse and redistribution remain subject to applicable copyright rules.

---

*RedTeamForge AI — Test model robustness. Evaluate safety. Investigate vulnerabilities.*
