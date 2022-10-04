#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x43EC92504F71955A (dave@dajobe.org)
#
Name     : raptor2
Version  : 2.0.15
Release  : 6
URL      : http://download.librdf.org/source/raptor2-2.0.15.tar.gz
Source0  : http://download.librdf.org/source/raptor2-2.0.15.tar.gz
Source1  : http://download.librdf.org/source/raptor2-2.0.15.tar.gz.asc
Summary  : RDF Syntax Library
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 LGPL-2.1
Requires: raptor2-bin = %{version}-%{release}
Requires: raptor2-lib = %{version}-%{release}
Requires: raptor2-license = %{version}-%{release}
Requires: raptor2-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : docbook-xml
BuildRequires : flex
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : icu4c-dev
BuildRequires : libxml2
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : libxslt-bin
BuildRequires : libxslt-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : xz-dev
BuildRequires : yajl-dev
BuildRequires : zlib-dev
Patch1: CVE-2017-18926.patch

%description
#DOAP
Raptor RDF Syntax Library
Dave Beckett
Overview
Raptor is a free software / Open Source C library that provides a set
of parsers and serializers that generate Resource Description Framework
(RDF) triples by parsing syntaxes or serialize the triples into a
syntax. The supported parsing syntaxes are RDF/XML, N-Quads, N-Triples
1.0 and 1.1, TRiG, Turtle 2008 and 2013, RDFa 1.0 and 1.1, RSS tag soup
including all versions of RSS, Atom 1.0 and 0.3, GRDDL and microformats
for HTML, XHTML and XML. The serializing syntaxes are RDF/XML (regular,
abbreviated, XMP), Turtle 2013, N-Quads, N-Triples 1.1, Atom 1.0, RSS
1.0, GraphViz DOT, HTML and JSON.

%package bin
Summary: bin components for the raptor2 package.
Group: Binaries
Requires: raptor2-license = %{version}-%{release}

%description bin
bin components for the raptor2 package.


%package dev
Summary: dev components for the raptor2 package.
Group: Development
Requires: raptor2-lib = %{version}-%{release}
Requires: raptor2-bin = %{version}-%{release}
Provides: raptor2-devel = %{version}-%{release}
Requires: raptor2 = %{version}-%{release}

%description dev
dev components for the raptor2 package.


%package doc
Summary: doc components for the raptor2 package.
Group: Documentation
Requires: raptor2-man = %{version}-%{release}

%description doc
doc components for the raptor2 package.


%package lib
Summary: lib components for the raptor2 package.
Group: Libraries
Requires: raptor2-license = %{version}-%{release}

%description lib
lib components for the raptor2 package.


%package license
Summary: license components for the raptor2 package.
Group: Default

%description license
license components for the raptor2 package.


%package man
Summary: man components for the raptor2 package.
Group: Default

%description man
man components for the raptor2 package.


%prep
%setup -q -n raptor2-2.0.15
cd %{_builddir}/raptor2-2.0.15
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664912502
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1664912502
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/raptor2
cp %{_builddir}/raptor2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/raptor2/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/raptor2-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/raptor2/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/raptor2-%{version}/LICENSE-2.0.txt %{buildroot}/usr/share/package-licenses/raptor2/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/raptor2-%{version}/LICENSE.html %{buildroot}/usr/share/package-licenses/raptor2/03c4dbd3651cbaa98383f73b4d008e47f0e289cd || :
cp %{_builddir}/raptor2-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/raptor2/19aba05b5b65bf9e591d8e129ac81af3b3e1152e || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rapper

