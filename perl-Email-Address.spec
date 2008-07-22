%define module  Email-Address
%define name        perl-%{module}
%define version     1.88.8
%define up_version  1.888
%define release     %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        RFC 2822 Address Parsing and Creation
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This class implements a complete RFC 2822 parser that locates
email addresses in strings and returns a list of "Email::Address"
objects found. Alternatley you may construct objects manually.
The goal of this software is to be correct, and very very fast.

%prep
%setup -q -n %{module}-%{up_version} 
perl -pi -e 's|/usr/local/bin/perl|%{__perl}|' bench/ea-vs-ma.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README bench
%{perl_vendorlib}/Email
%{_mandir}/man3/*

