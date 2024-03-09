# Run tests in check section
%bcond_without check

# https://github.com/moby/sys
%global goipath		github.com/moby/sys
%global forgeurl	https://github.com/moby/sys
Version:		0.7.1

# NOTE: the archive name is the name of the lastest updated subpackage
#       possible values are: mount, mountinfo, sequential, signal, user.
%global archive	mountinfo

%gometa

Summary:	Moby sys package for Go
Name:		golang-github-moby-sys

Release:	1
Source0:	https://github.com/moby/sys/archive/mountinfo/v%{version}/sys-%{archive}-%{version}.tar.gz
URL:		https://github.com/moby/sys
License:	ASL 2.0 and BSD with advertising
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildRequires:	golang(golang.org/x/sys/unix)
BuildArch:	noarch

%description
Moby sys package for Go.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n sys-%{archive}-v%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

