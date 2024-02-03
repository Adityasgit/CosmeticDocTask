from openai import OpenAI
# Set your OpenAI API key here
client = OpenAI(api_key = "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")

def generate_story(prompt):
    # Call the OpenAI GPT-3 completions API

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are GPT for making stories."},
        {"role": "user", "content": f"Create a story on '{prompt}'"},
    ]
    
)

    # Extract and display the generated text
    generated_story = response.choices[0].message.content.format()
    print("Generated Story:")
    print(generated_story)


