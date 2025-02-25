from _pipeline import create_payload, model_req

# (1) Define Task Types for Chained Processing
TASK_TYPE = "quiz"  # Options: "summarization", "flashcards", "quiz"

# (2) Define Simulated Input Message (Modify as Needed)
if TASK_TYPE == "summarization":
    MESSAGE = """Summarize the following text while maintaining a neutral, general explanation. 
Keep the summary under **40 words** for clarity.

Text: "Neural networks are a subset of machine learning that attempt to mimic the way the human brain processes information." """
elif TASK_TYPE == "flashcards":
    MESSAGE = """Generate exactly **five** concise flashcards based on the topic.  
Each flashcard should include:
- A **term** (bolded).
- A **brief definition** (15 words max).

Topic: "Neural networks use layers of interconnected nodes that transform input data through weighted connections."
"""
elif TASK_TYPE == "quiz":
    MESSAGE = """Create a **3-question multiple-choice quiz** based on the given topic.  
Each question should have **exactly four answer choices (A, B, C, D)**.  
Mark the correct answer clearly **in parentheses** at the end.

Topic: "Backpropagation is a supervised learning algorithm used for training artificial neural networks."
"""

# (3) Adjust the Few-Shot Prompt for Educational Use
FEW_SHOT = """You are an AI tutor that helps students learn effectively. Below are examples of how you should respond:

- If the user provides study material, generate a **concise summary**.
- If the user asks for flashcards, extract **key terms and definitions**.
- If the user asks for a quiz, create **multiple-choice questions** from the provided content.

Now process the following request: 
"""

PROMPT = FEW_SHOT + '\n' + MESSAGE

# (4) Configure the Payload with Optimized Parameters
payload = create_payload(
    target="ollama",
    model="llama3.2:latest",
    prompt=PROMPT,
    temperature=0.6,  # 🔽 Lowered for more accurate factual responses
    num_ctx=150,  # 🔽 Reduced for non-summarization tasks
    num_predict=200  
)

### NO MODIFICATIONS BELOW THIS POINT ###
# Send out request to the model
time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')