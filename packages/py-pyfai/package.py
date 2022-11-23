# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyPyfai(PythonPackage):
    """PyFAI is an azimuthal integration library that tries to be fast (as fast as C and even more
    using OpenCL and GPU). It is based on histogramming of the 2theta/Q positions of each (center of)
    pixel weighted by the intensity of each pixel, but parallel version uses a SparseMatrix-DenseVector
    multiplication. Neighboring output bins get also a contribution of pixels next to the border thanks
    to pixel splitting. Finally pyFAI provides also tools to calibrate the experimental setup using
    Debye-Scherrer rings of a reference compound."""

    homepage = "https://github.com/silx-kit/pyFAI"
    url      = "https://github.com/silx-kit/pyFAI/archive/v0.19.0.tar.gz"

    maintainers = ['RobertRosca', 'julianhoersch']

    version('0.21.0', sha256='b057de00754485748f3cd441d849e99e52917d9169ba06743b76e04efe694f3b')
    version('0.20.0', sha256='f39f56ff58868ab7f12d6fa5c7bf6b7d111b7fa687f3816c5d8d11cb75fa82f0')
    version('0.19.0', sha256='1e329d2bdd6f4ddc4c70460bb0b994a33b6885bff810b11a7871d83ef8756281')
    version('0.18.0', sha256='4637eaa40a5a3b10c97ef0fea9e6f935c4ae93eb8df48643d567db7796cb3ef8')
    version('0.17.1', sha256='e4c2b53c71b638d5f532f5e557a87a79d1a3ab46552e4b5ad0f071e996f3974d')

    # dependencies for install and setup
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')

    depends_on('py-numpy')
    depends_on('py-fabio@0.5:')
    depends_on('py-matplotlib')
    depends_on('py-scipy')
    depends_on('py-numexpr')
    depends_on('py-silx@0.10:', when='@:0.20.0')
    depends_on('py-silx@0.15.2:', when='@0.21.0:')

    # other dependencies in requirements.txt and not in setup.py
    # tests run without
    # depends_on('py-cython')
    # depends_on('py-wheel')
    # depends_on('py-transformations')
    # depends_on('py-nbsphinx')

    # gui dependencies
    depends_on('py-pyqt5')
    depends_on('py-hdf5plugin')
    depends_on('py-h5py')
    depends_on('py-pyopengl')
    # opencl
    depends_on('py-pyopencl')


    def test(self):
        prefix = self.spec.prefix
        # options to disable tests
        # WITH_QT_TEST=False to disable graphical tests
        # PYFAI_OPENCL=False to disable OpenCL tests.
        # PYFAI_LOW_MEM: set to True to skip all tests >100Mb
        # WITH_GL_TEST=False to disable tests using OpenGL

        # disable test option
        # pyFAI.tests.utils.test_options.WITH_QT_TEST=False
        with working_dir(prefix):
            python('-c', 'import pyFAI; pyFAI.tests()')
