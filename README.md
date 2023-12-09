# four-function-calc

A four function calculator, simulated using a Turing machine in python

## Usage

Run the driver.py file in the directory source-code\
You'll be prompted to enter the required calculation\
Enter it in the following format

```
x <symbol> y
```

x, y being the numbers to calculate upon\
Once you get your answer\
You will be asked if you want to do more calculations\
Respond with\
y for Yes\
n for No

## Features

### `+`

Input form:
`x + y`\
Adds x and y and returns the sum

### `-`

Input form:
`x - y`\
Subtracts y from x and returns the difference

### `*`

Input form:
`x * y`\
Multiplies x with y and returns the product

### `/`

Input form:
`x / y`\
Divides x by y and returns the quotient only

### `^`

Input form:
`x ^ y`\
Raises x to the y the power and returns that value

### `%`

Input form:
`x % y`\
Calculates x percent of y and returns that value

### Please note:

This calculator comes with some restrictions\
While negative valued inputs are welcome\
The exponent function, (`x^y`), can only accept `y >= 0`\
The percentage function, (`x%y`), can only accept `x,y >= 0`
