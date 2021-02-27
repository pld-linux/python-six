#
# Conditional build:
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module
%bcond_without	tests		# unit tests
%bcond_without	doc		# Sphinx documentation
%bcond_without	setuptools	# build without setuptools (for bootstraping)

%define 	module	six
Summary:	Six - Python 2 and 3 Compatibility Library (Python 2 module)
Summary(pl.UTF-8):	Biblioteka kompatybilności między Pythonem 2 i 3 (moduł Pythona 2)
Name:		python-%{module}
Version:	1.15.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/six/
Source0:	https://files.pythonhosted.org/packages/source/s/six/six-%{version}.tar.gz
# Source0-md5:	9f90a0eaa0ea7747fda01ca79d21ebcb
Patch0:		%{name}-tests.patch
URL:		https://pypi.org/project/six/
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
%{?with_setuptools:BuildRequires:	python-setuptools}
%if %{with tests}
BuildRequires:	python-pytest >= 2.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
%{?with_setuptools:BuildRequires:	python3-setuptools}
%if %{with tests}
BuildRequires:	python3-pytest >= 2.2.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg >= 1.0
%endif
Requires:	python-modules >= 1:2.7
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
Requires:	python3-modules >= 1:3.3

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

%package apidocs
Summary:	Documentation for Python six module
Summary(pl.UTF-8):	Dokumentacja modułu Pythona six
Group:		Documentation

%description apidocs
Documentation for Python six module.

%description apidocs -l pl.UTF-8
Dokumentacja modułu Pythona six.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python} -m pytest test_six.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} -m pytest test_six.py
%endif
%endif

%if %{with doc}
%{__make} -C documentation html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

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
%doc CHANGES LICENSE README.rst
%{py_sitescriptdir}/six.py[co]
%{py_sitescriptdir}/six-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/six.py
%{py3_sitescriptdir}/__pycache__/six.*.py[co]
%{py3_sitescriptdir}/six-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc documentation/_build/html/{_static,*.html,*.js}
%endif
