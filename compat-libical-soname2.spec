#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-libical-soname2
Version  : 2.0.0
Release  : 2
URL      : https://github.com/libical/libical/archive/v2.0.0.tar.gz
Source0  : https://github.com/libical/libical/archive/v2.0.0.tar.gz
Summary  : An implementation of basic iCAL protocols
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: compat-libical-soname2-lib
BuildRequires : cmake

%description
Arnout Engelen pointed out, that you could create a php libical wrapper:
PHP currently seems to lack proper iCalendar libraries.
Since there already is a LibicalWrap.i for the Python
bindings, it's not very hard to make a libical .so that
can be accessed from PHP. Would be a valuable building
block in the practical adoption of the iCalendar
standard (imho).

%package dev
Summary: dev components for the compat-libical-soname2 package.
Group: Development
Requires: compat-libical-soname2-lib
Provides: compat-libical-soname2-devel

%description dev
dev components for the compat-libical-soname2 package.


%package lib
Summary: lib components for the compat-libical-soname2 package.
Group: Libraries

%description lib
lib components for the compat-libical-soname2 package.


%prep
%setup -q -n libical-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509297617
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1509297617
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
%exclude /usr/lib64/cmake/LibIcal/LibIcalConfig.cmake
%exclude /usr/lib64/cmake/LibIcal/LibIcalConfigVersion.cmake
%exclude /usr/lib64/cmake/LibIcal/LibIcalTargets-relwithdebinfo.cmake
%exclude /usr/lib64/cmake/LibIcal/LibIcalTargets.cmake

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/libical/ical.h
%exclude /usr/include/libical/icalarray.h
%exclude /usr/include/libical/icalattach.h
%exclude /usr/include/libical/icalcalendar.h
%exclude /usr/include/libical/icalclassify.h
%exclude /usr/include/libical/icalcluster.h
%exclude /usr/include/libical/icalcomponent.h
%exclude /usr/include/libical/icalderivedparameter.h
%exclude /usr/include/libical/icalderivedproperty.h
%exclude /usr/include/libical/icalderivedvalue.h
%exclude /usr/include/libical/icaldirset.h
%exclude /usr/include/libical/icaldirsetimpl.h
%exclude /usr/include/libical/icalduration.h
%exclude /usr/include/libical/icalenums.h
%exclude /usr/include/libical/icalerror.h
%exclude /usr/include/libical/icalfileset.h
%exclude /usr/include/libical/icalfilesetimpl.h
%exclude /usr/include/libical/icalgauge.h
%exclude /usr/include/libical/icalgaugeimpl.h
%exclude /usr/include/libical/icallangbind.h
%exclude /usr/include/libical/icalmemory.h
%exclude /usr/include/libical/icalmessage.h
%exclude /usr/include/libical/icalmime.h
%exclude /usr/include/libical/icalparameter.h
%exclude /usr/include/libical/icalparameter_cxx.h
%exclude /usr/include/libical/icalparser.h
%exclude /usr/include/libical/icalperiod.h
%exclude /usr/include/libical/icalproperty.h
%exclude /usr/include/libical/icalproperty_cxx.h
%exclude /usr/include/libical/icalrecur.h
%exclude /usr/include/libical/icalrestriction.h
%exclude /usr/include/libical/icalset.h
%exclude /usr/include/libical/icalspanlist.h
%exclude /usr/include/libical/icalspanlist_cxx.h
%exclude /usr/include/libical/icalss.h
%exclude /usr/include/libical/icalssyacc.h
%exclude /usr/include/libical/icaltime.h
%exclude /usr/include/libical/icaltimezone.h
%exclude /usr/include/libical/icaltypes.h
%exclude /usr/include/libical/icaltz-util.h
%exclude /usr/include/libical/icalvalue.h
%exclude /usr/include/libical/icalvalue_cxx.h
%exclude /usr/include/libical/icalvcal.h
%exclude /usr/include/libical/icptrholder_cxx.h
%exclude /usr/include/libical/libical_ical_export.h
%exclude /usr/include/libical/libical_icalss_export.h
%exclude /usr/include/libical/libical_vcal_export.h
%exclude /usr/include/libical/pvl.h
%exclude /usr/include/libical/sspm.h
%exclude /usr/include/libical/vcaltmp.h
%exclude /usr/include/libical/vcc.h
%exclude /usr/include/libical/vcomponent_cxx.h
%exclude /usr/include/libical/vobject.h
%exclude /usr/lib64/libical.so
%exclude /usr/lib64/libical_cxx.so
%exclude /usr/lib64/libicalss.so
%exclude /usr/lib64/libicalss_cxx.so
%exclude /usr/lib64/libicalvcal.so
%exclude /usr/lib64/pkgconfig/libical.pc

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
