# Simple Calculator

A command-line calculator application written in Python that performs basic arithmetic operations.

## Features

- **Addition**: Add two numbers
- **Subtraction**: Subtract two numbers
- **Multiplication**: Multiply two numbers
- **Division**: Divide two numbers with zero-division protection
- **Interactive Menu**: Easy-to-use menu interface
- **Repeat Functionality**: Perform multiple calculations without restarting

## Requirements

- Python 3.6 or higher

## Installation

1. Clone or download the project
2. Navigate to the project directory:
   ```bash
   cd simple_calculator
   ```

## Usage

Run the calculator:
```bash
python simple_calculator.py
```

### How to Use

1. The program will display a menu with four operations:
   - 1. Addition
   - 2. Subtraction
   - 3. Multiplication
   - 4. Division

2. Enter your choice (1-4)
3. Enter two numbers when prompted
4. The result will be displayed
5. Choose whether to perform another calculation (y/n)

### Example

```
1. Addition
2. Subtraction
3. Multiplication
4. Division
Choose operation (1-4): 1
Enter first number: 10
Enter second number: 5
Result: 15.0
Use again? (y/n): n
Closing...
```

## Error Handling

- **Invalid Operation**: Selecting a number outside 1-4 will show an error
- **Invalid Input**: Non-numeric inputs will be caught and reported
- **Division by Zero**: Attempting to divide by zero will display an error message

## Project Structure

- `simple_calculator.py`: Main application file containing:
  - `Calculator`: Base class with arithmetic operations
  - `SimpleCalculator`: Subclass with user interface and input handling
