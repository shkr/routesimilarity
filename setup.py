import numpy as np
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext_modules=[Extension("directed_hausdorff", 
                       ["directed_hausdorff.pyx"], 
                       libraries=["m"], 
                       extra_compile_args = ["-O3", "-ffast-math", "-march=native"],
                       extra_link_args=[])]
cythonize("directed_hausdorff.pyx")

setup(
  name='routesimilarity',
  packages=['routesimilarity'],
  version='0.1',
  license='MIT',
  description='Methods for similarity scoring between routes',
  author='Shashank Shekhar',
  author_email='shashank.f1@gmail.com',
  url='https://github.com/shkr/routesimilarity',
  download_url='https://github.com/shkr/routesimilarity/archive/v_01.tar.gz',
  keywords=['route', 'similarity', 'hausdorff'],
  install_requires=[
    'numpy',
    'geopy'
   ],
  setup_requires=[
    'numpy'
  ],
  classifiers=[
    '5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 2.7'
  ],
  include_dirs=[np.get_include(), 'include'],
  cmdclass={"build_ext": build_ext},
  ext_modules=ext_modules
)
