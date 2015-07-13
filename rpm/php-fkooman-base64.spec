%global composer_vendor  fkooman
%global composer_project base64

%global github_owner     fkooman
%global github_name      php-lib-base64

Name:       php-%{composer_vendor}-%{composer_project}
Version:    1.0.2
Release:    1%{?dist}
Summary:    A base64 encoder and decoder

Group:      System Environment/Libraries
License:    ASL 2.0
URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    https://github.com/%{github_owner}/%{github_name}/archive/%{version}.tar.gz
BuildArch:  noarch

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

Requires:   php(language) >= 5.3.0
Requires:   php-spl
Requires:   php-standard

%description
A library to encode and decode base64 and base64url.

%prep
%setup -qn %{github_name}-%{version}

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/php
cp -pr src/* ${RPM_BUILD_ROOT}%{_datadir}/php

%files
%defattr(-,root,root,-)
%dir %{_datadir}/php/%{composer_vendor}/Base64
%{_datadir}/php/%{composer_vendor}/Base64/*
%doc README.md CHANGES.md composer.json
%license COPYING

%changelog
* Mon Jul 13 2015 François Kooman <fkooman@tuxed.net> - 1.0.2-1
- update to 1.0.2

* Mon Jul 13 2015 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Tue Jul 07 2015 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package
