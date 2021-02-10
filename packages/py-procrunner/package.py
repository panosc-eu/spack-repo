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
#     spack install py-procrunner
#
# You can edit this file again by typing:
#
#     spack edit py-procrunner
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyProcrunner(PythonPackage):
    """Versatile utility function to run external processes 
    Free software: BSD license Documentation: https://procrunner.readthedocs.io."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://procrunner.readthedocs.io"
    url      = "https://github.com/DiamondLightSource/python-procrunner/archive/v2.3.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['RobertRosca', 'julianhoersch']

    version('2.3.0', sha256='44a18bfdff242d2efae92a94da40a87b1a0eb3d6248cb459cf94ec719be5edd9')
    version('2.2.0', sha256='b5c4fe17ab31f8907db61284e037139f5facc3c7ca5a2a6dc83aa8828680a440')
    version('2.1.0', sha256='09b1c2b28e1442c5b8f22259f51de01ddbd0379ae23f51a094733178e58a38f5')
    version('2.0.0', sha256='36b05a76b706cb22123cbb4a815e35062f3ff1f77d66f0bf9970db03c4e4d9ae')
    version('1.1.0', sha256='412d7c181b1da633885b0cf7b7385d727bd23e1e3c8d40fbdb8ef9fa3db6d298')
    version('1.0.2', sha256='7fe03d1d426a4633cecc502c2ba6c8ba19302b72919d3b682ddfee67b61e025c')
    version('1.0.1', sha256='c8db5e7eff788e9eb8ec713ffa63448302458827dd300d8d3edf4b341e328b84')
    version('1.0.0', sha256='4b78cfa1d0f29e8731e550d5b08c0706967faa2f88130bcd76bb657d70e940f1')
    version('0.9.1', sha256='f721d7939156aa85fa3cee448005a3626fa23c915dd80e2d61e78f16d7857b4c')
    version('0.9.0', sha256='b38e889322603790aeb94b78a3682ee74b001a315f8b1df6772abb0bc0aa1afa')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    
    # test dependencies
    depends_on('py-coverage@:4.9', type='test')
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-cov', type='test')
    depends_on('py-testpath', type='test')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
