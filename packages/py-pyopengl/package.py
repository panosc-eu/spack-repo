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
#     spack install py-pyopengl
#
# You can edit this file again by typing:
#
#     spack edit py-pyopengl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyPyopengl(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://pypi.org/project/PyOpenGL/"
    # url      = "https://files.pythonhosted.org/packages/b8/73/31c8177f3d236e9a5424f7267659c70ccea604dab0585bfcd55828397746/PyOpenGL-3.1.5.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    pypi = 'PyOpenGL/PyOpenGL-3.1.6.tar.gz'
    # https://pypi.org/project/PyOpenGL/

    version('3.1.6', sha256='8ea6c8773927eda7405bffc6f5bb93be81569a7b05c8cac50cd94e969dce5e27')
    version('3.1.5', sha256='4107ba0d0390da5766a08c242cf0cf3404c377ed293c5f6d701e457c57ba3424')

    # FIXME: Add dependencies if required.
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    # depends_on('opengl')

    depends_on('py-cython')

    # depends_on('py-numpy')
    # depends_on('freeglut')
    # depends_on('py-pillow')


    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = ['PYOPENGL_PLATFORM=egl']
        return args

    # testing might be dificult due to tox thing

    # def test(self):

    #     with working_dir('.'):

    #         python('-c', 'import OpenGL; print(dir(OpenGL)); OpenGL.tests()')