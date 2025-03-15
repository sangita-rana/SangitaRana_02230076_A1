
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to calculate the sum of prime numbers in a range
def prime_sum_calculator(start, end):
    prime_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum
print("\n1. Prime Number Sum Calculator")
start = 10
end = 20
result = prime_sum_calculator(start, end)
print(f"Sum of prime numbers between {start} and {end}: {result}")

# Function to convert length units
def length_converter(value, direction):
    if direction == 'M':
        return round(value * 3.28084, 2)
# Convert meters to feet    
    elif direction == 'F':
        return round(value / 3.28084, 2)
# Convert feet to meters
    else:
        return "Invalid direction. Use 'M' or 'F'."
print("\n2. Length Unit Converter")
value = 5
direction = 'M'
result = length_converter(value, direction)
print(f"{value} meters = {result} feet")


# Function to count consonants in a string
def consonant_counter(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count
print("\n3. Consonant Counter")
text = "Hello World"
result = consonant_counter(text)
print(f"Number of consonants in '{text}': {result}")

# Function to find the smallest and largest numbers in a list
def min_max_finder(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest
print("\n4. Min-Max Number Finder")
numbers = [5, 2, 9, 1, 7]
smallest, largest = min_max_finder(numbers)
print(f"Numbers: {numbers} -> Smallest: {smallest}, Largest: {largest}")

# Function to check if a string is a palindrome
def palindrome_checker(text):
    cleaned_text = ''.join(text.split()).lower()
    return cleaned_text == cleaned_text[::-1]
print("\n5. Palindrome Checker")
text = "Race car"
result = palindrome_checker(text)
print(f"Is '{text}' a palindrome? {result}")

# Function to count specific words in a text file
def word_counter(file_path):
    target_words = ["the", "was", "and"]
    word_counts = {word: 0 for word in target_words}
        
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
            for word in target_words:
                word_counts[word] = text.split().count(word)
        return word_counts
    except FileNotFoundError:
        return "File not found."
print("\n6. Word Counter")
file_path = "sample.txt" # Replace with the path to your text file
# Create a sample text file for testing
with open(file_path, 'w') as file:
    file.write("The quick brown fox jumps over the lazy dog.")
result = word_counter(file_path)
print(f"Word counts in '{file_path}': {result}")

# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. Prime Number Sum Calculator")
    print("2. Length Unit Converter")
    print("3. Consonant Counter")
    print("4. Min-Max Number Finder")
    print("5. Palindrome Checker")
    print("6. Word Counter")
    print("7. Exit")

# Main program
def main():
    while True:
        display_menu()
        choice = input("Select a function (1-7): ")

        if choice == '1':
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                if start > end:
                    print("Invalid range. Start must be less than or equal to end.")
                else:
                    result = prime_sum_calculator(start, end)
                    print(f"Sum of prime numbers between {start} and {end}: {result}")
            except ValueError:
                    print("Invalid input. Please enter integers.")

        elif choice == '2':
            try:
                value = float(input("Enter the length value: "))
                direction = input("Enter direction ('M' for meters to feet, 'F' for feet to meters): ").upper()
                result = length_converter(value, direction)
                print(f"Converted length: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            text = input("Enter a text string: ")
            result = consonant_counter(text)
            print(f"Number of consonants: {result}")

        elif choice == '4':
            try:
                num_count = int(input("How many numbers do you want to enter? "))
                numbers = []
                for i in range(num_count):
                    number = float(input(f"Enter number {i + 1}: "))
                    numbers.append(number)
                smallest, largest = min_max_finder(numbers)
                print(f"Smallest: {smallest}, Largest: {largest}")
            except ValueError:
                print("Invalid input. Please enter numbers.")

        elif choice == '5':
            text = input("Enter a text string: ")
            result = palindrome_checker(text)
            print(f"Is palindrome: {result}")

        elif choice == '6':
            file_path = input("Enter the path to the text file: ")
            result = word_counter(file_path)
            print(f"Word counts: {result}")
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.")

# Run the program
if __name__ == "__main__":
    main()