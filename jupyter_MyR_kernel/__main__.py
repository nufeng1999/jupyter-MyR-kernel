from ipykernel.kernelapp import IPKernelApp
from .kernel import MyRKernel
IPKernelApp.launch_instance(kernel_class=MyRKernel)
