# Router v2 (stub) -- TODO: scoring par skill/size/context_tokens + budgets/limits
def select_driver(task):
    # placeholder: simple mapping
    if task["skill"] == "run_and_fix_locally":
        return "driver_codex_cli"
    if task["skill"] in ("generate_tests",):
        return "driver_jules"
    return "driver_gemini_cli"
