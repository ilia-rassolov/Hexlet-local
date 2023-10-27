from hexlet.fs import mkdir, mkfile

def generate():
    return mkdir('python-package', [
    mkfile('Makefile'),
    mkfile('README.md'),
    mkdir('dist'),
    mkdir('tests', [
    mkfile('test_solution.py'),
    ]),
    mkfile('pyproject.toml'),
    mkdir('.venv', [
        mkdir('lib', [
        mkdir('python3.6', [
            mkdir('site-packages', [
                mkfile('hexlet-python-package.egg-link'),
            ]),
        ]),
        ]),
    ],
    {'owner': 'root', 'hidden': False})
    ],
    {'hidden': True}
    )

print(generate())