# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyExtraGeom(PythonPackage):
    """Tools to work with EuXFEL detector geometry and assemble detector images."""

    homepage = "https://github.com/European-XFEL/EXtra-geom"
    url      = "https://github.com/European-XFEL/EXtra-geom/archive/0.9.0.tar.gz"

    maintainers = ['github_user1', 'github_user2']

    version('1.6.0',  sha256='6433a37a26d71a8b15aba79ddb3ab536dea924ff8afa50c021689746c94b586d')
    version('1.5.0',  sha256='7b793245c662c67f311fb7ca2e8ad4bf56b39ad9cc67c17308fbe4e146734092')
    version('1.4.0',  sha256='3c1b5b64bad9ab12accf3c70c00fd396563cb69d2b0415a5373f21a1dedd44e1')
    version('1.3.0',  sha256='adb5dc06a15ec31ddce3c4df0ce938cc533ec4f815bfdc40e50afb04244eb73e')
    version('1.2.0',  sha256='e97907cacd52b21a6d7a3a7d5bafd357e02a76af4ded9b94cbd3df7ff7b45ca7')
    version('1.1.1',  sha256='1131e1fdffe09266178e7df34425bc87e972c5a77c0081b54442cbf36a8eb0d1')
    version('1.1.0',  sha256='c59a0301ccab81b541717e406e1b97844eb450c10df5e031b417b87987d90deb')
    version('1.0.0',  sha256='5d3d6c275b4f3b734005d5eb6ec1fb77361fdf386ae1e973859c7deb7e2dea81')
    version('0.10.0', sha256='01d1bb2edf5c6b624f3d598833e2729fe108f53991e2a9c58588ae0719295a10')
    version('0.9.0',  sha256='3a757a1517d016ca95f438c5aa9383dc1eefe45a242e651fe54ef4308324e41d')
    version('0.8.0',  sha256='329d3addec5d992f592720d93242efcf2d1e1272917de3207408033e1657d21d')
    version('0.7.0',  sha256='035986e7875301cabd0e1cfef7c31fa359fb92755e89507421bbf8db8c76b8d6')
    version('0.6.2',  sha256='a210803286cbd3930830d38cc75fa8c591c7c9f3e64ebdb3df752f0d746092b6')
    version('0.6.1',  sha256='a31943bdef21c740c94cbeebde8ec9f1348f5596c28ed639eae5603ef1074775')
    version('0.6.0',  sha256='17ca1939117016f6337c5f4051c4222ca47192c6fc004835e85e782b4ee8653f')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-cfelpyutils@0.92:1') # excludes > 2.0
    depends_on('py-h5py@2.7.1:')
    depends_on('py-matplotlib')
    depends_on('py-numpy')
    depends_on('py-scipy')

    # test dependencies
    depends_on('py-coverage@:4.9', type='test')
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-cov', type='test')
    depends_on('py-testpath', type='test')
    depends_on('py-xarray', type='test')
    depends_on('py-extra-data', type='test')
    # depends_on('py-nbval', type='test') # not available, tests pass without

    # not implemented error
    # install_time_test_callbacks = ['import_module_test']
    # use
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
            env['PATH'] = env['PATH']+":"+prefix+"/bin"
            python('-m', 'pytest', '-v')
