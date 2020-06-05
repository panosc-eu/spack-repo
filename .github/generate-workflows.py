import yaml
from copy import copy


with open("./spack-config/spack.yaml") as f:
    spack = yaml.safe_load(f)
    specs = spack["spack"]["specs"][:]

with open("./template/package-test.template.yaml") as f:
    template = f.readlines()

for spec in specs:
    workflow = copy(template)
    workflow = [l.format(PACKAGE=spec) for l in workflow]

    with open(f"./workflows/package-test.{spec}.yaml", 'w') as f:
        f.writelines(workflow)
