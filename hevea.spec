#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	LaTeX to html translator
Summary(pl.UTF-8):	Konwerter z LaTeXa do HTML-a
Name:		hevea
# 2.24 has svg.hva file missing
Version:	2.23
Release:	1
License:	Free
Group:		Applications/Publishing/TeX
Source0:	http://para.inria.fr/~maranget/hevea/old/%{name}-%{version}.tar.gz
# Source0-md5:	38b157e78e8171dc6a47f9ea10d2bd60
Source1:	http://para.inria.fr/~maranget/hevea/%{name}-2.24-manual.pdf
# Source1-md5:	82414eb9bd85b69d8ae78e58c99d12c4
URL:		http://para.inria.fr/~maranget/hevea/
BuildRequires:	ocaml >= 3.12.0
BuildRequires:	texlive-latex
BuildRequires:	texlive-dvips
Requires:	ghostscript >= 4.03
Requires:	texlive-latex >= 0.4
Requires:	texlive-dvips >= 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		make_target		%{?with_ocaml_opt:opt}%{!?with_ocaml_opt:byte}
%define		_latexheveadir		%{_datadir}/texmf/tex/latex/%{name}

%description
HEVEA is a LaTeX to HTML translator. The input language is a fairly
complete subset of LaTeX2e (old LaTeX style is also accepted) and the
output language is HTML that is (hopefully) correct with respect to
version 4.0 (transitional).

%description -l pl.UTF-8
HEVEA to translator dokumentów LaTeXa do HTML-a. Pliki wejściowe
powinny składać się z komend LaTeX2e (stary styl LaTeXa również jest
akceptowany), a pliki wynikowe HTML są zgodne ze standardem 4.0.

%prep
%setup -q
cp -f %{SOURCE1} manual.pdf

%build
%{__make} config.sh \
	TARGET=%{make_target} \
	PREFIX=%{_prefix} \
	LIBDIR=%{_datadir}/%{name} \
	LATEXLIBDIR=%{_latexheveadir} \
	BINDIR=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} \
	TARGET=%{make_target}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_latexheveadir},%{_datadir},%{_bindir}}

%{__make} install \
	TARGET=%{make_target} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p %{_bindir}/texhash
%postun -p %{_bindir}/texhash

%files
%defattr(644,root,root,755)
%doc CHANGES README LICENSE manual.pdf
%attr(755,root,root) %{_bindir}/bibhva
%attr(755,root,root) %{_bindir}/esponja
%attr(755,root,root) %{_bindir}/hacha
%attr(755,root,root) %{_bindir}/hevea
%attr(755,root,root) %{_bindir}/imagen
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/html
%{_datadir}/%{name}/info
%{_datadir}/%{name}/mappings
%{_datadir}/%{name}/text
%{_datadir}/%{name}/*.gif
%{_datadir}/%{name}/*.hva
%{_datadir}/%{name}/*.sty
%attr(755,root,root) %{_datadir}/%{name}/imagen
%attr(755,root,root) %{_datadir}/%{name}/*.exe
%dir %{_latexheveadir}
%{_latexheveadir}/hevea.sty
