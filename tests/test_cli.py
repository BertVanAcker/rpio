from click.testing import CliRunner
from rpio.__main__ import cli
from utils import TemporaryPath

def test_cli_launch():
    """"""
    result = CliRunner().invoke(cli)
    assert result.exit_code == 0 # TODO This should not be 0
    output = result.output
    assert "Usage:" in output
    assert "Commands:" in output

def test_cli_package():
    """"""
    runner = CliRunner()
    result = runner.invoke(cli, ["package"])
    assert result.exit_code == 0  # TODO This should not be 0

    result = runner.invoke(cli, ["package", "--check"])
    assert result.exit_code == 0  # TODO This should not be 0
    assert "FAIL" in result.output

    result = runner.invoke(cli, ["package", "--verbose"])
    assert result.exit_code == 0  # TODO This should not be 0
    assert "Checking" in result.output

    package_name = "package"
    with TemporaryPath(package_name):
        result = runner.invoke(cli, ["package", "--verbose", "--create", "--name", package_name])
        assert result.exit_code == 0
        assert "package created" in result.output
