# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyExtraData(PythonPackage):
    """Tools to read and analyse data from European XFEL."""

    homepage = "https://github.com/European-XFEL/EXtra-data"
    url      = "https://github.com/European-XFEL/EXtra-data/archive/1.2.0.tar.gz"

    maintainers = ['robertrosca']

    version('1.9.0', sha256='5170d2a9ecfdc6a635e46c8acc8a7d2557345484ec505ffc54cb26f41c96214b')
    version('1.8.1', sha256='950d1d570d94a764a9f9d76bfdf387e6034fb550117346513a7585016781b58f')
    version('1.8.0', sha256='39e1fc539a96cd447049d87b751929123f88c5a003edeb873e9bae6107986c5f')
    version('1.7.0', sha256='2f3c988e721b4dc93805b9e31f1e9bb7541aa8b783b81ccfc1ccd415c8d07cbe')
    version('1.6.1', sha256='74a51dfd8ac0b73d867854a45c33d47934e37b508b61053eda5ae62af1ec9d16')
    version('1.6.0', sha256='741fa876d952936d89458dabce9104c92a9af98f89f9263fe66bb7aee5bf246d')
    version('1.5.0', sha256='2ca13478c75ef24793e67f66e7cbbc0946c22d39f01450c78f75be0f0dca34c4')
    version('1.4.1', sha256='b48205caf89562990dfb4413dca03be1f8856932c7ad052b356bf6bfe68036f5')
    version('1.4.0', sha256='bc4e8b5d5a295ea28b4b913d028026314c740df6684e99f0bf17d5ddbb32d67f')
    version('1.3.0', sha256='7150b0d7ec3ea97af9e0b81bd88aeddb0716e79b852c603a83f4f04ff65935ce')
    version('1.2.0', sha256='bdb1da5469d314dc1c22cbbd1ecc6e1c9e0660bd1bada4f9a8efd97b3d8b1a0e')


    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-fabio') #  custom
    depends_on('py-h5py@2.7.1:')
    depends_on('py-karabo-bridge@0.6:') #  custom
    depends_on('py-psutil')
    depends_on('py-matplotlib')
    depends_on('py-numpy')
    depends_on('py-pandas')
    depends_on('py-scipy')
    depends_on('py-xarray')

    # by using type=test I can't run test run py-extra-data
    # 2 tests concerning test_serve_files fail if it is run like
    # install '--test=root' if 'test run' is run tests pass
    depends_on('py-coverage')#, type='test')
    depends_on('py-dask')#, type='test')
    # depends_on ('py-nbval', type='test') #  Doesn't seem to be needed?
    depends_on('py-pytest')#, type='test')
    depends_on('py-pytest-cov')#, type='test')
    depends_on('py-testpath')#, type='test')

    # not implemented error
    # install_time_test_callbacks = ['import_module_test']
    # use test
    install_time_test_callbacks = ['test']

    def test(self):
        # `setup.py test` should not be used as:
        #   - `python3 -m pytest -v` should be ran instead
        #   - the builtin `test` method runs before `install` is finished
        self.pytest()

    def pytest(self):
        prefix = self.spec.prefix
        with working_dir(prefix):
            #  Add bin to path here, as tests also check entrypoints
            env['PATH'] = env['PATH'] + ":" + prefix + "/bin"
            python('-m', 'pytest', '-v')
