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
#     spack install py-fabio
#
# You can edit this file again by typing:
#
#     spack edit py-fabio
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyFabio(PythonPackage):
    """FabIO is an I/O library for images produced by 2D X-ray detectors and
    written in Python. FabIO support images detectors from a dozen of companies
    (including Mar, Dectris, ADSC, Hamamatsu, Oxford, ...), for a total of 20
    different file formats (like CBF, EDF, TIFF, ...) and offers an unified
    interface to their headers (as a python dictionary) and datasets (as a numpy
    ndarray of integers or floats)."""

    homepage = "https://github.com/silx-kit/fabio"
    url      = "https://github.com/silx-kit/fabio/archive/refs/tags/v0.12.0.tar.gz"

    maintainers = ['RobertRosca', 'julianhoersch']

    version('0.13.0', sha256='aae2bf104d563da879cb420cbbd19a96583a364791fd29bbc0190b45ca977dbc')
    version('0.12.0', sha256='654c19792b46a87815215d3254c98bb562394c24301fe8dc85391bb4c6cc2aee')
    version('0.10.2', sha256='597d7afe414da9b16afeb91439b669d268c8bcfefed1fe400b9a26d93ae58243')
    version('0.10.1', sha256='0c89c5afdead668beae8e79948a6eae7c1d4767c33acde96d68bfe3a2d7dcd96')
    version('0.10.0', sha256='b194fdb10f8293dd4b0000ff813c24b1a5f3a46bd0f61f82c5a7d1e8e96d462f')
    version('0.9.0',  sha256='5f3971b7d8a22410eab6eedb5725271304708feaa54a0fcb941ea54d3aa394d9')

    # dependencies
    depends_on('python@3.6:',   type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy')

    depends_on('py-lxml@4.6.3:')
    # depends_on('py-cython') # tests pass without
    depends_on('py-pillow+tiff')
    depends_on('py-h5py')
    depends_on('py-hdf5plugin')

    # dependencies for building docs
    # depends_on('py-sphinx')
    # depends_on('py-sphinxcontrib-programoutput')
    # depends_on('py-sphinx-rtd-theme')

    def test(self):
        prefix = self.spec.prefix
        with working_dir(prefix):
            python('-c', 'import fabio; fabio.tests()')
