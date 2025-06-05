import os
import subprocess

import click


@click.command()
def main():
    """Prints a greeting."""
    cwd = os.getcwd()
    click.echo(f"Running {click.style('ddinit', fg='yellow')} in {cwd}")

    venv_exists = os.path.exists(f"{cwd}/.venv")
    envrc_exists = os.path.exists(f"{cwd}/.envrc")

    if venv_exists:
        click.echo(".venv exists -> no action")
    if envrc_exists:
        click.echo(".envrc exists -> no action")
    if not (venv_exists or envrc_exists):
        with open(f"{cwd}/.envrc", "w") as f:
            f.write("layout uv")
        subprocess.run(["direnv", "allow"])


if __name__ == "__main__":
    main()
