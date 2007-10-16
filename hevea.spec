Summary:	LaTeX to html translator
Summary(pl.UTF-8):	Konwerter z LaTeXa do HTML-a
Name:		hevea
Version:	1.06
Release:	4
License:	Free
Group:		Applications/Publishing/TeX
Vendor:		Luc Maranget <Luc.Maranget@inria.fr>
Source0:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}.tar.gz
# Source0-md5:	7961cf05d12ccea2fdc9d57918564a72
Source1:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}-manual.pdf
URL:		http://para.inria.fr/~maranget/hevea/
BuildRequires:	ocaml >= 3.09.0
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
Requires:	ghostscript >= 4.03
Requires:	tetex-latex >= 0.4
Requires:	tetex-dvips >= 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__make} \
	TARGET=opt \
	LIBDIR=%{_datadir}/%{name} \
	BINDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_latexheveadir},%{_datadir},%{_bindir}}

%{__make} install \
	LIBDIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

mv -f	$RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.sty \
	$RPM_BUILD_ROOT%{_latexheveadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p %{_bindir}/texhash
%postun -p %{_bindir}/texhash

%files
%defattr(644,root,root,755)
%doc CHANGES README LICENSE manual.pdf
%attr(-,  root,root) %{_datadir}/%{name}
%attr(755,root,root) %dir %{_latexheveadir}
%attr(755,root,root) %{_bindir}/*
%{_latexheveadir}/*.sty
