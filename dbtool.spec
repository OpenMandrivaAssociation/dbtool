Summary:	Command Line Tool for GDBM
Name:		dbtool
Version:	1.6
Release:	%mkrel 8
License:	GPLv2
Group:		Databases
URL:		http://www.daemon.de/DBTOOL
Source0:	ftp://ftp.daemon.de/scip/Apps/dbtool/dbtool-%{version}.tar.bz2
Patch0:		dbtool.patch
Patch1:		dbtool-1.6-gcc411.diff
BuildRequires:	gdbm-devel
BuildRequires:	pcre-devel
#BuildRequires:	db4-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
dbtool can be used to store and retrieve data in a key/value format
in a GDBM hash database. Perl compatible regular expressions are
supported both for storing and retrieving of data. It's main
advantages are the ability to maintain huge amounts of data and
speed. It also supports encrypted databases using the AES cipher
algorithm.

%prep

%setup -q
%patch0 -p0
%patch1 -p1

# fix attribs
find samples -type f | xargs chmod 644
find samples -type d | xargs chmod 755
chmod 644 AUTHORS ChangeLog README

%build

# build the gdbm version
%configure --without-berkeley
%make CXXFLAGS="%{optflags} -Wall"
#mv dbtool dbtool-gdbm
#make clean

## build the berkley db version
#%%configure
#%%make
#mv dbtool dbtool-bdb

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 dbtool %{buildroot}%{_bindir}/
#install -m0755 dbtool-gdbm %{buildroot}%{_bindir}/
#install -m0755 dbtool-bdb %{buildroot}%{_bindir}/
install -m0644 dbtool.1 %{buildroot}%{_mandir}/man1/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog README samples
%attr(0755,root,root) %{_bindir}/dbtool*
%{_mandir}/man1/*




%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 1.6-8mdv2012.0
+ Revision: 772947
- relink against libpcre.so.1

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-7mdv2011.0
+ Revision: 617519
- the mass rebuild of 2010.0 packages

* Tue Jun 09 2009 Jérôme Brenier <incubusss@mandriva.org> 1.6-6mdv2010.0
+ Revision: 384580
- fix license

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.6-5mdv2009.0
+ Revision: 243965
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.6-3mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6-3mdv2007.0
+ Revision: 85655
- added a gcc4 patch (P1) from openpkg
- bunzip patches
- Import dbtool

* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6-2
- use the %%mkrel 2

* Thu Jul 07 2005 Oden Eriksson <oeriksson@mandriva.com> 1.6-1mdk
- initial Mandriva package, openpkg import with a twist

