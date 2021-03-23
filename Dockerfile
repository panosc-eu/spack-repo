FROM spack/centos7@sha256:5718b3db32a073cfebb78a3e16cfbbfb3a0c44131a0bd7e1385ee36b01db8066 AS core
#  Copy over our configurations
COPY .docker/. /.
COPY ./ /opt/spack/etc/spack/panosc-eu-repo
WORKDIR /opt/spack/etc/spack/
#  Set up E4S buildcache, this is used to speed up the installation of standard
#  packages like python and gcc
#  https://spack.readthedocs.io/en/latest/binary_caches.html#list-of-popular-build-caches
#  https://oaciss.uoregon.edu/e4s/inventory.html
#  https://e4s-project.github.io/
RUN yum install -y wget python3
#  Tried compiling newer version of gnugpg to fix the installation issue
#  mentioned below, this did not help...
# RUN curl -OL "https://gist.githubusercontent.com/simbo1905/ba3e8af9a45435db6093aea35c6150e8/raw/83561e214e36f6556fd6b1ec0a384cf28cb2debf/install-gnupg22.sh" && bash ./install-gnupg22.sh
RUN wget https://oaciss.uoregon.edu/e4s/e4s.pub
RUN spack gpg trust e4s.pub
RUN spack mirror add E4S https://cache.e4s.io
#  Install and set up GCC 8.1.0 - cache only
##  For some reason I've given up trying to figure out the first install call
##  fails, so here it's done twice. This seems to be a GPG issue but fixing it
##  is beyond me
##  Time wasted on this: 3 hours 5 minutes
RUN spack install --cache-only --file /opt/spack/etc/spack/specs/linux-centos7-x86_64-gcc-4.8.5-gcc-8.1.0-xwu6n6d5wz2slcestvpcba6hy5o6ypys.spec.yaml
RUN spack install --cache-only --file /opt/spack/etc/spack/specs/linux-centos7-x86_64-gcc-4.8.5-gcc-8.1.0-xwu6n6d5wz2slcestvpcba6hy5o6ypys.spec.yaml
RUN spack compiler find --scope=system $(spack location --install-dir gcc@8.1.0)
#  Install python 3.7.8
RUN spack install --cache-only --file /opt/spack/etc/spack/specs/linux-centos7-x86_64-gcc-8.1.0-python-3.7.8-ruvk2ilh4xbu3hpaeptwonpy54qtvbwi.spec.yaml
RUN spack find

FROM core
WORKDIR /opt/spack/etc/spack/
RUN spack repo add --scope=site /opt/spack/etc/spack/panosc-eu-repo
#  Parallel installation of the dependencies defined in
#  `.github/spack-config/spack.yaml`
RUN spack-parallel spack --env . install --test=root --only=dependencies
#  In case `--only=dependencies` accidentally installs a package we want to test
#  we find all the explicitly installed packages and uninstall them
RUN echo Uninstalling: && spack --env . find -xcl --no-groups
RUN for p in $(spack --env . find -xcl --no-groups | grep @ | cut -d' ' -f1); do spack --env . uninstall --force -y /$p; done || true
#  Remove the repo as it would conflict with the tests
RUN spack repo remove --scope=site panosc-eu-repo
#  Install some common test packages here
RUN spack install py-coverage py-pytest py-pytest-cov py-testpath py-mock
