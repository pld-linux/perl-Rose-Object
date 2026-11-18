#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Rose
%define	pnam	Object
Summary:	Rose::Object - A simple object base class.
#Summary(pl.UTF-8):	
Name:		perl-Rose-Object
Version:	0.860
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/J/JS/JSIRACUSA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	34d662a480065ea4fb6ff47fbe2e6ca3
URL:		http://search.cpan.org/dist/Rose-Object/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rose::Object is a generic object base class.  It provides very little
functionality, but a healthy dose of convention.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Rose/*.pm
%{perl_vendorlib}/Rose/Object
%{perl_vendorlib}/Rose/Class
%{_mandir}/man3/*
