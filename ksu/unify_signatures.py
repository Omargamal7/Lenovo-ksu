import os
import re

print("Starting nuclear signature unification...")

# Nuclear regex to match find_best_idle_cpu followed by ANYTHING in parentheses
# This targets any variation of: int find_best_idle_cpu(...)
pattern = re.compile(r'int\s+find_best_idle_cpu\s*\([^)]*\)')
replacement = 'int find_best_idle_cpu(struct task_struct *p, int prefer_idle)'

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(('.c', '.h')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                
                new_content = pattern.sub(replacement, content)
                
                if content != new_content:
                    print(f"Nuclear unified signature in {path}")
                    with open(path, 'w') as f:
                        f.write(new_content)
            except Exception as e:
                print(f"Error processing {path}: {e}")

print("Nuclear signature unification finished.")
