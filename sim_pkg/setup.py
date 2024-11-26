from setuptools import find_packages, setup

package_name = 'sim_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='iqqy',
    maintainer_email='akhmdashdq@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "gui_status = sim_pkg.gui_status:main",
            "mavros = sim_pkg.mavros:main"
        ],
    },
)
