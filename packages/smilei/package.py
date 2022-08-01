# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Smilei(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://smileipic.github.io"
    url      = "https://github.com/SmileiPIC/Smilei/archive/refs/tags/v4.7.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('4.7', sha256='890c04cc982707c2ea29f8eb5ac21513045ed3d7837e53e9e3ef223222200fe8')
    version('4.6', sha256='9ba8121040aef8ecf7ac1e781780edfc1507d98e3aebd174cfa2bca8070ec1c0')
    version('4.5', sha256='b4468f8078606f1bcf3d16d117b410aba0284b239536a2057e11be1066127d18')

    # FIXME: Add dependencies if required.
    depends_on('python@3:')
    depends_on('mpi', ) #type=['build', 'run'])
    depends_on('py-h5py^hdf5+mpi',) # type=['build', 'run'])
    depends_on('py-numpy',) # type=['build', 'run'])
    depends_on('py-matplotlib',) # type=['build', 'run'])
    depends_on('py-pint',) # type=['build', 'run'])

    def setup_build_environment(self, env):
        env.set('SMILEICXX', self.spec['mpi'].mpicxx)
        env.set('PYTHONEXE', self.spec['python'].prefix.bin.python)
        env.set('HDF5_ROOT_DIR', self.spec['hdf5'].prefix)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('smilei', prefix.bin)
        install('smilei_test', prefix.bin)

