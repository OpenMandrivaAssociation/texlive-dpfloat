Name:		texlive-dpfloat
Version:	20100224
Release:	1
Summary:	Support for double-page floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dpfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dpfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dpfloat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides fullpage and leftfullpage environments, that may be
used inside a figure, table, or other float environment. If the
first of a 2-page spread uses a "leftfullpage" environment, the
float will only be typeset on an even-numbered page, and the
two floats will appear side-by-side in a two-sided document.

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
%{_texmfdistdir}/tex/latex/dpfloat/dpfloat.sty
%doc %{_texmfdistdir}/doc/latex/dpfloat/README
%doc %{_texmfdistdir}/doc/latex/dpfloat/dpfloat.pdf
%doc %{_texmfdistdir}/doc/latex/dpfloat/dpfloat.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
