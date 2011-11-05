# revision 20745
# category Package
# catalog-ctan /macros/latex/contrib/curve
# catalog-date 2010-12-14 18:30:55 +0100
# catalog-license lppl
# catalog-version 1.16
Name:		texlive-curve
Version:	1.16
Release:	1
Summary:	A class for making curriculum vitae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/curve
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/curve.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
