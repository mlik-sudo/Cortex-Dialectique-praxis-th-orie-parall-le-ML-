"""
Router v2 - Agent task routing based on skills and capabilities.

TODO: Implement scoring by skill/size/context_tokens + budgets/limits
"""
from typing import Dict, Any


def select_driver(task: Dict[str, Any]) -> str:
    """
    Select the appropriate AI driver based on task skill requirements.

    Args:
        task: Dictionary containing task metadata including 'skill' field

    Returns:
        Driver identifier string (e.g., 'driver_codex_cli')

    Examples:
        >>> select_driver({"skill": "run_and_fix_locally"})
        'driver_codex_cli'
        >>> select_driver({"skill": "generate_tests"})
        'driver_jules'
    """
    # Simple mapping - placeholder for more sophisticated routing
    if task.get("skill") == "run_and_fix_locally":
        return "driver_codex_cli"
    if task.get("skill") in ("generate_tests",):
        return "driver_jules"
    return "driver_gemini_cli"
