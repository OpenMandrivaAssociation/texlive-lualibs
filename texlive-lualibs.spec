Name:		texlive-lualibs
Version:	64615
Release:	1
Summary:	Additional Lua functions for LuaTeX macro programmers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/lualibs
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualibs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualibs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualibs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Lualibs is a collection of Lua modules useful for general
programming. The bundle is based on lua modules shipped with
ConTeXt, and are made available in this bundle for use
independent of ConTeXt.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/luatex/lualibs
%doc %{_texmfdistdir}/doc/luatex/lualibs
#- source
%doc %{_texmfdistdir}/source/luatex/lualibs

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
