%global tl_name curve
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.16
Release:	%{tl_revision}.1
Summary:	A class for making curriculum vitae
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/curve
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/curve.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/curve.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/curve.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
CurVe is a class for writing a CV, with configuration for the language
in which you write. The class provides a set of commands to create
rubrics, entries in these rubrics etc. CurVe then format the CV
(possibly splitting it onto multiple pages, repeating the titles etc),
which is usually the most painful part of CV writing. Another nice
feature of CurVe is its ability to manage different CV 'flavours'
simultaneously. It is often the case that you want to maintain slightly
divergent versions of your CV at the same time, in order to emphasize on
different aspects of your background. CurVe also comes with support for
use with AUC-TeX.

