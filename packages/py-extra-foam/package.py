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
#     spack install py-extra-foam
#
# You can edit this file again by typing:
#
#     spack edit py-extra-foam
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os


class PyExtraFoam(PythonPackage):
    """EXtra-foam is a framework that provides real-time and off-line data analysis
    (detector geometry, pump-probe, azimuthal integration, ROI, statistics, etc.)
    and visualization for experiments that use 2D area detectors (AGIPD, LPD, DSSC,
    FastCCD, JungFrau, ePix100, etc.) and 1D detectors (Gotthard, XGM, digitizer, etc.)
    at European XFEL."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://extra-foam.readthedocs.io/en/latest/"
    url      = "https://github.com/European-XFEL/EXtra-foam/archive/1.0.0.tar.gz"
    git      = "https://github.com/European-XFEL/EXtra-foam.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['RobertRosca', 'julianhoersch']

    # test lates dev versionvc
    version('dev', branch='dev')
    # version('master', branch='master')
    # version('1.0.0beta3', sha256='38e1f7ea05ed32a3d041dbccb85862055436db4374a6c4007847d636ff2c003f')
    # version('1.0.0beta2', sha256='04a5bafcb2af2daf122b94c78219ad857b5ad732f121d443d340f2ab49a26581')
    # version('1.0.0beta1', sha256='938f0006ccb9042d44cc0bd6582ab5d191daf96b7db9c9d7afe8258a6798faf4')
    # version('1.0.0',      sha256='8bb214cb21a414175f9ca207485c6cf6fac9c569198ac59b23b3a023f0f420d8')
    # version('0.9.1',      sha256='7f3c48985d0f656e35e6364a6279e458841566b866c59bd509aa96b855d2d668')
    # version('0.9.0beta3', sha256='fbd3e2b23d9cfc623b225c4572be54b31ef3203597b43ba5a9cb8b1e333f983c')
    # version('0.9.0beta2', sha256='84eddd55220e4e89080442f267141a2688cf5cda397b5e22da6303622c675b4e')
    # version('0.9.0beta1', sha256='b1bbaa7d0edc4064106c10a837bfcf7f345889f51419d558734a292cefe737c7')
    # version('0.9.0',      sha256='aa3422639b6ef6f7cbe0b93155322d51af89115f30a4525104268adbb0fed6f7')
    # version('0.8.4',      sha256='ab36bb07952eb0b4e1956bdb626df0ce3975ab64dc64eda6822ddc5759fb8a14')


    # depends_on('python@3.6:', type=('build', 'run'))
    # depends_on('py-setuptools', type='build')
    # depends_on('cmake@3.17.0:', type='build')
    # depends_on('py-numpy@1.16.1:')
    # depends_on('py-scipy@1.2.1:')
    # depends_on('py-msgpack@0.5.6:')
    # depends_on('py-msgpack-numpy@0.4.4:')
    # depends_on('py-pyzmq@22.3.0:') # import tests of updated version fails
    # depends_on('py-pyfai@0.17.0:')

    # #depends_on('py-pyqt5@5.13.2') # needs higher compiler version as default on
    # # maxwell (gcc@4.8.5) -> gcc@:5.0.999
    # # version 5.13.2 not available
    # depends_on('py-pyqt5@5.13.1') # try with available version
    # # 'PyQt5-sip>=12.9.0',
    # # depends_on('py-sip@develeop') # versions too low
    # depends_on('py-extra-data@1.0.0:')
    # depends_on('py-extra-geom@0.8.0:')
    # depends_on('py-karabo-bridge@0.5.0:')
    # depends_on('py-toolz@0.9.0:')
    # depends_on('py-silx@0.9.0:')
    # depends_on('py-hiredis@1.0.1') # added version, import tests pass
    # # not available
    # #depends_on('py-redis@3.5.2')
    # depends_on('py-redis@3.5.3') # update?
    # depends_on('py-psutil@5.6.2:')
    # depends_on('py-imageio@2.8.0') # added 2.8.0 import tests pass
    # depends_on('py-pillow@8.3.2+tiff') # updated import test pass
    # depends_on('py-pyyaml@5.2:')

    # # open source build
    # # depends_on('intel-tbb@2021.1.1:') # doesn't work for 2021
    # # "Both intel-tbb and intel-oneapi-tbb do a provides('tbb')
    # # so they are interchangeable in that sense."
    # # https://github.com/spack/spack/pull/25613#issuecomment-905830566
    # # product build
    # depends_on('intel-oneapi-tbb@2021.1.1:')
    # # depends_on('xtensor')
    # depends_on('xtensor-python') # added new version and removed constraint on
    # # pybind that conflicted with opencl's pybind required version
    # depends_on('xtensor-blas') # created new package not tested, but installable

    # # # extras
    # # # docs
    # # depends_on('py-sphinx')
    # # depends_on('py-nbsphinx')
    # # depends_on('py-ipython')

    # # test
    # depends_on('py-pytest', type='test')
    # depends_on('py-pytest-cov', type='test')

    # # # web
    # # depends_on('py-dash1.1.0:')    # not available

    # # from failing tests
    # depends_on('py-pyside2')
    # # depends_on('py-pyqt4')#^py-sip@:4.19.18 module=PyQt4.sip+multi')
    # # depends_on('dash')

    # # depends_on('py-sip@:4.19.18 module=PyQt4.sip+multi')

    # # depends_on('py-sip module=PyQt5.sip+multi', type=('build', 'run'))
    # # depends_on('py-sip@:4.19.18 module=PyQt5.sip+multi',
    # #            type=('build', 'run'), when='@:5.13.0')


    # # variant('module', default='sip', when='@:4', description='Name of private SIP module',
    # #         values=str, multi=False)

    # # def setup_run_environment(self, env):

    # #     # set the path for plugins to an empty string, otherwise system default
    # #     # could be falsely used
    # #     env.set('HDF5_PLUGIN_PATH', '')


    # updated dependencies

    # does not work with 3.10! -> Error: py-extra-foam is unsatisfiable, errors are:
    # problem with 3.9 too, pyside2 doest work with current version would need to
    # chckout dev branch of spack
    # no version satisfies the given constraints#
    depends_on('python@:3.8', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('cmake@3.20.0:', type='build')
    depends_on('py-numpy')
    depends_on('py-pybind11')
    depends_on('py-scipy')
    depends_on('py-msgpack')
    depends_on('py-msgpack-numpy')
    depends_on('py-pyzmq') # import tests of updated version fails, switch back
    # to spack version
    depends_on('py-pyfai')

    #depends_on('py-pyqt5@5.13.2') # needs higher compiler version as default on
    # maxwell (gcc@4.8.5) -> gcc@:5.0.999
    # version 5.13.2 not available
    depends_on('py-pyqt5') # try with available version
    depends_on('py-pyqt5-sip')
    # 'PyQt5-sip>=12.9.0',
    # depends_on('py-sip@develeop') # versions too low
    depends_on('py-extra-data')
    depends_on('py-extra-geom')
    depends_on('py-karabo-bridge')

    # depends_on('py-silx@0.9.0:')
    depends_on('py-hiredis') # added version, import tests pass, switch back to spack

    # not available
    #depends_on('py-redis@3.5.2')
    depends_on('py-redis') # update, back to spack
    depends_on('py-psutil')
    depends_on('py-imageio') # added 2.8.0 import tests pass, back to spack
    #TODO tiff needed?
    depends_on('py-pillow+tiff') # updated import test pass, back to spack
    depends_on('py-pyyaml')

    # These dependencies are not directly used, but are needed to satisfy
    # pip's resolver:
    depends_on('py-pygments')
    depends_on('py-jinja2')
    depends_on('py-decorator')
    depends_on('py-pexpect')
    depends_on('py-toolz')
    depends_on('py-packaging')
    depends_on('py-cffi')

    # # extras
    # # docs
    # depends_on('py-sphinx')
    # depends_on('py-nbsphinx')
    # depends_on('py-ipython')

    # test
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-cov', type='test')

    # # web
    # depends_on('py-dash1.1.0:')    # not available

    # from failing tests
    # open source build
    # depends_on('intel-tbb@2021.1.1:') # doesn't work for 2021
    # "Both intel-tbb and intel-oneapi-tbb do a provides('tbb')
    # so they are interchangeable in that sense."
    # https://github.com/spack/spack/pull/25613#issuecomment-905830566
    # product build
    depends_on('intel-oneapi-tbb@2021.1.1:')
    # depends_on('xtensor')
    depends_on('xtensor-python') # added new version and removed constraint on
    # pybind that conflicted with opencl's pybind required version
    depends_on('xtensor-blas') # created new package not tested, but installable
    depends_on('py-pyside2')
    # depends_on('py-pyqt4')#^py-sip@:4.19.18 module=PyQt4.sip+multi')
    # depends_on('dash')
    depends_on('googletest+gmock')

    # depends_on('py-sip@:4.19.18 module=PyQt4.sip+multi')

    # depends_on('py-sip module=PyQt5.sip+multi', type=('build', 'run'))
    # depends_on('py-sip@:4.19.18 module=PyQt5.sip+multi',
    #            type=('build', 'run'), when='@:5.13.0')


    # variant('module', default='sip', when='@:4', description='Name of private SIP module',
    #         values=str, multi=False)

    # def setup_run_environment(self, env):

    #     # set the path for plugins to an empty string, otherwise system default
    #     # could be falsely used
    #     env.set('HDF5_PLUGIN_PATH', '')



    # phases = ['build', 'build_ext', 'install']
    phases = ['build_ext', 'install']#, 'test']

    def build_ext_args(self, spec, prefix):
        args = ['--with-tests', '--inplace']
        return args


    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args


    def _get_build_dir(self, dirname):
        version = sys.version_info
        return f"{dirname}.{sysconfig.get_platform()}-{version[0]}.{version[1]}"

    def run(self):
        # build and run cpp test
        build_temp = osp.join('build', self._get_build_dir('temp'))
        with changed_cwd(build_temp):
            self.spawn(['make', 'ftest'])

        # run Python test
        import pytest
        errno = pytest.main(['extra_foam'])
        sys.exit(errno)

    def test(self):
        # `setup.py test` should not be used as:
        #   - `python3 -m pytest -v` should be ran instead
        #   - the builtin `test` method runs before `install` is finished
        self.pytest()
        # self.staging_pytest()

    def staging_pytest(self):
        # spack('cd py-extra-foam')
        # python('-m', 'setup.py', 'test')
        # print('build_dir : ', self.build_directory)
        # print('spec', self.spec)
        # print('spec dir', dir(self.spec))

        # # for attr in dir(self.spec):
        # #     try:
        # #         print('{} : {}'.format(attr,
        # #         self.spec.))

        # # print('hash : ', self.content_hash())
        # # print('spec a', self.spec.build_hash())
        # # print('spec b', self.spec._build_hash)
        # # print('spec c', self.spec.__hash__())
        # # print('spec d', self.spec._cached_hash)
        # print('spec e', self.spec._hash)
        # print('spec v', self.spec.version)
        # # print('spec f', self.spec._full_hash)
        # # print('spec g', self.spec._hashes_final)
        # # print('spec h', self.spec._package_hash)
        # # print('spec i', self.spec.package_hash())
        # # print('spec j', self.spec._spec_hash)
        # # print('spec k', self.spec.full_hash())
        # # print('spec l', self.spec.fullname)
        # # print('spec m', self.spec.namespace)
        # # print('spec n', self.spec.node_dict_with_hashes())

        # print('test', self.spec['python'].command.path)
        # print('name', self.name)
        # # print(self.stage.stage_prefix)
        # # print(dir(self))



        # staging_name = 'spack-stage-{}-{}-{}'.format(
        #     self.name, self.spec.version, self.spec._hash)
        # print('nam', staging_name)
        # staging_dir = self.build_directory + staging_name
        # print('dir', staging_dir, ' end')
        # print('\n')

        with working_dir(self.build_directory):
            print('working in ', self.build_directory)
            python('-m', 'setup.py', 'test')

    def pytest(self):

        # self.run()
        prefix = self.spec.prefix
        print('prefix: ', prefix)
        import os
        directory = prefix #+ '/lib/python3.8/site-packages/' #extra_foam'
        print(directory)
        with working_dir(directory):


            absolute_path = os.path.abspath(__file__)
            cwd = os.getcwd()
            print('cwd', cwd)
            print("Full path: " + absolute_path)
            print("Directory Path: " + os.path.dirname(absolute_path))

            # /gpfs/exfel/data/scratch/jhoersch/spack/opt/spack/
            # linux-centos7-x86_64/gcc-11.1.0/
            # py-extra-foam-dev-oijwvx2uw4bq3shbrkkq3pevspiym2y5/
            # lib/python3.8/site-packages/extra_foam/setup.py

            # mkdir build && cd build')
            # os.mkdir('build')
            # os.chdir('build')
            # cmake('-m', 'make ftest', '-DBUILD_FOAM_TESTS')
            # #  Add bin to path here, as tests also check entrypoints
            # os.chdir(directory)
            env['PATH'] = env['PATH']+":"+prefix+"/bin"
            python('-m', 'pytest', '-v')
            # python('-m', "pytest.main()", '-v')
            # python('-m', 'setup.py test', '-v')
            # python('-m', 'pytest extra_foam', '-v')
            # python('-m', 'extra_foam.pytest', '-v')
            # python('-m', 'setup.py', 'test')