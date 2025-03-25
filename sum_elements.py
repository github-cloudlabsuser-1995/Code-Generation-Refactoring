MAX_ELEMENTS = 100

def calculate_sum(arr):
   return sum(arr)

def main():
   try:
      while True:
         try:
            n = int(input(f"Enter the number of elements (1-{MAX_ELEMENTS}): "))
            if 1 <= n <= MAX_ELEMENTS:
               break
            else:
               print("Invalid input. Please enter a number from 1 to 100.")
         except ValueError:
            print("Invalid input. Please enter a valid integer.")

      arr = []
      for i in range(n):
         while True:
            try:
               arr.append(int(input(f"Enter integer {i+1} of {n}: ")))
               break
            except ValueError:
               print("Invalid input. Please enter a valid integer.")

      total = calculate_sum(arr)
      print("Sum of the numbers:", total)
   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
      exit(1)

if __name__ == '__main__':
   main()
   print("\nExiting program. Goodbye!")
