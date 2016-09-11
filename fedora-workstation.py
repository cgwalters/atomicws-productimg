from pyanaconda.installclasses.fedora import FedoraBaseInstallClass
from pyanaconda.constants import *
from pyanaconda.product import *
from pyanaconda import network
from pyanaconda import nm
from pyanaconda import iutil
import types
from pyanaconda.kickstart import getAvailableDiskSpace
from blivet.partspec import PartSpec
from blivet.autopart import swap_suggestion
from blivet.platform import platform
from blivet.size import Size

class FedoraWorkstationInstallClass(FedoraBaseInstallClass):
    name = "Atomic Workstation"
    stylesheet = "/usr/share/anaconda/fedora-workstation.css"
    defaultFS = "xfs"
    defaultPackageEnvironment = "workstation-product-environment"

    def setDefaultPartitioning(self, storage):
        autorequests = [PartSpec(mountpoint="/", fstype=storage.default_fstype,
                                 size=Size("4GiB"),
                                 max_size=Size("30GiB"),
                                 grow=True,
                                 btr=True, lv=True, thin=True, encrypted=True)]

        bootreqs = platform.set_default_partitioning()
        if bootreqs:
            autorequests.extend(bootreqs)

        disk_space = getAvailableDiskSpace(storage)
        swp = swap_suggestion(disk_space=disk_space)
        autorequests.append(PartSpec(fstype="swap", size=swp, grow=False,
                                     lv=True, encrypted=True))

        for autoreq in autorequests:
            if autoreq.fstype is None:
                if autoreq.mountpoint == "/boot":
                    autoreq.fstype = storage.default_boot_fstype
                else:
                    autoreq.fstype = storage.default_fstype

        storage.autopart_requests = autorequests
