%define modname	Socket6
%define modver 0.25

Summary:	IPv6 related part of the C socket.h defines and structure manipulators
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	BSD-like
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Socket6/Socket6-%{modver}.tar.gz
BuildRequires:	perl-devel

%description
This module provides glue routines to the various IPv6 functions.

If you use the Socket6 module, be sure to specify "use Socket" as
well as "use Socket6".

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/Socket6
%{perl_vendorarch}/Socket6.pm
%{_mandir}/man3/Socket6.3pm.*


