
import openai

# Set up your OpenAI API key (stored securely)
openai.api_key = ""


# Define the prompt
prompt = """
You will receive a file of any coding language, the first line will have the path to the file you are looking at. I would like you to parse the code and only store a header for each function in this format. One issue you need to check for is that there are comments in the code, so you need to make sure you are starting at the correct line number and ending at the correct line number. Don't forget that different coding languages use different methods to comment things in and out. Also if you see a new line assume it counts toward the total line number count. Finally, if the function is within a class, give the class name:function name.

For a function within a class:
{class_name:function_name, path, starting_line_number, last_line_number}

For a function without a class:
{function_name, path, starting_line_number, last_line_number}

Example output:
{dataGen:load_data, /functions/main.py, 6, 14}
{load_data, /functions/main.py, 6, 14}

Only send the output with nothing else.

Here is the function:
1: import math
2: 
3: def rectangle_area():
4:     width = float(input("Enter the width of the rectangle: "))
5:     height = float(input("Enter the height of the rectangle: "))
6:     return width * height
7: 
8: def square_area():
9:     side = float(input("Enter the side length of the square: "))
10:     return side * side
11: 
12: def triangle_area():
13:     base = float(input("Enter the base of the triangle: "))
14:     height = float(input("Enter the height of the triangle: "))
15:     return 0.5 * base * height
16: 
17: def circle_area():
18:     radius = float(input("Enter the radius of the circle: "))
19:     return math.pi * radius * radius
20: 
21: def trapezoid_area():
22:     base1 = float(input("Enter the length of the first base of the trapezoid: "))
23:     base2 = float(input("Enter the length of the second base of the trapezoid: "))
24:     height = float(input("Enter the height of the trapezoid: "))
25:     return 0.5 * (base1 + base2) * height
26: 
27: def main():
28:     print("Choose a shape to calculate the area:")
29:     print("1. Rectangle")
30:     print("2. Square")
31:     print("3. Triangle")
32:     print("4. Circle")
33:     print("5. Trapezoid")
34: 
35:     choice = int(input("Enter the number of the shape (1-5): "))
36: 
37:     if choice == 1:
38:         print(f"The area of the rectangle is: {rectangle_area()}")
39:     elif choice == 2:
40:         print(f"The area of the square is: {square_area()}")
41:     elif choice == 3:
42:         print(f"The area of the triangle is: {triangle_area()}")
43:     elif choice == 4:
44:         print(f"The area of the circle is: {circle_area()}")
45:     elif choice == 5:
46:         print(f"The area of the trapezoid is: {trapezoid_area()}")
47:     else:
48:         print("Invalid choice. Please enter a number between 1 and 5.")
49: 
50: if __name__ == "__main__":
51:     main()

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
with open("functionsToHash.txt", "w") as file:
    file.write(response)
