from click.testing import CliRunner
from src.python_cli_setup.cli import cli

def test_cli():
  runner = CliRunner()
  result = runner.invoke(cli)
  assert "Hello World!" in result.output