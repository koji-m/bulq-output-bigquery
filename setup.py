import setuptools


setuptools.setup(
    name='bulq-output-bigquery',
    version='0.0.1',
    install_requires=[],
    packages=setuptools.find_packages(),
    entry_points={
        'bulq.plugins.output': [
            f'bigquery = bulq_output_bigquery',
        ],
    }
)

