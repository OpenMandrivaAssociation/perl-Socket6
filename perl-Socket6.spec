%define upstream_name	 Socket6
%define upstream_version 0.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.230.0-6mdv2012.0
+ Revision: 765644
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.230.0-5
+ Revision: 764156
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.230.0-4
+ Revision: 667309
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.230.0-3mdv2011.0
+ Revision: 564579
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-2mdv2011.0
+ Revision: 556144
- rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.1
+ Revision: 404391
- rebuild using %%perl_convert_version

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2009.1
+ Revision: 299404
- update to new version 0.23

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2009.0
+ Revision: 277972
- update to new version 0.22

* Sun Aug 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2009.0
+ Revision: 272892
- update to new version 0.21

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.20-2mdv2009.0
+ Revision: 224054
- rebuild

* Mon Feb 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2008.1
+ Revision: 170103
- new version

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.19-3mdv2008.1
+ Revision: 151409
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-2mdv2008.0
+ Revision: 67064
- rebuild


* Sat Jul 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.19-1mdv2007.0
- rebuild

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdk
- New release 0.19
- fix source URL

* Tue Jun 07 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.18-1mdk
- 0.18
- Make rpmbuildupdate happy

* Tue Nov 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.17-2mdk
- rebuild for new perl

* Thu Aug 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.17-1mdk
- initial mandrake package

