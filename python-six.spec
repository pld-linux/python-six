# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module

%define 	module	six
Summary:	Six – Python 2 and 3 Compatibility Library
Summary(pl.UTF-8):	Biblioteka kompatybilności między Pythonem 2 i 3
Name:		python-%{module}
Version:	1.3.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz
# Source0-md5:	ec47fe6070a8a64c802363d2c2b1e2ee
URL:		http://pythonhosted.org/six/
%if %{with python2}
BuildRequires:	python >= 1:2.4
BuildRequires:	python-modules
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-modules
Requires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Six provides simple utilities for wrapping over differences between
Python 2 and Python 3. It is intended to support codebases that work
on both Python 2 and 3 without modification. six consists of only one
Python file, so it is painless to copy into a project.

%package -n python3-%{module}
Summary:	Six – Python 2 and 3 Compatibility Library
Summary(pl.UTF-8):	Biblioteka kompatybilności między Pythonem 2 i 3
Group:		Libraries/Python

%description -n python3-%{module}
Six provides simple utilities for wrapping over differences between
Python 2 and Python 3. It is intended to support codebases that work
on both Python 2 and 3 without modification. six consists of only one
Python file, so it is painless to copy into a project.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2
%endif
%if %{with python3}
%{__python3} setup.py build --build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES README documentation/*.rst
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES README documentation/*.rst
%{py3_sitescriptdir}/*.py
%{py3_sitescriptdir}/__pycache__
%{py3_sitescriptdir}/*.egg-info
%endif
