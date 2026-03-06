import pytest
import os


def start_process():
    # This must match the filename created in Step 1
    script_file = "script/cib_script/test_loginscript.py"

    if not os.path.exists(script_file):
        print(f"❌ Error: File '{script_file}' not found!")
        return

    print(f"🔄 Running {script_file}...")

    # Run pytest through python
    pytest.main(["-v", "-s", script_file])


if __name__ == "__main__":
    start_process()

