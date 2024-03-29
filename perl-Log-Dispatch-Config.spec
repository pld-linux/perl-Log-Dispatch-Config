#
# Conditional build:
%bcond_without	tests	# do not perform "./Build test"
#
%define		pdir	Log
%define		pnam	Dispatch-Config
Summary:	Log::Dispatch::Config - Log4j for Perl
Summary(pl.UTF-8):	Log::Dispatch::Config - Log4j dla Perla
Name:		perl-Log-Dispatch-Config
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Log/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ac6f91b838743adb3a47cb09bf8defe5
URL:		http://search.cpan.org/dist/Log-Dispatch-Config/
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Log::Dispatch::Config jest to podklasa Log::Dispatch udostępniająca
metodę konfiguracji obiektu Log::Dispatch za pomocą pliku
konfiguracyjnego (domyślnie w formacie AppConfig). Oznacza to, że jest
to log4j dla Perla, nie koniecznie zgodne ze wszystkimi API.

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
