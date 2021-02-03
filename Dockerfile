FROM spack/centos7:latest

COPY ./.github/spack-config/* /opt/spack/etc/spack/
COPY ./ /opt/spack/etc/panosc-spack-repo

WORKDIR /opt/spack/etc/spack/
RUN spack repo add --scope=site /opt/spack/etc/panosc-spack-repo
#  In case `--only=dependencies` accidentally installs a package we want to test
#  we find all the explicitly installed packages and uninstall them
RUN for p in $(spack find -xc --no-groups | grep @); do spack uninstall --force -y $p; done; exit 0
#  Remove the repo as it would conflict with the tests
RUN spack repo remove panosc-spack-repo
#  Install some common test packages here
RUN spack install py-coverage py-pytest py-pytest-cov py-testpath py-mock
