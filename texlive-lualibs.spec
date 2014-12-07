# revision 33861
# category Package
# catalog-ctan /macros/luatex/generic/lualibs
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license gpl2
# catalog-version 2.1a
Name:		texlive-lualibs
Version:	2.1a
Release:	5
Summary:	Additional Lua functions for LuaTeX macro programmers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/lualibs
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualibs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualibs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lualibs.source.tar.xz
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
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-basic-merged.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-basic.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-boolean.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-compat.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-dir.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-extended-merged.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-extended.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-file.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-function.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-gzip.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-io.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-lpeg.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-lua.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-math.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-md5.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-number.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-os.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-package.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-set.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-string.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-table.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-trac-inf.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-unicode.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-url.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-deb.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-dim.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-jsn.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-lua.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-prs.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-sta.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-sto.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-str.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-tab.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-tpl.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs.lua
%doc %{_texmfdistdir}/doc/luatex/lualibs/LICENSE
%doc %{_texmfdistdir}/doc/luatex/lualibs/NEWS
%doc %{_texmfdistdir}/doc/luatex/lualibs/README
%doc %{_texmfdistdir}/doc/luatex/lualibs/lualibs.pdf
#- source
%doc %{_texmfdistdir}/source/luatex/lualibs/Makefile
%doc %{_texmfdistdir}/source/luatex/lualibs/lualibs.dtx
%doc %{_texmfdistdir}/source/luatex/lualibs/test-lualibs.lua
%doc %{_texmfdistdir}/source/luatex/lualibs/whatsnew.lua

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
