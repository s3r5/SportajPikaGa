import nox
locations = "sportaj_app", "sportaj_core", "noxfile.py"


@nox.session(python=["3.9", "3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-import-order")
    session.run("flake8", *args)
