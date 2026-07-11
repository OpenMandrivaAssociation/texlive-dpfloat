%global tl_name dpfloat
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for double-page floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dpfloat
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dpfloat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dpfloat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides fullpage and leftfullpage environments, that may be used inside
a figure, table, or other float environment. If the first of a 2-page
spread uses a "leftfullpage" environment, the float will only be typeset
on an even-numbered page, and the two floats will appear side-by-side in
a two-sided document.

