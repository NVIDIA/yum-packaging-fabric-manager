# The MIT License (MIT)
# 
# Copyright (c) 2020 NVIDIA Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:           nvidia-fabricmanager-%{branch}
Version:        %{?version}
Release:        1
Summary:        Fabric Manager for NVSwitch based systems

License:        NVIDIA Proprietary
URL:            http://www.nvidia.com
Source0:        fabricmanager-%{version}.tar.gz

Obsoletes:      nvidia-fabricmanager

Provides:       nvidia-fabricmanager-branch = %{version}
Obsoletes:      nvidia-fabricmanager-branch < %{version}
Conflicts:      nvidia-fabricmanager-branch

%description
Fabric Manager for NVIDIA NVSwitch based systems.

%package -n nvidia-fabricmanager-devel-%{branch}
Summary:        Fabric Manager API headers and associated library
# Normally we would have a dev package depend on its runtime package. However
# FM isn't a normal package. All the libs are in the dev package, and the
# runtime package is actually a service package.
Obsoletes:      nvidia-fabricmanager-devel

Provides:       nvidia-fabricmanager-devel-branch = %{version}
Obsoletes:      nvidia-fabricmanager-devel-branch < %{version}
Conflicts:      nvidia-fabricmanager-devel-branch

%description -n nvidia-fabricmanager-devel-%{branch}
Fabric Manager API headers and associated library

%package -n cuda-drivers-fabricmanager-%{branch}
Summary:        Meta-package for FM and Driver
Requires:       nvidia-fabricmanager-%{branch} = %{version}
Requires:       cuda-drivers-%{branch} = %{version}

Provides:       cuda-drivers-fabricmanager-branch = %{version}
Obsoletes:      cuda-drivers-fabricmanager-branch < %{version}
Conflicts:      cuda-drivers-fabricmanager-branch

%description -n cuda-drivers-fabricmanager-%{branch}
Convience meta-package for installing fabricmanager and the cuda-drivers
meta-package simultaneously while keeping version equivalence. This meta-
package is branch-specific.

%package -n cuda-drivers-fabricmanager
Summary:        Meta-package for FM and Driver
Requires:       cuda-drivers-fabricmanager-%{branch} = %{version}

%description -n cuda-drivers-fabricmanager
Convience meta-package for installing fabricmanager and the cuda-drivers
meta-package simultaneously while keeping version equivalence. This meta-
package is across all driver branches.

%prep
%setup -q -n fabricmanager-%{version}

%build

%install
export DONT_STRIP=1

rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/
cp -a nv-fabricmanager %{buildroot}%{_bindir}/
cp -a nvswitch-audit %{buildroot}%{_bindir}/

mkdir -p %{buildroot}/usr/lib/systemd/system
cp -a nvidia-fabricmanager.service  %{buildroot}/usr/lib/systemd/system

mkdir -p %{buildroot}/usr/share/nvidia/nvswitch
cp -a *_topology %{buildroot}/usr/share/nvidia/nvswitch
cp -a fabricmanager.cfg %{buildroot}/usr/share/nvidia/nvswitch

mkdir -p %{buildroot}%{_libdir}/
cp libnvfm.so.1 %{buildroot}%{_libdir}/
ln -s libnvfm.so.1 %{buildroot}%{_libdir}/libnvfm.so

mkdir -p %{buildroot}%{_includedir}/
cp nv_fm_agent.h %{buildroot}%{_includedir}/
cp nv_fm_types.h %{buildroot}%{_includedir}/

mkdir -p %{buildroot}/usr/share/doc/nvidia-fabricmanager/
cp -a LICENSE %{buildroot}/usr/share/doc/nvidia-fabricmanager/
cp -a third-party-notices.txt %{buildroot}/usr/share/doc/nvidia-fabricmanager/

%post -n nvidia-fabricmanager-devel-%{branch} -p /sbin/ldconfig

%postun -n nvidia-fabricmanager-devel-%{branch} -p /sbin/ldconfig

%files
%{_bindir}/*
/usr/lib/systemd/system/*
/usr/share/nvidia/nvswitch/*
/usr/share/doc/nvidia-fabricmanager/*

%files -n nvidia-fabricmanager-devel-%{branch}
%{_libdir}/*
%{_includedir}/*

%files -n cuda-drivers-fabricmanager-%{branch}

%files -n cuda-drivers-fabricmanager

%changelog
* Fri Jun 29 2018 Shibu Baby
- Initial Fabric Manager RPM packaging
