import subprocess, sys, tempfile
HERE = "process-audit"
for module in ("record_reading", "problem_register"):
    code = f"import sys; here = sys.argv[1]; sys.path.insert(0, here); import {module}"
    with tempfile.TemporaryFile() as output, tempfile.TemporaryFile() as errors:
        process = subprocess.Popen([sys.executable, "-I", "-B", "-c", code, HERE],
                                   stdin=subprocess.PIPE, stdout=output, stderr=errors)
        try:
            exit_code = process.wait(timeout=30)
        except subprocess.TimeoutExpired:
            process.kill(); process.wait(); print(module, "WAITS FOR INPUT"); continue
        finally:
            process.stdin.close()
        output.seek(0); errors.seek(0)
        print(module, "exit", exit_code, "stdout", output.read(), "stderr", errors.read())
