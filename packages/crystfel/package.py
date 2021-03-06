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
#     spack install crystfel
#
# You can edit this file again by typing:
#
#     spack edit crystfel
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Crystfel(CMakePackage):
    """CrystFEL is a suite of programs for processing (and simulating) Bragg
       diffraction data from "serial crystallography" experiments, often (but
       not always) performed using an X-ray Free-Electron Laser.
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://www.desy.de/~twhite/crystfel/crystfel-0.9.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('0.9.1',
        sha256='1eaf757eb093385fbc16298168e683a5b3ef572800b8b22072886a76143b70be')
    version('0.9.0',
        sha256='1aeb6b8ddee598aa57475a53add36dab176b74cdea5f08808c96837aff40e3f8')
    version('0.8.0', '99d34906d6677f5a10f5e9f782485d8c',
        url='http://www.desy.de/~twhite/crystfel/crystfel-0.8.0.tar.gz')

    #  Versions 0.7.0 and under used AutoTools, 0.8.0 and above use CMake
    #  not too sure how to handle the change in build tools in spack
    # version('0.7.0', 'b064bf00f1de96ff23febe3337c4ac1d',
    #     url='http://www.desy.de/~twhite/crystfel/crystfel-0.7.0.tar.gz')
    # version('0.6.3',
    #     sha256='69a96b77b4b395b3827c2ac5c4aa2496427077ff31e23244d0a24837a23d5d6a')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    depends_on('cmake@3.12:')

    depends_on('bison@2.6:')
    depends_on('zlib@1.2.3:')
    depends_on('hdf5@1.10:')
    depends_on('gsl')
    depends_on('flex')
