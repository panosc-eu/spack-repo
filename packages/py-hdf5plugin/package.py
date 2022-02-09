# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyHdf5plugin(PythonPackage):
    """This module provides HDF5 compression filters (namely: blosc, bitshuffle,
    lz4, FCIDECOMP, ZFP, zstd) and registers them to the HDF5 library used by
    h5py. Supported operating systems: Linux, Windows, macOS. Supported versions
    of Python: >= 3.4 hdf5plugin provides a generic way to enable the use of the
    provided HDF5 compression filters with h5py that can be installed via pip or
    conda. Alternatives to install HDF5 compression filters are: system-wide
    installation on Linux or other conda packages: blosc-hdf5-plugin, hdf5-lz4."""

    homepage = "https://github.com/silx-kit/hdf5plugin"
    url      = "https://github.com/silx-kit/hdf5plugin/archive/refs/tags/v3.1.1.tar.gz"

    maintainers = ['RobertRosca', 'julianhoersch']

    version('3.2.0',   sha256='9aee017ad1bb13bb1ec54358126399d6f2957cd2a7a5c977b991f07c5fd67db5')
    version('3.1.1',   sha256='3a5bfa1f03b903aaf8d089f51bdceba711319bd61240055613a6a6b9e77d0540')
    version('3.0.0',   sha256='b6048482692f3e98f6b015cee1b0c992ca972a07a211682eb1f66becd50db952')
    version('2.3.2b0', sha256='f65788755121a4bfb9a1825950e152794f8ccb7c0a7c85683e0f14351cc1e12f')
    version('2.3.2',   sha256='7012f93aabbdcd9be6179070a5b00fc6899eecffac9b598b9835cc1439216e2c')
    version('2.3.1',   sha256='c57e02e87879a89dc2194eb546087c678b3bba2bfcce72d8e68005075896403b')
    version('2.3.0',   sha256='fb540387dcda725ce47913867ca80e07379aa87608f61c77bb24c205c74f4006')
    version('2.2.0',   sha256='f61da65905fb00c501fac281916811f48c6c9d82040281a0b4a082c0cd426027')
    version('2.1.2',   sha256='cf2cbf410d152a294a119b0559ae409a63066b6cda0886674ee716417b395066')
    version('2.1.1',   sha256='53c7eeab66a6eaf3813bab8db545ca29945b22d517952e245b77d1a7db79e977')
    version('2.1.0',   sha256='ad9014e7a9c0c0db9c4860dc6069b7c5839325c36ba989b10c94fc50bec77334')
    version('2.0.0',   sha256='7714e4ddc85129b2824aa0cb299f9db3dc4d9a046a5685344e8a5f299a60b527')


    depends_on('python@3.4:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-h5py')

    # extras_require
    # depends_on('sphinx')
    # depends_on('sphinx_rtd_theme')


    def setup_build_environment(self, env):
        # Needed for `spack install --test=root py-hdf5plugin`
        # set the path for plugins to an empty string, otherwise system default
        # could be falsely used
        env.set('HDF5_PLUGIN_PATH', '')

    # Needed for `spack test run py-hdf5plugin`
    setup_run_environment = setup_build_environment

    def test(self):
        prefix = self.spec.prefix
        with working_dir(prefix):
            python('-c', 'import hdf5plugin.test; hdf5plugin.test.run_tests()')
