import numpy
from hemato_tf_dataset import HemSelfSupDataset


def test_HemSelfSupDataset():
    ds = HemSelfSupDataset("tests/test_data", image_width=256)
    assert ds
    assert ds.__len__() == 78
    x1 = ds.get_batch(0)
    assert len(x1) == ds.batch_size
    item = ds[0]
    assert numpy.max(item["img"]) == 1.0
