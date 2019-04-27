
pip install moviepy

ERROR: Cannot uninstall 'imageio'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.

pip install moviepy --upgrade --ignore-install imageio
