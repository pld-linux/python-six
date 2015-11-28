#
# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module

%define 	module	six
Summary:	Six - Python 2 and 3 Compatibility Library (Python 2 module)
Summary(pl.UTF-8):	Biblioteka kompatybilności między Pythonem 2 i 3 (moduł Pythona 2)
Name:		python-%{module}
Version:	1.10.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/six/
Source0:	https://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz
# Source0-md5:	34eed507548117b2ab523ab14b2f8b55
URL:		http://pythonhosted.org/six/
%if %{with python2}
BuildRequires:	python >= 1:2.4
BuildRequires:	python-modules >= 1:2.4
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Six provides simple utilities for wrapping over differences between
Python 2 and Python 3. It is intended to support codebases that work
on both Python 2 and 3 without modification. six consists of only one
Python file, so it is painless to copy into a project.

This package contains Python 2 module.

%description -l pl.UTF-8
Six dostarcza proste narzędzia obudowujące różnice między Pythonem 2 a
Pythonem 3. Celem jest wsparcie kodu działającego zarówno z Pythonem 2
jak i 3 bez modyfikacji. six składa się z tylko jednego pliku
pythonowego, więc można go bezproblemowo skopiować do projektu.

Ten pakiet zawiera moduł Pythona 2.

%package -n python3-%{module}
Summary:	Six - Python 2 and 3 Compatibility Library (Python 3 module)
Summary(pl.UTF-8):	Biblioteka kompatybilności między Pythonem 2 i 3 (moduł Pythona 3)
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Six provides simple utilities for wrapping over differences between
Python 2 and Python 3. It is intended to support codebases that work
on both Python 2 and 3 without modification. six consists of only one
Python file, so it is painless to copy into a project.

This package contains Python 3 module.

%description -n python3-%{module} -l pl.UTF-8
Six dostarcza proste narzędzia obudowujące różnice między Pythonem 2 a
Pythonem 3. Celem jest wsparcie kodu działającego zarówno z Pythonem 2
jak i 3 bez modyfikacji. six składa się z tylko jednego pliku
pythonowego, więc można go bezproblemowo skopiować do projektu.

Ten pakiet zawiera moduł Pythona 3.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES README documentation/*.rst
%{py_sitescriptdir}/six.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/six-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES README documentation/*.rst
%{py3_sitescriptdir}/six.py
%{py3_sitescriptdir}/__pycache__/six.*.py[co]
%{py3_sitescriptdir}/six-%{version}-py*.egg-info
%endif
