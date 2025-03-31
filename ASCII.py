import pywhatkit as kit
import os

# Function to convert image to ASCII art
def image_to_ascii(image_path, output_file):
    try:
        # Check if the image file exists
        if not os.path.exists(image_path):
            print(f"Error: Image file '{image_path}' not found.")
            return

        # Convert image to ASCII art
        kit.image_to_ascii_art(image_path, output_file)
        print(f"ASCII art saved to {output_file}.txt")
    except Exception as e:
        print(f"Error: {e}")

# Provide the correct file path
image_path = r"C:\Users\Fathima M P\Downloads\istockphoto-479629586-612x612.jpg"# Replace with the correct image path
output_file = r"C:\Users\Fathima M P\Desktop\Python_Games\ascii_art"    # Output file path without extension

# Convert image to ASCII
image_to_ascii(image_path, output_file)

# Check if the ASCII file exists and display it
ascii_file = f"{output_file}.txt"
if os.path.exists(ascii_file):
    with open(ascii_file, "r") as file:
        print(file.read())
else:
    print(f"Error: ASCII art file '{ascii_file}' was not created.")





### Code Explanation:

# ```python
# import pywhatkit as kit
# import os
# ```
# - **`import pywhatkit as kit`:** This imports the `pywhatkit` library and gives it an alias `kit`. `pywhatkit` is a Python library that provides many useful functions, one of which is converting images into ASCII art. The `image_to_ascii_art()` function is part of this library.
# - **`import os`:** This imports the `os` library, which provides functions to interact with the operating system, such as checking if files or directories exist.



# ```python
# # Function to convert image to ASCII art
# def image_to_ascii(image_path, output_file):
# ```
# - This line defines a function called `image_to_ascii` that takes two parameters:
#   - **`image_path`**: The path to the image file you want to convert into ASCII art.
#   - **`output_file`**: The path (without the `.txt` extension) where the ASCII art will be saved.



# ```python
#     try:
# ```
# - This line starts a **try block**, which is used to handle exceptions (errors). Any code inside this block is "tried," and if any errors occur, they will be caught in the `except` block below.



# ```python
#         # Check if the image file exists
#         if not os.path.exists(image_path):
#             print(f"Error: Image file '{image_path}' not found.")
#             return
# ```
# - **`os.path.exists(image_path)`** checks if the file at the specified `image_path` exists. If the file doesn't exist, it returns `False`.
# - **`if not os.path.exists(image_path)`**: If the file is not found, the program prints an error message and **`return`** exits the function early, so the program doesn't try to proceed with an invalid image file.



# ```python
#         # Convert image to ASCII art
#         kit.image_to_ascii_art(image_path, output_file)
#         print(f"ASCII art saved to {output_file}.txt")
# ```
# - **`kit.image_to_ascii_art(image_path, output_file)`**: This is the core function from the `pywhatkit` library that converts the image at `image_path` into ASCII art and saves it to the specified `output_file` path (without the `.txt` extension).
# - After conversion, it prints a success message showing the path where the ASCII art is saved.



# ```python
#     except Exception as e:
#         print(f"Error: {e}")
# ```
# - If any error occurs during the process inside the `try` block (e.g., file not found, permission issue), the **`except`** block will catch the error and print it.
# - **`Exception as e`** captures the error and stores it in the variable `e`, which is then printed.



# ```python
# # Provide the correct file path
# image_path = r"C:\Users\Fathima M P\Downloads\istockphoto-479629586-612x612.jpg"# Replace with the correct image path
# output_file = r"C:\Users\Fathima M P\Desktop\Python_Games\ascii_art"    # Output file path without extension
# ```
# - **`image_path`** is the location of the image on your computer that you want to convert. You should replace the path with the location of your image.
# - **`output_file`** is where the ASCII art will be saved. The program will save the output as a `.txt` file at this location (you don't need to add the `.txt` extension here).



# ```python
# # Convert image to ASCII
# image_to_ascii(image_path, output_file)
# ```
# - This line calls the function `image_to_ascii()` with the `image_path` and `output_file` as arguments. This triggers the process of converting the image to ASCII art.



# ```python
# # Check if the ASCII file exists and display it
# ascii_file = f"{output_file}.txt"
# if os.path.exists(ascii_file):
#     with open(ascii_file, "r") as file:
#         print(file.read())
# else:
#     print(f"Error: ASCII art file '{ascii_file}' was not created.")
# ```
# - **`ascii_file = f"{output_file}.txt"`**: This creates the final ASCII art file name by appending `.txt` to the `output_file` path.
# - **`if os.path.exists(ascii_file)`**: This checks if the ASCII file has been created by verifying if the file exists.
# - If the file exists, it opens the file in read mode (`"r"`) and prints the content of the ASCII art.
# - If the file doesn't exist, it prints an error message indicating that the ASCII art file wasn't created.



# ### Summary of Program Flow:
# 1. The program checks if the image file exists.
# 2. If it does, it converts the image to ASCII art and saves it as a `.txt` file.
# 3. Then, it checks if the ASCII file was created successfully and displays its content.
# 4. If any errors occur during the process (e.g., the image file is not found), it catches and prints the error message.
