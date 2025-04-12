import subprocess
import tempfile
import os

def execute_plan(plan):
    try:
        lines = plan.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith("```python"):
                code = ""
                continue
            elif line.startswith("```"):
                continue
            elif line.startswith("#") or not line:
                continue
            elif "print(" in line or "def " in line:
                # Python code block detected
                with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                    f.write("\n".join(lines))
                    temp_filename = f.name
                subprocess.run(["python", temp_filename], check=True)
                os.unlink(temp_filename)
                return True
            else:
                print(f"➡️ Running: {line}")
                subprocess.run(line, shell=True, check=True)
        return True
    except Exception as e:
        print(f"⚠️ Error: {e}")
        return False
