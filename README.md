# Codestral Benchmarking - AI Code Generation Performance Test

This repository benchmarks the **Codestral model** using **Ollama** to generate Python code across different complexity levels. It measures **Time to First Token (TTFT)** to analyze how quickly the model starts generating responses.

---

## Prerequisites - Setup Guide

###  Install Ollama (AI Model Manager)
Ollama is required to run the **Codestral** model. Install it based on your OS:

#### Windows
Download and install Ollama from:
[Ollama Official Website](https://ollama.com/download)


###  Install Python
Ensure Python 3.8+ is installed.

#### Windows
Download and install Python from:  Python Official Website.

###  Clone the GitHub Repository 
Run the following command to download this repository:

```
git clone https://github.com/dipanwita2019/codestral_benchmarking.git

```
Move into the project directory:

```
cd codestral_benchmarking
```

Navigate to the Python Scripts
```
cd python_scripts
```
###  Running the Benchmark Scripts 
The repository contains three Python scripts, each corresponding to different complexity levels:

| Script |  Complexity  | What it Generates? |
|:-----|:--------:|------:|
| medium_query.py   | `Medium`	 | A Merge Sort function in Python |
|high_query.py	   |  `High`  |   A FastAPI authentication system with JWT |
| super_complex_query.py	   | `Super Complex` |    A PyTorch deep learning model for CIFAR-10 classification |























