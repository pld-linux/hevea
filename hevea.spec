Summary:	LaTeX to html translator
Summary(pl):	Konwerter z LaTeXa do HTML-a
Name:		hevea
Version:	1.05
Release:	3
License:	free
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoraci�n/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplica��es/Editora��o/TeX
Vendor:		Luc Maranget <Luc.Maranget@inria.fr>
Source0:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}-manual.tar.gz
Source2:	ftp://ftp.inria.fr/INRIA/Projects/para/hevea/%{name}-%{version}-manual.ps.gz
#Patch0:		%{name}-opt.patch
URL:		http://para.inria.fr/~maranget/hevea/
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
HEVEA to translator dokument�w LaTeXa do HTML. Pliki wej�ciowe powinny
sk�ada� si� z komend LaTeX2e (stary styl LaTeXa r�wnie� jest
akceptowany), a pliki wynikowe HTML s� zgodne ze standardem 4.0.

%package doc-ps
Summary:	PostScript documentation for Hevea
Summary(pl):	Dokumentacja dla Hevea w formacie PostScript
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Requires:	%{name} = %{version}

%description doc-ps
PostScript documentation for Hevea.

%description doc-ps -l pl
Dokumentacja dla Hevea w formacie PostScript.

%package doc-html
Summary:	HTML documentation for Hevea
Summary(pl):	Dokumentacja dla Hevea w formacie HTML
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Requires:	%{name} = %{version}

%description doc-html
HTML documentation for Hevea.

%description doc-html -l pl
Dokumentacja dla Hevea w formacie PostScript.

%prep 
%setup -q -a1
#%patch0 -p1
cp -f %{SOURCE2} manual.ps.gz
mv -f %{name}-%{version}-manual manual

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

%files doc-ps
%defattr(644,root,root,755)
%doc *.ps.gz

%files doc-html
%defattr(644,root,root,755)
%doc manual
