%define module	Getopt-Tabular
%define name	perl-%{module}
%define version 0.3
%define release %mkrel 7

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Table-driven argument parsing for Perl 5
License:	    GPL or Artistic
Group:		    Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Algorithm/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Getopt
%{_mandir}/*/*

