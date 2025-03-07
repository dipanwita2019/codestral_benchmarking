# Codestral Benchmarking - AI Code Generation Performance Test

This repository benchmarks the **Codestral model** using **Ollama** to generate Python code across different complexity levels. It measures **Time to First Token (TTFT)** to analyze how quickly the model starts generating responses.

---

## Prerequisites - Setup Guide

###  Install Ollama (AI Model Manager)
Ollama is required to run the **Codestral** model. Install it based on your OS:

#### Windows
Download and install Ollama from:
[Ollama Official Website](https://ollama.com/download)

### Install Codestral ###
```
ollama pull codestral
```

```
ollama show codestral
```

###  Install Python

```
https://www.python.org/downloads/
```
Ensure Python 3.8+ is installed.

#### Windows
Download and install Python from:  Python Official Website.

### Install the Ollama Python Package
To interact with Ollama via Python, install the Ollama Python API:

```
pip install ollama
```

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
##  Running the Benchmark Scripts 
The repository contains three Python scripts, each corresponding to different complexity levels:

Run each script to generate the respective Python code and measure TTFT (Time to First Token) and Time to Completion(TTC).

### Run the Medium Query Script

```
python general_script_1.py

```

### Calculate TTFT

```
stream = ollama.chat(model='codestral', messages=[{"role": "user", "content": query}], stream=True)

# **NOW Start Timing** (Correct placement)
overall_start_time = time.perf_counter()  # Start timing AFTER sending the query

first_token_time = None
generated_code = ""

for chunk in stream:
    if first_token_time is None:
        first_token_time = time.perf_counter()  # Capture TTFT after first response token
        ttft = first_token_time - overall_start_time  # Compute TTFT (query processing excluded)
        print(f" First token received! TTFT (excluding query time): {ttft:.4f} seconds\n")
    
    # Store the full response
    generated_code += chunk['message']['content']

# Step 3: Capture overall time after receiving the last token
overall_end_time = time.perf_counter()
ttc = overall_end_time - overall_start_time  # Compute Time to Completion (TTC)

```
1. time.perf_counter() provides high-precision timing.
2. The loop captures when the first response token arrives.
3. TTFT is displayed for each script in seconds.

## Support
### If you encounter issues:

1. Check if Ollama is installed properly using:
```
ollama version

```
2. Ensure Python 3.8+ is installed.















