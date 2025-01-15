Name:      rsleep
Summary:   rsleep is an executable which provides random sleep for scripts
Version:   0.05
Release:   3%{?dist}
License:   gplv2
Group:     System Environment/Daemons
URL:       https://github.com/mrdvt92/rsleep
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc
BuildRequires: make
BuildRequires: /usr/bin/pod2man
BuildRequires: gzip
BuildRequires: /usr/bin/time

%description 
rsleep is an executable which provides random sleep for scripts

%prep
%setup -q

%build
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p       $RPM_BUILD_ROOT%{_bindir}/
mkdir -p       $RPM_BUILD_ROOT%{_mandir}/man1/
mkdir -p       $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/
cp rsleep      $RPM_BUILD_ROOT%{_bindir}/
cp rsleep.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/
cp LICENSE     $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/

%files
%defattr(0644,root,root,-)
%attr(0755,root,root) %{_bindir}/rsleep
%{_mandir}/man1/rsleep.1.gz
%{_datadir}/doc/%{name}-%{version}/LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
