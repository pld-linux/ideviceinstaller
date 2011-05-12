Summary:	Manage Applications of an iPhone or iPod Touch
Name:		ideviceinstaller
Version:	1.0.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	877a1597797c292b47f4a9de581e8974
URL:		http://www.libimobiledevice.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libimobiledevice-devel >= 0.9.7
BuildRequires:	libplist-devel >= 0.15
BuildRequires:	libtool
BuildRequires:	libzip-devel >= 0.8
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ideviceinstaller is a tool to interact with the installation_proxy of
an iPhone/iPod Touch device allowing to install, upgrade, uninstall,
archive, restore, and enumerate installed or archived apps.

%prep
%setup -q

%{__sed} -i -e 's/-Werror//' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/ideviceinstaller
%{_mandir}/man1/ideviceinstaller.1*
