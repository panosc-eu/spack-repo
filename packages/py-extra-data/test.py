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
    url      = "https://github.com/European-XFEL/EXtra-data/archive/1.3.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['robertrosca']
    install_time_test_callbacks = ['import_module_test']

    version('1.3.0', sha256='7150b0d7ec3ea97af9e0b81bd88aeddb0716e79b852c603a83f4f04ff65935ce')
    version('1.3.0', sha256='7150b0d7ec3ea97af9e0b81bd88aeddb0716e79b852c603a83f4f04ff65935ce')
    version('1.2.0', sha256='bdb1da5469d314dc1c22cbbd1ecc6e1c9e0660bd1bada4f9a8efd97b3d8b1a0e')

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

    depends_on('py-coverage', type='test')
    depends_on('py-dask', type='test')
    # depends_on ('py-nbval', type='test') #  Doesn't seem to be needed?
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-cov', type='test')
    depends_on('py-testpath', type='test')

    install_time_test_callbacks = ['import_module_test']

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
            python('-m', 'pytest', '-v')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
