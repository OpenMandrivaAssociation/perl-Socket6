%define modname	Socket6

Summary:	IPv6 related part of the C socket.h defines and structure manipulators
Name:		perl-%{modname}
Version:	0.29
Release:	2
License:	BSD-like
Group:		Development/Perl
Url:		https://metacpan.org/pod/Socket6
Source0:	http://www.cpan.org/modules/by-module/Socket6/Socket6-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:  perl(Test)

%description
This module provides glue routines to the various IPv6 functions.

If you use the Socket6 module, be sure to specify "use Socket" as
well as "use Socket6".

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
%make_install

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/Socket6
%{perl_vendorarch}/Socket6.pm
%{_mandir}/man3/Socket6.3pm*
