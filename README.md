# Prompt Engine – Reusable Prompt Management Framework for LLMs

 Project Overview

**Prompt Engine** is a reusable Python library designed for creating, managing, validating, and rendering dynamic Large Language Model (LLM) prompts using external templates. It enables consistent prompt usage, easy experimentation, and scalable AI application development without modifying application code.

This project demonstrates how foundational AI tooling can be built from scratch using best practices such as schema validation, templating engines, modular design, and clear documentation.



 Project Architecture


prompt-engine/
├── prompt_engine/ # Core Python package
│ ├── init.py
│ ├── engine.py # PromptEngine (loading, rendering, chaining)
│ ├── models.py # Pydantic template schema
│ ├── exceptions.py # Custom error classes
│
├── templates/ # Prompt templates (YAML)
│ ├── zero_shot_qa.yaml
│ ├── zero_shot_summarize.yaml
│ ├── few_shot_sentiment.yaml
│ ├── few_shot_math.yaml
│ ├── cot_reasoning.yaml
│ ├── cot_debugging.yaml
│ ├── role_python_expert.yaml
│ ├── role_career_mentor.yaml
│ ├── structured_json.yaml
│ └── structured_table.yaml
│
├── examples.py # Usage demonstrations
├── pyproject.toml # Package configuration
├── requirements.txt # Dependencies
└── README.md # Documentation
```



##  Template Schema

Each prompt template is defined using **YAML** and validated using **Pydantic**. The schema ensures consistency and prevents runtime errors.

### Required Fields

```yaml
name: unique_template_name
description: Description of the prompt’s purpose
pattern: zero-shot | few-shot | cot | role-based | structured
input_variables:
  - variable1
  - variable2
template: |
  Prompt text using {{ variable1 }}
```

 Optional Field (Few-Shot Only)

```yaml
examples:
  - input: "example input"
    output: "example output"
```



 Supported Prompt Patterns

The framework supports **five advanced prompt engineering patterns**, with **two templates for each pattern** (10 total):

### 1️ Zero-Shot

Direct instructions or questions without examples.

### 2️ Few-Shot

Prompts that include multiple input/output examples to guide the model.

### 3️ Chain-of-Thought (CoT)

Prompts that explicitly encourage step-by-step reasoning before producing the final answer.

### 4️ Role-Based

Prompts that assign a specific persona or role to the LLM (e.g., expert, mentor).

### 5️ Structured Output

Prompts that instruct the model to respond in a strict format such as JSON or tables.



  Prompt Chaining

Prompt chaining allows the output of one rendered prompt to be used as the input for another prompt.

### Example

```python
summary = engine.render(
    "zero_shot_summarize",
    {"text": "Machine learning is a subset of AI."}
)

final_output = engine.render(
    "structured_json",
    {"text": summary}
)
```

This demonstrates how prompts can be composed into multi-step workflows.



  Installation

 Clone the Repository

```bash
git clone https://github.com/<your-username>/prompt-engine.git
cd prompt-engine
```

### Install as a Python Package

```bash
pip install .
```

### Dependencies

* Python 3.9+
* pydantic
* jinja2
* pyyaml

(All dependencies are declared in `pyproject.toml`)



 Usage

### Initialize the Prompt Engine

```python
from prompt_engine.engine import PromptEngine

engine = PromptEngine("templates")
```

### Render a Prompt

```python
output = engine.render(
    "zero_shot_qa",
    {"question": "What is Artificial Intelligence?"}
)
print(output)
```

### Run Examples

```bash
python examples.py
```

The example script demonstrates:

* Template loading
* Rendering all five prompt patterns
* Prompt chaining
* Validation error handling



 Error Handling & Validation

The engine validates all required input variables before rendering.

Example Error

```text
Missing required variable "text" for template "structured_json"
```

This ensures prompt integrity and makes debugging easy.

---

 Evaluation Checklist Compliance

Standard Python package structure (`pyproject.toml`)

10 YAML templates covering all required patterns

Pydantic-based schema validation
 
Jinja2-based rendering engine
 
Prompt chaining support

Clear and informative error messages

Comprehensive examples demonstrating all features



  Conclusion

This project demonstrates how a robust, extensible prompt management framework can be built using Python. The design emphasizes clarity, validation, reusability, and scalability—key qualities required for production-grade AI systems.

