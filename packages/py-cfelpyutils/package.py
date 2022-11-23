# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCfelpyutils(PythonPackage):
    """CfelPyUtils is a library of several utility functions and classes used by
    several software projects developed at the Center For Free Electron Laser
    Science (CFEL) in Hamburg."""

    homepage = "https://github.com/ondateam/cfelpyutils"
    url      = "https://github.com/ondateam/cfelpyutils/archive/1.0.0.tar.gz"

    maintainers = ['robertrosca']

    version('1.0.0', sha256='303c02b28191dc612c27c8420c2878503e56bde309975db676249784111e9ee1')

    depends_on('python@3.6:',   type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy')
    depends_on('py-future')

