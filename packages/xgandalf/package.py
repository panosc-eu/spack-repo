# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Xgandalf(CMakePackage):
    """Extended gradient descent algorithm for lattice finding."""

    homepage = "https://stash.desy.de/users/gevorkov/repos/xgandalf/browse"
    url      = "https://stash.desy.de/rest/api/latest/projects/~GEVORKOV/repos/xgandalf/archive?at=refs%2Ftags%2Fv1.0&format=tgz"

    maintainers = ['RobertRosca', 'julianhoersch']

    version('1.0', '60c38c41a3e630d6bfa0e2a3d18e40e56b42413f6e1641e0abd0b1cd2e1a38ca', extension='tar.gz')

    depends_on('cmake@3.1:')
    depends_on('boost@1.60.0')
    depends_on('eigen@3.3.7')
    depends_on('intel-mkl@:2018')

    # does not work
    def cmake_args(self):
        args = [
            self.define('XGANDALF_BUILD_EXECUTABLE', True),
            # self.define('USE_INSTALLED_PRECOMUTED_DATA', False),
            ]

        return args
