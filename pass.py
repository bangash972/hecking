Certainly! Here's an example of a simple Python program that finds a password using a brute-force approach:

```python
import itertools

def find_password(allowed_chars, password_length, target_password):
    for password in itertools.product(allowed_chars, repeat=password_length):
        password = ''.join(password)
        if password == target_password:
            return password

    return None

allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password_length = 6
target_password = 'abc123'

found_password = find_password(allowed_chars, password_length, target_password)
if found_password:
    print(f"Password found: {found_password}")
else:
    print("Password not found.")
```

In this example, the `find_password` function takes in the allowed characters, password length, and target password as parameters. It uses the `itertools.product` function to generate all possible combinations of characters of the given length. For each combination, it checks if it matches the target password. If a match is found, the function returns the password; otherwise, it returns `None`.

In the main part of the program, you can modify the `allowed_chars`, `password_length`, and `target_password` variables to suit your needs. The program then calls the `find_password` function and prints the result.

Keep in mind that this is a simple example meant to demonstrate the concept of password finding using brute-force. In practical scenarios, brute-forcing passwords is highly discouraged as it can be time-consuming and potentially illegal if done without proper authorization.
