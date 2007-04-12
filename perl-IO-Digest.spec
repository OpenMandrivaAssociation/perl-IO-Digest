%define module  IO-Digest
%define version 0.10
%define release %mkrel 2

Summary: 	%{module} module, calculate digests while reading or writing  
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{module}-%{version}.tar.bz2
Url:        http://search.cpan.org/dist/%{module}/
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	perl-devel perl-PerlIO-via-dynamic

%description
This module allows you to calculate digests while reading or writing file 
handles. This avoids the case you need to reread the same content to 
compute the digests after written a file.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(444,root,root,755)
%doc CHANGES README 
%{perl_vendorlib}/IO/*
%_mandir/man*/*

