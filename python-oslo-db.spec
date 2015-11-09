# Created by pyp2rpm-1.1.0b
%global pypi_name oslo.db

Name:           python-oslo-db
Version:        XXX
Release:        XXX
Summary:        OpenStack oslo.db library

License:        ASL 2.0
URL:            http://launchpad.net/oslo
Source0:        https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr

Requires:       MySQL-python
Requires:       python-oslo-config >= 2:2.3.0
Requires:       python-oslo-context >= 0.2.0
Requires:       python-oslo-i18n >= 1.5.0
Requires:       python-oslo-utils >= 2.0.0
Requires:       python-alembic >= 0.8.0
Requires:       python-babel
Requires:       python-iso8601
Requires:       python-migrate >= 0.9.6
Requires:       python-six >= 1.9.0
Requires:       python-sqlalchemy >= 0.9.9
Requires:       python-stevedore >= 1.5.0


%description
The OpenStack Oslo database handling library. Provides database connectivity
to the different backends and helper utils.
* Documentation: http://docs.openstack.org/developer/oslo.db
* Source: http://git.openstack.org/cgit/openstack/oslo.db
* Bugs: http://bugs.launchpad.net/oslo


%package doc
Summary:    Documentation for the Oslo database handling library
Group:      Documentation

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslo-utils
BuildRequires:  python-oslo-config
BuildRequires:  python-six
BuildRequires:  python-alembic
BuildRequires:  python-fixtures
BuildRequires:  python-migrate
BuildRequires:  python-testresources
BuildRequires:  python-testscenarios

%description doc
Documentation for the Oslo database handling library.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}

# Let RPM handle the dependencies
rm -f requirements.txt


%build
%{__python2} setup.py build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst LICENSE
%{python2_sitelib}/oslo_db
%{python2_sitelib}/*.egg-info

%files doc
%doc html LICENSE

%changelog