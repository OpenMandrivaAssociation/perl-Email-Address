%define upstream_name    Email-Address
%define upstream_version 1.892

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:        RFC 2822 Address Parsing and Creation
License:        GPL+ or Artistic
Group:          Development/Perl
urL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This class implements a complete RFC 2822 parser that locates
email addresses in strings and returns a list of "Email::Address"
objects found. Alternatley you may construct objects manually.
The goal of this software is to be correct, and very very fast.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
perl -pi -e 's|/usr/local/bin/perl|%{__perl}|' bench/ea-vs-ma.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README bench META.yml
%{perl_vendorlib}/Email
%{_mandir}/man3/*
