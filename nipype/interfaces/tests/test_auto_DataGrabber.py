# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..io import DataGrabber


def test_DataGrabber_inputs():
    input_map = dict(base_directory=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    raise_on_empty=dict(usedefault=True,
    ),
    sort_filelist=dict(mandatory=True,
    ),
    template=dict(mandatory=True,
    ),
    template_args=dict(),
    )
    inputs = DataGrabber.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DataGrabber_outputs():
    output_map = dict()
    outputs = DataGrabber.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
