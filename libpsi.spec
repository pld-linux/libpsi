%define		_snap	031117
Summary:	A library containing jabber functions
Summary(pl):	Biblioteka zawieraj±ca funkcje jabbera
Name:		libpsi
Version:	%{_snap}
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Libraries
# From kdenonbeta kde cvs module
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	29c6302a26549b667fa77c21a5e05b3f
BuildRequires:	openssl-devel >= 0.9.7c
Requires:	openssl >= 0.9.7c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpsi contains jabber client functions used among others by psi and
kopete.

%description -l pl
libpsi zawiera funkcje klienckie jabbera. Jest wykorzystywana m.in. w
psi i kopete.

%package devel
Summary:	Header files for libpsi
Summary(pl):	Pliki nag³ówkowe dla libpsi
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	openssl-devel >= 0.9.7c

%description devel
Header files for libpsi.

%description devel -l pl
Pliki nag³ówkowe dla libpsi.

%prep
%setup -q

%build

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpsi.so
%attr(755,root,root) %{_libdir}/libqssl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/libpsi.la
%{_libdir}/libqssl.la
