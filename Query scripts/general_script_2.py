import ollama
import time

# Define the query for generating a reverse string function
query = ("Write a Python function to find the second largest number in a list without using built-in sorting functions.")
output_file = "output.py"

print("\n Starting the script...\n")

# Step 1: Warm-up Query
print(" Sending a warm-up query to ensure the model is loaded...")
ollama.chat(model='codestral', messages=[{"role": "user", "content": "Warm-up"}])
print(" Warm-up complete. Model is ready for querying.\n")

# Step 2: Send the query (Start timing only AFTER sending)
print(f" Querying the model:\n{query}\n")

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

# Step 4: Capture the tokens per second
tokens_used = chunk.get("eval_count")
tokens_per_second = tokens_used / ttc
print(f" Tokens per second using timer: {tokens_per_second:.4f} seconds\n")

# Step 5: Save the generated code to a Python file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("# Generated by Codestral (Ollama)\n")
    f.write(generated_code)

# Step 6: Display final timing metrics
print(f"\n Code successfully generated and saved to `{output_file}`.")
print(f" TTFT (excluding query time): {ttft:.4f} seconds")
print(f" Tokens per second using timer: {tokens_per_second:.4f} seconds")
print(f" Time to Completion (TTC): {ttc:.4f} seconds")
print(" Script execution complete!\n")
