Summary:	LaTeX to html translator
Summary(pl):	konwerter z LaTeXa do html'a
Name:		hevea
Version:	1.05
Release:	1
Copyright:	free
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
URL:		http://para.inria.fr/~maranget/hevea/
Vendor:		Luc Maranget <Luc.Maranget@inria.fr>
Source0:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}-manual.tar.gz
Source2:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}-manual.ps.gz
Patch0:		%{name}-opt.patch
BuildRequires:	ocaml
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
Requires:	ghostscript >= 4.03
Requires:	tetex-latex >= 0.4
Requires:	tetex-dvips >= 0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_latexhevadir		%{_datadir}/texmf/tex/latex/%{name}

%description
HEVEA is a LaTeX to HTML translator. The input language is a fairly
complete subset of LaTeX2e (old LaTeX style is also accepted) and the
output language is HTML that is (hopefully) correct with respect to
version 4.0 (transitional)

%description -l pl
HEVEA to translator dokumentów LaTeXa do HTML. Pliki wej¶ciowe powinny
sk³adaæ siê z komend LaTeX2e (stary styl LaTeXa równie¿ jest
akceptowany), a pliki wynikowe HTML s± zgodne ze standardem 4.0.

%package doc-ps
Summary:	PostScript documentation for Hevea
Summary(pl):	Dokumentacja dla Hevea w formacie PostSript
Group:		Development/Tools
Requires:	%{name} = %{version}

%description doc-ps
PostScript documentation for OCaml

%description doc-ps -l pl
Dokumentacja dla OCaml-a w formacie PostSript

%package doc-html
Summary:	HTML documentation for Hevea
Summary(pl):	Dokumentacja dla Hevea w formacie HTML
Group:		Development/Tools
Requires:	%{name} = %{version}

%description doc-html
PostScript documentation for Hevea

%description doc-html -l pl
Dokumentacja dla Hevea w formacie PostSript

%prep 
%setup -q
%patch0 -p1
%setup -q -a1
cp %{SOURCE2} manual.ps.gz
mv %{name}-%{version}-manual manual

%build
%{__make} \
	TARGET=opt \
	LIBDIR=%{_datadir}/%{name} \
	BINDIR=%{_bindir} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_latexhevadir},%{_datadir},%{_bindir}}

%{__make} install \
	LIBDIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}
mv -f	$RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.sty \
	$RPM_BUILD_ROOT%{_latexhevadir}

gzip -9nf CHANGES README LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p %{_bindir}/texhash
%postun -p %{_bindir}/texhash

%files
%defattr(644,root,root,755)
%doc CHANGES.gz README.gz LICENSE.gz
%attr(-,  root,root) %{_datadir}/%{name}
%attr(755,root,root) %dir %{_latexhevadir}
%attr(755,root,root) %{_bindir}/*
%{_latexhevadir}/*.sty

%files doc-html
%doc *.ps.gz

%files doc-ps
%doc manual
