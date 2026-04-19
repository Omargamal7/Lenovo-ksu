import os
import re

print("Starting signature unification...")

# Broad regex to match the signature regardless of spacing, 'extern' keyword, or variable names
# This targets: [extern] int find_best_idle_cpu(struct task_struct *p, bool prefer_idle)
pattern = re.compile(r'(extern\s+)?int\s+find_best_idle_cpu\s*\(\s*struct\s+task_struct\s*\*\s*\w+\s*,\s*bool\s+prefer_idle\s*\)')
replacement = r'\1int find_best_idle_cpu(struct task_struct *p, int prefer_idle)'

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(('.c', '.h')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', errors='ignore') as f:
                    content = f.read()
                
                new_content = pattern.sub(replacement, content)
                
                if content != new_content:
                    print(f"Unified signature in {path}")
                    with open(path, 'w') as f:
                        f.write(new_content)
            except Exception as e:
                print(f"Error processing {path}: {e}")

print("Signature unification finished.")
