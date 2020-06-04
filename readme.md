## Package status:

- [ ] crystfel
- [ ] py-cfelpyutils
- [ ] py-extra-data
- [ ] py-extra-geom - dep on py-fabio
- [ ] py-fabio - complex setup
- [ ] py-karabo-bridge
- [x] py-msgpack-numpy
- [ ] py-pyfai
- [ ] py-pyopengl

## Plan

1. Create a docker image based on spack/centos7 which has python pre-installed
2. Set up GitHub actions to run a basic tests where all the packages in this
   repo are installed and tested in the docker image
3. Use fancier actions, something like [File Changes Action](https://github.com/marketplace/actions/file-changes-action),
   [Get All Changed Files](https://github.com/marketplace/actions/get-all-changed-files),
   [stackoverflow example](https://stackoverflow.com/questions/59288971/retrieving-list-of-modified-files-in-github-action)
   to run the tests individually on each package only when it's modified
4. *fantasy land* have actions trigger, per-package, whenever a new tag for that
   package has been released

## Docker Image

Building the packages from scratch to perform the tests would take a very long
time, so a special `spack-repo-testenv` docker image is used for the tests.

Spack has an option to install `--only=dependencies`, which lets us install all
of the dependencies of our packages into the image first, and then the tests
only need to install our packages, which massively cuts down on the time.

TODO: Verify what happens when you have a spec in an environment which contains
a dependency that is also in our environment, e.g. we define `py-msgpack-python`
here, but that is a dependency for some of our other packages, does it get built
as it technically is a depencency, or does it get excluded? If it is still built,
we can run a final pass of `spack uninstall ...` to make sure that all the
packages we want to test are not pre-installed in the image.
