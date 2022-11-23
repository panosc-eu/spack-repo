# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PySilx(PythonPackage):
    """The purpose of the silx project is to provide a collection of Python
    packages to support the development of data assessment, reduction and
    analysis applications at synchrotron radiation facilities. silx aims
    to provide reading/writing tools for different file formats, data
    reduction routines and a set of Qt widgets to browse and visualise
    data."""

    homepage = "http://www.silx.org/doc/silx/latest/"
    url      = "https://github.com/silx-kit/silx/archive/v0.14.0.tar.gz"

    maintainers = ['RobertRosca', 'julianhoersch']


    version('1.0.0',  sha256='c9a57b7a253d9cdca92404cd0ba0bed88115681e1982bae45101b7d85c55bde0')
    version('0.15.2', sha256='ab46c133a65d875512c0eef9e45cf0b7e2b55c8ed400a73efb19d15d6f7994db')
    version('0.15.1', sha256='c40da18a700f5bf8b8d370164b2218dff6ef8f7cb5c45b6be544f9e565626138')
    version('0.15.0', sha256='c5d5bf21e3c86463371dd33890afba666d331aa6970d9cd96168fab29be41056')
    version('0.14.1', sha256='72f78b05865aa2a5d43c1b96ba615ec95a934e3fed0b3a7f655535b5750ad233')
    version('0.14.0', sha256='17c595fe18c9eb3403a9d1f0ee6ea7b523607043c46c944573ecf406f6997866')
    version('0.13.2', sha256='88a16187283c8684be63ab37aee7267c370962dfbcf45cca77ae494ee5e4e773')
    version('0.13.1', sha256='2c5dbc1c043ecb78dafd1f7afbfd45833c87332818307196878b759956687491')
    version('0.13.0', sha256='8c2fe896a26ffd4811a1944481328faa60e05214b84e873bffbdd8cb13729535')

    # Required dependencies (from setup.py setup_requires and install_requires)
    depends_on('py-setuptools@:59', type='build')
    depends_on('py-numpy@1.12:')
    depends_on('py-cython@0.21.1:')
    depends_on('py-h5py')
    depends_on('py-fabio@0.9:')
    depends_on('py-six')

    depends_on('py-pytest', when='@1.0.0:')#, type='test')
    depends_on('py-pytest-xvfb', when='@1.0.0:')#, type='test')

    ## Extra dependencies (from setup.py extra_requires 'full' target)
    depends_on('py-pyopencl')             # platform_machine in "i386, x86_64, AMD64"  # For silx.opencl
    depends_on('py-mako')                 # For pyopencl reduction

    ## gui
    depends_on('py-qtconsole')            # For silx.gui.console
    depends_on('py-matplotlib@1.2.0:')    # For silx.gui.plot
    depends_on('py-pyopengl')             # For silx.gui.plot3d
    depends_on('py-python-dateutil')      # For silx.gui.plot
    depends_on('py-pyqt5')                 # PySide2, PySide6 # For silx.gui

    ## extra
    depends_on('py-scipy')                 # For silx.math.fit demo, silx.image.sift demo, silx.image.sift.test
    depends_on('py-pillow')                # For silx.opencl.image.test


    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args


    def pytest(self):

        prefix = self.spec.prefix
        with working_dir(prefix):
            #  Add bin to path here, as tests also check entrypoints
            env['PATH'] = env['PATH']+":"+prefix+"/bin"
            python('-m', 'pytest -h')#, '--no-gui=False')


    def test(self):
        # self.pytest()

        prefix = self.spec.prefix

        with working_dir(prefix):
            # it is possible to disable graphical tests and others below
            # works like this only if < 1.0.0
            with_qt_test = False        # to disable graphical tests
            silx_opencl = False        #to disable OpenCL tests
            silx_test_low_mem = False   # to disable tests taking large amount of memory
            gpu = False                 # to disable the use of a GPU with OpenCL test
            with_gl_test = False

            python('-c', 'import os; print(os.getcwd())')
            # python('-c', 'import silx.test; print(dir(silx.test))')
            # python('-c', 'import silx.test; print(silx.test.__path__)')

            # python('-c', 'import silx.test; \
            #        print(dir(silx.test)); \
            #        silx.test.utils.test_options.WITH_QT_TEST={}; \
            #        silx.test.utils.test_options.SILX_OPENCL={}; \
            #        silx.test.utils.test_options.SILX_TEST_LOW_MEM={}; \
            #        silx.test.utils.test_options.GPU={}; \
            #        silx.test.utils.test_options.WITH_GL_TEST={}; \
            #        silx.test.run_tests()'.format(with_qt_test, silx_opencl,
            #                                      silx_test_low_mem, gpu,
            #                                      with_gl_test))
            # from silx.test.utils import test_options

            python('-c', 'import silx.test; silx.test.run_tests(verbosity=1)')

            # python('-c', '//lib/python3.8//site-packages//silx//run_tests.py --no-gui')
            # python('-c', 'run_tests.py --no-gui')

            # python('-c', 'import silx.test; silx.test.pytest', '-v')
