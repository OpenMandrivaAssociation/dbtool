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


