# 这个新的配置文件继承自一个原始配置文件，只需要突出必要的修改部分即可
# -*- coding: utf-8 -*-
_base_ = 'configs/mask_rcnn_r50_fpn_mstrain-poly_3x_coco.py'

# 我们需要对头中的类别数量进行修改来匹配数据集的标注
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))

# 修改数据集相关设置
dataset_type = 'CocoDataset'
classes = ('balloon',)
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=1,
    train=dict(
        dataset=dict(
        img_prefix='./data/balloon/train/',
        classes=classes,
        ann_file='./data/balloon/train/annotation_coco.json')),
    val=dict(
        img_prefix='./data/balloon/val/',
        classes=classes,
        ann_file='./data/balloon/val/annotation_coco.json'),
    test=dict(
        img_prefix='./data/balloon/val/',
        classes=classes,
        ann_file='./data/balloon/val/annotation_coco.json'))

model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=1),
        mask_head=dict(
            num_classes=1))
)

# 我们可以使用预训练的 Mask R-CNN 来获取更好的性能
load_from = 'checkpoints/mask_rcnn_r50_fpn_mstrain-poly_3x_coco_20210524_201154-21b550bb.pth'