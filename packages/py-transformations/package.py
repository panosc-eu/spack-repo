# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyTransformations(PythonPackage):
    """Transformations is a Python library for calculating 4x4 matrices for translating, rotating,
    reflecting, scaling, shearing, projecting, orthogonalizing, and superimposing arrays of 3D
    homogeneous coordinates as well as for converting between rotation matrices, Euler angles, and
    quaternions. Also includes an Arcball control object and functions to decompose transformation
    matrices."""

    homepage = "https://github.com/cgohlke/transformations"
    url      = "https://github.com/cgohlke/transformations/archive/v2020.1.1.tar.gz"

    maintainers = ['RobertRosca', 'julianhoersch']

    version('2021.6.6',  sha256='7e61af64c46137f18db601e54a71263946e08e2d107434ce8e1edbb92163a10f')
    version('2020.1.1',  sha256='cd9cd29ba7f0ec4c109293fe5007cf632e9f5b8107acba5572672002e72860a6')
    version('2019.4.22', sha256='5686de316e2f65a67788de25ab180995429283c531814815ce4508de0df96c9a')
    version('2019.2.20', sha256='5cb940b9df13707a88bbffffdd2cb0347afa1329b7770a8350d9d4415b00f46d')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools@18.0:', type='build')
    depends_on('py-numpy@1.14.5:')
