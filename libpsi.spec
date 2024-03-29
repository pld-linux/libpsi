%define		_snap	031117
Summary:	A library containing Jabber functions
Summary(pl.UTF-8):	Biblioteka zawierająca funkcje Jabbera
Name:		libpsi
Version:	%{_snap}
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Libraries
# From kdenonbeta kde cvs module
Source0:	http://ep09.pld-linux.org/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	29c6302a26549b667fa77c21a5e05b3f
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	artsc-devel
Requires:	openssl >= 0.9.7c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpsi contains Jabber client functions used among others by psi and
kopete.

%description -l pl.UTF-8
libpsi zawiera funkcje klienckie Jabbera. Jest wykorzystywana m.in. w
psi i kopete.

%package devel
Summary:	Header files for libpsi
Summary(pl.UTF-8):	Pliki nagłówkowe dla libpsi
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	openssl-devel >= 0.9.7c

%description devel
Header files for libpsi.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libpsi.

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
