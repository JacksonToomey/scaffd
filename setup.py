from setuptools import setup


setup(
    name='scaffd',
    version='0.1',
    py_modules=['scaffd'],
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        scaffd=scaffd:cli
    """,
)
