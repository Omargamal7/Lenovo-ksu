import os
import re

print("Starting flexible signature unification...")

# Flexible regex to match find_best_idle_cpu regardless of parameter names or 'extern'
# Targets: int find_best_idle_cpu(struct task_struct [*{name}], bool [name])
pattern = re.compile(r'(int\s+find_best_idle_cpu\s*\(\s*struct\s+task_struct\s*\*\s*\w*\s*,\s*)bool(\s*\w*\s*\))')
replacement = r'\1int\2'

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

print("Flexible signature unification finished.")
