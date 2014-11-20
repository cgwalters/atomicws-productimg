%global pixmaptarget %{_datadir}/lorax/product/usr/share/anaconda/pixmaps
%global pixmapsource %{_datadir}/anaconda/pixmaps/workstation

Name:           fedora-productimg-workstation
Version:        22
Release:        3%{?dist}
Summary:        Installer branding and configuration for Fedora Workstation

# Copyright and related rights waived via CC0
# http://creativecommons.org/publicdomain/zero/1.0/
License:        CC0

Source0:        anaconda-gtk.css

BuildArch:      noarch

BuildRequires:  cpio, findutils, xz

Conflicts:      fedora-productimg-cloud, fedora-productimg-server

%description
This package contains differentiated branding and configuration for Fedora
Workstation for use in a product.img file for Anaconda, the Fedora
installer. It is not useful on an installed system.

%prep

%build

%install

install -m 755 -d %{buildroot}%{pixmaptarget}

install -m 644 %{SOURCE0} %{buildroot}%{pixmaptarget}/../

ln -sf %{pixmapsource}/sidebar-bg.png %{buildroot}%{pixmaptarget}
ln -sf %{pixmapsource}/topbar-bg.png %{buildroot}%{pixmaptarget}

# note filename change with this one
ln -sf %{pixmapsource}/sidebar-logo.png %{buildroot}%{pixmaptarget}/sidebar-logo_flavor.png

install -m 755 -d %{buildroot}%{_datadir}/fedora-productimg

find %{buildroot}%{pixmaptarget} -depth -printf '%P\0' | \
   cpio --null --quiet -H newc -o | \
   xz -9 > \
   %{buildroot}%{_datadir}/fedora-productimg/product.img


%files
%dir %{_datadir}/lorax/product/usr/share/anaconda
%{_datadir}/lorax/product/usr/share/anaconda/anaconda-gtk.css
%dir %{_datadir}/lorax/product/usr/share
%dir %{_datadir}/lorax/product/usr
%dir %{pixmaptarget}
%{pixmaptarget}/*.png
%dir %{_datadir}/fedora-productimg
%{_datadir}/fedora-productimg/product.img

%changelog
* Thu Nov 20 2014 Matthew Miller <mattdm@fedoraproject.org> 22-3
- merge changes in from f21

* Fri Nov  7 2014 Matthew Miller <mattdm@fedoraproject.org> 22-2
- actually also generate a product.img cpio archive and store
  that in the rpm (for use with livecd-creator or other convenience)

* Fri Nov  7 2014 Matthew Miller <mattdm@fedoraproject.org> 22-1 
- bump to 22 for rawhide

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-2
- conflict with the other fedora-productimg packages

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-1
- Change license to CC0

* Thu Nov  6 2014 Matthew Miller <mattdm@fedoraproject.org> 21-0
- Initial creation for Fedora 21
