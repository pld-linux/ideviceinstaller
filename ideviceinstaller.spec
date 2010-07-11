Summary:	Manage Applications of an iPhone or iPod Touch
Name:		ideviceinstaller
Version:	0.1.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}.tar.bz2
# Source0-md5:	1fafde989d8178f137fb208766e02f9a
URL:		http://www.libimobiledevice.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libimobiledevice-devel >= 0.9.7
BuildRequires:	libtool
BuildRequires:	libzip-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ideviceinstaller is a tool to interact with the installation_proxy of
an iPhone/iPod Touch device allowing to install, upgrade, uninstall,
archive, restore, and enumerate installed or archived apps.

%prep
%setup -q -n %{name}

%build
%{__aclocal} -I m4
%{__libtoolize}
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
