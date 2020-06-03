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
