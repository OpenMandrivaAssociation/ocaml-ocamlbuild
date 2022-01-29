%define  _empty_manifest_terminate_build 0
%define subname ocamlbuild
Name:		ocaml-ocamlbuild
Version:	0.14.1
Release:	1
Summary:	Pre-Processor-Pretty-Printer for OCaml
License:	LGPLv2+ with exceptions
URL:		https://github.com/ocaml/ocamlbuild
Source0:	https://github.com/ocaml/ocamlbuild/archive/%{subname}-0.14.1.tar.xz
Group:		Development/Other

# This package used to be part of the upstream compiler.  We still
# need to keep it in lock step with the compiler, so whenever a new
# compiler is released we will also update this package also.
BuildRequires:	ocaml
Requires:	ocaml
Provides:	ocamlbuild = %{EVRD}

%description
Camlbuild is a legacy buildtool for older ocaml packages.
It had been superceded by 'dune'
This package contains the runtime files.

%prep
%setup -qn %{subname}-%{version}

%build
unset MAKEFLAGS
make configure		OCAMLBUILD_PREFIX=%{_prefix} \
			OCAMLBUILD_BINDIR=%{_bindir} \
			OCAMLBUILD_LIBDIR=%{_libdir}/ocaml/ \
			OCAMLBUILD_MANDIR=%{_datadir}/man/ \
			OCAML_NATIVE=false \
			OCAML_NATIVE_TOOLS=false
			
# Incompatible with parallel builds:
unset MAKEFLAGS
make 

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/ocaml/ocamlbuild
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/ocaml/ocamlbuild/META


%files
%license LICENSE
%doc Readme.md CONTRIBUTING.adoc Changes 
%dir %{_libdir}/ocaml/ocamlbuild
%{_bindir}/ocamlbuild
%{_bindir}/ocamlbuild.byte
%{_libdir}/ocaml/ocamlbuild/*.cma
%{_libdir}/ocaml/ocamlbuild/*.cmo
%{_libdir}/ocaml/ocamlbuild/*.cmi
%{_libdir}/ocaml/ocamlbuild/*.mli
%{_libdir}/ocaml/ocamlbuild/*.cmti
%{_mandir}/man1/ocamlbuild.1.*
   