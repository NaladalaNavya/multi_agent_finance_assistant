from transformers import pipeline

class LanguageAgent:
    def __init__(self):
        self.generator = pipeline(
            "text-generation",
            model="mistralai/Mistral-7B-Instruct-v0.1",
            device_map="auto",               # Automatically chooses CPU/GPU
            trust_remote_code=True,          # Required for Mistral
            offload_folder="offload",        # Avoids memory overload on small RAM
            max_length=200                   # Adjust based on your output need
        )

    def generate_narrative(self, prompt: str):
        output = self.generator(prompt, max_new_tokens=100)[0]["generated_text"]
        return output.strip()