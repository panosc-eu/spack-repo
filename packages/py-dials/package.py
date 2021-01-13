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
#     spack install py-dials
#
# You can edit this file again by typing:
#
#     spack edit py-dials
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyDials(PythonPackage):
    """X-ray crystallography for structural biology has benefited greatly from 
    a number of advances in recent years including high performance pixel array 
    detectors, new beamlines capable of delivering micron and sub-micron focus 
    and new light sources such as XFELs. The DIALS project is a collaborative 
    endeavour to develop new diffraction integration software to meet the data 
    analysis requirements presented by these recent advances. There are three end 
    goals: to develop an extensible framework for the development of algorithms to 
    analyse X-ray diffraction data; the implementation of algorithms within this 
    framework and finally a set of user facing tools using these algorithms to 
    allow integration of data from diffraction experiments on synchrotron and 
    free electron sources."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://dials.github.io"
    url      = "https://github.com/dials/dials/archive/v3.2.3.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['RobertRosca', 'julianhoersch']

    version('3.3.0',                sha256='163ffd5da4b6c783e5e37ffedae751b86b26d0266c88b95280d727a69180e14c')
    version('3.2.3',                sha256='e9b52b9bc61595579401bbae2447d42e49a4a30d15c2908bea0899216cf8fedb')
    version('3.2.2',                sha256='3df1c0d0145d59f176fe81f0e8b23ea28955781021183d2497c183a26ec0a7bb')
    version('3.2.1',                sha256='1bca865ebb2fa3b8e789dcc1805956934332af7629642c5d556bc6c11bc6583e')
    version('3.2.0',                sha256='0cd2a8905ee239d8577b2150d9d97d2d83527b26f9d01ce7cb940bd04bd6c3eb')
    version('3-1-4',                sha256='c54e8948e06ddab5be99e0a499f5f9067d72af97cbaddf9f5d88919fe7aa08ac')
    version('3-1-3',                sha256='b26aea14ad48fa44a8c1db8fe5ef533e95a1f7ad9b6a2e0048810255fec12709')
    version('3-1-2',                sha256='47625e40d2dcee5364fa5ba0b2b2256e3f0f58c706179d66cd03acf901ee8181')
    version('3-1-1',                sha256='68c96a82e8e21b0e5e1dbc85ca00aa4bba91690d9d9a2aee757da00cad4ff636')
    version('3.1.0',                sha256='031d6073f9c4a40f73e31cd4bb4e466b04a994a47923bea9e7b85b092a687f74')
    version('3-0-4',                sha256='7c8123868e5d9d8090cc946f694be51b474de92def1876c9a3d468ef71c2ea38')
    version('3-0-3',                sha256='55b2be86f3079f8d153331c78e2efd88a26471b2a8a134738b1b65be3e86ca06')
    version('3-0-2',                sha256='dd3be99a91111169bcf0a763f46c86b4352c0e68b3063f7202fc2ef1393cd143')
    version('3-0-1',                sha256='cdfad52648399e781c02ee8d9d557555a1e99090ebe149b9a953f8bcac8d35ec')
    version('3.0.0',                sha256='ab39ea80d5e35883087ef36d5b871893fbf8956ee34a22775f6b4e27fb1eb5c2')
    version('3.dev',                sha256='ccbdf49f0a53d92bffa6e0c463a8d8e438d474d470447809baf2f2d771dd8151')
    version('2-2-10-macosx-conda3', sha256='32e4e418cf837514eb79c7462073dd8a2605c71299a52e370d00dc6c4c6a98d9')
    version('2-2-10',               sha256='09468f2fa8abb273e9c34d51bb657a05bf40e472ef668d886b8b21bd54b8af96')
    version('2-2-9-macosx-conda3',  sha256='48b7fc4c18b59b0bbd7431cb9836f81479d8dd1fbf266f46225f2058faaccf31')
    version('2-2-9',                sha256='70b615f9f8a152f603d8f65280be3c72c8ea6916e6cba81bc033aff7c2fda450')
    version('2-2-8-macosx-conda3',  sha256='54250bbc8ecbe37ffef048a4bbb501fab7adcebc0a8b71238c2bf25de486ef67')
    version('2-2-8',                sha256='8ad6572faf1bd07e2a1aee417c148b9b40c1b04b0356fc2df2ce2bc70368e675')
    version('2-2-7-macosx-conda3',  sha256='07b9855dffc59aa26ed6d4d842b8338da336b1f732379ca755d6b58e09799bc0')
    version('2-2-7',                sha256='d22c75eed5198fb9c3e11b0d957590e5caaf404dedc1910b67f6d7cfe47b530a')
    version('2-2-6-macosx-conda3',  sha256='9ac227d8ddf6117215b4a446118efa2068438d17b8a29abda7d392dcb13014ac')
    version('2-2-6',                sha256='371ddbee804cfea3e82767919458d0e92c6d7a06227914cc75c9b53034f3df65')
    version('2-2-5-macosx-conda3',  sha256='234771cb45ea3df336313c2e388909bd522cd17d067501dcb6c872f872b1d8bd')
    version('2-2-5',                sha256='52301ea90059911cafc9b508f665c279a45fcf0e1945e25e3bf2c7e3be18a0e5')
    version('2-2-4-macosx-conda3',  sha256='d32ca2719fdf3a546166c916ce638cf7c2a642ca64b42cf0fd204274b1396987')
    version('2-2-4',                sha256='6007ad8c7912d662ccca2bfc4042ad6914e384e0cc082a9d30b17482f2c7384c')
    version('2-2-3-macosx-conda3',  sha256='51dea8c04e3bcfae184124da3b63a32e85893d76de2b7fe11f0edd2b2bc79278')
    version('2-2-3',                sha256='c6428fb633886be0fe27f4c88640c560c259fbb836dd468e79911f124b8fdb31')
    version('2-2-2-macosx-conda3',  sha256='d9b749642ffd79bb7b7f116e2e2e2511dd627609356ad695500287a6b2ee2bae')
    version('2-2-2',                sha256='fc7af3b57c9d1ef72eeb9d6d7537dad07de9ca1e7a2e6f713f5707227d8557f8')
    version('2-2-1-macosx-conda3',  sha256='727a1a5994d806d67e8cf0a788cc0577045a12d5c473512fe0d8557aaaeb9e8a')
    version('2-2-1',                sha256='f836216fd3aff7e341e045935acbbbc1446a005c0b88cd133cae940941dc566f')
    version('2-2-0-macosx-conda3',  sha256='3690c19b0ac1d9ad1ffd6e89ee1cf998a4bc38315c5bf3d79a62cf11685a041d')
    version('2.2.0',                sha256='5b5d8b8bd071f519ac031a2aa8e01819a355ff0647753ac3e30028f05331dce0')
    version('2-1-5-macosx-conda3',  sha256='f874ee1f0fa35e213fcb7c329c3e642712f5d96dc9c35c7337ade8ddcec49d68')
    version('2-1-5',                sha256='2744cc7842296913bd6e2794704fd6ba416df0cf4784101f3341386ac0b3b426')
    version('2-1-4-macosx-conda3',  sha256='e8d4cb4efc48e1fff1e8325c37cfecba525a38ceae75c1254d49d73b8f38b9fe')
    version('2-1-4',                sha256='7cc48986e6b17a979ac7e8b4d99a03fe8a5d0943f22f437731538ab0802ed6f6')
    version('2-1-3-macosx-conda3',  sha256='7b5c374643183773f0324971fedc251e9c2db62cf9efdb9c73ee5de09ee79558')
    version('2-1-3',                sha256='0b35f0c8409edc6f84adc37212a1749fae9ec4cc67b6e1f53a1a4fc8fc8c02d8')
    version('2-1-2-macosx-conda3',  sha256='e797efd61a95526ea19c92ed896801774f81eb571a03c7f510d7c9e227de588e')
    version('2-1-2',                sha256='2b5e63419377a14f3d7f17a56eb84f9551fab4eb2568ce0c342a1ba307e0337d')
    version('2-1-1-macosx-conda3',  sha256='6b436e8cb1c88a8b6226e9511b8c9176e72ac9cfad548537ebbedb1d863f04a8')
    version('2-1-1',                sha256='c41bb0376d80d60c608778ca0364170369b138f40de37e1823c886b5476373a1')
    version('2-1-0-macosx-conda3',  sha256='cfce998484e07d9eeec7c645f49f5761a7b1dff871917b7dda60fc1e69e2ba25')
    version('2.1.0',                sha256='f89c02377d3190950b75fa29b36d91fd2515256434dbe96364eb48bfc3caf832')
    version('2-0-4',                sha256='27695b68fa33e9b2c3a683ed8fc24bb48b1d6d020bac9aa6c48df20a8aa34d17')
    version('2-0-3',                sha256='d6e90e9dfdfdabd761f90281a8c8ebeddf2e04443253d093becb60addd0e8897')
    version('2-0-2',                sha256='ce713ee1ee2c234f9ec00e5d8ba452e0aa682900b74dcd8dfc5ae01fd6342b08')
    version('2-0-1',                sha256='dcdadb8af35d4348770aef531ab1109c6af77b5f390a8003b5b025e300b7fa7f')
    version('2.0.0',                sha256='3aaa6274646886d640c362ec8937e5ae3d63c3cdf2a0236ac1dc532e87869f10')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-dials-data')
    depends_on('py-jinja2')
    depends_on('py-procrunner')
    depends_on('py-six')
    
    # tests
    depends_on('py-pytest-runner', type='test') # add type=test? only needed during development
    depends_on('py-mock', type='test')
    depends_on('py-coverage@:4.9', type='test')
    depends_on('py-pytest', type='test')
    depends_on('py-pytest-cov', type='test')
    depends_on('py-testpath', type='test')
    

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
