%define		_snapshot	20021108
Summary:	A library containing jabber functions
Summary(pl):	Biblioteka zawieraj±ca funkcje jabbera
Name:		libpsi
Version:	%{_snapshot}
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
BuildRequires:	qt-devel >= 3.1
Requires:	qt >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
libpsi contains jabber client functions used among others by psi and
kopete.

%description -l pl
libpsi zawiera funkcje klienckie jabbera. Jest wykorzystywana m.in. w
psi i kopete.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

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
%{_includedir}/*
%{_libdir}/libpsi.so
