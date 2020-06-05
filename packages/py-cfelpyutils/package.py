# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-cfelpyutils
#
# You can edit this file again by typing:
#
#     spack edit py-cfelpyutils
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyCfelpyutils(PythonPackage):
    """CfelPyUtils is a library of several utility functions and classes used by
    several software projects developed at the Center For Free Electron Laser
    Science (CFEL) in Hamburg."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/ondateam/cfelpyutils"
    url      = "https://github.com/ondateam/cfelpyutils/archive/1.0.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['robertrosca']

    version('1.0.0', sha256='303c02b28191dc612c27c8420c2878503e56bde309975db676249784111e9ee1')

    # FIXME: Add dependencies if required.
    depends_on('python@3.6:',   type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy')
    depends_on('py-future')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
