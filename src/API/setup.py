import glob

from cx_Freeze import setup, Executable

# Add any additional modules or packages your application requires.
additional_modules = []

# Replace 'your_script.py' with the name of your main Python script.
executable = Executable('main.py')


# Define a function to get a list of files matching a wildcard pattern.
def get_files_by_pattern(pattern):
    files = glob.glob(pattern)
    return [(x, x) for x in files]


# Use the function to get a list of files matching the wildcard pattern.
include_files = []
for file in get_files_by_pattern('./scripts/postgres/*.sql'):
    include_files.append(file)
for file in get_files_by_pattern('./environments/*.json'):
    include_files.append(file)
for file in get_files_by_pattern('./api/static/*'):
    include_files.append(file)
include_files.append(("server-run.sh", "run.sh"))
include_files.append(("config.json", "config.json"))


setup(
    name='CamundaViewer',
    version='1.0.3',
    description='Check for running and completed tasks in Camunda',
    executables=[executable],
    options={'build_exe':
        {
            'packages': additional_modules,
            'include_files': include_files
        }
    }
)
