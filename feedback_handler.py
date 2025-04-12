import openai

openai.api_key = "sk-abc123your-real-key-here"
  # Same key

def handle_feedback(original_task, old_plan, error_reason):
    prompt = f"""
The following task was attempted: {original_task}

Original plan:
{old_plan}

It failed due to: {error_reason}

Please suggest a corrected plan to fix the issue and retry.
Only provide updated commands or code.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
