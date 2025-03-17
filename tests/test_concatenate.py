# Copyright (c) 2025 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase

obj = APIBase("torch.concatenate")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(2, 3)
        result = torch.concatenate((x, x, x))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(2, 3)
        y = torch.zeros(2, 3)
        result = torch.concatenate((x, y), 0)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.concatenate((torch.zeros(2, 3), torch.zeros(2, 3)), dim=1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.ones(2, 3)
        y = torch.ones(2, 3)
        result = torch.concatenate([x, y], 0)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.ones(2, 3)
        y = torch.ones(2, 3)
        out = torch.zeros(4, 3)
        result = torch.concatenate([x, y], dim=0, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.ones(2, 3)
        y = torch.ones(2, 3)
        out = torch.zeros(4, 3)
        result = torch.concatenate(tensors=[x, y], dim=0, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.ones(2, 3)
        y = torch.ones(2, 3)
        out = torch.zeros(4, 3)
        result = torch.concatenate(dim=0, tensors=[x, y], out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.zeros(2, 3)
        y = torch.zeros(2, 3)
        result = torch.concatenate((x, y), axis=0)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.ones(2, 3)
        y = torch.ones(2, 3)
        out = torch.zeros(4, 3)
        result = torch.concatenate([x, y], axis=0, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])


def test_case_10():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.ones(2, 3)
        y = torch.ones(2, 3)
        out = torch.zeros(4, 3)
        result = torch.concatenate(axis=0, tensors=[x, y], out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])
