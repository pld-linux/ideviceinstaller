Summary:	Manage Applications of an iPhone or iPod Touch
Summary(pl.UTF-8):	Zarządzanie aplikacjami na urządzeniach iPhone oraz iPod Touch
Name:		ideviceinstaller
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		Applications
#Source0Download: https://libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/ideviceinstaller/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	0ff6252c3c2cc9edc671120369ce492e
URL:		https://libimobiledevice.org/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	libimobiledevice-devel >= 1.3.0
BuildRequires:	libplist-devel >= 2.3.0
BuildRequires:	libtool >= 2:2
BuildRequires:	libzip-devel >= 0.10
BuildRequires:	pkgconfig
Requires:	libimobiledevice >= 1.3.0
Requires:	libplist >= 2.3.0
Requires:	libzip >= 0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ideviceinstaller is a tool to interact with the installation_proxy of
an iPhone/iPod Touch device allowing to install, upgrade, uninstall,
archive, restore, and enumerate installed or archived apps.

%description -l pl.UTF-8
ideviceinstaller to narzędzie do interakcji z installation_proxy
urządzeń iPhone/iPod Touch, co pozwala instalować, uaktualniać,
odinstalowywać, archiwizować, przywracać i wyliczać zainstalowane lub
zarchiwizowane aplikacje.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/ideviceinstaller
%{_mandir}/man1/ideviceinstaller.1*
