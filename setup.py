from setuptools import setup

setup(name='superinactive',
      version='0.1',
      license='MIT',
      description='Supervisor plugin to monito the activity of a file and restart '
                  'programs on inactivity',
      author='Dr. Volker Jaenisch',
      author_email='volker.jaenisch@inqbus.de',
      url='https://github.com/inqbus/superinactive',
      install_requires=['supervisor'],
      entry_points = {
            'console_scripts': [
                'superinactive=superinactive:main',
                'touch_file=touch_file:main'
            ],
           }
      )
