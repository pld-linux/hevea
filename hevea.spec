Summary:	LaTeX to html translator
Summary(pl):	Konwerter z LaTeXa do HTML-a
Name:		hevea
Version:	1.06
Release:	1
License:	Free
Group:		Applications/Publishing/TeX
Vendor:		Luc Maranget <Luc.Maranget@inria.fr>
Source0:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}-manual.tar.gz
Source2:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}-manual.ps.gz
URL:		http://para.inria.fr/~maranget/hevea/
BuildRequires:	ocaml
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
version 4.0 (transitional)

%description -l pl
HEVEA to translator dokumentów LaTeXa do HTML. Pliki wej¶ciowe powinny
sk³adaæ siê z komend LaTeX2e (stary styl LaTeXa równie¿ jest
akceptowany), a pliki wynikowe HTML s± zgodne ze standardem 4.0.

%package doc-ps
Summary:	PostScript documentation for Hevea
Summary(pl):	Dokumentacja dla Hevea w formacie PostScript
Group:		Development/Tools
Requires:	%{name} = %{version}

%description doc-ps
PostScript documentation for Hevea.

%description doc-ps -l pl
Dokumentacja dla Hevea w formacie PostScript.

%package doc-html
Summary:	HTML documentation for Hevea
Summary(pl):	Dokumentacja dla Hevea w formacie HTML
Group:		Development/Tools
Requires:	%{name} = %{version}

%description doc-html
HTML documentation for Hevea.

%description doc-html -l pl
Dokumentacja dla Hevea w formacie PostScript.

%prep
%setup -q -a1
cp -f %{SOURCE2} manual.ps.gz
mv -f %{name}-%{version}-manual manual

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
%doc CHANGES README LICENSE
%attr(-,  root,root) %{_datadir}/%{name}
%attr(755,root,root) %dir %{_latexheveadir}
%attr(755,root,root) %{_bindir}/*
%{_latexheveadir}/*.sty

%files doc-ps
%defattr(644,root,root,755)
%doc *.ps.gz

%files doc-html
%defattr(644,root,root,755)
%doc manual
