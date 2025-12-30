Summary:	PEP 621 metadata parsing
Name:		python-pyproject_metadata
Version:	0.7.1
Release:	3
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pyproject_metadata/
Source0:	https://pypi.io/packages/source/p/pyproject_metadata/pyproject-metadata-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{py_ver}dist(setuptools)
BuildRequires:	python%{py_ver}dist(wheel)
BuildArch:	noarch

%description
Dataclass for PEP 621 metadata with support for core metadata generation

This project does not implement the parsing of pyproject.toml containing PEP
621 metadata.

Instead, given a Python data structure representing PEP 621 metadata (already
parsed), it will validate this input and generate a PEP 643-compliant metadata
file (e.g. PKG-INFO).

%files
%{py_sitedir}/pyproject_metadata
%{py_sitedir}/pyproject_metadata-*.*-info

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n pyproject-metadata-%{version}

%build
%py_build

%install
%py_install

