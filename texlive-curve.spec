Name:		texlive-curve
Version:	20745
Release:	2
Summary:	A class for making curriculum vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/curve
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
CurVe is a class for writing a CV, with configuration for the
language in which you write. The class provides a set of
commands to create rubrics, entries in these rubrics etc. CurVe
then format the CV (possibly splitting it onto multiple pages,
repeating the titles etc), which is usually the most painful
part of CV writing. Another nice feature of CurVe is its
ability to manage different CV 'flavours' simultaneously. It is
often the case that you want to maintain slightly divergent
versions of your CV at the same time, in order to emphasize on
different aspects of your background. CurVe also comes with
support for use with AUC-TeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/curve/curve.cls
%doc %{_texmfdistdir}/doc/latex/curve/NEWS
%doc %{_texmfdistdir}/doc/latex/curve/README
%doc %{_texmfdistdir}/doc/latex/curve/THANKS
%doc %{_texmfdistdir}/doc/latex/curve/curve.el
%doc %{_texmfdistdir}/doc/latex/curve/curve.pdf
%doc %{_texmfdistdir}/doc/latex/curve/examples/Makefile
%doc %{_texmfdistdir}/doc/latex/curve/examples/bib.bib
%doc %{_texmfdistdir}/doc/latex/curve/examples/bib.tex
%doc %{_texmfdistdir}/doc/latex/curve/examples/raw.tex
%doc %{_texmfdistdir}/doc/latex/curve/examples/rubric.tex
%doc %{_texmfdistdir}/doc/latex/curve/header.inc
#- source
%doc %{_texmfdistdir}/source/latex/curve/curve.dtx
%doc %{_texmfdistdir}/source/latex/curve/curve.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
