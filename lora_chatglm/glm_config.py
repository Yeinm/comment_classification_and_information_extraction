# -*- coding:utf-8 -*-
import torch


class ProjectConfig(object):
    def __init__(self):
        # self.device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
        self.device = 'cpu'
        self.pre_model = '/Users/ligang/PycharmProjects/llm/ChatGLM-6B/THUDM/chatglm-6b'
        self.train_path = '/Users/ligang/PycharmProjects/llm/ptune_chatglm/data/mixed_train_dataset.jsonl'
        self.dev_path = '/Users/ligang/PycharmProjects/llm/ptune_chatglm/data/mixed_dev_dataset.jsonl'
        self.use_lora = True
        self.use_ptuning = False
        self.lora_rank = 8
        self.batch_size = 1
        self.epochs = 2
        self.learning_rate = 3e-5
        self.weight_decay = 0
        self.warmup_ratio = 0.06
        self.max_source_seq_len = 400
        self.max_target_seq_len = 300
        self.logging_steps = 10
        self.save_freq = 200
        self.pre_seq_len = 128
        self.prefix_projection = False # 默认为False,即p-tuning,如果为True，即p-tuning-v2
        self.save_dir = '/Users/ligang/PycharmProjects/llm/ptune_chatglm/checkpoints/ptune'


if __name__ == '__main__':
    pc = ProjectConfig()
    print(pc.save_dir)