%define debug_package %{nil}

%global gh_user jc21

Name:           json-strip-comments
Version:        1.0.0
Release:        1%{?dist}
Summary:        A command to strip c style comments from a given file
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
This is a very simple command that will remove comments from JSON files.

%prep
%setup -qn %{name}-%{version}

%build
go build -o bin/%{name} cmd/%{name}/main.go

%install
install -Dm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Apr 26 2022 Jamie Curnow <jc@jc21.com> 1.0.0-1
- v1.0.0
