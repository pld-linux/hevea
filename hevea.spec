Summary:	LaTeX to html translator
Summary(pl.UTF-8):	Konwerter z LaTeXa do HTML-a
Name:		hevea
Version:	1.10
Release:	1
License:	Free
Group:		Applications/Publishing/TeX
Vendor:		Luc Maranget <Luc.Maranget@inria.fr>
Source0:	http://para.inria.fr/~maranget/hevea/distri/%{name}-%{version}.tar.gz
# Source0-md5:	24a631570bee3cc4b8350e9db39be62b
Source1:	http://para.inria.fr/~maranget/hevea/distri/%{name}-%{version}-manual.pdf
# Source1-md5:	d9cc1d90aa85e0149a058b7fe7d5a9dd
URL:		http://para.inria.fr/~maranget/hevea/
BuildRequires:	ocaml >= 3.09.0
BuildRequires:	texlive-latex
BuildRequires:	texlive-dvips
Requires:	ghostscript >= 4.03
Requires:	texlive-latex >= 0.4
Requires:	texlive-dvips >= 0.4
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
%{__rm} config.sh

%build
%{__make} config.sh \
	TARGET=opt \
	PREFIX=%{_prefix} \
	LIBDIR=%{_datadir}/%{name} \
	LATEXLIBDIR=%{_latexheveadir} \
	BINDIR=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} \
	TARGET=opt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_latexheveadir},%{_datadir},%{_bindir}}

%{__make} install

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
