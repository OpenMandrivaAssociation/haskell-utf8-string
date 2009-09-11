%define module utf8-string
%define _cabal_setup Setup.lhs

Name: haskell-%{module}
Version: 0.3.3
Release: %mkrel 2
Summary: Support for reading and writing UTF8 Strings
Group: Development/Other
License: BSD3
Url: http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{module}-%{version}/
Source: http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{module}-%{version}/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: haskell-macros
BuildRequires: ghc
BuildRequires: haddock

%description
A UTF8 layer for IO and Strings. The utf8-string
package provides operations for encoding UTF8
strings to Word8 lists and back, and for reading and
writing UTF8 without truncation.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%{_docdir}/%{module}-%{version}/*
%_libdir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot
