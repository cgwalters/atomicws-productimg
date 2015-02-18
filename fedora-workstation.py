from pyanaconda.installclasses.fedora import FedoraBaseInstallClass

class FedoraWorkstationInstallClass(FedoraBaseInstallClass):
    name = "Fedora Workstation"
    stylesheet = "/usr/share/anaconda/fedora-workstation.css"
    defaultPackageEnvironment = "workstation-product-environment"
