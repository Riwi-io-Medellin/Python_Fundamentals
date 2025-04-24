<h1 align="center">Variable Types</h1>

<p>Variables are one of the fundamental building blocks of programs written in Python. Variables hold data in memory. Python mainly handles these types of data:</p>

<ul>
    <li>Numbers</li>
    <li>Strings</li>
    <li>Booleans</li>
</ul>

<h2>Numbers</h2>

<p>Most programs manipulate numbers. Computers treat whole numbers and decimal numbers differently. Consider the following code:</p>

```bash
x = 1       # integer
x = 1.0     # decimal (floating point)
```

<h2>Strings</h2>
<p>Strings, along with numbers, are one of the most used data types. A string is a collection of zero or more characters. Strings are typically declared using single quotes but can also use double quotes:</p>

```bash
x = 'This is a string'
print(x) # outputs: This is a string
print(type(x)) # outputs: <class 'str'>
y = "This is also a string"
```

<p>You can add a string to other strings (an operation known as "concatenation") with the same + operator that adds two numbers:</p>

```bash
x = 'Hello' + ' ' + 'world!'
print(x) # outputs: Hello world!
```

<h2>Booleans</h2>
<p>Another common data type is the boolean type, which contains the value <strong>True</strong> or <strong>False</strong>. Internally, bool is treated as a special type of integer. Technically, True has a value of 1 and False has a value of 0.

```bash
x = True
print(type(x)) # outputs: <class 'bool'>
```

Boolean values are generally not used to perform mathematical operations but are used to make decisions and perform branching. However, it's interesting to understand the relationship between types. Many types are just specialized versions of more general types. Integers are a subset of floating-point numbers, and boolean values are a subset of integers.</p>

Explore [Examples](variable_types.py)