#
# TODO
# tests broken:
#  - AttributeError: 'module' object has no attribute 'will_cause_import_error'

# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		subver	a7
%define		rel		1
%define 	module	venusian
Summary:	A library for deferring decorator actions
Name:		python-%{module}
Version:	1.0
Release:	0.%{subver}.%{rel}
License:	BSD-derived (http://www.repoze.org/LICENSE.txt)
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/v/venusian/%{module}-%{version}%{subver}.tar.gz
# Source0-md5:	6f67506dd3cf77116f1c01682a6c3f27
URL:		http://docs.pylonsproject.org/projects/venusian/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Venusian is a library which allows you to defer the action of
decorators.

Instead of taking actions when a function, method, or class decorator
is executed at import time, you can defer the action until a separate
"scan" phase.

%description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}%{subver}

%build
%{__python} setup.py build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests

# change %{py_sitescriptdir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}/compat
%{py_sitescriptdir}/%{module}-%{version}*.egg-info
