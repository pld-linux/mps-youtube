%define		pypi_name	mps-youtube
%define		module		mps_youtube
%define		egg_name	mps_youtube
Summary:	Terminal-based YouTube player and downloader
Name:		mps-youtube
Version:	0.2.7.1
Release:	2
License:	GPL v3
Group:		Applications/Multimedia
Source0:	https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	6b834b25fab8f87378976f1a798044e0
URL:		https://github.com/mps-youtube/mps-youtube
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	desktop-file-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is based on mps, a terminal based program to search,
stream and download music. This implementation uses YouTube as a
source of content and can play and download video as well as audio.
The pafy library handles interfacing with YouTube.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc README.rst CHANGELOG
%attr(755,root,root) %{_bindir}/mpsyt
%{_desktopdir}/%{name}.desktop
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
