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

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/silx-kit/fabio"
    url      = "https://github.com/silx-kit/fabio/archive/v0.9.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['RobertRosca']

    version('0.10.2', sha256='597d7afe414da9b16afeb91439b669d268c8bcfefed1fe400b9a26d93ae58243')
    version('0.10.1', sha256='0c89c5afdead668beae8e79948a6eae7c1d4767c33acde96d68bfe3a2d7dcd96')
    version('0.10.0', sha256='b194fdb10f8293dd4b0000ff813c24b1a5f3a46bd0f61f82c5a7d1e8e96d462f')
    version('0.9.0',  sha256='5f3971b7d8a22410eab6eedb5725271304708feaa54a0fcb941ea54d3aa394d9')

    # FIXME: Add dependencies if required.
    depends_on('python@3.6:',   type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy')
    
    #test dependencies
    depends_on('py-coverage@:4.9', type='test')
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-cov', type='test')
    depends_on('py-testpath', type='test')
    
    def test(self):
    # `setup.py test` should not be used as:
    #   - `python3 -m pytest -v` should be ran instead
    #   - the builtin `test` method runs before `install` is finished
        self.pytest()

    def pytest(self):
        with working_dir('.'):
            prefix = self.spec.prefix
            #  Add bin to path here, as tests also check entrypoints
            env['PATH'] = env['PATH']+":"+prefix+"/bin"
            python3('-m', 'pytest', '-v')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
