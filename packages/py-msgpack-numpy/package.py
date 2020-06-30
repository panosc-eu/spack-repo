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
#     spack install py-msgpack-numpy
#
# You can edit this file again by typing:
#
#     spack edit py-msgpack-numpy
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os


class PyMsgpackNumpy(PythonPackage):
    """This package provides encoding and decoding routines that enable the
    serialization and deserialization of numerical and array data types provided
    by numpy using the highly efficient msgpack format. Serialization of
    Python's native complex data types is also supported.."""

    homepage = "https://github.com/lebedov/msgpack-numpy"
    url      = "https://github.com/lebedov/msgpack-numpy/archive/0.4.5.tar.gz"

    import_modules = ['msgpack_numpy']

    maintainers = ['robertrosca']

    version('0.4.6.post0', sha256='dfcb0c9cb5850e656344ac464a260e7b8b9b1c62d77c2e1d3d9ef15a88f1df6b',
        url='https://files.pythonhosted.org/packages/86/ee/9e0fa0979a3aee96b3e2efe86f6253a2527c8faac1d8c1c48aa5e977ca3d/msgpack-numpy-0.4.6.post0.tar.gz')
    version('0.4.6',   sha256='ef3c5fe3d6cbab5c9db97de7062681c18f82d32a37177aaaf58b483d0336f135',
        url='https://files.pythonhosted.org/packages/14/c7/9140e75f2c9dfbd1423500fe7d3652c20a721919c63e74cadcc09276b25a/msgpack-numpy-0.4.6.tar.gz')
    version('0.4.5',   sha256='4e88a4147db70f69dce1556317291e04e5107ee7b93ea300f92f1187120da7ec')
    version('0.4.4.3', sha256='c7db37ce01e268190568cf66a6a65d1ad81e3bcfa55dd824103c9b324608a44e')
    version('0.4.4.2', sha256='ac3db232710070ac64d8e1c5123550a1c1fef45d77b6789d2170cbfd2ec711f3')
    version('0.4.4.1', sha256='b7641ccf9f0f4e91a533e8c7be5e34d3f12ff877480879b252113d65c510eeef')

    depends_on('python@3.6:',       type=('build', 'run'))
    depends_on('py-setuptools',     type=('build', 'test'))
    depends_on('py-numpy@1.9.0:',   type=('build', 'run'))
    depends_on('py-msgpack@0.5.2:', type=('build', 'run'))
