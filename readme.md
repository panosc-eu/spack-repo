#  EuXFEL Spack Repository

Repository of Spack packages used at EuXFEL.

This contains an early attempt to run CI tests on the package files themselves
to ensure that the created packages run correctly. The CI is based on GitHub
Workflows and Actions, and runs using a Docker container which contains all
dependencies required for the packages being tested to be installed to save on
build times.

## Package status:

| package          | status                                                                                                                  | repo-deps                  | notes |
|------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------|-------|
| crystfel         | ![](https://github.com/robertrosca/spack-repo/workflows/.github/workflows/package-test.crystfel.yaml/badge.svg)         |                            | wip   |
| py-cfelpyutils   | ![](https://github.com/robertrosca/spack-repo/workflows/.github/workflows/package-test.py-cfelpyutils.yaml/badge.svg)  |                             | wip   |
| py-extra-data    | ![](https://github.com/robertrosca/spack-repo/workflows/.github/workflows/package-test.py-extra-data.yaml/badge.svg)    | py-karabo-bridge, py-fabio | wip   |
| py-extra-geom    | ![](https://github.com/robertrosca/spack-repo/workflows/.github/workflows/package-test.py-extra-geom.yaml/badge.svg)    | py-cfelpyutils             | wip   |
| py-fabio         | ![](https://github.com/robertrosca/spack-repo/workflows/.github/workflows/package-test.py-fabio.yaml/badge.svg)         |                            | wip   |
| py-karabo-bridge | ![](https://github.com/robertrosca/spack-repo/workflows/.github/workflows/package-test.py-karabo-bridge.yaml/badge.svg) | py-msgpack-numpy           | wip   |
| py-msgpack-numpy | ![](https://github.com/robertrosca/spack-repo/workflows/.github/workflows/package-test.py-msgpack-numpy.yaml/badge.svg) |                            | wip   |
| py-pyfai         | ![](https://github.com/robertrosca/spack-repo/workflows/.github/workflows/package-test.py-pyfai.yaml/badge.svg)         | py-fabio, py-hdf5plugin    | wip   |

## Notes

### CI

CI runs on GitHub Workflows. There is a file `.github/generate-workflows.py`
which uses a template workflow `.github/template/package-test.template.yaml`
file to generate a workflow for each of the packages in this repo.

The workflows run only when their respective package files change, which means
that tests are not re-ran if a dependency changes, only if the package file
changes.

Workflows run in a docker container `roscarxfel/spack-repo-testenv:latest` which
is covered in a different sections.

Workflows run the following commands:

```
source /opt/spack/share/spack/setup-env.sh
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

### PR Checklist:

- Add new package to `.github/spack-config/spack.yaml`
- Rebuild Docker container so that new dependencies are added
- Add package to status table in readme

## Notes

GitHub Workflows are cool for a few reasons, but one reason alone makes them
amazing: act https://github.com/nektos/act

It lets you run the workflows locally. For example, run `act -b` in the root of
this repo to run all the workflows, or for a specific workflow use `-j` to set
the job, e.g. `act -b -j package-test-py-extra-data`

## TODO

- Scheduled tests?
- Dependabot integration?
