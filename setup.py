from setuptools import setup

setup(name='SESAR-Web-Services-Library',
      version='0.8',
      description='SESAR web services library for IGSN management.',
      url='https://github.com/Adam-Brown/SESAR-Web-Services-Lib',
      author='Adam David Brown',
      author_email='adam.brown@evbane.com',
      license='MIT',
      packages=['sesarwslib', 'sesarwslib.sample'],
      install_requires=['generateds'],
      zip_safe=False)
