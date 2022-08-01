# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
from pathlib import Path


class PyHappi(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"

    # FIXME: ensure the package is not available through PyPI. If it is,
    # re-run `spack create --force` with the PyPI URL.
    url      = "https://github.com/SmileiPIC/Smilei/archive/refs/tags/v4.7.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('4.7', sha256='890c04cc982707c2ea29f8eb5ac21513045ed3d7837e53e9e3ef223222200fe8')

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on('python@3:', type=('build', 'run'))
    depends_on('smilei', type=('build', 'run'))
    depends_on('py-h5py^hdf5+mpi',) # type=['build', 'run'])
    depends_on('py-numpy',) # type=['build', 'run'])
    depends_on('py-matplotlib',) # type=['build', 'run'])
    depends_on('py-pint',) # type=['build', 'run'])

    def patch(self):
        copy(str(Path(self.package_dir) / "setup.py"), self.build_directory)

