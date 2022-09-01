%global debug_package %{nil}

Name: python-keyring
Epoch: 100
Version: 23.9.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Store and access your passwords safely
License: MIT
URL: https://github.com/jaraco/keyring/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The Python keyring library provides an easy way to access the system
keyring service from python. It can be used in any application that
needs safe password storage.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-keyring
Summary: Store and access your passwords safely
Requires: python3
Requires: python3-importlib-metadata >= 3.6
Requires: python3-jaraco.classes
Requires: python3-jeepney >= 0.4.2
Requires: python3-secretstorage >= 3.2
Provides: python3-keyring = %{epoch}:%{version}-%{release}
Provides: python3dist(keyring) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-keyring = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(keyring) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-keyring = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(keyring) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-keyring
The Python keyring library provides an easy way to access the system
keyring service from python. It can be used in any application that
needs safe password storage.

%files -n python%{python3_version_nodots}-keyring
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-keyring
Summary: Store and access your passwords safely
Requires: python3
Requires: python3-importlib-metadata >= 3.6
Requires: python3-jaraco.classes
Requires: python3-jeepney >= 0.4.2
Requires: python3-secretstorage >= 3.2
Provides: python3-keyring = %{epoch}:%{version}-%{release}
Provides: python3dist(keyring) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-keyring = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(keyring) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-keyring = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(keyring) = %{epoch}:%{version}-%{release}

%description -n python3-keyring
The Python keyring library provides an easy way to access the system
keyring service from python. It can be used in any application that
needs safe password storage.

%files -n python3-keyring
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-keyring
Summary: Store and access your passwords safely
Requires: python3
Requires: python3-importlib-metadata >= 3.6
Requires: python3-jaraco.classes
Requires: python3-jeepney >= 0.4.2
Requires: python3-secretstorage >= 3.2
Provides: python3-keyring = %{epoch}:%{version}-%{release}
Provides: python3dist(keyring) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-keyring = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(keyring) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-keyring = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(keyring) = %{epoch}:%{version}-%{release}

%description -n python3-keyring
The Python keyring library provides an easy way to access the system
keyring service from python. It can be used in any application that
needs safe password storage.

%files -n python3-keyring
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
