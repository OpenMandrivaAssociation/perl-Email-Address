%define modname	Email-Address

Summary:	RFC 2822 Address Parsing and Creation
Name:		perl-%{modname}
Version:	1.913
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Email/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This class implements a complete RFC 2822 parser that locates
email addresses in strings and returns a list of "Email::Address"
objects found. Alternatley you may construct objects manually.
The goal of this software is to be correct, and very very fast.

%prep
%autosetup -p1 -n %{modname}-%{version} 
perl -pi -e 's|/usr/local/bin/perl|%{__perl}|' bench/ea-vs-ma.pl
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes README bench META.yml
%{perl_vendorlib}/Email
%{_mandir}/man3/*
