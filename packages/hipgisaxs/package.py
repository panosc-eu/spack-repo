# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class Hipgisaxs(SConsPackage):
    version('develop', git='https://github.com/HipGISAXS/HipGISAXS')

    depends_on('boost+filesystem@1.49.0:')
    depends_on('libtiff')
    depends_on('python@2.7.18')
    depends_on('hdf5+mpi+szip')
    # depends_on('zlib')  # Provided by hdf5
    # depends_on('mpi')  # Provided by hdf5+mpi

    patch("sconscript_remove_march.patch")
    patch("add_missing_includes.patch")
    
#   depends_on('cuda')  # Disabled CUDA as it is not compatible with our GPUs
#
#   def setup_build_environment(self, env):
#       env.set("CUDA_TOOLKIT_PATH", self.spec["cuda"].prefix)
#
#   def setup_run_environment(self, env):
#       env.set("CUDA_TOOLKIT_PATH", self.spec["cuda"].prefix)

    def setup_build_environment(self, env):
        env.set('CC', self.spec['mpi'].mpicc)
        env.set('CXX', self.spec['mpi'].mpicxx)
        env.set('F77', self.spec['mpi'].mpif77)
        env.set('FC', self.spec['mpi'].mpifc)

    def build_args(self, spec, prefix):
        all_prefixes = [s.prefix for s in spec.dependencies()]

        args = [
            f'--extrapath={",".join(all_prefixes)}',
            f'--cpppath={self.stage.source_path}/include',
            '--with-mpi',
            f'--directory={self.stage.source_path}'
        ]

        return args

    def install(self, spec, prefix):
        mkdirp(prefix.bin, prefix.lib, prefix.include, prefix.man.man1)
        install('bin/hipgisaxs', prefix.bin)
        install('lib/libhipgisaxs.a', prefix.lib)
        install('man/hipgisaxs.1', prefix.man.man1)

