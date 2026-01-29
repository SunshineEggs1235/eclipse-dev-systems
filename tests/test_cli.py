import subprocess
import sys


def test_cli_help_exits_zero():
    """Portfolio-grade smoke test: CLI should respond to --help."""
    # Adjust to your actual entrypoint if needed:
    # - If you have a console_script: `reportgen --help`
    # - If you have a module: `python -m reportgen --help`
    #
    # This test uses python -m to avoid relying on PATH in CI.
    result = subprocess.run(
        [sys.executable, "-m", "reportgen", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "usage" in (result.stdout + result.stderr).lower()
