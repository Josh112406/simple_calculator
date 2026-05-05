class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        return num1 / num2
    
    def display_result(self, result):
        print(f"Result: {result}")
    
    def ask_try_again(self):
        again =  input("Again? (y/n): ").lower()
        return again == "y"
    
    
    
    