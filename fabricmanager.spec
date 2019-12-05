%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:           nvidia-fabricmanager
Version:        %{?version}
Release:        1
Summary:        Fabric Manager for NVSwitch based systems

License:        NVIDIA Proprietary
URL:            http://www.nvidia.com
Source0:        fabricmanager-%{version}.tar.gz

%description
Fabric Manager for NVIDIA NVSwitch based systems.

%package -n nvidia-fabricmanager-devel
Summary:        Fabric Manager API headers and associated library

%description -n nvidia-fabricmanager-devel
Fabric Manager API headers and associated library

%prep
%setup -q -n fabricmanager-%{version}

%build

%install
export DONT_STRIP=1

rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/
cp -a nv-fabricmanager %{buildroot}%{_bindir}/
#cp -a nvswitch-audit %{buildroot}%{_bindir}/

mkdir -p %{buildroot}/usr/lib/systemd/system
cp -a nvidia-fabricmanager.service  %{buildroot}/usr/lib/systemd/system

mkdir -p %{buildroot}/usr/share/nvidia/nvswitch
cp -a dgx2_hgx2_topology %{buildroot}/usr/share/nvidia/nvswitch
cp -a dgxlr_hgxlr_topology %{buildroot}/usr/share/nvidia/nvswitch
cp -a fabricmanager.cfg %{buildroot}/usr/share/nvidia/nvswitch

mkdir -p %{buildroot}%{_libdir}/
cp libnvfm.so.1 %{buildroot}%{_libdir}/
ln -s libnvfm.so.1 %{buildroot}%{_libdir}/libnvfm.so

mkdir -p %{buildroot}%{_includedir}/
cp nv_fm_agent.h %{buildroot}%{_includedir}/
cp nv_fm_types.h %{buildroot}%{_includedir}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
/usr/lib/systemd/system/*
/usr/share/nvidia/nvswitch/*

%files -n nvidia-fabricmanager-devel
%{_libdir}/*
%{_includedir}/*

%changelog
* Fri Jun 29 2018 Shibu Baby
- Initial Fabric Manager RPM packaging
