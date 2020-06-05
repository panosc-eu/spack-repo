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
#     spack install py-extra-data
#
# You can edit this file again by typing:
#
#     spack edit py-extra-data
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyExtraData(PythonPackage):
    """Tools to read and analyse data from European XFEL."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/European-XFEL/EXtra-data"
    url      = "https://github.com/European-XFEL/EXtra-data/archive/1.1.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['robertrosca']

    version('1.1.0', sha256='0083632f46bf9c93848727babc1e25d3c0382f4798776cff4a42972111e3f5f1')

    # FIXME: Add dependencies if required.
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-fabio') #  custom
    depends_on('py-h5py@2.7.1:')
    depends_on('py-karabo-bridge@0.6:') #  custom
    depends_on('py-matplotlib')
    depends_on('py-numpy')
    depends_on('py-pandas')
    depends_on('py-scipy')
    depends_on('py-xarray')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
