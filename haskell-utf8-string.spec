%global debug_package %{nil}
%define _cabal_setup Setup.lhs
#% define _no_haddock 1
%define module utf8-string
Name:           haskell-%{module}
Version:        0.3.7
Release:        1
Summary:        Support for reading and writing UTF8 Strings
Group:          Development/Other
License:        BSD
URL:            https://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
Requires(pre):  ghc

%description
A UTF8 layer for IO and Strings. The utf8-string package provides operations
for encoding UTF8 strings to Word8 lists and back, and for reading and writing
UTF8 without truncation.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files



