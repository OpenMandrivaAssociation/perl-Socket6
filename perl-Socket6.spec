%define upstream_name	 Socket6
%define upstream_version 0.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	IPv6 related part of the C socket.h defines and structure manipulators
License:	BSD-like
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Socket6/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides glue routines to the various IPv6 functions.

If you use the Socket6 module, be sure to specify "use Socket" as
well as "use Socket6".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
