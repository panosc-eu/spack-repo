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
#     spack install py-silx
#
# You can edit this file again by typing:
#
#     spack edit py-silx
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PySilx(PythonPackage):
    """The purpose of the silx project is to provide a collection of Python 
    packages to support the development of data assessment, reduction and 
    analysis applications at synchrotron radiation facilities. silx aims 
    to provide reading/writing tools for different file formats, data 
    reduction routines and a set of Qt widgets to browse and visualise 
    data."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.silx.org/doc/silx/latest/"
    url      = "https://github.com/silx-kit/silx/archive/v0.14.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['RobertRosca', 'julianhoersch']

    version('0.14.0rc3',                   sha256='37f66a56022505b714b72e3975f5f992320b86fa368cfa0d11e4225f8c5451b1')
    version('0.14.0rc2',                   sha256='486739a1ea1631271af7ffd9c4c4ec1bbc230e7ebea6829319abdb6d3d5adeb1')
    version('0.14.0rc1',                   sha256='67936501fd7ed68006f570c1623cff762c225087b8f850729ee94a77c2168eb7')
    version('0.14.0',                      sha256='17c595fe18c9eb3403a9d1f0ee6ea7b523607043c46c944573ecf406f6997866')
    version('0.13.3b0',                    sha256='798bee0a4f83195d0e120fbbbbd11d692d2429888fdac81b75b9335d7545f931')
    version('0.13.2-ubuntu20.04-packages', sha256='3c7b912be00954e9275056ac4e8b8f2d9772402ed8509eb2b6538fbf22438277')
    version('0.13.2-debian10-packages',    sha256='acab83206d18dd183fffb74a2ee18129cbff75185b39fc8e77561e7b3e4315ec')
    version('0.13.2-debian9-packages',     sha256='b32139153ea25d1bc336a14acebeb5f1b60b477171ef615b70c7a902e2a95cbc')
    version('0.13.2',                      sha256='88a16187283c8684be63ab37aee7267c370962dfbcf45cca77ae494ee5e4e773')
    version('0.13.1',                      sha256='2c5dbc1c043ecb78dafd1f7afbfd45833c87332818307196878b759956687491')
    version('0.13.0b2',                    sha256='f3061d5cec39b6134b05cba19d26f3598a64440320351b94b6ca91129481bbdc')
    version('0.13.0b1',                    sha256='c934f9b65a7c8a0cb44e274983b412b22cc710d36c192b077abbdae3e08b82e2')
    version('0.13.0',                      sha256='8c2fe896a26ffd4811a1944481328faa60e05214b84e873bffbdd8cb13729535')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy@1.12:')
    depends_on('py-cython@0.21.1:')
    depends_on('py-h5py')
    depends_on('py-fabio@0.9:')
    depends_on('py-six')
    
    # test dependencies
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
            python3('-m', 'silx.test.run_tests()', '-v')    

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
