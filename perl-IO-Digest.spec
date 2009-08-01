%define upstream_name    IO-Digest
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary: 	%{upstream_name} module, calculate digests while reading or writing  
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-PerlIO-via-dynamic 
# for test
BuildRequires:	perl-Internals
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module allows you to calculate digests while reading or writing file 
handles. This avoids the case you need to reread the same content to 
compute the digests after written a file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
