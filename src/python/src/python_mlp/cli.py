import typer

app = typer.Typer()


@app.command()
def run():
    print("Hello, world!")


def entrypoint():
    app()
