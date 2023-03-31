Name:		texlive-lectures
Version:	53642
Release:	2
Summary:	A document class for quickly drafting nice looking lecture notes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lectures
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lectures.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lectures.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX documentclass provides a number of gimmicks to draft
nice looking lecture notes, such as a number of theorem
environments, automatic spacing and alignment of figures and
much more. More information is available in the package readme.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/lectures
%doc %{_texmfdistdir}/doc/latex/lectures

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
