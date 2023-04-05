from rich import print
from rich.prompt import Prompt

def pretty_print_gpt(string):
    """
    Prints a formatted string representing an assistant message.

    Args:
        string (str): The message to be printed.

    Returns:
        None
    """
    print(f'[bold blue]>>[/bold blue] [bold cyan]Assistant:[/bold cyan] {string}')


def pretty_print_system(string):
    """
    Prints a formatted string representing a system message.

    Args:
        string (str): The message to be printed.

    Returns:
        None
    """
    print(f'[bold red]>>SYSTEM MESSAGE<<[/bold red] {string}')


def pretty_input_user():
    """
    Prompts the user for input with a formatted string.

    Args:
        None

    Returns:
        str: The user's input.
    """
    return Prompt.ask(f'[bold pink]>>[/bold pink] [bold red]User:[/bold red]')