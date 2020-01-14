Summary: Service Management Client and CLI 
Name: sm-client
Version: 1.0
Release: %{tis_patch_ver}%{?_tis_dist}
License: Apache-2.0
Group: base
Packager: Wind River <info@windriver.com>
URL: unknown
Source0:          %{name}-%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-pip
BuildRequires: python3-wheel
Requires: python3-libs
Requires: python3-six
%prep
%setup -q

%build
%{__python3} setup.py build
%py3_build_wheel

%install
%global _buildsubdir %{_builddir}/%{name}-%{version}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
mkdir -p $RPM_BUILD_ROOT/wheels
install -m 644 dist/*.whl $RPM_BUILD_ROOT/wheels/
install -d %{buildroot}/usr/bin
install -m 755 %{_buildsubdir}/usr/bin/smc %{buildroot}/usr/bin

%description
Service Management Client and CLI 

#%package -n sm-client-py-src-tar
#Summary: Service Management Client and CLI source tarball 
#Group: base

#%description -n sm-client-py-src-tar
#Service Management API


#%post -n sm-client-py-src-tar
## sm-client-py-src-tar - postinst
#	if [ -f $D/usr/src/sm-client-1.0.tar.bz2 ] ; then
#		( cd $D/ && tar -xf $D/usr/src/sm-client-1.0.tar.bz2 )
#	fi


%files
%defattr(-,root,root,-)
%dir "%{python3_sitelib}/sm_client"
%{python3_sitelib}/sm_client/*
"/usr/bin/smc"
%dir "%{python3_sitelib}/sm_client-1.0.0-py3.6.egg-info"
%{python3_sitelib}/sm_client-1.0.0-py3.6.egg-info/*

#%files -n sm-client-py-src-tar
#%defattr(-,-,-,-)
#"/usr/src/sm-client-1.0.tar.bz2"

%package wheels
Summary: %{name} wheels

%description wheels
Contains python wheels for %{name}

%files wheels
/wheels/*
