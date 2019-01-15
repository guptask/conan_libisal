#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment
from conans.util import files
from conans import tools
import os

class LibisalConan(ConanFile):
    name = "isa-l"
    version = "2.21.0"
    description = "Intel's Intelligent Storage Acceleration Library"
    url = "https://github.com/bincrafters/conan-libisal"
    homepage = "https://github.com/01org/isa-l"
    license = "MIT"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = (
        "shared=False",
        "fPIC=True"
    )

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        os.rename("%s-%s" % (self.name, self.version), self.source_subfolder)

    def build(self):
        with tools.chdir(self.source_subfolder):
            self.run("./autogen.sh")
            files.mkdir("_build")
            with tools.chdir("_build"):
                env_build = AutoToolsBuildEnvironment(self)
                extra_args = list()
                if self.options.shared:
                    extra_args.extend(('--enable-static=no',))
                else:
                    extra_args.extend(('--enable-shared=no',))
                env_build.configure("../", args=extra_args, build=False, host=False, target=False)
                env_build.make()

    def package(self):
        self.copy("*/isa-l.h", dst="include", keep_path=False)
        self.copy("*/isa-l.h", dst="include/isa-l", keep_path=False)
        self.copy("*.h", dst="include/isa-l", src="%s/include" % (self.source_subfolder) , keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

    def configure(self):
        del self.settings.compiler.libcxx
