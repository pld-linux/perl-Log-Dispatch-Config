#
# Conditional build:
%bcond_without	tests	# do not perform "./Build test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Dispatch-Config
Summary:	Log::Dispatch::Config - Log4j for Perl
Summary(pl):	Log::Dispatch::Config - Log4j dla Perla
Name:		perl-Log-Dispatch-Config
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9d9b7b5d3426819e6b6e14e91b867242
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-AppConfig >= 1.52
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-Log-Dispatch >= 2.00
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Dispatch::Config is a subclass of Log::Dispatch and provides a
way to configure Log::Dispatch object with configuration file
(default, in AppConfig format). I mean, this is log4j for Perl, not
with all API compatibility though.

%description -l pl
Log::Dispatch::Config jest to podklasa Log::Dispatch udostêpniaj±ca
metodê konfiguracji obiektu Log::Dispatch za pomoc± pliku
konfiguracyjnego (domy¶lnie w formacie AppConfig). Oznacza to, ¿e jest
to log4j dla Perla, nie koniecznie zgopdne ze wszystkimi API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Log/Dispatch/*
%{_mandir}/man3/*
