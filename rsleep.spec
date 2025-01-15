Name:      rsleep
Summary:   rsleep is an executable which provides random sleep for scripts
Version:   0.05
Release:   1%{?dist}
License:   gplv2
Group:     System Environment/Daemons
URL:       https://github.com/mrdvt92/rsleep
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc
BuildRequires: make
BuildRequires: /usr/bin/pod2man
BuildRequires: gzip

%description 
rsleep is an executable which provides random sleep for scripts

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp rsleep $RPM_BUILD_ROOT%{_bindir}/

%files
%defattr(0644,root,root,-)
%attr(0755,root,root) %{_bindir}/rsleep

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
