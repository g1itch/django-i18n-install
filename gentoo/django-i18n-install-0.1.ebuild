# Copyright 2014 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header$

EAPI=5
PYTHON_COMPAT=( python{2_7,3_3,3_4} )

inherit distutils-r1

DESCRIPTION="A helper to run django compilemessages command before install"
HOMEPAGE="https://github.com/g1itch/${PN}"
SRC_URI="${HOMEPAGE}/archive/${PV}.tar.gz -> ${P}.tar.gz"

LICENSE="BSD"
SLOT="0"
KEYWORDS="~x86 ~amd64 ~x86-fbsd"
RESTRICT="nomirror"

DEPEND=">=dev-python/setuptools-0.7"
RDEPEND="dev-python/django"
