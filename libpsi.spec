%define		_snapshot	20030217
Summary:	A library containing jabber functions
Summary(pl):	Biblioteka zawieraj±ca funkcje jabbera
Name:		libpsi
Version:	%{_snapshot}
Release:	4
License:	GPL
Group:		X11/Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5: 94fd68eda467bffc4b760f2d28e1f867
Patch0:		%{name}-am.patch
Patch1:		%{name}-qssl.patch
BuildRequires:	qt-plugin-ssl-devel >= 1.0
BuildRequires:	qt-devel >= 3.1
Requires:	qt >= 3.1
Requires:	qt-plugin-ssl >= 1.0
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
Requires:	%{name} = %{version}
Requires:	qt-devel >= 3.1
Requires:	qt-plugin-ssl-devel >= 1.0

%description devel
Header files for libpsi.

%description devel -l pl
Pliki nag³ówkowe dla libpsi.

%prep
%setup -q
##%patch0 -p1
%patch1 -p1

%build
%{__make} -f Makefile.cvs
%configure

%{__make} -C psi/libpsi

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C psi/libpsi install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpsi.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.la
