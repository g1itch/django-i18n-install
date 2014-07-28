# -*- coding: utf-8 -*-
# $Id$

import os
from distutils.errors import DistutilsError
from setuptools import Command
import setuptools.command.install as orig


class django_compilemessages(Command):
    description = "run django management command 'compilemessages'"
    command_consumes_arguments = False
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            from django.core import management
        except ImportError:
            raise DistutilsError(
                "Cannot run compilemessages because Django is not installed.")

        build_cmd = self.get_finalized_command('build_py')
        setup_dir = os.path.abspath(os.curdir)
        for package in self.distribution.packages:
            package_dir = build_cmd.get_package_dir(package)
            if os.path.exists(os.path.join(package_dir, 'locale')):
                try:
                    os.chdir(package_dir)
                    management.call_command('compilemessages')
                finally:
                    os.chdir(setup_dir)


class install(orig.install):
    def run(self):
        self.run_command('django_compilemessages')
        return orig.install.run(self)
