# revision 17196
# category Package
# catalog-ctan /macros/latex/contrib/dpfloat
# catalog-date 2010-02-24 00:01:31 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-dpfloat
Version:	20100224
Release:	10
Summary:	Support for double-page floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dpfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dpfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dpfloat.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100224-2
+ Revision: 751083
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100224-1
+ Revision: 718255
- texlive-dpfloat
- texlive-dpfloat
- texlive-dpfloat
- texlive-dpfloat

