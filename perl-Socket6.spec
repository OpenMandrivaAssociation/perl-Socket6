%define module	Socket6

Name:		perl-%{module}
Version:	0.23
Release:	%mkrel 1
Summary:	IPv6 related part of the C socket.h defines and structure manipulators
License:	BSD-like
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Socket6/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorarch}/auto/Socket6
%{perl_vendorarch}/Socket6.pm
