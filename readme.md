# PaNOSC Spack Repository

Repository of Spack packages used at PaNOSC partner facilities.

This contains an early attempt to run CI tests on the package files themselves
to ensure that the created packages run correctly. The CI is based on GitHub
Workflows and Actions, and runs using a Docker container which contains all
dependencies required for the packages being tested to be installed to save on
build times.

## Package status:

| package          |                                                                                                                                                                     status | repo-deps                   | notes |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|-----------------------------|-------|
| crystfel         | [![](https://github.com/panosc-eu/spack-repo/workflows/crystfel/badge.svg)](https://github.com/panosc-eu/spack-repo/actions?query=workflow%3Acrystfel)                 |                             | wip   |
| py-cfelpyutils   | [![](https://github.com/panosc-eu/spack-repo/workflows/py-cfelpyutils/badge.svg)](https://github.com/panosc-eu/spack-repo/actions?query=workflow%3Apy-cfelpyutils)     |                             | wip   |
| py-extra-data    | [![](https://github.com/panosc-eu/spack-repo/workflows/py-extra-data/badge.svg)](https://github.com/panosc-eu/spack-repo/actions?query=workflow%3Apy-extra-data)       | py-karabo-bridge, py-fabio  | wip   |
| py-extra-geom    | [![](https://github.com/panosc-eu/spack-repo/workflows/py-extra-geom/badge.svg)](https://github.com/panosc-eu/spack-repo/actions?query=workflow%3Apy-extra-geom)       | py-cfelpyutils              | wip   |
| py-fabio         | [![](https://github.com/panosc-eu/spack-repo/workflows/py-fabio/badge.svg)](https://github.com/panosc-eu/spack-repo/actions?query=workflow%3Apy-fabio)                 |                             | wip   |
| py-karabo-bridge | [![](https://github.com/panosc-eu/spack-repo/workflows/py-karabo-bridge/badge.svg)](https://github.com/panosc-eu/spack-repo/actions?query=workflow%3Apy-karabo-bridge) | py-msgpack-numpy            | wip   |
| py-msgpack-numpy | [![](https://github.com/panosc-eu/spack-repo/workflows/py-msgpack-numpy/badge.svg)](https://github.com/panosc-eu/spack-repo/actions?query=workflow%3Apy-msgpack-numpy) |                             | wip   |
| py-pyfai         | [![](https://github.com/panosc-eu/spack-repo/workflows/py-pyfai/badge.svg)](https://github.com/panosc-eu/spack-repo/actions?query=workflow%3Apy-pyfai)                 | py-fabio, py-hdf5plugin     | wip   |

## Notes

### CI

CI runs on GitHub Workflows. There is a file `.github/generate-workflows.py`
which uses a template workflow `.github/template/package-test.template.yaml`
file to generate a workflow for each of the packages in this repo.

The workflows run only when their respective package files change, which means
that tests are not re-ran if a dependency changes, only if the package file
changes.

Workflows run in a docker container `robertrosca/panosc-spack-centos7:0.16.0v3`
which is explained in the [Test Environment Image](#test-environment-image)
section.

Workflows run the following commands:

```
echo Spack version: $(spack --version)
echo Tests for package {PACKAGE}
spack repo add --scope=site ./
spack install --test=root --verbose {PACKAGE}
```

Currently only the tests included in the packages themselves (e.g. for a
Python package, those run by `python setup.py test`) are ran.

### Test Environment Image

The `Dockerfile` in this repository is used to build the container used during
the package tests.

The container has all of the dependencies of the packages pre-installed, so that
only the package being tested needs to be installed. If this wasn't done, each
test would need to build a substantial amount of software and would take over 20
minutes to well over an hour to run, which is a bit too long.

This means that whenever a new package is added, the package should be added to
the spack environment file and then the Docker image should be re-built so that
the required dependencies are included.

To speed up the initial container build process we use the [E4S
Buildcache](https://e4s-project.github.io/download.html) which provides a binary
mirror of some common packages. For the cache to be valid the configurations for
the package being installed **must** be identical down to the hash, to ensure
this is the case we use the same `packages.yaml` configuration as the one used
by E4S, this is at `.docker/opt/spack/etc/spack/packages.yaml` and is copied
into the container during the docker build process.

### GitHub Workflows

GitHub Workflows are cool for a few reasons, but one reason alone makes them
amazing: act https://github.com/nektos/act

It lets you run the workflows locally. For example, run `act -b` in the root of
this repo to run all the workflows, or for a specific workflow use `-j` to set
the job, e.g. `act -b -j package-test-py-extra-data`

### Dependabot

Dependabot is set up on this repository to provide notifications of package
updates.

`.github/dependabot/requirements.txt` is a pip requirements file which has a
list of all of the python pip packages provided in this repository, pinned to
the highest version specified in the `package.py` file.

For example, `requirements.txt` has `extra_data==1.2.0` as a 'requirement'
because in `packages/py-extra-data/package.py` we have:

```
version('1.2.0', sha256='bdb1da5469d314dc1c22cbbd1ecc6e1c9e0660bd1bada4f9a8efd97b3d8b1a0e')
```

When Dependabot finds an outdated dependency it will open a PR to bump the
version, this is an indication that the version in the `package.py` file should
also be bumped.

Dependabot automatically creates a branch like:
`dependabot/pip/dot-github/dependabot/{PACKAGE_NAME}-{BUMP_VERSION}`, you should
switch to that branch and make any relevant updates to the `package.py` file
there, before merging.

For example, look at this [PR from Dependabot](https://github.com/panosc-eu/spack-repo/pull/2)
which bumps extra-geom to a newer version. The PR was automatically generated,
then locally you switch to the branch, do this the 'traditional' way by:

```
> git fetch dependabot/pip/dot-github/dependabot/extra-geom-0.10.0
> git checkout dependabot/pip/dot-github/dependabot/extra-geom-0.10.0
```

Or use the fancier github CLI:

```
> gh pr list
> #  Easier to go by the PR number
> gh pr checkout PR_NUMBER
```

Then, if you only need to bump the version number as there are no other changes
required, you just need to get the hash for the new version, do this manually
by downloading the release tar or with spack by:

```
> spack checksum py-extra-geom
#  Enter how many versions you want to get checksums for
version('0.10.0', sha256='01d1bb2edf5c6b624f3d598833e2729fe108f53991e2a9c58588ae0719295a10'
```

And copy/paste the new version into the relevant `package.py` file, in this case
`packages/py-extra-geom/package.py`. Commit the changes, push them, and then if
the tests pass on the PR merge to master.

### PR Checklist:

- Add new package to `.docker/opt/spack/etc/spack/packages.yaml`
- If it is a python package, also add `.github/dependabot/requirements.txt`
- Rebuild Docker container so that new dependencies are added *
- Add package to status table in readme

\* To really speed up the container build it should include all of the **test
  dependencies** as well, however there currently is no way to install a package
  through spack with the test dependencies and without running tests
  (https://github.com/spack/spack/issues/21647). A workaround for this is to
  temporarily comment out all of the tests in our packages, build the image so
  that the tests do not run but so that the dependencies are included, push the
  updated image, and then revert the packages to their original versions.

## TODO

- Scheduled tests?
