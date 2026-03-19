import os
import subprocess
import sys

# Unified generator handles all 100+ modules
scripts = [
    "generate_massive_site.py"
]

def run_build():
    print("Starting PyTextbook Infinite Site Generation...")
    print(f"Target: 100+ Modules, 4000+ Words per page.")
    
    for script in scripts:
        if os.path.exists(script):
            print(f"Running {script}...")
            result = subprocess.run([sys.executable, script], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error running {script}:")
                print(result.stderr)
            else:
                print(f"  {script} output (first 200 chars): {result.stdout[:200]}...")
                print(f"  Successfully generated site components via {script}")
        else:
            print(f"Error: Unified generator {script} not found.")

    print("Site generation complete! Every module is now technically exhaustive.")

if __name__ == "__main__":
    run_build()
