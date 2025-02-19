# This file is part of pyunicorn.
# Copyright (C) 2008--2022 Jonathan F. Donges and pyunicorn authors
# URL: <http://www.pik-potsdam.de/members/donges/software>
# License: BSD (3-clause)
#
# Please acknowledge and cite the use of this software and its authors
# when results are used in publications or published elsewhere.
#
# You can use the following reference:
# J.F. Donges, J. Heitzig, B. Beronov, M. Wiedermann, J. Runge, Q.-Y. Feng,
# L. Tupikina, V. Stolbova, R.V. Donner, N. Marwan, H.A. Dijkstra,
# and J. Kurths, "Unified functional network and nonlinear time series analysis
# for complex systems science: The pyunicorn package"

from platform import system
from setuptools import setup, Extension

from Cython.Build import cythonize
import numpy as np


# ==============================================================================


win = system() == 'Windows'
c_args = {
    'include_dirs': [np.get_include()],
    'extra_compile_args': ['/O2' if win else '-O3', '-D_GNU_SOURCE',
                           *([] if win else ['-std=c99'])],
    'define_macros': [('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')]}
cy_args = {
    'language_level': 3, 'embedsignature': True,
    'boundscheck': True, 'wraparound': False,
    'initializedcheck': True, 'nonecheck': True}


# ==============================================================================


setup(
    ext_modules=cythonize(
        [Extension(
            f'pyunicorn.{pkg}._ext.numerics',
            sources=[f'src/pyunicorn/{pkg}/_ext/numerics.pyx'],
            **c_args)
         for pkg in ['climate', 'core', 'funcnet', 'timeseries']],
        compiler_directives=cy_args,
        nthreads=4))
