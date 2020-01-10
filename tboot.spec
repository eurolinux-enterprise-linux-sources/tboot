Summary:        Performs a verified launch using Intel TXT
Name:           tboot
Version:        1.8.1
Release:        1%{?dist}

Group:          System Environment/Base
License:        BSD
URL:            http://sourceforge.net/projects/tboot/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         tboot-%{version}-coverity.patch
Patch1:         tboot-%{version}-README.patch
Patch2:         tboot-%{version}-cmdline-size.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  trousers-devel
BuildRequires:  openssl-devel
ExclusiveArch:  x86_64

%description
Trusted Boot (tboot) is an open source, pre-kernel/VMM module that uses
Intel Trusted Execution Technology (Intel TXT) to perform a measured
and verified launch of an OS kernel/VMM.

%prep
%setup -q
%patch0 -p1 -b .coverity
%patch1 -p1 -b .README
%patch2 -b .cmdline

%build
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
make debug=y %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make debug=y DISTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING docs/* lcptools/lcptools2.txt lcptools/Linux_LCP_Tools_User_Manual.pdf
%doc %{_mandir}/man8/acminfo.8.gz
%doc %{_mandir}/man8/lcp_*.8.gz
%doc %{_mandir}/man8/tb_polgen.8.gz
%doc %{_mandir}/man8/txt-stat.8.gz
%{_sysconfdir}/grub.d/20_linux_tboot
%{_sysconfdir}/grub.d/20_linux_xen_tboot
%{_sbindir}/acminfo
%{_sbindir}/lcp_crtpconf
%{_sbindir}/lcp_crtpol
%{_sbindir}/lcp_crtpol2
%{_sbindir}/lcp2_crtpol
%{_sbindir}/lcp_crtpolelt
%{_sbindir}/lcp2_crtpolelt
%{_sbindir}/lcp_crtpollist
%{_sbindir}/lcp2_crtpollist
%{_sbindir}/lcp_mlehash
%{_sbindir}/lcp2_mlehash
%{_sbindir}/lcp_readpol
%{_sbindir}/lcp_writepol
%{_sbindir}/parse_err
%{_sbindir}/tb_polgen
%{_sbindir}/tpmnv_defindex
%{_sbindir}/tpmnv_getcap
%{_sbindir}/tpmnv_lock
%{_sbindir}/tpmnv_relindex
%{_sbindir}/txt-stat
/boot/tboot.gz
/boot/tboot-syms

%changelog
* Wed May 28 2014 Samantha N. Bueno <sbueno@redhat.com> - 1.8.1-1
- Upgrade to 1.8.1 release
  Resolves: rhbz#1037469
- Rebase patches, including one I missed a chunk of last release
  Resolves: rhbz#1065320

* Thu Jul 25 2013 Samantha N. Bueno <sbueno@redhat.com> - 1.7.4-1
- Upgrade to 1.7.4 release
  Resolves: rhbz#957158

* Thu Jun 27 2013 Samantha N. Bueno <sbueno@redhat.com> - 1.7.3-2
- Fix patches and spec file in accordance with changes from 1.7.3 release.
  Related: rhbz#916046

* Thu Jun 27 2013 Samantha N. Bueno <sbueno@redhat.com> - 1.7.3-1
- Upgrade to 1.7.3 release
  Resolves: rhbz#916046

* Tue Jan 08 2013 David Cantrell <dcantrell@redhat.com> - 1.7.0-4
- Fix kernel command line handling.
  Resolves: rhbz#885684

* Tue Oct 16 2012 David Cantrell <dcantrell@redhat.com> - 1.7.0-3
- Remove incorrect statement about what kernels are supported
  Resolves: rhbz#834323

* Thu Jan 26 2012 David Cantrell <dcantrell@redhat.com> - 1.7.0-2
- Source tree is now NAME-VERSION
  Related: rhbz#773406

* Thu Jan 26 2012 David Cantrell <dcantrell@redhat.com> - 1.7.0-1
- Upgrade to 1.7.0 release
  Resolves: rhbz#773406
- Restrict tboot to x86_64 systems
  Resolves: rhbz#754345
- Fix problems found during Coverity scan
  Resolves: rhbz#732439

* Wed Jul 27 2011 David Cantrell <dcantrell@redhat.com> - 1.5.0-0.1.20110714-1
- Intel uploaded a new snapshot, fix the version and release to match guidelines
  Related: rhbz#691617

* Mon Jul 25 2011 David Cantrell <dcantrell@redhat.com> - 20110429-1
- Import from F15
  Resolves: rhbz#691617

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 1 2010 Joseph Cihula <joseph.cihula@intel.com> - 20101005-1.fc13
- Initial import
