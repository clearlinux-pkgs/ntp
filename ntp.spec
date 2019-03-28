#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ntp
Version  : 4.2.8p13
Release  : 2
URL      : http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-4.2.8p13.tar.gz
Source0  : http://www.eecis.udel.edu/~ntp/ntp_spool/ntp4/ntp-4.2/ntp-4.2.8p13.tar.gz
Summary  : libevent_pthreads adds pthreads-based threading support to libevent
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0 MIT NTP
Requires: ntp-bin
Requires: ntp-license
Requires: ntp-man
Requires: ntp-data
BuildRequires : bison
BuildRequires : intltool-dev
BuildRequires : libcap-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : ruby
BuildRequires : sed

%description
Submit patches, bug reports, and enhancement requests via
http://bugs.ntp.org
The ntp Distribution Base Directory

%package bin
Summary: bin components for the ntp package.
Group: Binaries
Requires: ntp-data = %{version}-%{release}
Requires: ntp-license = %{version}-%{release}
Requires: ntp-man = %{version}-%{release}

%description bin
bin components for the ntp package.


%package data
Summary: data components for the ntp package.
Group: Data

%description data
data components for the ntp package.


%package doc
Summary: doc components for the ntp package.
Group: Documentation
Requires: ntp-man = %{version}-%{release}

%description doc
doc components for the ntp package.


%package license
Summary: license components for the ntp package.
Group: Default

%description license
license components for the ntp package.


%package man
Summary: man components for the ntp package.
Group: Default

%description man
man components for the ntp package.


%prep
%setup -q -n ntp-4.2.8p13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537883038
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1537883038
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ntp
cp COPYRIGHT %{buildroot}/usr/share/doc/ntp/COPYRIGHT
cp libjsmn/LICENSE %{buildroot}/usr/share/doc/ntp/libjsmn_LICENSE
cp sntp/COPYRIGHT %{buildroot}/usr/share/doc/ntp/sntp_COPYRIGHT
cp sntp/libevent/LICENSE %{buildroot}/usr/share/doc/ntp/sntp_libevent_LICENSE
cp sntp/libopts/COPYING.gplv3 %{buildroot}/usr/share/doc/ntp/sntp_libopts_COPYING.gplv3
cp sntp/libopts/COPYING.lgplv3 %{buildroot}/usr/share/doc/ntp/sntp_libopts_COPYING.lgplv3
cp sntp/libopts/COPYING.mbsd %{buildroot}/usr/share/doc/ntp/sntp_libopts_COPYING.mbsd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/calc_tickadj
%exclude /usr/bin/ntp-keygen
%exclude /usr/bin/ntp-wait
%exclude /usr/bin/ntpd
%exclude /usr/bin/ntpdc
%exclude /usr/bin/ntpq
%exclude /usr/bin/ntptime
%exclude /usr/bin/ntptrace
%exclude /usr/bin/sntp
%exclude /usr/bin/tickadj
%exclude /usr/bin/update-leap
/usr/bin/ntpdate

