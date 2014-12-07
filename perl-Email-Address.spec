%define modname	Email-Address
%define modver 1.905

Summary:	RFC 2822 Address Parsing and Creation

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Email/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This class implements a complete RFC 2822 parser that locates
email addresses in strings and returns a list of "Email::Address"
objects found. Alternatley you may construct objects manually.
The goal of this software is to be correct, and very very fast.

%prep
%setup -qn %{modname}-%{modver} 
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
