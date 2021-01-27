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


class PyExtraFoam(PythonPackage):
    """EXtra-foam is a framework that provides real-time and off-line data analysis 
    (detector geometry, pump-probe, azimuthal integration, ROI, statistics, etc.) 
    and visualization for experiments that use 2D area detectors (AGIPD, LPD, DSSC, 
    FastCCD, JungFrau, ePix100, etc.) and 1D detectors (Gotthard, XGM, digitizer, etc.) 
    at European XFEL."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://extra-foam.readthedocs.io/en/latest/"
    url      = "https://github.com/European-XFEL/EXtra-foam/archive/1.0.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['RobertRosca', 'julianhoersch']

    version('1.0.0beta3', sha256='38e1f7ea05ed32a3d041dbccb85862055436db4374a6c4007847d636ff2c003f')
    version('1.0.0beta2', sha256='04a5bafcb2af2daf122b94c78219ad857b5ad732f121d443d340f2ab49a26581')
    version('1.0.0beta1', sha256='938f0006ccb9042d44cc0bd6582ab5d191daf96b7db9c9d7afe8258a6798faf4')
    version('1.0.0',      sha256='8bb214cb21a414175f9ca207485c6cf6fac9c569198ac59b23b3a023f0f420d8')
    version('0.9.1',      sha256='7f3c48985d0f656e35e6364a6279e458841566b866c59bd509aa96b855d2d668')
    version('0.9.0beta3', sha256='fbd3e2b23d9cfc623b225c4572be54b31ef3203597b43ba5a9cb8b1e333f983c')
    version('0.9.0beta2', sha256='84eddd55220e4e89080442f267141a2688cf5cda397b5e22da6303622c675b4e')
    version('0.9.0beta1', sha256='b1bbaa7d0edc4064106c10a837bfcf7f345889f51419d558734a292cefe737c7')
    version('0.9.0',      sha256='aa3422639b6ef6f7cbe0b93155322d51af89115f30a4525104268adbb0fed6f7')
    version('0.8.4',      sha256='ab36bb07952eb0b4e1956bdb626df0ce3975ab64dc64eda6822ddc5759fb8a14')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy@1.16.1:')
    depends_on('py-scipy@1.2.1:')
    depends_on('py-msgpack@0.5.6:')
    depends_on('py-msgpack-numpy@0.4.4:')
    depends_on('py-pyzmq@17.1.2:')
    depends_on('py-pyfai@0.17.0:')
    depends_on('py-pyqt5@5.13.2') # needs higher compiler version as default on maxwell (gcc@4.8.5) -> gcc@:5.0.999
    depends_on('py-extra-data@1.0.0:')
    depends_on('py-extra-geom@0.8.0:')
    depends_on('py-karabo-bridge@0.5.0:')
    depends_on('py-toolz@0.9.0:')
    depends_on('py-silx@0.9.0:')
    depends_on('py-hiredis@1.0.1')
    depends_on('py-redis@3.5.2')
    depends_on('py-psutil@5.6.2:')
    depends_on('py-imageio@2.8.0')
    depends_on('py-pillow@7.0.0')
    depends_on('py-pyyaml@5.2:')

    depends_on('py-coverage@:4.9', type='test')
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-cov', type='test')
    depends_on('py-testpath', type='test')


    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
