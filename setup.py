import re
from distutils.core import setup

long_description = ''

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except:
    pass

# Get the version
version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('fbmqasync/__init__.py', 'r') as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        VERSION = match.group(1)
    else:
        raise RuntimeError("No version number found!")

setup(name='fbmqasync',
      version=VERSION,
      description='A Python Library For Using The Facebook Messenger Platform API with async',
      long_description=long_description,
      url='https://github.com/pasalino/fbmq_async',
      author='Pasqualino de Simone',
      author_email='pasalino@gmail.com',
      license='MIT',
      packages=['fbmqasync'],
      install_requires=['requests>=2.0', 'flask', 'aiohttp>=2.1'],
      keywords='Facebook Messenger Platform Chatbot Async',
      )
