import argparse
import json
import pathlib
import subprocess
import os

# --- Argument Parsing ---
parser = argparse.ArgumentParser(
    description="Dispatch tasks to CLI agents based on a task.json file."
)
parser.add_argument(
    "--request",
    required=True,
    help="Path to the request task.json file, relative to the repository root.",
)
args = parser.parse_args()

# --- Path and Task Loading ---
# The path is constructed from the GitHub workspace (if available) and the command-line argument.
req_path = pathlib.Path(os.getenv("GITHUB_WORKSPACE", ".")) / args.request

print(f"Attempting to read task file from: {req_path}")

try:
    task = json.loads(req_path.read_text(encoding="utf-8"))
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error: Could not read or parse the task file at '{req_path}'. Details: {e}")
    raise SystemExit(1)

# --- Output Directory Setup ---
out_dir = pathlib.Path("responses") / task.get("id", "unknown-task")
out_dir.mkdir(parents=True, exist_ok=True)
print(f"Output directory created at: {out_dir}")


def run_cli(cmd: list[str], out_file: pathlib.Path) -> None:
    """Executes a command and writes its stdout and stderr to files."""

    print(f"Running command: {' '.join(cmd)}")

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        out_file.write_text(res.stdout, encoding="utf-8")
        if res.stderr:
            (out_file.parent / (out_file.name + ".stderr")).write_text(
                res.stderr, encoding="utf-8"
            )
        print(f"Successfully wrote output to {out_file}")
    except subprocess.CalledProcessError as e:
        error_message = (
            f"Command failed with exit code {e.returncode}\n"
            f"--- STDOUT ---\n{e.stdout}\n"
            f"--- STDERR ---\n{e.stderr}"
        )
        out_file.write_text(error_message, encoding="utf-8")
        print(error_message)
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        out_file.write_text(error_message, encoding="utf-8")
        print(error_message)


# --- Placeholder CLI Calls ---
# In a real implementation, you would build these commands dynamically based on the task drivers.
task_id = task.get("id", "unknown-task")

print("\n--- Dispatching to Gemini ---")
gemini_out = out_dir / "gemini-cli"
gemini_out.mkdir(exist_ok=True)
run_cli(
    ["echo", f"Gemini CLI output for task {task_id}"],
    gemini_out / "output.txt",
)

print("\n--- Dispatching to Codex ---")
codex_out = out_dir / "codex-cli"
codex_out.mkdir(exist_ok=True)
run_cli(
    ["echo", f"Codex CLI output for task {task_id}"],
    codex_out / "output.txt",
)

print("\n--- Dispatching to Claude ---")
claude_out = out_dir / "claude-code"
claude_out.mkdir(exist_ok=True)
run_cli(
    ["echo", f"Claude Code CLI output for task {task_id}"],
    claude_out / "output.txt",
)

print("\nDispatch script finished.")
