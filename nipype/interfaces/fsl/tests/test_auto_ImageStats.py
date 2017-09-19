# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import ImageStats


def test_ImageStats_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=2,
    ),
    mask_file=dict(argstr='',
    ),
    op_string=dict(argstr='%s',
    mandatory=True,
    position=3,
    ),
    output_type=dict(),
    split_4d=dict(argstr='-t',
    position=1,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = ImageStats.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ImageStats_outputs():
    output_map = dict(out_stat=dict(),
    )
    outputs = ImageStats.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
