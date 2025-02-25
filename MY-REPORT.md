# Enhancing AI-Powered Learning Assistants through Prompt Engineering

## **1-liner Description**
Using **chained prompting and automated prompt generation** to optimize requirement analysis for an AI-powered Discord learning assistant.

### **Authors**
Kevin Rodriguez, Benjamin Castro
Academic Supervisor: Dr. Fernando Koch

---

## **Research Question**
How can **chained prompting + automated prompt generation** enhance AI-driven requirement analysis for an interactive learning assistant?

---

## **Arguments**
### **What is already known?**
- Prompt Engineering is **essential for improving LLM responses** in various applications.
- AI-driven educational tools **improve engagement and comprehension**.
- Automated prompt generation **reduces manual input efforts** and **enhances efficiency**.
- **Chained prompting** allows models to handle **multi-step processing**, making them more effective for complex use cases.

### **Challenges in Applying Prompt Engineering**
- Finding the **optimal prompt format** for multi-step educational tasks.
- Ensuring **responses remain relevant, structured, and concise**.
- Avoiding **truncated outputs** while maintaining **response speed**.
- Balancing **creativity (temperature) vs. accuracy** for different task types.

### **What This Research Explores**
- We **apply chained prompting** to automate **requirement analysis**.
- We **test different prompt formats** for **summarization, flashcards, and quiz generation**.
- We **fine-tune model parameters** to optimize **latency vs. response quality**.

---

## **Implications for Practice**
**Easier AI Model Adaptation** → Pre-configured prompt chains simplify AI integration into learning environments.  
**Optimized Content Generation** → AI efficiently extracts and structures study material with minimal manual intervention.  
**Scalability & Automation** → The technique reduces the need for human moderation in AI-assisted learning tools.

---

## **Research Method**
1. **Implemented a prompt engineering experiment** on a **Discord AI tutor bot** using `few_shots.py`.
2. **Modified the baseline** "few-shot prompting" technique to support **chained task processing**:
   - **Summarization**
   - **Flashcard generation**
   - **Quiz question creation**
3. **Tested variations of key parameters**:
   - **Temperature:** Adjusted for accuracy vs. creativity.
   - **Token output limits:** Ensured full responses for complex outputs.
   - **Task chaining:** Structured model responses into **progressive learning steps**.
4. **Ran three test versions**, adjusting:
   - Prompt structure
   - Token limits (`num_predict`)
   - Temperature settings
   - Context size (`num_ctx`)
5. **Analyzed results for clarity, completeness, and efficiency.**
6. **Finalized prompt refinements based on iterative testing.**

---

## **Results: Version Comparisons & Improvements**
### ** Version 1: Initial Test (Baseline)**
#### **Settings Used**
- **Temperature:** `1.0`  
- **Token Limit:** `100`  
- **Context Size:** `100`  
- **Prompt Format:** Simple instruction-based  
#### **Results**
✔️ **Summarization:**  
- **Output:** "Neural networks are a type of machine learning model inspired by the human brain's ability to process information."  
- **Issues:** Summary was **clear but overly short** and sometimes omitted key points.  
- **Time Taken:** `7.014s`  

✔️ **Flashcards:**  
- **Output:** AI generated **4-5 flashcards**, but **some definitions were cut off**.  
- **Issues:** Definitions were **too verbose**, causing truncation.  
- **Time Taken:** `5.554s`  

✔️ **Quiz:**  
- **Output:** AI-generated **multiple-choice questions**, but **one was incomplete**.  
- **Issues:** Not all questions had **four answer choices**, cutting off answers.  
- **Time Taken:** `6.793s`  

---

### ** Version 2: Parameter Refinements**
#### **Changes Made**
- **Lowered Temperature:** `0.7` (better balance between factual accuracy & creativity)  
- **Increased Token Limit:** `150` (prevents truncation)  
- **Modified Prompt Format:** Provided structured **examples** of desired responses  
#### **Results**
✔️ **Summarization:**  
- **Output:** "Neural networks are a type of machine learning that aim to replicate how the human brain processes information..."  
- **Improvements:** Slightly **longer and more informative summary**.  
- **Time Taken:** `5.521s` (**~1.5s improvement**)  

✔️ **Flashcards:**  
- **Output:** Five **fully generated** flashcards with clear definitions.  
- **Improvements:** No cut-off text; definitions **more concise**.  
- **Time Taken:** `6.084s` (**slightly longer but complete**)  

✔️ **Quiz:**  
- **Output:** Each question now **includes four answer choices**.  
- **Improvements:** Answer formatting was **more consistent**, but sometimes **not all questions had correct answers explicitly marked**.  
- **Time Taken:** `6.778s`  

---

### ** Version 3: Final Optimized Model**
#### **Final Adjustments**
- **Further Lowered Temperature:** `0.6` (to improve factual accuracy in quiz generation)  
- **Increased Token Limit:** `200` (ensured complete responses)  
- **Improved Prompt Formatting:**  
  - **Summary now enforces 40-word max length**  
  - **Flashcards enforce exactly five**  
  - **Quiz explicitly requires four answer choices + correct answer marking**  
#### **Final Results**
✔️ **Summarization:**  
- **Output:** "Neural networks simulate human brain function by processing and analyzing data, aiming to recognize patterns and make predictions."  
- **Improvements:** Perfectly **concise (~39 words)** and well-structured.  
- **Time Taken:** `6.488s`  

✔️ **Flashcards:**  
- **Output:** Exactly **five** well-structured cards.  
- **Improvements:** Formatting is **consistent**, and all definitions are **concise yet informative**.  
- **Time Taken:** `6.084s`  

✔️ **Quiz:**  
- **Output:** Each question includes **four answer choices**, **correct answers clearly marked**.  
- **Improvements:** AI **follows all formatting rules**, making the quiz **easy to read & evaluate**.  
- **Time Taken:** `6.778s`  

---

## **Key Takeaways from Progressive Testing**
- **Lowering temperature (1.0 → 0.6) improved factual accuracy** in quiz and summary responses.  
- **Increasing `num_predict` (100 → 200) eliminated truncation issues** in flashcards & quizzes.  
- **Prompt structure played a major role** in response consistency.  
- **Final performance is optimal**, balancing **accuracy, efficiency, and clarity**.  

---

## **Further Research**
**Future Enhancements:**
- **Dynamic prompt adaptation** based on **user feedback loops**.
- **Experimenting with Retrieval-Augmented Generation (RAG)** for improved Q&A accuracy.
- **Fine-tuning multi-turn conversation handling** for deeper interactive learning.
- **Testing with multiple AI models** to compare response consistency.

---

## **Final Thoughts**
By combining **chained prompting** with **automated prompt generation**, we successfully **optimized AI-driven requirement analysis** for educational tools. These techniques can **scale AI learning assistants**, making them **more effective, structured, and adaptable** to real-world student needs.

---