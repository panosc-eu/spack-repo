# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Crystfel(CMakePackage):
    """CrystFEL is a suite of programs for processing (and simulating) Bragg
       diffraction data from "serial crystallography" experiments, often (but
       not always) performed using an X-ray Free-Electron Laser.
    """

    homepage = "https://www.desy.de/~twhite/crystfel/index.html"
    url      = "https://www.desy.de/~twhite/crystfel/crystfel-0.10.0.tar.gz"


    maintainers = ['RobertRosca', 'julianhoersch']

    version('0.10.1',
        sha256='e9e88ae41080beb8a7e2942c262aec130470b46fb2b79324558745aade2b2d45')
    # from version 0.10.0 also supports meson build system cmake is depreceated
    version('0.10.0',
        sha256='cfb3c99328b9ecc02548d82ddc2feb76d19b49c82e46e655f0d2f83d4e3cfa9a')
    version('0.9.1',
        sha256='1eaf757eb093385fbc16298168e683a5b3ef572800b8b22072886a76143b70be')
    version('0.9.0',
        sha256='1aeb6b8ddee598aa57475a53add36dab176b74cdea5f08808c96837aff40e3f8')
    version('0.8.0',
        sha256='6139b818079a16aa4da90344d4f413810e741c321013a1d6980c01f5d79c7b3a')

    #  Versions 0.7.0 and under used AutoTools, 0.8.0 and above use CMake
    #  not too sure how to handle the change in build tools in spack

    # see https://spack.readthedocs.io/en/latest/build_systems/multiplepackage.html
    # to create a package that supports earlier versions

    # version('0.7.0', 'b064bf00f1de96ff23febe3337c4ac1d',
    #     url='http://www.desy.de/~twhite/crystfel/crystfel-0.7.0.tar.gz')
    # version('0.6.3',
    #     sha256='69a96b77b4b395b3827c2ac5c4aa2496427077ff31e23244d0a24837a23d5d6a')

    # required dependecies
    depends_on('cmake@3.12:')
    depends_on('bison@2.6:')
    depends_on('zlib@1.2.3.5:')
    depends_on('hdf5+hl@1.10:')
    depends_on('gsl')
    depends_on('flex')

    # optional dependencies, will work without them but with reduced features
    # https://gitlab.desy.de/thomas.white/crystfel/-/blob/master/INSTALL.md
    # GUI
    depends_on('gtkplus@3.12:3.24')
    depends_on('cairo@1.2:')
    depends_on('pango@1.0:')
    depends_on('gdk-pixbuf+x11@2.0:2.41') # seems to have a plroblem in spack
    # with x11 an meson from 2.42

    # depends_on('libccp4') # not available # required for MTZ import/export
    depends_on('fftw@3.0:') # required for asdf indexing
    depends_on('fdip') # for peakFinder9 peak search algorithm
    depends_on('ncurses') # for integration diagnostics: indexamajig --int-diag

    depends_on('xgandalf') # for xgandalf indexing
    # depends_on('pinkindexer') https://stash.desy.de/users/gevorkov/repos/pinkindexer/browse
    #for indexing electron or wide bandwidth diffraction patterns
    depends_on('libzmq') #for online data streaming
    depends_on('msgpack-c', when='@0.10.1:')# for online data streaming
    depends_on('slurm', when='@0.10.1:') #required for submitting jobs via GUI

    # for CMake packages run 'spack install --test=root crystfel'
    # 'spack test run crystfel' after install does not work.
    install_time_test_callbacks = ['import_module_test']

    # one GPU test fails
    # Setting up GPU...
    # Couldn't get platform IDs: -1001
    # Couldn't set up GPU.
    # <end of output>
    # Test time =   0.05 sec
    # ----------------------------------------------------------
    # Test Failed.
    # "gpu_sim_check" end time: Jan 19 09:34 CET
    # "gpu_sim_check" time elapsed: 00:00:00