from setuptools import setup 
import subprocess

with open('README.rst','r') as f:
	long_description = f.read()
	
setup(name='pyAIRtools',
      version='0.1',
	  description='Python port of Matlab AIRtools and ReguTools regularization toolbox',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/pyAIRtools',
      packages=['airtools'],
	  )

#%%
try:
    subprocess.call(['conda','install','--yes','--quiet','--file','requirements.txt'],shell=False) #don't use os.environ
except Exception as e:
    print('you will need to install packages in requirements.txt  {}'.format(e))
