class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    
    def display_result(self, result):
        print(f"Result: {result}")
    
    def ask_try_again(self):
        again =  input("Again? (y/n): ").lower()
        return again == "y"
    
    
class SimpleCalculator(Calculator):
    def get_operation(self):
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Choose operation (1-4): "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Invalid choice!")
        return choice
    
    def get_inputs(self):
        try: 
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except Exception as e:
            print(e)   
        
        return num1, num2
    def run(self):
        choice = self.get_operation()
        num1, num2 = self.get_numbers()

        if choice == 1:
            self.display_result(self.add(num1, num2))
        elif choice == 2:
            self.display_result(self.subtract(num1, num2))
        elif choice == 3:
            self.display_result(self.multiply(num1, num2))
        elif choice == 4:
            self.display_result(self.divide(num1, num2))
