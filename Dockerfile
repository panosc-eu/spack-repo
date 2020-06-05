FROM spack/centos7:latest

COPY ./.github/spack-config/* /opt/spack/etc/spack/
COPY ./ /spack-repo

WORKDIR /opt/spack/etc/spack/
RUN spack repo add --scope=site /spack-repo
RUN spack install --only=dependencies
#  In case `--only=dependencies` accidentally installs a package we want to test
#  we find all the explicitly installed packages and uninstall them
RUN for p in $(spack find -xc --no-groups | grep @); do spack uninstall --force -y $p; done; exit 0
#  Remove the repo as it would conflict with the tests
RUN spack repo remove euxfel-repo
#  Remove environment as it is not needed anymore
RUN rm -f spack.lock spack.yaml
#  Install some common test packages here
RUN spack install py-coverage py-pytest py-pytest-cov py-testpath py-mock
