FROM spack/centos7:latest

COPY ./.ci-spack-config/* /opt/spack/etc/spack/*
COPY ./ /spack-repo

RUN /opt/spack/bin/spack repo add --scope=site /spack-repo
RUN cd /opt/spack/etc/spack/; /opt/spack/bin/spack install --only=dependencies