%files dev
%defattr(-,root,root,-)
/usr/include/raptor2/raptor.h
/usr/include/raptor2/raptor2.h
/usr/lib64/libraptor2.so
/usr/lib64/pkgconfig/raptor2.pc
/usr/share/man/man3/libraptor2.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/raptor2/home.png
/usr/share/gtk-doc/html/raptor2/index.html
/usr/share/gtk-doc/html/raptor2/index.sgml
/usr/share/gtk-doc/html/raptor2/introduction.html
/usr/share/gtk-doc/html/raptor2/ix01.html
/usr/share/gtk-doc/html/raptor2/left.png
/usr/share/gtk-doc/html/raptor2/parser-grddl.html
/usr/share/gtk-doc/html/raptor2/parser-guess.html
/usr/share/gtk-doc/html/raptor2/parser-json.html
/usr/share/gtk-doc/html/raptor2/parser-ntriples.html
/usr/share/gtk-doc/html/raptor2/parser-rdfa.html
/usr/share/gtk-doc/html/raptor2/parser-rdfxml.html
/usr/share/gtk-doc/html/raptor2/parser-rss-tag-soup.html
/usr/share/gtk-doc/html/raptor2/parser-trig.html
/usr/share/gtk-doc/html/raptor2/parser-turtle.html
/usr/share/gtk-doc/html/raptor2/raptor-formats-types-by-parser.html
/usr/share/gtk-doc/html/raptor2/raptor-formats-types-by-serializer.html
/usr/share/gtk-doc/html/raptor2/raptor-formats-types-index.html
/usr/share/gtk-doc/html/raptor2/raptor-formats.html
/usr/share/gtk-doc/html/raptor2/raptor-parsers.html
/usr/share/gtk-doc/html/raptor2/raptor-serializers.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-1-4-21-to-2-0-0.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-10-to-2-0-11.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-11-to-2-0-12.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-13-to-2-0-14.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-14-to-2-0-15.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-3-to-2-0-4.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-4-to-2-0-5.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-5-to-2-0-6.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-6-to-2-0-7.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-7-to-2-0-8.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-9-to-2-0-10.html
/usr/share/gtk-doc/html/raptor2/raptor2-changes.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-avltree.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-constants.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-general.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-iostream.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-locator.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-memory.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-option.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-parser.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-sax2.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-sequence.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-serializer.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-stringbuffer.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-triples.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-unicode.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-uri.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-world.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-www.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-xml-namespace.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-xml-qname.html
/usr/share/gtk-doc/html/raptor2/raptor2-section-xml.html
/usr/share/gtk-doc/html/raptor2/raptor2.devhelp2
/usr/share/gtk-doc/html/raptor2/reference-manual.html
/usr/share/gtk-doc/html/raptor2/restrict-parser-network-access.html
/usr/share/gtk-doc/html/raptor2/right.png
/usr/share/gtk-doc/html/raptor2/serializer-atom.html
/usr/share/gtk-doc/html/raptor2/serializer-dot.html
/usr/share/gtk-doc/html/raptor2/serializer-json.html
/usr/share/gtk-doc/html/raptor2/serializer-nquads.html
/usr/share/gtk-doc/html/raptor2/serializer-ntriples.html
/usr/share/gtk-doc/html/raptor2/serializer-rdfxml-abbrev.html
/usr/share/gtk-doc/html/raptor2/serializer-rdfxml-xmp.html
/usr/share/gtk-doc/html/raptor2/serializer-rdfxml.html
/usr/share/gtk-doc/html/raptor2/serializer-rss-1-0.html
/usr/share/gtk-doc/html/raptor2/serializer-turtle.html
/usr/share/gtk-doc/html/raptor2/style.css
/usr/share/gtk-doc/html/raptor2/tutorial-initialising-finishing.html
/usr/share/gtk-doc/html/raptor2/tutorial-parse-strictness.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-abort.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-content.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-create.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-destroy.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-example.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-features.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-runtime-info.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-set-error-warning-handlers.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-set-id-handler.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-set-namespace-handler.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-set-triple-handler.html
/usr/share/gtk-doc/html/raptor2/tutorial-parser-static-info.html
/usr/share/gtk-doc/html/raptor2/tutorial-parsing.html
/usr/share/gtk-doc/html/raptor2/tutorial-querying-functionality.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-create.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-declare-namespace.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-destroy.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-example.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-features.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-get-triples.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-runtime-info.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-send-triples.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-set-error-warning-handlers.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializer-to-destination.html
/usr/share/gtk-doc/html/raptor2/tutorial-serializing.html
/usr/share/gtk-doc/html/raptor2/tutorial.html
/usr/share/gtk-doc/html/raptor2/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libraptor2.so.0
/usr/lib64/libraptor2.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/raptor2/03c4dbd3651cbaa98383f73b4d008e47f0e289cd
/usr/share/package-licenses/raptor2/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/raptor2/19aba05b5b65bf9e591d8e129ac81af3b3e1152e
/usr/share/package-licenses/raptor2/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/raptor2/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rapper.1
