%define module	Socket6

Summary:	IPv6 related part of the C socket.h defines and structure manipulators
Name:		perl-%{module}
Version:	0.19
Release:	%mkrel 3
License:	BSD-like
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/U/UM/UMEMOTO/%{module}/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides glue routines to the various IPv6 functions.

If you use the Socket6 module, be sure to specify "use Socket" as
well as "use Socket6".

%prep

%setup -q -n %{module}-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

%make

%check
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorarch}/auto/Socket6/Socket6.so
%{perl_vendorarch}/Socket6.pm

