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
#     spack install py-dials-data
#
# You can edit this file again by typing:
#
#     spack edit py-dials-data
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyDialsData(PythonPackage):
    """A python package providing data files used for regression tests in DIALS, dxtbx, xia2 
    and related packages.If you want to know more about what py-dials-data is you can have a read 
    through the background information. For everything else the main documentation is probably 
    the best start."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://dials-data.readthedocs.io/en/latest/"
    url      = "https://github.com/dials/data/archive/v2.1.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['RobertRosca', 'julianhoersch']

    version('2.1.0', sha256='17935ff9e3791dae992f4b606899d407ea8ede7ea047faa6580a7552429c0a7b')
    version('2.0.0', sha256='d68708af31e6325de30c6f191c05c5299b3a19fba5c657262b8d75fb24af3593')
    version('1.0.0', sha256='0c28046f95fd89f55ce270eade4bece0862c8aa31c1b3baff3da4a6aa277cadb')
    version('0.6.0', sha256='84397fa24a6d805f9a223becb4c986e47fa11b2e0abb5373be56aeabe6f28883')
    version('0.5.0', sha256='317c6bea2db078c342c85845363ccf1487dd8e9178afa33dc3aa034490a23246')
    version('0.4.0', sha256='35652e5cfa5d49f3b4de0bbdb1067914b788672bbc67c2ec169d982b69e84155')
    version('0.3.0', sha256='b90480ad6540c05e4017f3e7c1fed43c26f0928e3301e65114b8d5d13d94f50e')
    version('0.2.0', sha256='8285b619cf56acb50163f2040e5d26c6ea2a7de9606f0d8e9d313977fbbc95f0')
    version('0.1.0', sha256='5239f50ed13ead45229488bf578806289e5ee5b482d6cbd3a365cd60387aa4e2')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-importlib-resources@1.1.0:')
    depends_on('py-pytest@6.1.2') # in install_requires
    depends_on('py-pyyaml@5.3.1')
    depends_on('py-py@1.9.0')



    depends_on('py-coverage@:4.9', type='test')
    # depends_on('py-pytest', type='test') #specify for test too?
    depends_on('py-pytest-cov', type='test')
    depends_on('py-testpath', type='test')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
