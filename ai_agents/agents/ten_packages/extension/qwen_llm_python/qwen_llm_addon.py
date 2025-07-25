#
#
# Agora Real Time Engagement
# Created by Wei Hu in 2024-05.
# Copyright (c) 2024 Agora IO. All rights reserved.
#
#
from ten_runtime import (
    Addon,
    register_addon_as_extension,
    TenEnv,
)


@register_addon_as_extension("qwen_llm_python")
class QWenLLMExtensionAddon(Addon):
    def on_create_instance(self, ten: TenEnv, addon_name: str, context):
        from .qwen_llm_extension import QWenLLMExtension

        ten.log_info("on_create_instance")
        ten.on_create_instance_done(QWenLLMExtension(addon_name), context)
