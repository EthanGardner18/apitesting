
import openai

# Set up your OpenAI API key (stored securely)
openai.api_key = "sk-dKkRWlmUofaExHEFJQRi0QRG-Nq1IxPOk0Zq5C_JvpT3BlbkFJd41IeOSaBXNQjwEyMDrS33MigiW_FW_gvSpIoK3fMA"


# Define the prompt
prompt = """
Here are the current functions in the code, The last value in these hashed names are a boolean for if its been visited
or not. If something has been visited (value of 1) don't ask for it again.:

{rectangle_area, /functions/main.py, 3, 6, 1}
{square_area, /functions/main.py, 8, 10, 1}
{triangle_area, /functions/main.py, 12, 15, 1}
{circle_area, /functions/main.py, 17, 19, 1}
{trapezoid_area, /functions/main.py, 21, 25, 1}
{main, /functions/main.py, 27, 49, 1}

I would like you to do the code review by asking what function you would like to see next. Which function would you 
like to look at first?


Start by the first line being the hash i sent to you:
ex. {main, /functions/main.py, 27, 49}


If you find an error but it in this type of block:
*********
expecting string in ..
********

The next block is for the code review:

^^^^^^^^^^^^^^^^
10 word review of the function

^^^^^^^^^^^^^^^^

Then in this block put only the function name that you would like to see:

$$$$$$$$$$$
function name
$$$$$$$$$$$


Here is the function to review:

def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    return mathpi * radius * radius

    
"""

# Make a request to the OpenAI API
completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Print the completion result (assistant's response)
response = completion.choices[0].message["content"]

# Write the response to a file named "functionsToHash.txt"
with open("currentReview.txt", "w") as file:
    file.write(response)
