from setuptools import setup

setup(name='jupyter_MyR_kernel',
      version='0.0.1',
      description='Minimalistic R kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyR-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyR-kernel/tarball/0.0.1',
      packages=['jupyter_MyR_kernel'],
      scripts=['jupyter_MyR_kernel/install_MyR_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'R','r'],
      include_package_data=True
      )
