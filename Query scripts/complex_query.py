import ollama
import time

# Define the super-complex query (Deep Learning Model in PyTorch)
query = ("Create a deep learning model using PyTorch for image classification on the CIFAR-10 dataset. "
         "Include data preprocessing, model architecture, training, and evaluation.")

# Output file to save the generated code
output_file = "pytorch_cifar10.py"

print("\n🚀 Starting the script...\n")

# Step 1: Warm-up Query (Preloading the model into memory)
print("⏳ Sending a warm-up query to ensure the model is loaded...")
ollama.chat(model='codestral', messages=[{"role": "user", "content": "Warm-up"}])
print("✅ Warm-up complete. Model is ready for querying.\n")

# Step 2: Start timing before sending the request
print("⏳ Measuring Time to First Token (TTFT)...")
start_time = time.perf_counter()

# Step 3: Send query using streaming mode to capture first token instantly
print("💡 Querying the model for a PyTorch deep learning implementation...")
stream = ollama.chat(model='codestral', messages=[{"role": "user", "content": query}], stream=True)

# Step 4: Capture time when the first token arrives
first_token_time = None
generated_code = ""

for chunk in stream:
    if first_token_time is None:
        first_token_time = time.perf_counter()  # Capture TTFT at first token arrival
        ttft = first_token_time - start_time  # Compute TTFT
        print(f"✅ First token received! TTFT: {ttft:.4f} seconds\n")
    
    # Store the full response
    generated_code += chunk['message']['content']

# Step 5: Save the generated code to a Python file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("# Generated by Codestral (Ollama)\n")
    f.write("# PyTorch Deep Learning Model for CIFAR-10 Classification\n\n")
    f.write(generated_code)

# Step 6: Display completion message
print(f"✅ Code successfully generated and saved to `{output_file}`.")
print("🚀 Script execution complete!\n")
