import openai

# Make sure to replace this with your actual API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def get_plan_from_ai(task):
    print(f"Generating a plan for the task: {task}")
    
    # Using the updated OpenAI Completion API for newer versions
    response = openai.Completion.create(
        model="gpt-4",  # Specify the GPT model (e.g., gpt-4)
        prompt=f"Generate a step-by-step plan to {task}.",
        max_tokens=150
    )
    
    # Extract the text from the response
    plan = response.choices[0].text.strip()
    return plan
