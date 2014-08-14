%global pypi_name oslo.db

Name:           python-oslo-db
Version:        XXX
Release:        1%{?dist}
Summary:        Oslo db

License:        ASL 2.0
URL:            https://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr


%description
oslo.db library

%prep
%setup -q -n oslo.db-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%dir %{python_sitelib}/oslo
%{python_sitelib}/oslo/db
%{python_sitelib}/oslo.db-%{version}*

%changelog
* Thu Aug 14 2014 Derek Higgins <derekh@redhat.com> - XXX
- Don't remove the bundled egg-info

* Fri Aug 01 2014 Derek Higgins <derekh@redhat.com> - XXX
- Initial package.
