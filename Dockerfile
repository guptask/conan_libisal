# ##########   #######   ############
FROM ecr.vip.ebayc3.com/sds/sds_cpp_base:1.7
LABEL description="Automated SDS compilation"

ARG CONAN_CHANNEL
ARG CONAN_USER
ARG CONAN_PASS=${CONAN_USER}
ENV CONAN_USER=${CONAN_USER:-bincrafters}
ENV CONAN_CHANNEL=${CONAN_CHANNEL:-testing}
ENV CONAN_PASS=${CONAN_PASS:-password}
ENV SOURCE_PATH=/tmp/source/

COPY conanfile.py ${SOURCE_PATH}
COPY CMakeLists.txt ${SOURCE_PATH}
COPY test_package/ ${SOURCE_PATH}test_package
COPY lib_Makefile_add.am ${SOURCE_PATH}
COPY LICENSE.md ${SOURCE_PATH}

WORKDIR /output
RUN conan create -pr debug ${SOURCE_PATH} "${CONAN_USER}"/"${CONAN_CHANNEL}"
RUN conan create ${SOURCE_PATH} "${CONAN_USER}"/"${CONAN_CHANNEL}"

CMD set -eux; \
    eval $(grep 'name =' ${SOURCE_PATH}conanfile.py | sed 's, ,,g' | sed 's,name,PKG_NAME,'); \
    eval $(grep -m 1 'version =' ${SOURCE_PATH}conanfile.py | sed 's, ,,g' | sed 's,version,PKG_VERSION,'); \
    conan user -r origin -p "${CONAN_PASS}" sds; \
    conan upload ${PKG_NAME}/"${PKG_VERSION}"@"${CONAN_USER}"/"${CONAN_CHANNEL}" --all -r origin;
# ##########   #######   ############
