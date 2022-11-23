# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Vagabond(MesonPackage):
    """Vagabond is a free and open-source implementation of bond-based
    refinement algorithms for fitting protein models to electron density from
    structural data. These algorithms seek to faithfully represent the real
    content of the protein crystal as much as possible. """

    homepage = "https://vagabond.hginn.co.uk/index.php?page=install"
    url      = "https://github.com/helenginn/vagabond/archive/refs/tags/0.3.1cb4f94f.tar.gz"

    maintainers = ['julianhoersch', 'RobertRosca']


    version('develop', git='https://github.com/helenginn/vagabond.git', submodules=True)
    version('0.2',                                          sha256='e1e2e7ab0a646febfdb15c775f6703b993c50ede794a6b9b1b1c00c2d234cd76')
    version('0.1.fb1204b309d48b8aa7b47274df2ce8487e0bebc1', sha256='d5a547fd5d9afe6d77e029298f93080ffc1f4e9321d06fb2901d3309c4e24455')
    version('0.0.0.95d54531',                               sha256='4ca686c28969ae275cbf5eef93b7dd8bcb8e5e6b9f5669c3eb4979a3fa19151f')

    depends_on('cmake@3.4:')
    depends_on('libpng')
    depends_on('fftw')
    depends_on('mariadb')
    depends_on('boost')
    depends_on('crystfel@:0.9')

    variant('gui', default=False, description='Builds with Qt GUI enabled')
    depends_on('qt+opengl', when='+gui')
    depends_on('opengl', when='+gui')

