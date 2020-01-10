Summary:        Performs a verified launch using Intel TXT
Name:           tboot
Version:        1.8.3
Release:        2%{?dist}

Group:          System Environment/Base
License:        BSD
URL:            http://sourceforge.net/projects/tboot/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch01:	tboot-%{version}-%{release}-0001-Disable-fstack-check-in-CFLAG-for-compatibility-with.patch
Patch02:	tboot-%{version}-%{release}-0002-Enhanced-tboot-compatiblity-running-on-non-Intel-TXT.patch
Patch03:	tboot-%{version}-%{release}-0003-This-is-a-fix-for-Gentoo-Hardened.patch
Patch04:	tboot-%{version}-%{release}-0004-Add-64bit-ELF-object-support.patch
Patch05:	tboot-%{version}-%{release}-0005-Correct-a-typo-of-lcp2_mlehash-command-parameter-in-.patch
Patch06:	tboot-%{version}-%{release}-0006-Updated-TPM-2.0-SGX-NV-Index-to-0x01800004.patch
Patch07:	tboot-%{version}-%{release}-0007-Some-changes-were-made-to-avoid-stack-overflow.patch
Patch08:	tboot-%{version}-%{release}-0008-Fixed-a-minor-bug-in-txt-stat-tool.patch
Patch09:	tboot-%{version}-%{release}-0009-Revisited-and-fixed-a-security-vulnerability.patch
Patch10:	tboot-%{version}-%{release}-0010-Removed-some-redundant-codes-in-loader.c.patch
Patch11:	tboot-%{version}-%{release}-0011-1.-Mitigated-S3-resume-delay-by-adjusting-LZ_MAX_OFF.patch
Patch12:	tboot-%{version}-%{release}-0012-Added-an-ACPI_RSDP-structure-g_rsdp-in-tboot.patch
Patch13:	tboot-%{version}-%{release}-0013-Make-a-minor-change-to-tboot.c.patch
Patch14:	tboot-%{version}-%{release}-0014-Added-TPM-2.0-CRB-Command-Response-Buffer-interface-.patch
Patch15:	tboot-%{version}-%{release}-0015-Don-t-skip-first-argument-in-Linux-kernel-command-li.patch
Patch16:	tboot-%{version}-%{release}-0016-grub2-xen-insert-just-one-dummy-command-line-argumen.patch
Patch17:	tboot-%{version}-%{release}-0017-grub2-support-allow-the-user-to-customize-the-comman.patch
Patch18:	tboot-%{version}-%{release}-0018-grub2-Allow-addition-of-policy-data-in-grub.cfg.patch
Patch19:	tboot-%{version}-%{release}-0019-grub2-sanitize-whitespace-in-command-lines.patch
Patch20:	tboot-%{version}-%{release}-0020-grub2-tboot-doesn-t-skip-first-argument-any-more.patch
Patch21:	tboot-%{version}-%{release}-0021-Add-TCG-2.0-compliant-NV-indices-support.patch

BuildRequires:  trousers-devel
BuildRequires:  openssl-devel
ExclusiveArch:  x86_64

%description
Trusted Boot (tboot) is an open source, pre-kernel/VMM module that uses
Intel Trusted Execution Technology (Intel TXT) to perform a measured
and verified launch of an OS kernel/VMM.

%prep
%setup -q
%patch01 -p1 -b .0001-Disable-fstack-check-in-CFLAG-for-compatibility-with
%patch02 -p1 -b .0002-Enhanced-tboot-compatiblity-running-on-non-Intel-TXT
%patch03 -p1 -b .0003-This-is-a-fix-for-Gentoo-Hardened
%patch04 -p1 -b .0004-Add-64bit-ELF-object-support
%patch05 -p1 -b .0005-Correct-a-typo-of-lcp2_mlehash-command-parameter-in-
%patch06 -p1 -b .0006-Updated-TPM-2.0-SGX-NV-Index-to-0x01800004
%patch07 -p1 -b .0007-Some-changes-were-made-to-avoid-stack-overflow
%patch08 -p1 -b .0008-Fixed-a-minor-bug-in-txt-stat-tool
%patch09 -p1 -b .0009-Revisited-and-fixed-a-security-vulnerability
%patch10 -p1 -b .0010-Removed-some-redundant-codes-in-loader.c
%patch11 -p1 -b .0011-1.-Mitigated-S3-resume-delay-by-adjusting-LZ_MAX_OFF
%patch12 -p1 -b .0012-Added-an-ACPI_RSDP-structure-g_rsdp-in-tboot
%patch13 -p1 -b .0013-Make-a-minor-change-to-tboot.c
%patch14 -p1 -b .0014-Added-TPM-2.0-CRB-Command-Response-Buffer-interface-
%patch15 -p1 -b .0015-Don-t-skip-first-argument-in-Linux-kernel-command-li
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1 -b .0021-Add-TCG-2.0-compliant-NV-indices-support

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
* Wed Mar 02 2016 Tony Camuso <tcamuso@redhat.com> - 1.8.3-2
- Backport important upstream patches
  Resolves rhbz#1313873

* Wed Jan 13 2016 Tony Camuso <tcamuso@redhat.com> - 1.8.3-1
- Upgrade t0 1.8.3 release
- Removed 1.8.1 patches, since the've been merged
- Fixed bad day-of-week of first entry in changelog
- updated .gitignore
  Resolves: rhbz#1043060

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

* Wed Dec 1 2010 Joseph Cihula <joseph.cihula@intel.com> - 20101005-1.fc13
- Initial import
