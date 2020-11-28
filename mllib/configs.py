import os
from dataclasses import dataclass, fields


@dataclass
class ROIFeaturesFRCNN:

    out_file: str
    input_dir: str
    batch_size: int = 4
    log_name: str = "extract_logs.txt"
    config_path: str = ""

    def __init__(self, out_file, input_dir, **kwargs):
        self.out_file = out_file
        self.input_dir = input_dir
        for f in fields(self):
            str_field = f.name
            if str_field in kwargs:
                setattr(self, str_field, kwargs.get(str_field))


@dataclass
class GlobalConfig:

    log_dir: str = (
        os.path.join(os.environ.get("HOME"), "logs")
        if os.environ.get("HOME", False)
        else os.path.join(os.getcwd(), "logs")
    )
    data_dir: str = "/playpen1/home/avmendoz/data"
    output_dir: str = "/playpen1/home/avmendoz/outputs"
    gpus: int = 1

    def __init__(self, **kwargs):
        for f in fields(self):
            str_field = f.name
            if str_field in kwargs:
                setattr(self, str_field, kwargs.get(str_field))


@dataclass
class LossConfig:
    msm: bool = True  # matched_sentence_modeling
    mlm: bool = True  # masked_language_modeling

    def __init__(self, **kwargs):
        for f in fields(self):
            str_field = f.name
            if str_field in kwargs:
                setattr(self, str_field, kwargs.get(str_field))


@dataclass
class DataConfig:
    sent_length: int = 20
    max_objects: int = 36
    attribute_file: str = ""
    object_file: str = ""
    img_format: str = "jpg"
    percent_data: int = 1.0
    use_raw_images: bool = False
    skip_eval: bool = False
    split: bool = "train"
    use_arrow: bool = True
    num_attrs: int = 400
    num_objects: int = 1600
    ignore_id: int = -100
    word_mask_rate: float = 0.15
    feature_mask_rate: float = 0.15
    random_feature_rate: float = 0.10
    random_word_rate: float = 0.10
    sentence_match_rate: float = 0.50
    truncate_sentence: bool = True
    return_token_type_ids: bool = True
    add_special_tokens: bool = True
    return_tensors: str = "pt"
    return_attention_mask: bool = True

    def __init__(self, **kwargs):
        for f in fields(self):
            str_field = f.name
            if str_field in kwargs:
                setattr(self, str_field, kwargs.get(str_field))


@dataclass
class LoaderConfig:
    shuffle: bool = True
    num_workers: int = 8
    drop_last: bool = True
    pin_memory: bool = True
    batch_size: int = 128
    collate_pytorch: bool = True

    def __init__(self, **kwargs):
        for f in fields(self):
            str_field = f.name
            if str_field in kwargs:
                setattr(self, str_field, kwargs.get(str_field))


@dataclass
class PathesConfig:
    coco_imgs: str = "coco/"
    vg_imgs: str = "vg/"
    vqa: str = "vqa/"
    gqa: str = "gqa/"
    vq_qa: str = "vg_qa/"
    vg_captions: str = "vg_captions/"
    coco_captions: str = "coco_captions/"
    coco_train_arrow: str = "arrow/coco_train2017.arrow"
    coco_valid_arrow: str = "arrow/coco_val2017.arrow"
    vg_arrow: str = "arrow/vg.arrow"
    temp_lxmert_answers: str = "labels/lxmert_answers.json"
    temp_lxmert_train: tuple = "lxmert_data/train/"
    temp_lxmert_eval: str = "lxmert_data/mscoco_minival.json"
    temp_lxmert_test: str = ""
    label_file: str = ""

    def __init__(self, **kwargs):
        for f in fields(self):
            str_field = f.name
            if str_field in kwargs:
                setattr(self, str_field, kwargs.get(str_field))