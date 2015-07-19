%define upstream_name	 Getopt-Tabular
%define upstream_version 0.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Table-driven argument parsing for Perl 5
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Getopt::Tabular is a Perl 5 module for table-driven argument parsing, vaguely
inspired by John Ousterhout's Tk_ParseArgv. All you really need to do to use
the package is set up a table describing all your command-line options, and
call &GetOptions with three arguments: a reference to your option table, a
reference to @ARGV (or something like it), and an optional third array
reference (say, to @newARGV). &GetOptions will process all arguments in @ARGV,
and copy any leftover arguments (i.e. those that are not options or arguments
to some option) to the @newARGV array. (If the @newARGV argument is not
supplied, GetOptions will replace @ARGV with the stripped-down argument list.)
If there are any invalid options, GetOptions will print an error message and
return 0.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Getopt
%{_mandir}/*/*

%changelog
* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.1
+ Revision: 504892
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-8mdv2010.0
+ Revision: 430460
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3-7mdv2009.0
+ Revision: 241442
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-5mdv2008.0
+ Revision: 67060
- rebuild


* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-4mdv2007.0
- Rebuild

* Mon Jun 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-3mdk 
- first mdk release

