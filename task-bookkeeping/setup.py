from setuptools import setup, find_packages


setup(
    name='task-bookkeeping',
    version='1.0.0',
    description='Console bookkeeping.',
    license='Apache License 2.0',
    author='Vladislav Myadzel',
    author_email='capybarralt@gmail.com.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bookkeeping = task_bookkeeping:main',
        ],
    },
    package_data={
        'task_bookkeeping': ['resources/*']
    }
)
