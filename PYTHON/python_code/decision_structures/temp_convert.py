def main():
    celsius = int(raw_input("What is the Celsius temperature? "))
    
    fahrenheit = 9/5 * celsius + 32
 
    print("The temperature is "+ str(fahrenheit)+ " degrees fahrenheit.")

    # multi-way decision pattern, if-elif
    if fahrenheit > 85:
        print("It's really hot in there. Be careful!")
    elif fahrenheit < 45:
        print("Brrrr. Be sure to layer up!")   

main()
