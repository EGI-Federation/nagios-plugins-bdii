Summary: Nagios Plugin - check_bdii_entries
Name: nagios-plugins-bdii
Version: 1.0.16
Release: 1%{?dist}
Source0: %{name}-%{version}.tar.gz
License: ASL 2.0
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: openldap-devel%{?_isa}
Requires: nagios-common
URL: https://github.com/EGI-Foundation/nagios-plugins-bdii

%description
Provides check_bdii_entries support for Nagios.

%prep
%setup -q

%build
CFLAGS='%{optflags}' make compile

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_bdii_entries
%{_defaultdocdir}/%{name}/LICENSE.txt

%clean
rm -rf %{buildroot}

%changelog
* Thu Jul 30 2020 Baptiste Grenier <baptiste.grenier@egi.eu> - 1.0.16-1%{?dist}
- Fix build and bump version
* Wed Aug 07 2013 Laurence Field <laurence.field@cern.ch> - 1.0.15-1%{?dist}
- Fix for Redhat bug 993990
* Thu Dec 08 2011 Laurence Field <laurence.field@cern.ch> - 1.0.14-1%{?dist}
- Added LICENSE file to binary
* Fri Dec 02 2011 Laurence Field <laurence.field@cern.ch> - 1.0.13-1%{?dist}
- Added LICENSE file to source
* Wed Nov 16 2011 Laurence Field <laurence.field@cern.ch> - 1.0.12-1%{?dist}
- Initial Release