%files data
%defattr(-,root,root,-)
%exclude /usr/share/ntp/lib/NTP/Util.pm

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/ntp/html/access.html
/usr/share/doc/ntp/html/accopt.html
/usr/share/doc/ntp/html/assoc.html
/usr/share/doc/ntp/html/audio.html
/usr/share/doc/ntp/html/authentic.html
/usr/share/doc/ntp/html/authopt.html
/usr/share/doc/ntp/html/autokey.html
/usr/share/doc/ntp/html/bugs.html
/usr/share/doc/ntp/html/build.html
/usr/share/doc/ntp/html/clock.html
/usr/share/doc/ntp/html/clockopt.html
/usr/share/doc/ntp/html/cluster.html
/usr/share/doc/ntp/html/comdex.html
/usr/share/doc/ntp/html/config.html
/usr/share/doc/ntp/html/confopt.html
/usr/share/doc/ntp/html/copyright.html
/usr/share/doc/ntp/html/debug.html
/usr/share/doc/ntp/html/decode.html
/usr/share/doc/ntp/html/discipline.html
/usr/share/doc/ntp/html/discover.html
/usr/share/doc/ntp/html/drivers/driver1.html
/usr/share/doc/ntp/html/drivers/driver10.html
/usr/share/doc/ntp/html/drivers/driver11.html
/usr/share/doc/ntp/html/drivers/driver12.html
/usr/share/doc/ntp/html/drivers/driver16.html
/usr/share/doc/ntp/html/drivers/driver18.html
/usr/share/doc/ntp/html/drivers/driver19.html
/usr/share/doc/ntp/html/drivers/driver20.html
/usr/share/doc/ntp/html/drivers/driver22.html
/usr/share/doc/ntp/html/drivers/driver26.html
/usr/share/doc/ntp/html/drivers/driver27.html
/usr/share/doc/ntp/html/drivers/driver28.html
/usr/share/doc/ntp/html/drivers/driver29.html
/usr/share/doc/ntp/html/drivers/driver3.html
/usr/share/doc/ntp/html/drivers/driver30.html
/usr/share/doc/ntp/html/drivers/driver31.html
/usr/share/doc/ntp/html/drivers/driver32.html
/usr/share/doc/ntp/html/drivers/driver33.html
/usr/share/doc/ntp/html/drivers/driver34.html
/usr/share/doc/ntp/html/drivers/driver35.html
/usr/share/doc/ntp/html/drivers/driver36.html
/usr/share/doc/ntp/html/drivers/driver37.html
/usr/share/doc/ntp/html/drivers/driver38.html
/usr/share/doc/ntp/html/drivers/driver39.html
/usr/share/doc/ntp/html/drivers/driver4.html
/usr/share/doc/ntp/html/drivers/driver40-ja.html
/usr/share/doc/ntp/html/drivers/driver40.html
/usr/share/doc/ntp/html/drivers/driver42.html
/usr/share/doc/ntp/html/drivers/driver43.html
/usr/share/doc/ntp/html/drivers/driver44.html
/usr/share/doc/ntp/html/drivers/driver45.html
/usr/share/doc/ntp/html/drivers/driver46.html
/usr/share/doc/ntp/html/drivers/driver5.html
/usr/share/doc/ntp/html/drivers/driver6.html
/usr/share/doc/ntp/html/drivers/driver7.html
/usr/share/doc/ntp/html/drivers/driver8.html
/usr/share/doc/ntp/html/drivers/driver9.html
/usr/share/doc/ntp/html/drivers/icons/home.gif
/usr/share/doc/ntp/html/drivers/icons/mail2.gif
/usr/share/doc/ntp/html/drivers/mx4200data.html
/usr/share/doc/ntp/html/drivers/oncore-shmem.html
/usr/share/doc/ntp/html/drivers/scripts/footer.txt
/usr/share/doc/ntp/html/drivers/scripts/style.css
/usr/share/doc/ntp/html/drivers/tf582_4.html
/usr/share/doc/ntp/html/extern.html
/usr/share/doc/ntp/html/filter.html
/usr/share/doc/ntp/html/hints.html
/usr/share/doc/ntp/html/hints/a-ux
/usr/share/doc/ntp/html/hints/aix
/usr/share/doc/ntp/html/hints/bsdi
/usr/share/doc/ntp/html/hints/changes
/usr/share/doc/ntp/html/hints/decosf1
/usr/share/doc/ntp/html/hints/decosf2
/usr/share/doc/ntp/html/hints/freebsd
/usr/share/doc/ntp/html/hints/hpux
/usr/share/doc/ntp/html/hints/linux
/usr/share/doc/ntp/html/hints/mpeix
/usr/share/doc/ntp/html/hints/notes-xntp-v3
/usr/share/doc/ntp/html/hints/parse
/usr/share/doc/ntp/html/hints/refclocks
/usr/share/doc/ntp/html/hints/rs6000
/usr/share/doc/ntp/html/hints/sco.html
/usr/share/doc/ntp/html/hints/sgi
/usr/share/doc/ntp/html/hints/solaris-dosynctodr.html
/usr/share/doc/ntp/html/hints/solaris.html
/usr/share/doc/ntp/html/hints/solaris.xtra.4023118
/usr/share/doc/ntp/html/hints/solaris.xtra.4095849
/usr/share/doc/ntp/html/hints/solaris.xtra.S99ntpd
/usr/share/doc/ntp/html/hints/solaris.xtra.patchfreq
/usr/share/doc/ntp/html/hints/sun4
/usr/share/doc/ntp/html/hints/svr4-dell
/usr/share/doc/ntp/html/hints/svr4_package
/usr/share/doc/ntp/html/hints/todo
/usr/share/doc/ntp/html/hints/vxworks.html
/usr/share/doc/ntp/html/hints/winnt.html
/usr/share/doc/ntp/html/history.html
/usr/share/doc/ntp/html/howto.html
/usr/share/doc/ntp/html/huffpuff.html
/usr/share/doc/ntp/html/icons/home.gif
/usr/share/doc/ntp/html/icons/mail2.gif
/usr/share/doc/ntp/html/icons/sitemap.png
/usr/share/doc/ntp/html/index.html
/usr/share/doc/ntp/html/kern.html
/usr/share/doc/ntp/html/kernpps.html
/usr/share/doc/ntp/html/keygen.html
/usr/share/doc/ntp/html/leap.html
/usr/share/doc/ntp/html/miscopt.html
/usr/share/doc/ntp/html/monopt.html
/usr/share/doc/ntp/html/msyslog.html
/usr/share/doc/ntp/html/ntp-wait.html
/usr/share/doc/ntp/html/ntp_conf.html
/usr/share/doc/ntp/html/ntpd.html
/usr/share/doc/ntp/html/ntpdate.html
/usr/share/doc/ntp/html/ntpdc.html
/usr/share/doc/ntp/html/ntpdsim.html
/usr/share/doc/ntp/html/ntpdsim_new.html
/usr/share/doc/ntp/html/ntpq.html
/usr/share/doc/ntp/html/ntptime.html
/usr/share/doc/ntp/html/ntptrace.html
/usr/share/doc/ntp/html/orphan.html
/usr/share/doc/ntp/html/parsedata.html
/usr/share/doc/ntp/html/parsenew.html
/usr/share/doc/ntp/html/pic/9400n.jpg
/usr/share/doc/ntp/html/pic/alice11.gif
/usr/share/doc/ntp/html/pic/alice13.gif
/usr/share/doc/ntp/html/pic/alice15.gif
/usr/share/doc/ntp/html/pic/alice23.gif
/usr/share/doc/ntp/html/pic/alice31.gif
/usr/share/doc/ntp/html/pic/alice32.gif
/usr/share/doc/ntp/html/pic/alice35.gif
/usr/share/doc/ntp/html/pic/alice38.gif
/usr/share/doc/ntp/html/pic/alice44.gif
/usr/share/doc/ntp/html/pic/alice47.gif
/usr/share/doc/ntp/html/pic/alice51.gif
/usr/share/doc/ntp/html/pic/alice61.gif
/usr/share/doc/ntp/html/pic/barnstable.gif
/usr/share/doc/ntp/html/pic/beaver.gif
/usr/share/doc/ntp/html/pic/boom3.gif
/usr/share/doc/ntp/html/pic/boom3a.gif
/usr/share/doc/ntp/html/pic/boom4.gif
/usr/share/doc/ntp/html/pic/broad.gif
/usr/share/doc/ntp/html/pic/bustardfly.gif
/usr/share/doc/ntp/html/pic/c51.jpg
/usr/share/doc/ntp/html/pic/description.jpg
/usr/share/doc/ntp/html/pic/discipline.gif
/usr/share/doc/ntp/html/pic/dogsnake.gif
/usr/share/doc/ntp/html/pic/driver29.gif
/usr/share/doc/ntp/html/pic/driver43_1.gif
/usr/share/doc/ntp/html/pic/driver43_2.jpg
/usr/share/doc/ntp/html/pic/fg6021.gif
/usr/share/doc/ntp/html/pic/fg6039.jpg
/usr/share/doc/ntp/html/pic/fig_3_1.gif
/usr/share/doc/ntp/html/pic/flatheads.gif
/usr/share/doc/ntp/html/pic/flt1.gif
/usr/share/doc/ntp/html/pic/flt2.gif
/usr/share/doc/ntp/html/pic/flt3.gif
/usr/share/doc/ntp/html/pic/flt4.gif
/usr/share/doc/ntp/html/pic/flt5.gif
/usr/share/doc/ntp/html/pic/flt6.gif
/usr/share/doc/ntp/html/pic/flt7.gif
/usr/share/doc/ntp/html/pic/flt8.gif
/usr/share/doc/ntp/html/pic/flt9.gif
/usr/share/doc/ntp/html/pic/freq1211.gif
/usr/share/doc/ntp/html/pic/gadget.jpg
/usr/share/doc/ntp/html/pic/gps167.jpg
/usr/share/doc/ntp/html/pic/group.gif
/usr/share/doc/ntp/html/pic/hornraba.gif
/usr/share/doc/ntp/html/pic/igclock.gif
/usr/share/doc/ntp/html/pic/neoclock4x.gif
/usr/share/doc/ntp/html/pic/offset1211.gif
/usr/share/doc/ntp/html/pic/oncore_evalbig.gif
/usr/share/doc/ntp/html/pic/oncore_remoteant.jpg
/usr/share/doc/ntp/html/pic/oncore_utplusbig.gif
/usr/share/doc/ntp/html/pic/oz2.gif
/usr/share/doc/ntp/html/pic/panda.gif
/usr/share/doc/ntp/html/pic/pd_om006.gif
/usr/share/doc/ntp/html/pic/pd_om011.gif
/usr/share/doc/ntp/html/pic/peer.gif
/usr/share/doc/ntp/html/pic/pogo.gif
/usr/share/doc/ntp/html/pic/pogo1a.gif
/usr/share/doc/ntp/html/pic/pogo3a.gif
/usr/share/doc/ntp/html/pic/pogo4.gif
/usr/share/doc/ntp/html/pic/pogo5.gif
/usr/share/doc/ntp/html/pic/pogo6.gif
/usr/share/doc/ntp/html/pic/pogo7.gif
/usr/share/doc/ntp/html/pic/pogo8.gif
/usr/share/doc/ntp/html/pic/pzf509.jpg
/usr/share/doc/ntp/html/pic/pzf511.jpg
/usr/share/doc/ntp/html/pic/rabbit.gif
/usr/share/doc/ntp/html/pic/radio2.jpg
/usr/share/doc/ntp/html/pic/sheepb.jpg
/usr/share/doc/ntp/html/pic/stack1a.jpg
/usr/share/doc/ntp/html/pic/stats.gif
/usr/share/doc/ntp/html/pic/sx5.gif
/usr/share/doc/ntp/html/pic/thunderbolt.jpg
/usr/share/doc/ntp/html/pic/time1.gif
/usr/share/doc/ntp/html/pic/tonea.gif
/usr/share/doc/ntp/html/pic/tribeb.gif
/usr/share/doc/ntp/html/pic/wingdorothy.gif
/usr/share/doc/ntp/html/poll.html
/usr/share/doc/ntp/html/pps.html
/usr/share/doc/ntp/html/prefer.html
/usr/share/doc/ntp/html/quick.html
/usr/share/doc/ntp/html/rate.html
/usr/share/doc/ntp/html/rdebug.html
/usr/share/doc/ntp/html/refclock.html
/usr/share/doc/ntp/html/release.html
/usr/share/doc/ntp/html/scripts/accopt.txt
/usr/share/doc/ntp/html/scripts/audio.txt
/usr/share/doc/ntp/html/scripts/authopt.txt
/usr/share/doc/ntp/html/scripts/clockopt.txt
/usr/share/doc/ntp/html/scripts/command.txt
/usr/share/doc/ntp/html/scripts/config.txt
/usr/share/doc/ntp/html/scripts/confopt.txt
/usr/share/doc/ntp/html/scripts/external.txt
/usr/share/doc/ntp/html/scripts/footer.txt
/usr/share/doc/ntp/html/scripts/hand.txt
/usr/share/doc/ntp/html/scripts/install.txt
/usr/share/doc/ntp/html/scripts/manual.txt
/usr/share/doc/ntp/html/scripts/misc.txt
/usr/share/doc/ntp/html/scripts/miscopt.txt
/usr/share/doc/ntp/html/scripts/monopt.txt
/usr/share/doc/ntp/html/scripts/refclock.txt
/usr/share/doc/ntp/html/scripts/special.txt
/usr/share/doc/ntp/html/scripts/style.css
/usr/share/doc/ntp/html/select.html
/usr/share/doc/ntp/html/sitemap.html
/usr/share/doc/ntp/html/sntp.html
/usr/share/doc/ntp/html/stats.html
/usr/share/doc/ntp/html/tickadj.html
/usr/share/doc/ntp/html/warp.html
/usr/share/doc/ntp/html/xleave.html
/usr/share/doc/ntp/ntp-keygen.html
/usr/share/doc/ntp/ntp-wait.html
/usr/share/doc/ntp/ntp.conf.html
/usr/share/doc/ntp/ntp.keys.html
/usr/share/doc/ntp/ntpd.html
/usr/share/doc/ntp/ntpdc.html
/usr/share/doc/ntp/ntpq.html
/usr/share/doc/ntp/ntpsnmpd.html
/usr/share/doc/ntp/ntpsweep.html
/usr/share/doc/ntp/ntptrace.html
/usr/share/doc/ntp/update-leap.html
/usr/share/doc/sntp/sntp.html

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/ntp/COPYRIGHT
/usr/share/doc/ntp/libjsmn_LICENSE
/usr/share/doc/ntp/sntp_COPYRIGHT
/usr/share/doc/ntp/sntp_libevent_LICENSE
/usr/share/doc/ntp/sntp_libopts_COPYING.gplv3
/usr/share/doc/ntp/sntp_libopts_COPYING.lgplv3
/usr/share/doc/ntp/sntp_libopts_COPYING.mbsd

%files man
%defattr(-,root,root,-)
%exclude /usr/share/man/man1/calc_tickadj.1
%exclude /usr/share/man/man1/ntp-keygen.1
%exclude /usr/share/man/man1/ntp-wait.1
%exclude /usr/share/man/man1/ntpd.1
%exclude /usr/share/man/man1/ntpdc.1
%exclude /usr/share/man/man1/ntpq.1
%exclude /usr/share/man/man1/ntptrace.1
%exclude /usr/share/man/man1/sntp.1
%exclude /usr/share/man/man1/update-leap.1
%exclude /usr/share/man/man5/ntp.conf.5
%exclude /usr/share/man/man5/ntp.keys.5
