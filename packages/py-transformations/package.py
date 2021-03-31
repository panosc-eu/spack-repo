# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
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
#     spack install py-transformations
#
# You can edit this file again by typing:
#
#     spack edit py-transformations
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyTransformations(PythonPackage):
    """Transformations is a Python library for calculating 4x4 matrices for translating, rotating, 
    reflecting, scaling, shearing, projecting, orthogonalizing, and superimposing arrays of 3D 
    homogeneous coordinates as well as for converting between rotation matrices, Euler angles, and 
    quaternions. Also includes an Arcball control object and functions to decompose transformation 
    matrices."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/cgohlke/transformations"
    url      = "https://github.com/cgohlke/transformations/archive/v2020.1.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['RobertRosca', 'julianhoersch']

    version('2020.1.1',  sha256='cd9cd29ba7f0ec4c109293fe5007cf632e9f5b8107acba5572672002e72860a6')
    version('2019.4.22', sha256='5686de316e2f65a67788de25ab180995429283c531814815ce4508de0df96c9a')
    version('2019.2.20', sha256='5cb940b9df13707a88bbffffdd2cb0347afa1329b7770a8350d9d4415b00f46d')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools@18.0:', type='build')
    depends_on('py-numpy@1.14.5:')

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
            python3('-m', 'pytest', '-v')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
