import os
import re

print("Starting Makefile cleaning...")

# Regex to match -Werror and anything attached to it until a space or closing parenthesis
# This is safer than simple sed as it handles parentheses correctly
regex = re.compile(r'-Werror[^\s)]*')

for root, dirs, files in os.walk('.'):
    for file in files:
        if file == 'Makefile' or file.endswith('.mk'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                
                new_content = regex.sub('', content)
                
                if content != new_content:
                    print(f"Cleaning {path}")
                    with open(path, 'w') as f:
                        f.write(new_content)
            except Exception as e:
                print(f"Error processing {path}: {e}")

print("Makefile cleaning finished.")
