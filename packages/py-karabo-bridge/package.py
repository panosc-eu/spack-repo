# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyKaraboBridge(PythonPackage):
    """karabo_bridge is a Python 3 client to receive pipeline data from the
    Karabo control system used at European XFEL. A simulated Karabo bridge
    server is included to allow testing code without a connection to a real
    Karabo server.."""

    homepage = "https://github.com/European-XFEL/karabo-bridge-py"
    url      = "https://github.com/European-XFEL/karabo-bridge-py/archive/0.6.0.tar.gz"

    maintainers = ['robertrosca']

    version('0.6.1', sha256='a41d7bf473d8dbaf57071aa5b9bf6b5ddbdb3545d653224385cc7a8895008e54')
    version('0.6.0', sha256='8873e922995837520070ce61049036faef7f5f257d8307310081184c84971479')
    version('0.5.0', sha256='d9410231f9f42dd33e6dcaf3bc03aa14f3d56c801fcdc6875a9ebe79653312c6')
    version('0.4.0', sha256='1cb4a0056bc630b0cbc17c3268bd5dd1fa8ccbe2af71bebe6a8e57da31a424cf')
    version('0.3.0', sha256='5ff6bd7f90461e5dcca93ab22e96417b44527a32662a93963a046c264d22635c')

    depends_on('python@3.6:',   type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-msgpack@0.5.4:')
    depends_on('py-msgpack-numpy')
    depends_on('py-numpy')
    depends_on('py-pyzmq@17.0.0:')

    # Test dependencies
    depends_on('py-pytest',     type=('test'))
    depends_on('py-pytest-cov', type=('test'))
    depends_on('py-h5py',       type=('test'))
    depends_on('py-testpath',   type=('test'))


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
