# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
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
#     spack install vagabond
#
# You can edit this file again by typing:
#
#     spack edit vagabond
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
from spack import *


class Vagabond(MesonPackage):
    """Vagabond is a free and open-source implementation of bond-based
    refinement algorithms for fitting protein models to electron density from
    structural data. These algorithms seek to faithfully represent the real
    content of the protein crystal as much as possible. """

    homepage = "https://vagabond.hginn.co.uk/index.php?page=install"
    url      = "https://github.com/helenginn/vagabond/archive/refs/tags/0.3.1cb4f94f.tar.gz"

    version('develop', git='https://github.com/helenginn/vagabond.git', submodules=True)
    version('0.3', git='https://github.com/helenginn/vagabond.git', commit='1cb4f94f344c0d556b905d7ab4e7af99dc6f559d', submodules=True)

    depends_on('cmake@3.4:')
    depends_on('libpng')
    depends_on('fftw')
    depends_on('mariadb')
    depends_on('boost')

    variant('gui', default=False, description='Builds with Qt GUI enabled')
    depends_on('qt+opengl', when='+gui')
    depends_on('opengl', when='+gui')

