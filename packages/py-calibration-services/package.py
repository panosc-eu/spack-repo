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
#     spack install py-karabo-bridge
#
# You can edit this file again by typing:
#
#     spack edit py-karabo-bridge
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyCalibrationServices(PythonPackage):
    """Library from European XFEL."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://git.xfel.eu/gitlab/dataAnalysis/calibration-services"
    url      = "https://git.xfel.eu/gitlab/dataAnalysis/calibration-services/-/archive/dev/calibration-services-dev.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['daviddoji']
    install_time_test_callbacks = ['import_module_test']

    version('0.1.0', sha256='8c2da949587a730d1e26e2da7de713d38619a08bc3d058f6587a2b01848b6233')

    # FIXME: Add dependencies if required.
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-extra_data@1.1.0:')
    depends_on('py-extra_geom@0.9.0:')
    depends_on('py-dash@1.6.1:')
    depends_on('py-dash-daq@0.3.1:')
    depends_on('py-ipywidgets@7.5.1:')
    depends_on('py-mpi4py@3.0.2:')
    depends_on('py-iminuit')
    depends_on('py-pyfai@0.16.0:')

    depends_on ('py-coverage', type='test')
    depends_on ('py-dask', type='test')
    # depends_on ('py-nbval', type='test') #  Doesn't seem to be needed?
    depends_on ('py-pytest', type='test')
    depends_on ('py-pytest-cov', type='test')
    depends_on ('py-testpath', type='test')

    def test(self):
        # `setup.py test` should not be used as:
        #   - `python3 -m pytest -v` should be ran instead
        #   - the builtin `test` method runs before `install` is finished
        pass

    @run_after('install')
    def pytest(self):
        with working_dir('.'):
            prefix = self.spec.prefix
            #  Add bin to path here, as tests also check entrypoints
            env['PATH'] = env['PATH']+":"+prefix+"/bin"
            python('-m', 'pytest', '-v')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args