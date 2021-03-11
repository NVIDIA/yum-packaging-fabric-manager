# yum packaging fabric manager

[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT-license)
[![Contributing](https://img.shields.io/badge/Contributing-Developer%20Certificate%20of%20Origin-violet)](https://developercertificate.org)

## Overview

Packaging templates for `yum`, `dnf`, and `zypper` based Linux distros to build NVIDIA fabricmanager packages.

Fabric Manager is intended for hardware containing NvSwitch such as DGX systems.

> _note:_ the version of fabricmanager must match the NVIDIA driver installed.

## Table of Contents

- [Overview](#Overview)
- [Deliverables](#Deliverables)
- [Installation](#Installation)
- [Prerequisites](#Prerequisites)
  * [Clone this git repository](#Clone-this-git-repository)
  * [Install build dependencies](#Install-build-dependencies)
- [Related](#Related)
  * [NSCQ library](#NSCQ-library)
  * [NVIDIA driver](#NVIDIA-driver)
- [Contributing](#Contributing)


## Deliverables

This repo contains the `.spec` file used to build the following **RPM** packages:


> _note:_ `XXX` is the first `.` delimited field in the driver version, ex: `460` in `460.32.03`

```shell
- cuda-drivers-fabricmanager
- cuda-drivers-fabricmanager-XXX
- nvidia-fabricmanager-XXX
- nvidia-fabricmanager-devel-XXX
```


## Installation

* **RHEL8** or **Fedora** streams: `XXX`, `XXX-dkms`, `latest`, and `latest-dkms`

  The NvSwitch modularity profile (`fm`) installs all of the NVIDIA driver packages, as well as Fabric Manager and NCSQ

  ```shell
  dnf module install nvidia-driver:${stream}/fm
  ```

* **RHEL7**

  ```shell
  yum install cuda-drivers-fabricmanager-XXX
  ```

* **openSUSE15** or **SLES15**

  ```shell
  zypper install cuda-drivers-fabricmanager-XXX
  ```


## Prerequisites

### Clone this git repository:

Supported branches: `main`

```shell
git clone https://github.com/NVIDIA/yum-packaging-fabric-manager
```

### Download a NVIDIA fabricmanager tarball:

* TBD

  *ex:* fabricmanager-460.32.03.tar.gz

### Install build dependencies

```shell
# Packaging
yum install rpm-build
```

## Related

### NSCQ library

- libnvidia-nscq
  * [https://github.com/NVIDIA/yum-packaging-libnvidia-nscq](https://github.com/NVIDIA/yum-packaging-libnvidia-nscq)

### NVIDIA driver

- nvidia-driver
  * [https://github.com/NVIDIA/yum-packaging-nvidia-driver](https://github.com/NVIDIA/yum-packaging-nvidia-driver)


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)
