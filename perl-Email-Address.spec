%define upstream_name    Email-Address
%define upstream_version 1.892

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	RFC 2822 Address Parsing and Creation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch


%description
This class implements a complete RFC 2822 parser that locates
email addresses in strings and returns a list of "Email::Address"
objects found. Alternatley you may construct objects manually.
The goal of this software is to be correct, and very very fast.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
perl -pi -e 's|/usr/local/bin/perl|%{__perl}|' bench/ea-vs-ma.pl

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README bench META.yml
%{perl_vendorlib}/Email
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.892.0-4mdv2012.0
+ Revision: 765193
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.892.0-3
+ Revision: 763709
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.892.0-2
+ Revision: 676771
- rebuild

* Mon Sep 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1.892.0-1mdv2011.0
+ Revision: 576296
- update to 1.892

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 1.891.0-1mdv2011.0
+ Revision: 575395
- update to 1.891

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.890.0-1mdv2011.0
+ Revision: 572703
- update to 1.890

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.889.0-3mdv2011.0
+ Revision: 337631
- new release
- use standardized version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.88.8-3mdv2009.0
+ Revision: 241209
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.88.8-1mdv2008.0
+ Revision: 56079
- update to new version 1.88.8

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.88.7-1mdv2008.0
+ Revision: 20063
- 1.887


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.87.0-1mdv2007.0
- new version (upstream version 1.870)

* Wed Aug 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.86-1mdv2007.0
- new version
- spec cleanup
- fix directory ownership

* Sun Jul 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.80-1mdk
- initial Mandriva package

