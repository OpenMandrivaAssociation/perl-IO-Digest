%define upstream_name    IO-Digest
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	%{upstream_name} module, calculate digests while reading or writing  
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-PerlIO-via-dynamic
# for test
BuildRequires:	perl-Internals
BuildArch:	noarch

%description
This module allows you to calculate digests while reading or writing file 
handles. This avoids the case you need to reread the same content to 
compute the digests after written a file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%defattr(444,root,root,755)
%doc CHANGES README 
%{perl_vendorlib}/IO/*
%{_mandir}/man*/*

%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 406066
- rebuild using %%perl_convert_version

* Thu Jul 03 2008 Michael Scherer <misc@mandriva.org> 0.10-4mdv2009.0
+ Revision: 230905
- add missing BuildRequires
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 21 2007 Michael Scherer <misc@mandriva.org> 0.10-3mdv2008.0
+ Revision: 41994
- rebuild


* Thu Sep 29 2005 Michael Scherer <misc@mandriva.org> 0.10-2mdk
- Rebuild
- update the spec ( mkrel, check, update url )

* Tue Sep 21 2004 Michael Scherer <misc@mandrake.org> 0.10-1mdk
- First Mandrakelinux package

