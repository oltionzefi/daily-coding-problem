from setuptools import setup
import re

# parameter variables
install_requires = []

# determine version
with open('constants.py') as f:
    constants = f.read()
version = re.search(r'^\s*VERSION\s*=\s*[\'"](.+)[\'"]\s*$', constants, re.MULTILINE).group(1)


# determine requirements
with open('requirements.txt') as f:
    requirements = f.read()
for line in re.split('\n', requirements):
    if line and line[0] == '#' and '#egg=' in line:
        line = re.search(r'#\s*(.*)', line).group(1)
    if line and line[0] != '#':
        lib_stripped = line.split(' #')[0].strip()
        install_requires.append(lib_stripped)


if __name__ == '__main__':
    setup(
        name='dailycodingproblem',
        version=version,
        description='Daily Coding Problems from https://www.dailycodingproblem.com/',
        author='Oltion Zefi',
        author_email='oltionzefi@gmail.com',
        url='https://github.com/oltionzefi/daily-coding-problem',
        install_requires=install_requires,
        license='MIT',
        zip_safe=False,
        include_package_data=True,
        classifiers=[
            'Programming Language :: Python :: 3.7',
            'Topic :: Coding Problems :: Algorithms',
            'Topic :: Coding Problems :: Performance',
        ]
    )
