from base import Phase

preparation = Phase('Preparation', 'Initializing connections, fetching data etc.')
volume_creation = Phase('Volume creation', 'Creating the volume to bootstrap onto')
volume_preparation = Phase('Volume preparation', 'Formatting the bootstrap volume')
volume_mounting = Phase('Volume mounting', 'Mounting bootstrap volume')
os_installation = Phase('OS installation', 'Installing the operating system')
system_modification = Phase('System modification', 'Installing software, modifying configuration files etc.')
system_cleaning = Phase('System cleaning', 'Removing sensitive data, temporary files and other leftovers')
volume_unmounting = Phase('Volume unmounting', 'Unmounting the bootstrap volume')
image_registration = Phase('Image registration', 'Uploading/Registering with the provider')
image_conversion = Phase('Image conversion', 'Conversion/Compression of the image result file')
cleaning = Phase('Cleaning', 'Removing temporary files')

order = [preparation,
         volume_creation,
         volume_preparation,
         volume_mounting,
         os_installation,
         system_modification,
         system_cleaning,
         volume_unmounting,
         image_registration,
         image_conversion,
         cleaning,
         ]
