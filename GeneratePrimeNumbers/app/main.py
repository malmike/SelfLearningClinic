from generate_prime_numbers import *

def main():
    print ("\n\n\t\tApplication to generate prime numbers\n")
    start_message = "\nEnter a value greater than or equal to 3 to generate list of prime numbers\nor less than 3 to terminate the application\n"
    while True:
        print (start_message)
        value = int(input("Insert any number:"))
        if value >= 3:
            #Generate the list of prime numbers less than value
            prime_list = generatePrimeNumbers(value)
            #Print out the list of prime numbers
            print (prime_list)
            
        else:
            break


if __name__ == "__main__":
    main()