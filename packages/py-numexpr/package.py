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
#     spack install py-numexpr
#
# You can edit this file again by typing:
#
#     spack edit py-numexpr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyNumexpr(PythonPackage):
    """NumExpr is a fast numerical expression evaluator for NumPy. With it, 
    expressions that operate on arrays (like '3*a+4*b') are accelerated and 
    use less memory than doing the same calculation in Python. 
    
    In addition, its multi-threaded capabilities can make use of all your cores 
    -- which generally results in substantial performance scaling compared to NumPy. 
    
    Last but not least, numexpr can make use of Intel's VML (Vector Math Library, 
    normally integrated in its Math Kernel Library, or MKL). This allows further 
    acceleration of transcendent expressions."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/pydata/numexpr/"
    url      = "https://github.com/pydata/numexpr/archive/v2.7.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['RobertRosca', 'julianhoersch']

    version('3.0.1a5', sha256='e2ff7f3244a6c780059b7d80f22af07bbf93b01502da0df10c553fb30c6e8de2')
    version('2.7.2',   sha256='7d1b3790103221feda07f4a93a4fa5c6654f46865197a677ca6f27eb5cb4e5ef')
    version('2.7.1',   sha256='5c6ae3bb5688184b922b43fc47de49d642576d0feec55a1b679caa66efae90a1')
    version('2.7.0',   sha256='1923f038b90cc69635871968ed742be7775c879451c612f173c2547c823c9561')
    version('2.6.9',   sha256='d57267bbdf10906f5ed7841b3484bec4af0494102b50e89ba316924cc7a7fd46')
    version('2.6.8',   sha256='1a9684008c5ff7d69a5aa2998a3186587ee89f6cc6c4966f76aed8c4ee9f5b92')
    version('2.6.7',   sha256='e81a1a13656712aff072d89f49ecf905fd3c6b6722544c1decb132903c54a967')
    version('2.6.6',   sha256='f1f65fb3e0534b3391055e056ef7ecd537c9a2880af66f5a15e7abc029547c4a')
    version('2.6.5',   sha256='fe78a78e002806e87e012b6105f3b3d52d47fc7a72bafb56341fcec7ce02cfd7')
    version('2.6.4',   sha256='049da1c07bd62d2aba29887130ccc9aff9b90962cb779a7b7ddc15e580368fba')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    depends_on('python@2.6:', type=('build', 'run')) 
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy@1.7:')

    # test dependencies
    depends_on('py-coverage@:4.9', type='test')
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-cov', type='test')
    depends_on('py-testpath', type='test')
    
    def test(self):
        # `setup.py test` should not be used as:
        #   - `python3 -m pytest -v` should be ran instead
        #   - the builtin `test` method runs before `install` is finished
        self.pytest()

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
