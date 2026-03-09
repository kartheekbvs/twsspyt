import os
import subprocess
import sys

# All expansion scripts in logical order
scripts = [
    "gen_batch1.py",
    "gen_batch2.py",
    "gen_batch3.py",
    "gen_batch4.py",
    "gen_batch5.py",
    "gen_batch6.py",
    "expand_np1.py",
    "expand_np2.py",
    "expand_np3.py",
    "expand_np4.py",
    "expand_np5.py",
    "expand_np6.py",
    "expand_pd1.py",
    "expand_pd2.py",
    "expand_pd3.py",
    "expand_pd4.py",
    "expand_sklearn1.py",
    "expand_sklearn2.py",
    "expand_sklearn3.py",
    "expand_sklearn4.py",
    "expand_sklearn5.py",
    "expand_sklearn6.py",
    "expand_dl1.py",
    "expand_dl2.py",
    "expand_dl3.py",
    "expand_data1.py",
    "expand_matplotlib.py",
    "expand_adv1.py",
    "expand_adv2.py",
    "expand_resources.py",
    "expand_final.py"
]

def run_build():
    print("Starting full site generation...")
    for script in scripts:
        if os.path.exists(script):
            print(f"Running {script}...")
            # Run in a separate process to ensure clean sys.path handling
            result = subprocess.run([sys.executable, script], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error running {script}:")
                print(result.stderr)
            else:
                print(f"  Completed {script}")
        else:
            print(f"Warning: Script {script} not found, skipping.")

    print("Site generation complete!")

if __name__ == "__main__":
    run_build()
