Name:		texlive-dpfloat
Version:	17196
Release:	2
Summary:	Support for double-page floats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dpfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dpfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dpfloat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides fullpage and leftfullpage environments, that may be
used inside a figure, table, or other float environment. If the
first of a 2-page spread uses a "leftfullpage" environment, the
float will only be typeset on an even-numbered page, and the
two floats will appear side-by-side in a two-sided document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dpfloat/dpfloat.sty
%doc %{_texmfdistdir}/doc/latex/dpfloat/README
%doc %{_texmfdistdir}/doc/latex/dpfloat/dpfloat.pdf
%doc %{_texmfdistdir}/doc/latex/dpfloat/dpfloat.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
