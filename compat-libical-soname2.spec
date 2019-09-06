#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-libical-soname2
Version  : 2.0.0
Release  : 8
URL      : https://github.com/libical/libical/archive/v2.0.0.tar.gz
Source0  : https://github.com/libical/libical/archive/v2.0.0.tar.gz
Summary  : An implementation of basic iCAL protocols
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: compat-libical-soname2-lib = %{version}-%{release}
Requires: compat-libical-soname2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : doxygen
BuildRequires : icu4c-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(gobject-introspection-1.0)
# Suppress generation of debuginfo
%global debug_package %{nil}
Patch1: CVE-2016-9584.patch

%description
Arnout Engelen pointed out, that you could create a php libical wrapper:
PHP currently seems to lack proper iCalendar libraries.
Since there already is a LibicalWrap.i for the Python
bindings, it's not very hard to make a libical .so that
can be accessed from PHP. Would be a valuable building
block in the practical adoption of the iCalendar
standard (imho).

%package lib
Summary: lib components for the compat-libical-soname2 package.
Group: Libraries
Requires: compat-libical-soname2-license = %{version}-%{release}

%description lib
lib components for the compat-libical-soname2 package.


%package license
Summary: license components for the compat-libical-soname2 package.
Group: Default

%description license
license components for the compat-libical-soname2 package.


%prep
%setup -q -n libical-2.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567813031
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567813031
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-libical-soname2
cp COPYING %{buildroot}/usr/share/package-licenses/compat-libical-soname2/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/compat-libical-soname2/LICENSE
cp debian/copyright %{buildroot}/usr/share/package-licenses/compat-libical-soname2/debian_copyright
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/lib64/cmake/LibIcal/LibIcalConfig.cmake
rm -f %{buildroot}/usr/lib64/cmake/LibIcal/LibIcalConfigVersion.cmake
rm -f %{buildroot}/usr/lib64/cmake/LibIcal/LibIcalTargets-relwithdebinfo.cmake
rm -f %{buildroot}/usr/lib64/cmake/LibIcal/LibIcalTargets.cmake
rm -f %{buildroot}/usr/include/libical/ical.h
rm -f %{buildroot}/usr/include/libical/icalarray.h
rm -f %{buildroot}/usr/include/libical/icalattach.h
rm -f %{buildroot}/usr/include/libical/icalcalendar.h
rm -f %{buildroot}/usr/include/libical/icalclassify.h
rm -f %{buildroot}/usr/include/libical/icalcluster.h
rm -f %{buildroot}/usr/include/libical/icalcomponent.h
rm -f %{buildroot}/usr/include/libical/icalderivedparameter.h
rm -f %{buildroot}/usr/include/libical/icalderivedproperty.h
rm -f %{buildroot}/usr/include/libical/icalderivedvalue.h
rm -f %{buildroot}/usr/include/libical/icaldirset.h
rm -f %{buildroot}/usr/include/libical/icaldirsetimpl.h
rm -f %{buildroot}/usr/include/libical/icalduration.h
rm -f %{buildroot}/usr/include/libical/icalenums.h
rm -f %{buildroot}/usr/include/libical/icalerror.h
rm -f %{buildroot}/usr/include/libical/icalfileset.h
rm -f %{buildroot}/usr/include/libical/icalfilesetimpl.h
rm -f %{buildroot}/usr/include/libical/icalgauge.h
rm -f %{buildroot}/usr/include/libical/icalgaugeimpl.h
rm -f %{buildroot}/usr/include/libical/icallangbind.h
rm -f %{buildroot}/usr/include/libical/icalmemory.h
rm -f %{buildroot}/usr/include/libical/icalmessage.h
rm -f %{buildroot}/usr/include/libical/icalmime.h
rm -f %{buildroot}/usr/include/libical/icalparameter.h
rm -f %{buildroot}/usr/include/libical/icalparameter_cxx.h
rm -f %{buildroot}/usr/include/libical/icalparser.h
rm -f %{buildroot}/usr/include/libical/icalperiod.h
rm -f %{buildroot}/usr/include/libical/icalproperty.h
rm -f %{buildroot}/usr/include/libical/icalproperty_cxx.h
rm -f %{buildroot}/usr/include/libical/icalrecur.h
rm -f %{buildroot}/usr/include/libical/icalrestriction.h
rm -f %{buildroot}/usr/include/libical/icalset.h
rm -f %{buildroot}/usr/include/libical/icalspanlist.h
rm -f %{buildroot}/usr/include/libical/icalspanlist_cxx.h
rm -f %{buildroot}/usr/include/libical/icalss.h
rm -f %{buildroot}/usr/include/libical/icalssyacc.h
rm -f %{buildroot}/usr/include/libical/icaltime.h
rm -f %{buildroot}/usr/include/libical/icaltimezone.h
rm -f %{buildroot}/usr/include/libical/icaltypes.h
rm -f %{buildroot}/usr/include/libical/icaltz-util.h
rm -f %{buildroot}/usr/include/libical/icalvalue.h
rm -f %{buildroot}/usr/include/libical/icalvalue_cxx.h
rm -f %{buildroot}/usr/include/libical/icalvcal.h
rm -f %{buildroot}/usr/include/libical/icptrholder_cxx.h
rm -f %{buildroot}/usr/include/libical/libical_ical_export.h
rm -f %{buildroot}/usr/include/libical/libical_icalss_export.h
rm -f %{buildroot}/usr/include/libical/libical_vcal_export.h
rm -f %{buildroot}/usr/include/libical/pvl.h
rm -f %{buildroot}/usr/include/libical/sspm.h
rm -f %{buildroot}/usr/include/libical/vcaltmp.h
rm -f %{buildroot}/usr/include/libical/vcc.h
rm -f %{buildroot}/usr/include/libical/vcomponent_cxx.h
rm -f %{buildroot}/usr/include/libical/vobject.h
rm -f %{buildroot}/usr/lib64/libical.so
rm -f %{buildroot}/usr/lib64/libical_cxx.so
rm -f %{buildroot}/usr/lib64/libicalss.so
rm -f %{buildroot}/usr/lib64/libicalss_cxx.so
rm -f %{buildroot}/usr/lib64/libicalvcal.so
rm -f %{buildroot}/usr/lib64/pkgconfig/libical.pc

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libical.so.2
/usr/lib64/libical.so.2.0.0
/usr/lib64/libical_cxx.so.2
/usr/lib64/libical_cxx.so.2.0.0
/usr/lib64/libicalss.so.2
/usr/lib64/libicalss.so.2.0.0
/usr/lib64/libicalss_cxx.so.2
/usr/lib64/libicalss_cxx.so.2.0.0
/usr/lib64/libicalvcal.so.2
/usr/lib64/libicalvcal.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-libical-soname2/COPYING
/usr/share/package-licenses/compat-libical-soname2/LICENSE
/usr/share/package-licenses/compat-libical-soname2/debian_copyright
